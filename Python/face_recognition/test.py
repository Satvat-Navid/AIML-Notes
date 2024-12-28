import cv2 # type: ignore
import numpy as np
import time

cap = cv2.VideoCapture(0)
i = 22
t1 = time.time()

while(i):

    ret, frame = cap.read()
    print(frame)
    arr = np.array(frame)
    print(len(frame))
    print(arr.shape)
    print(arr.size)
     # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break
    cv2.imshow("Video", frame)

    i = i-1

t2 = time.time()
print(t2 - t1)
cap.release()
cv2.destroyAllWindows()