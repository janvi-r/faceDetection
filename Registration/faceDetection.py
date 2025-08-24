import os
import threading
import cv2
from deepface import DeepFace

from attendance import mark_attendance

match_found = False
matched_filename = None

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
                break
            else:
                print(f"Comparing with {filename}: No match")
    except Exception as e:
        match_found = False
        matched_filename = None
        print("Error during face verification:", e)



