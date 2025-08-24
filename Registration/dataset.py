import os
import cv2
import time
import csv

face_classifier = cv2.CascadeClassifier("Registration/haarcascade_frontalface_default.xml")
dir = "Dataset"
os.makedirs(dir, exist_ok=True)

def create_dataset(name):
    person = os.path.join(dir, name)
    os.makedirs(person, exist_ok=True)
    folder_path = person
    return folder_path

def detect_and_save_face(frame,name, face_id, folder_path):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("No face detected.")
        return False

    for (x, y, w, h) in faces:
        count = 0
        cropped_face = frame[y:y+h, x:x+w]
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, f"{name}_{count}.jpg")
        print(file_path)
        count += 1
        cv2.imwrite(file_path, cropped_face)
        print(f"Saved: {file_path}")
        return file_path
    return False

def capture_face_with_countdown(folder_path, name, face_id=0, countdown_seconds=5):
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

    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if ret:
        return detect_and_save_face(frame,name, face_id, folder_path)
    else:
        print("No frame captured to save face.")
        return False

def create(name):
    folder_path = create_dataset(name)
    print("Dataset created successfully.")
    capture_face_with_countdown(folder_path, name, face_id=0, countdown_seconds=5)

    data = {
        'name': name,
        'attendance_today': False,
        'attendance_timestamp': None,
        'total_attendance': 0
    }

    file_path = "attendance.csv"

    write_header = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

    with open(file_path, "a", newline="") as file:
        fieldnames = ['name', 'attendance_today', 'attendance_timestamp', 'total_attendance']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        print("Data to be written:", data)

        writer.writerow(data)
