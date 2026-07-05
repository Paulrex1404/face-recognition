import face_recognition
import os
import cv2

known_face_encodings = []
known_face_names = []

dataset_path = "dataset"
for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(dataset_path, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_face_names.append(name)
            print(f"Encoded {name}")
        else:
            print(f"No face found in {filename}, skipping.")

# ✅ Save encodings for use in main script (optional)
import pickle

with open("encodings.pkl", "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("All face encodings saved.")