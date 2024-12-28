import cv2 # type: ignore
import face_recognition

# Load known face encoding and names
known_face_encodings = []
known_face_names = []

#Load known faces and their names.
known_p1_image = face_recognition.load_image_file("1.png")
img = cv2.cvtColor(known_p1_image, cv2.COLOR_BGR2RGB)
# known_p8_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\rayan.jpg")
# known_p7_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\waleed.jpg")
# known_p2_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\kaif.jpg")
# known_p3_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\tushar.jpg")
# known_p4_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\amit.jpg")
# known_p5_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\abuzar.jpg")
# known_p6_image = face_recognition.load_image_file("D:\\MLCODE\\Python\\face_recognition\\shivam.jpg")

known_p1_encoding = face_recognition.face_encodings(img)[0]
# known_p8_encoding = face_recognition.face_encodings(known_p8_image)[0]
# known_p7_encoding = face_recognition.face_encodings(known_p7_image)[0]
# known_p2_encoding = face_recognition.face_encodings(known_p2_image)[0]
# known_p3_encoding = face_recognition.face_encodings(known_p3_image)[0]
# known_p4_encoding = face_recognition.face_encodings(known_p4_image)[0]
# known_p5_encoding = face_recognition.face_encodings(known_p5_image)[0]
# known_p6_encoding = face_recognition.face_encodings(known_p6_image)[0]

known_face_encodings.append(known_p1_encoding)
# known_face_encodings.append(known_p8_encoding)
# known_face_encodings.append(known_p7_encoding)
# known_face_encodings.append(known_p2_encoding)
# known_face_encodings.append(known_p3_encoding)
# known_face_encodings.append(known_p4_encoding)
# known_face_encodings.append(known_p5_encoding)
# known_face_encodings.append(known_p6_encoding)

known_face_names.append("Naveed")
# known_face_names.append("Rayan")
# known_face_names.append("Waleed")
# known_face_names.append("Kaif")
# known_face_names.append("Tushar")
# known_face_names.append("Amit")
# known_face_names.append("Abuzar")
# known_face_names.append("Shivam")

# Initialize webcam
video_capture = cv2.VideoCapture(0) #Real time face recognition

while True:
    #Capture frame by frame.
    ret, frame = video_capture.read()

    #find all face location in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #Check if the face matches to any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with name.
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


     # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break

    # Display the resulting frame
    cv2.imshow("Video", frame)

# Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()