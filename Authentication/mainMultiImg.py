import threading
import cv2
from deepface import DeepFace
import os
import shelve
#####from Registration.student import getstudentName
import sys
sys.path.append('/Users/janvi/hello/Registration')
# from student import Student
####import Registration.student as student
####import getstudentName
# from Registration.student import Student

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
folder_path = "/Users/janvi/hello/Registration/stored-faces"

# List of tuples: (image, filename)
reference_images = []
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.png')):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)
        if img is not None:
            reference_images.append((img, filename))  # store tuple

match_found = False
matched_filename = None

def check_face(frame):
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

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if counter % 30 == 0 and not match_found:
        try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
        except Exception as e:
            print("Thread error:", e)

    counter += 1

    if match_found:
        cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        if matched_filename:
            print(f"Matched with: {matched_filename}")
            with shelve.open('studentInfo.db') as db:
                folder_path = "/Users/janvi/hello/Registration/stored-faces"
                full_path = os.path.join(folder_path, matched_filename)
                
                try:
                    data = db[full_path]
                    print(f"Full path: {data}")
                except KeyError:
                    print(f"No data found for {full_path}")
                    print(data)


                
            
    else:
        cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
