import threading

import cv2
from deepface import DeepFace
import os

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

#reference_img = cv2.imread("3.jpg") 
reference_images = []
folder_path = "stored-faces"

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.png')):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)
        if img is not None:
            reference_images.append(img)



trueFace = 0
falseFace = 0
def check_face(frame):
    global trueFace
    global falseFace
    global face_match
    try:
        for ref_img in reference_images:
            if DeepFace.verify(frame, ref_img.copy())['verified']:
                trueFace += 1
            else:
                falseFace += 1
                
    except ValueError:
        falseFace += 1

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if trueFace >= falseFace:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()