import cv2

cap = cv2.VideoCapture(0)
try:
    while (1):
        ret, frame = cap.read()
        print frame.shape
        print type(frame)
        continue
        cv2.imshow("capture", frame)

        cv2.waitKey(1)

except KeyboardInterrupt:
    print "release resources"
    cap.release()
    cv2.destroyAllWindows()
