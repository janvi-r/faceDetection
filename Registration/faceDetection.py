import cv2
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

        timestamp = int(time.time())
        file_path = os.path.join(folder_path, f"{face_id}_{timestamp}.jpg")
        cv2.imwrite(file_path, cropped_face)
        print(f"Saved: {file_path}")
        return file_path
    return False

def capture_face_with_countdown(face_id=0, countdown_seconds=5):
    cap = cv2.VideoCapture(0)
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from camera.")
            break

        elapsed = int(time.time() - start_time)
        countdown = countdown_seconds - elapsed

        if countdown > 0:
            cv2.putText(frame, f"Taking photo in: {countdown}s", (50, 400),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        cv2.imshow("Face Capture", frame)

        if cv2.waitKey(1) == ord("q") or countdown <= 0:
            break

    # Capture face after countdown
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if ret:
        return detect_and_save_face(frame, face_id)
    else:
        print("No frame captured to save face.")
        return False
