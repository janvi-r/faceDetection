import cv2
import numpy as np
import os
import time

face_classifier = cv2.CascadeClassifier("/Users/janvi/hello/Registration/haarcascade_frontalface_default.xml")

def detect_and_save_face(frame, face_id):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("No face detected.")
        return False

    for (x, y, w, h) in faces:
        cropped_face = frame[y:y+h, x:x+w]
        folder_path = "/Users/janvi/hello/Registration/stored-faces"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"{face_id}.jpg")
        cv2.imwrite(file_path, cropped_face)
        print(f"Saved: {file_path}")
        return file_path
    return False

    #take the file_path and save it to the dictionary for each student

cap = cv2.VideoCapture(0)
face_id = 0
start_time = time.time()

# Countdown loop (10 seconds)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    elapsed = int(time.time() - start_time)
    countdown = 10 - elapsed
    if countdown > 0:
        cv2.putText(frame, f"Taking photo in: {countdown}s", (50, 400),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    cv2.imshow("Face Capture", frame)

    if cv2.waitKey(1) == ord("q"):
        break
    if countdown <= 0:
        break

# Capture face after countdown
ret, frame = cap.read()
if ret:
    detect_and_save_face(frame, face_id)

cap.release()
cv2.destroyAllWindows()
