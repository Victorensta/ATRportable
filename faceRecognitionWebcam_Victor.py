import face_recognition
import faces_database
import cv2
import numpy as np

known_face_encodings = faces_database.known_face_encodings
known_face_names = faces_database.known_face_names

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


# capture1 = cv2.VideoCapture(2)#principal
# capture2 = cv2.VideoCapture('http://172.19.132.92:4747/video')#Victor
# capture3= cv2.VideoCapture('http://172.19.128.126:4747/video')#Nicolas
# capture4= cv2.VideoCapture('http://172.19.133.32:4747/video')#Eliot
capture5=cv2.VideoCapture('http://172.19.128.195:4747/video')#Salman


captures=[
    # capture1,
    # capture2,
    # capture3,
    # capture4
    capture5
          ]
while True:
    for capture in captures:
        frame_width = capture.get(3)
        frame_height = capture.get(4)
        # Grab a single frame of video
        ret, frame = capture.read()

        print(type(frame))

        # if capture!=capture1:
        frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame
        # [:, :, ::-1]
        # face_names = []
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

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
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            # name = str((left, top))
            # name = str((right, bottom))
            #name = str((frame_width, frame_height))
            name = face_names[0]
            # 1280, 716
            cv2.putText(frame, name, (left + 4, bottom - 4), font, 1, (0, 0, 255), 2)

        print(face_names==[])
        # Display the resulting image


        cv2.imshow(f'{capture}', frame)



        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release handle to the webcam
for capture in captures:
    capture.release()
cv2.destroyAllWindows()
