import cv2
import numpy as np
def event_mouse(events, x, y, flags, para):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+', '+str(y)
        cv2.putText(img, strXY,(x, y), font, .5, (207,27,153), 2)
        cv2.imshow('image', img)
    if events == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        strBGR = str(blue)+', '+str(green)+', '+str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strBGR, (x, y), font, .5, (255,255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('messi.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image',event_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
