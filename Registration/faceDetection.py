#file_path = capture_face_with_countdown(face_id=0, countdown_seconds=5)
import os
import time
#from Authentication.mainMultiImg import everything

import threading
import cv2
from deepface import DeepFace

match_found = False
matched_filename = None

def everything():
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

    print(f"Loaded {(reference_images)} reference images from {folder_path}") 
    match_found = False
    matched_filename = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if counter % 30 == 0 and not match_found:
            try:
                threading.Thread(target=check_face, args=(frame.copy(), reference_images)).start()
            except Exception as e:
                print("Thread error:", e)

        counter += 1

        if match_found:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            if matched_filename:
                print(f"Matched with: {matched_filename}")
 
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return reference_images



def check_face(frame, reference_images):
    global match_found, matched_filename
    if match_found:
        return
    try:
        for ref_img, filename in reference_images:
            result = DeepFace.verify(frame, ref_img.copy(), enforce_detection=False)
            if result['verified']:
                match_found = True
                matched_filename = filename
                break
    except Exception as e:
        print("Error:", e)


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
    # name = input("Enter your name: ")
    # folder_path = create_dataset(name)
    # print("Dataset created successfully.")
    # capture_face_with_countdown(folder_path, name, face_id=0, countdown_seconds=5 )
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

