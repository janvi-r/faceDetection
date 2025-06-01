import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("/Users/janvi/hello/haarcascade_frontalface_default.xml")

# Global counter for image filenames
face_id = 0

def detect_faces(img):
    global face_id
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return img
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cropped_image = img[y:y + h, x:x + w]
        target_file_name = 'stored-faces/' + str(face_id) + '.jpg'
        cv2.imwrite(target_file_name, cropped_image)
        face_id += 1


    return img

cap = cv2.VideoCapture(0)

#eachList = set()

counter = 0
while True:
    counter += 1
    ret, frame = cap.read()
    if not ret:
        break
    if counter%60:
        frame = detect_faces(frame)

    #if frame == frame:
       # eachList.append(frame)
        

    cv2.imshow("Video Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
