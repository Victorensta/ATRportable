# import the necessary packages
import numpy as np
import cv2 as cv2
import time
from tracker import EuclideanDistTracker

# initialize the trackers
body_tracker = EuclideanDistTracker("Person")
#frontal_face_tracker = EuclideanDistTracker("Frontal Face")
#profile_face_tracker = EuclideanDistTracker("Profile Face")
#upper_body_tracker = EuclideanDistTracker("Upper Body")

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# face and eyes detection
#frontal_face_cascade = cv2.CascadeClassifier('Haar_copies/haarcascade_frontalface_default_localcopy.xml')
#profile_face_cascade = cv2.CascadeClassifier('Haar_copies/haarcascade_profileface_localcopy.xml')
#upper_body_cascade = cv2.CascadeClassifier('Haar_copies/data_copy/haarcascade_upperbody.xml')
#according to online and my own testing, Haar_cascade is not great at identifying bodies, but works well for faces
#I copied the files locally rather than typing out the long filepath of the openCV original

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0) #object for video capture, can receive either video file or an index corresponding to a camera

# the output will be written to output.avi
out = cv2.VideoWriter('output.avi', fourcc=cv2.VideoWriter_fourcc(*'MJPG'), fps=7.,frameSize=(640, 400))
frame_count=0
detect_times=[]
frame_times=[]
while (True):
    t0=time.time()
    frame_count+=1
    # Capture frame-by-frame, the frequency is limited by computer's camera or waitkey() command
    ret, frame = cap.read()
    # resizing for faster detection, this determines the picture size for imshow. If we make it smaller, then go
    # fullscreen, then the image is pixelated
    frame = cv2.resize(frame, (640, 400)) #my screen is 2560x1600, so a smaller variant of same aspect ratio is best
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    td0=time.time()
    # detect people in the image
    # returns the bounding boxes for the detected objects
    bodies, weights_body = hog.detectMultiScale(img=gray, padding=(4, 4), scale=1.03, winStride=(8, 8))
    #frontal_faces = frontal_face_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5)
    #profile_faces = profile_face_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5)
    #upper_bodies = upper_body_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5)

    bodies = np.array([[x, y, w, h] for (x, y, w, h) in bodies])
    #frontal_faces = np.array([[x, y, w, h] for (x, y, w, h) in frontal_faces])
    #profile_faces = np.array([[x, y, w, h] for (x, y, w, h) in frontal_faces])
    #upper_bodies = np.array([[x, y, w, h] for (x, y, w, h) in frontal_faces])
    bodies_ids = body_tracker.update(bodies)
    #frontal_faces_ids = frontal_face_tracker.update(frontal_faces)
    #profile_faces_ids = profile_face_tracker.update(profile_faces)
    #upper_bodies_ids = upper_body_tracker.update(upper_bodies)
    #before trying this, it only had frontal_faces


    for body_id in bodies_ids: #body in green
        # display the detected boxes in the colour picture
        x, y, w, h, id = body_id
        cv2.putText(frame, 'Person '+str(id), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #(image, (start point), (endpoint), (BGR color), thickness)
        '''
    for frontal_face_id in frontal_faces_ids: #frontal_faces in blue
        x, y, w, h, id = frontal_face_id
        cv2.putText(frame, 'Frontal Face '+str(id), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        '''
        '''
    for profile_face_id in profile_faces_ids: #profile_faces in blue
        x, y, w, h, id = profile_face_id
        cv2.putText(frame, 'Profile Face '+str(id), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        '''
        '''
    for upper_body_id in upper_bodies_ids: #body in green
        # display the detected boxes in the colour picture
        x, y, w, h, id = upper_body_id
        cv2.putText(frame, 'Torso '+str(id), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (14, 255, 142), 2)
        '''

    td1 = time.time()
    detect_times.append(td1-td0)
    # Write the output video
    out.write(frame)
    #out.write(frame.astype('uint8')) #this is the code used by the creator
    # Display the resulting frame
    cv2.imshow('frame', frame) #what matters for the picture itself is the frame
    if cv2.waitKey(50) & 0xFF == ord('q'): #waits 1ms before we can proceed
        break
    t1=time.time()
    frame_times.append(t1-t0)

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
print("There are ",frame_count," frames.")
detect_time=round(np.average(detect_times),3)
print("Detection and box drawing takes ",detect_time," seconds.")
frame_time=round(np.average(frame_times),3)
print("Processing a frame takes ",frame_time," seconds.")
print("So in theory we should be able to process ",round(1/np.average(frame_times),3)," frames per second.")
#this line of code gives us the ideal framerate if we want the output to look like the imshow

'''
Notes on this code:
The waitkey() inside the loop dictates the framerate without other code to slow it down.
It works in ms/frame, so 42ms/frame is roughly 24fps, or 17 corresponds to 60fps.
The fourCC code is used to identify a file format. It's a thing, look it up.
'''