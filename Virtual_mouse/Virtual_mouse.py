import cv2
import numpy as np
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

       
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

       
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append((cx, cy))

                # Index fingertip - landmark 8
                x, y = lm_list[8]

               
                screen_x = np.interp(x, [0, w], [0, screen_width])
                screen_y = np.interp(y, [0, h], [0, screen_height])

                pyautogui.moveTo(screen_x, screen_y)

                
                thumb_x, thumb_y = lm_list[4]

               
                distance = np.linalg.norm(np.array([x, y]) - np.array([thumb_x, thumb_y]))
                if distance < 30:
                    pyautogui.click()
                    cv2.putText(image, 'Click', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Virtual Mouse', image)

        if cv2.waitKey(1) & 0xFF == 27: 
            break

cap.release()
cv2.destroyAllWindows()
