import cv2
import face_recognition
import face_recognition_models

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names here
known_person1_image = face_recognition_models.load_image_file(r"D:\MLCOE\task3\Prakhar.jpg")
known_person3_image = face_recognition_models.load_image_file(r"D:\MLCOE\task3\shahrukh khan.jpg")

known_person1_encoding = face_recognition_models.face_encodings(known_person1_image)[0]
known_person3_encoding = face_recognition_models.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("Prakhar")
known_face_names.append("Shahrukh Khan")

# Initialize Webcam
Video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = Video_capture.read()

    # Find all face locations in the current frame
    face_locations = face_recognition_models.face_locations(frame)
    face_encodings = face_recognition_models.face_encodings(frame, face_locations)

    # Loop through each found face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        # Redirect to the recognized page
        #return redirect(url_for('final.html'))
  
        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
Video_capture.release()
cv2.destroyAllWindows()