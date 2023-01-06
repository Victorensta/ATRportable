import math


class EuclideanDistTracker:
    def __init__(self, name):
        # Store the center positions of the objects
        self.name = name
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0


    def update(self, objects_rect):
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
                #print("\nWe have registered :",self.center_points)
                #print("The new points is (", cx, ",", cy, "). The possible match is", self.name,id,"at",pt)
                dist = math.hypot(cx - pt[0], cy - pt[1])
                #print("The distance between them was", dist)

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    #print("We have updated",self.name, self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                #print("\nNew",self.name,"!")
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        #print("\nThis is the dictionary before the process",self.center_points)
        # Clean the dictionary by center points to remove IDS not used anymore
        '''
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        #print("\nThis is the dictionary after the process", self.center_points)
        '''
        print("I have",self.id_count,"instances of",self.name,"on memory.")
        return objects_bbs_ids