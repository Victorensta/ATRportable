# import the necessary packages
import numpy as np
import cv2 as cv2
import time
import face_recognition
from tracker import EuclideanDistTracker

# Elgato
camera_input = 0
# Computer camera
#camera_input = 1

# initialize the trackers
body_tracker = EuclideanDistTracker("Person")

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# face and eyes detection
# according to online and my own testing, Haar_cascade is not great at identifying bodies, but works well for faces
# I copied the files locally rather than typing out the long filepath of the openCV original

# Identification
known_face_encodings = np.load('known_face_encodings.npy')
known_face_names = []
with open('known_face_names.txt', 'r') as f:
    for line in f:
        known_face_names.append(line[:-1])
print(known_face_names)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

cv2.startWindowThread()

# open webcam video stream
# object for video capture, can receive either video file or an index corresponding to a camera
# currently, 0 is for elgato, and 1 is for computer camera
cap = cv2.VideoCapture(camera_input)
#cap = cv2.VideoCapture("http://192.168.11.12:4014/") #didn't work

# the output will be written to output.avi
out = cv2.VideoWriter('output.avi', fourcc=cv2.VideoWriter_fourcc(*'MJPG'), fps=7., frameSize=(640, 400))
frame_count = 0
detect_times = []
frame_times = []
while True:
    # measurements I take for performance analysis
    t0 = time.time()
    frame_count += 1

    # Capture frame-by-frame, the frequency is limited by computer's camera or waitkey() command
    ret, frame = cap.read()
    frame_width = cap.get(3)
    frame_height = cap.get(4)

    # resizing for faster processing, this determines the picture size for imshow.
    # If we make it smaller, then go fullscreen, then the image is pixelated
    # incoming frames are at (1280, 720)=720p, my screen resolution is 2560x1600
    frame = cv2.resize(frame, (640, 400))
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    td0 = time.time()

    # detect people and faces in the image
    # returns the bounding boxes for the detected objects
    bodies, weights_body = hog.detectMultiScale(img=gray, padding=(8, 8), scale=1.03, winStride=(8, 8))

    # convert bounding boxes to new format
    bodies = np.array([[x, y, w, h] for (x, y, w, h) in bodies])

    # id handling
    bodies_ids = body_tracker.update(bodies)

    # display the detected body boxes in the colour picture
    for body_id in bodies_ids:
        x, y, w, h, id = body_id
        cv2.putText(frame, 'Person '+str(id), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        # body in green
        # (image, (left, top), (right, bottom), (B, G, R), thickness)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 17), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        #name = str((left, top))+str((right, bottom))+str((frame_width, frame_height))
        cv2.putText(frame, name, (left + 4, bottom - 4), font, 1, (0, 0, 255), 2)

    #for face_id in frontal_faces_ids

    # Display the resulting image
    cv2.imshow('Image', frame)

    td1 = time.time()
    detect_times.append(td1-td0)
    # Write the output video
    out.write(frame)
    # out.write(frame.astype('uint8')) #this is the code used by the creator
    # Display the resulting frame
    # what matters for the picture itself is the frame
    #cv2.imshow('frame', frame)
    # waits 1ms before we can proceed
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
    t1 = time.time()
    frame_times.append(t1-t0)

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
print("There are ", frame_count, " frames.")
detect_time = round(np.average(detect_times), 3)
print("Detection and box drawing takes ", detect_time, " seconds.")
frame_time = round(np.average(frame_times), 3)
print("Processing a frame takes ", frame_time, " seconds.")
print("So in theory we should be able to process ", round(1/np.average(frame_times), 3), " frames per second.")
# this line of code gives us the ideal framerate if we want the output to look like the imshow

'''
Notes on this code:
The waitkey() inside the loop dictates the framerate without other code to slow it down.
It works in ms/frame, so 42ms/frame is roughly 24fps, or 17 corresponds to 60fps.
The fourCC code is used to identify a file format. It's a thing, look it up.
'''

'''
Idea : the detect-tracking and identification work symbiotically. If the tracking is not obstructed,
then the name is maintained despite the face not being visible. If the tracking is obstructed,
the face will work for re-identification. This should give it abilities similar to a baby, no?
We should compare the centers of the identification squares and the detection ones. IF they are close
then we should say that they're the same. 
'''