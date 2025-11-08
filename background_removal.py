import cv2
import numpy as np
import mediapipe as mp

mp_selfie = mp.solutions.selfie_segmentation
segment = mp_selfie.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)

# Default background is solid color (green)
background_mode = "color"
bg_color = (0, 255, 0)
bg_image = None

def select_background_color():
    # Open a blank UI window
    color = np.zeros((150, 450, 3), dtype=np.uint8)
    cv2.rectangle(color, (10, 10), (140, 140), (255, 0, 0), -1)   # Blue
    cv2.rectangle(color, (160, 10), (290, 140), (0, 255, 0), -1) # Green
    cv2.rectangle(color, (310, 10), (440, 140), (0, 0, 255), -1) # Red
    cv2.imshow("Select Color", color)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('1'):
            return (255, 0, 0)
        elif key == ord('2'):
            return (0, 255, 0)
        elif key == ord('3'):
            return (0, 0, 255)
        elif key == ord('q'):
            break

    cv2.destroyWindow("Select Color")
    return None

def select_background_image():
    filename = input("Enter background image name (example: room.jpg): ")

    try:
        img = cv2.imread(filename)
        if img is not None:
            img = cv2.resize(img, (640, 480))
            print("✅ Image loaded successfully.")
            return img
        else:
            print("❌ Image not found.")
            return None
    except:
        print("❌ Error loading image.")
        return None

print("✅ Controls:")
print("Press C = Choose solid color background")
print("Press I = Choose custom background image")
print("Press Q = Quit")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = segment.process(rgb)
    mask = (result.segmentation_mask > 0.6).astype(np.uint8)

    # Decide background type
    if background_mode == "color":
        background = np.zeros_like(frame)
        background[:] = bg_color
    else:
        background = bg_image

    # Combine person + background
    output = frame * mask[:, :, None] + background * (1 - mask[:, :, None])

    cv2.imshow("Background Removal Project", output)

    key = cv2.waitKey(1) & 0xFF

    # ✅ Select background color
    if key == ord('c'):
        print("🎨 Select color: Press 1=Blue, 2=Green, 3=Red")
        selected = select_background_color()
        if selected:
            bg_color = selected
            background_mode = "color"

    # ✅ Select background image
    if key == ord('i'):
        print("🖼 Type the image filename in terminal:")
        img = select_background_image()
        if img is not None:
            bg_image = img
            background_mode = "image"

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
