import cv2
import numpy as np
import imutils
import shutil,os


shutil.rmtree('frames')
try:
    os.makedirs('frames')
except OSError as e:
    pass

video='2.mp4'

cap = cv2.VideoCapture(video)
cnt=0
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
ret,first_frame = cap.read()
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow("image",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    cv2.imwrite('frames/'+str(cnt)+'.png',frame)
    cnt=cnt+1
  else: 
    break

cv2.destroyAllWindows()
