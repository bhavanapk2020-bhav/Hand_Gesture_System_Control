import mediapipe as mp
import cv2
import pyautogui
import screen_brightness_control as sbc   # brightness control

# -----------------------
# Mediapipe Setup
# -----------------------
mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# -----------------------
# Webcam Setup
# -----------------------
video = cv2.VideoCapture(0)

# Track previous gesture
prev_finger_count = None

while True:
    success, img = video.read()
    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)

    tip_ids = [4, 8, 12, 16, 20]
    lm_list = []

    finger_count = 0  # default

    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            for id,lm in enumerate(hand_lm.landmark):
                # print(id,lm)
                cx = lm.x
                cy = lm.y
                lm_list.append([id,cx,cy])
            # print(lm_list)
            if len(lm_list) == 21:
                fingerlist = []
                # thumb
                if lm_list[8][1] < lm_list[20][1]:
                    if lm_list[4][1] > lm_list[3][1]:
                        fingerlist.append(0)
                    else:
                        fingerlist.append(1)
                else:
                    if lm_list[4][1] < lm_list[3][1]:
                        fingerlist.append(0)
                    else:
                        fingerlist.append(1)

                # Other fingers
                for i in range(1, 5):
                    fingerlist.append(1 if lm_list[tip_ids[i]][2] < lm_list[tip_ids[i] - 2][2] else 0)

                finger_count = fingerlist.count(1)
                print("Finger Count:", finger_count)

                # -----------------------
                # Gesture Actions (only trigger on change)
                # -----------------------
                if finger_count != prev_finger_count:  
                    if finger_count == 1:
                        sbc.set_brightness('+10')
                        print("Brightness Up")

                    elif finger_count == 2:
                        pyautogui.hotkey("win", "prtsc")
                        print("Screenshot Taken")

                    elif finger_count == 3:
                        pyautogui.hotkey("win", "tab")   # Task View
                        print("Task View Opened")

                prev_finger_count = finger_count  

            # Draw landmarks
            mp_drawings.draw_landmarks(
                img, hand_lm, mp_hands.HAND_CONNECTIONS,
                mp_drawings.DrawingSpec(color=(0, 0, 0), circle_radius=4, thickness=3),
                mp_drawings.DrawingSpec(color=(255, 255, 255), thickness=3)
            )
            cv2.putText(img, str(finger_count), (35, 400),cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 5)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()