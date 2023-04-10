import math
from datetime import datetime


class EuclideanDistTracker:
    def __init__(self, name):
        # Store the center positions of the objects
        self.name = name
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0
        # Keep track of time, to wipe memory
        self.unused_ids = []
        # Measured in minutes, determines how long an ID stays in memory before being erased
        self.memory = 1

    def update(self, objects_rect):
        minute = datetime.now().minute
        second = datetime.now().second
        time_sig = [minute, second]

        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                # print("\nWe have registered :",self.center_points)
                # print("The new points is (", cx, ",", cy, "). The possible match is", self.name,id,"at",pt)
                dist = math.hypot(cx - pt[0], cy - pt[1])
                # print("The distance between them was", dist)

                if dist < 25:
                    self.center_points[id] = [cx, cy, time_sig]
                    # print("We have updated",self.name, self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if not same_object_detected:
                if len(self.unused_ids) == 0:
                    self.center_points[self.id_count] = [cx, cy, time_sig]
                    objects_bbs_ids.append([x, y, w, h, self.id_count])
                    print("We have detected a new", self.name, "it will the new ID", self.id_count)
                    self.id_count += 1
                    #print("There are now", self.id_count, self.name, "on memory", "and the dictionary is", len(self.center_points), "long.")
                else:
                    num = self.unused_ids[-1]
                    self.unused_ids.pop(-1)
                    self.center_points[num] = [cx, cy, time_sig]
                    objects_bbs_ids.append([x, y, w, h, num])
                    print("We have detected a new", self.name, "it will reuse ID", num)
                    self.id_count += 1
                    #print("There are now", self.id_count, self.name, "on memory", "and the dictionary is",len(self.center_points), "long.")


        # Clean the dictionary by center points to remove IDS not used anymore
        if self.id_count > 0 and len(self.center_points) > 0:
            for i in range(len(self.center_points)):
                if (((datetime.now().minute+(datetime.now().second/60)) -
                        (self.center_points[i][2][0]+(self.center_points[i][2][1]/60))) > self.memory
                        and self.center_points[i][0] != 99999):
                    self.unused_ids.append(i)
                    self.id_count -= 1
                    self.center_points[i][0] = 99999
                    self.center_points[i][1] = 99999
                    #print("ID", i, "has been wiped from memory, freeing its spot. There were", 1+self.id_count, self.name, "before, now", self.id_count, "and the dictionary is", len(self.center_points), "long.")
                    #print("Dic is now", self.center_points)
        elif self.id_count == 0 and len(self.center_points) > 0:
            self.center_points = {}
            self.unused_ids = []
            print("Memory totally wiped, there are now", self.id_count, self.name, "on memory and the dictionary is",
                  len(self.center_points), "long")

        return objects_bbs_ids
