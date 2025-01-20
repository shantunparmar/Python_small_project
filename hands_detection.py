import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize hands detection
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a better selfie-view experience
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # You can track finger positions here 
            for landmark in hand_landmarks.landmark:
                # You can access the x, y, z coordinates of each finger joint here
                print(f"X: {landmark.x}, Y: {landmark.y}, Z: {landmark.z}")
                
                # you can use specific landmarks to track fingers (e.g., tip of the index finger)
                if landmark == hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]:
                    print("Index Finger Tip coordinates: ", landmark.x, landmark.y, landmark.z)

    # Display the frame with hand landmarks
    cv2.imshow("Finger Movement Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
