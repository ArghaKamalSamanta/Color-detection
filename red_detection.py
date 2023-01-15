import cv2

# Capturing video
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    if not ret:
        break
    
    # Converting to LAB color space
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    # Performing the Otsu threshold on the A-channel 
    thresh = cv2.threshold(lab[:,:,1], 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.imshow("Camera footage", frame)
    cv2.imshow("Detecting red...", thresh)

    # Press q to stop capturing video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()