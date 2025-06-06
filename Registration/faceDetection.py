import os
import time
import csv
import threading
import cv2
from deepface import DeepFace
import pandas as pd

match_found = False
matched_filename = None

def mark_attendance(name, attendance):
    print("in mark_attendance")
    with open("attendance.csv") as file:
        df = pd.read_csv("attendance.csv")  
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print("Found the row:", row)
               # row[1] = attendance
              #  print(row[1])
                df["attendance"] = df["attendance"].replace(False, True)
                
               # row[1] = row[1].replace("False", "True")


    # line_number = 0
    # found_line = None

    # with open('attendance.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for i, row in enumerate(reader, start=1):
    #         if name in row:
    #             line_number = i
    #             found_line = row
    #             break
    # if found_line:
    #     csvFile = pd.read_csv("attendance.csv")
    #     csvFile.loc[line_number, 'attendance_today'] = attendance
    #     csvFile.loc[line_number, 'total_attendance'] += 1
    #     csvFile.loc[line_number, 'attendance_timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")

    #     csvFile.to_csv("attendance.csv", index=False)
    # else:
    #     print(f"this should never happen - replace later lol")

def everything():
    global match_found, matched_filename
    counter = 0
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    folder_path = "Dataset"

    reference_images = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.png')):
                img_path = os.path.join(foldername, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    reference_images.append((img, filename)) 

    print(f"Loaded {len(reference_images)} reference images from {folder_path}") 

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if ret:
            if counter % 30 == 0 and not match_found:
                try:
                    threading.Thread(target=check_face, args=(frame.copy(), reference_images)).start()
                    #check_face(frame.copy(), reference_images)
                except Exception as e:
                    print("Thread error:", e)
            counter += 1

        if match_found:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            if matched_filename:
                print(f"Matched with: {matched_filename}")
                name = matched_filename[:matched_filename.find("_")]
               # print(name)
                mark_attendance(name, True)
                break
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)


        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

    return reference_images

def check_face(frame, reference_images):
    global match_found, matched_filename
    try:
        for ref_img, filename in reference_images:
            if DeepFace.verify(frame, ref_img.copy())['verified']:
                match_found = True
                matched_filename = filename
                print(f"Matched with: {matched_filename}")
                # If a match is found, we can break out of the loop, and then do the attendance part
                break
            else:
                print(f"Comparing with {filename}: No match")
    except Exception as e:
        match_found = False
        matched_filename = None
        print("Error during face verification:", e)
    # try:
    #     for ref_img, filename in reference_images:
    #         result = DeepFace.verify(frame, ref_img.copy(), enforce_detection=False)
    #         print(f"Comparing with {filename}: {result['verified']}")
    #         if result['verified']:
    #             match_found = True
    #             matched_filename = filename
    #             break
    # except Exception as e:
    #     print("Error:", e)


face_classifier = cv2.CascadeClassifier("Registration/haarcascade_frontalface_default.xml")

dir = "Dataset"
os.makedirs(dir, exist_ok=True)

def create_dataset(name):
    person = os.path.join(dir, name)
    os.makedirs(person, exist_ok=True)
    folder_path = person  # Define folder_path for saving images
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
       # #folder_path = "/Users/janvi/hello/Registration/stored-faces"
        os.makedirs(folder_path, exist_ok=True)

        #timestamp = int(time.time())
    #WE CAN HAVE MULTIPLE IMAGES FOR THE SAME PERSON, BUT YOU'd NEED TO add to the count so it doesn't replace existing image or use timestamp
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

    # Capture face after countdown
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if ret:
        return detect_and_save_face(frame,name, face_id, folder_path)
    else:
        print("No frame captured to save face.")
        return False

def main():
#     name = input("Enter your name: ")
#     folder_path = create_dataset(name)
#     print("Dataset created successfully.")
#     capture_face_with_countdown(folder_path, name, face_id=0, countdown_seconds=5)

#     data = {
#         'name': name,
#         'attendance_today': False,
#         'attendance_timestamp': None,
#         'total_attendance': 0
#     }

#     file_path = "attendance.csv"

# # Check if the file already exists and is non-empty
#     write_header = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

#     with open(file_path, "a", newline="") as file:
#         fieldnames = ['name', 'attendance_today', 'attendance_timestamp', 'total_attendance']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         if write_header:
#             writer.writeheader()  # Write header only if file is new or empty

#         writer.writerow(data)     # Write the actual data row
 


    everything()

main()


    # cap = cv2.VideoCapture(0)
    # count = 0

    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         print("Failed to capture frame from camera.")
    #         break

    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     #faces = cv2.CascadeClassifier(cv2.data.haarcascades + "/Users/janvi/hello/Registration/haarcascade_frontalface_default.xmal")
    #     faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    #     for (x, y, w, h) in faces:
    #         face_img = frame[y:y+h, x:x+w]
    #         face_path = os.path.join(folder_path, f"{name}_{count}.jpg")
    #         cv2.imwrite(face_path, face_img)

    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
    #         cv2.imshow("Face Capture")
            
    #         if cv2.waitkey(1) == ord("q") & 0xFF==ord(1) or count >= 50:
    #             break

    # cap.release()
    # cv2.destroyAllWindows()  



# def detect_and_save_face(frame, face_id, name):
#     count = 0
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray, 1.3, 5)

#     if len(faces) == 0:
#         print("No face detected.")
#         return False

#     for (x, y, w, h) in faces:
#         cropped_face = frame[y:y+h, x:x+w]
#         # folder_path = "/Users/janvi/hello/Registration/stored-faces"
#         folder_path = os.path.join(folder_path, f"{name}_{count}.jpg")
#         cv2.imwrite(folder_path, cropped_face)
#         # os.makedirs(folder_path, exist_ok=True)
        
#         count += 1
        
#         # cv2.imwrite(file_path, cropped_face)
#         print(f"Saved: {folder_path}")
#         return folder_path

#     return False

# def capture_face_with_countdown(face_id=0, countdown_seconds=5):
#     cap = cv2.VideoCapture(0)
#     start_time = time.time()

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture frame from camera.")
#             break

#         elapsed = int(time.time() - start_time)
#         countdown = countdown_seconds - elapsed

#         if countdown > 0:
#             cv2.putText(frame, f"Taking photo in: {countdown}s", (50, 400),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
#         cv2.imshow("Face Capture", frame)

#         if cv2.waitKey(1) == ord("q") & 0xFF == ord(1):
#             break

#     # Capture face after countdown
#     ret, frame = cap.read()
#     cap.release()
#     cv2.destroyAllWindows()

#     if ret:
#         return detect_and_save_face(frame, face_id)
#     else:
#         print("No frame captured to save face.")
#         return False