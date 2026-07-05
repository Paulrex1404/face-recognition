import cv2
import os
# Ask the user for their name
name = input("Enter your name: ")
# Check if dataset folder exists
if not os.path.exists("dataset"):
    os.makedirs("dataset")
# Start webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Capture Face")
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    cv2.imshow("Capture Face", frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = f"dataset/{name}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved!")
        break
cam.release()
cv2.destroyAllWindows()