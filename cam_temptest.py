import cv2 
import numpy as np

goFlag=0

def mouse_click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goFlag
    if event==cv2.EVENT_LBUTTONDOWN:
        x1=x
        y1=y
        goFlag=0
    if event==cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y
        goFlag=1

cv2.namedWindow('Thermal Image')
cv2.setMouseCallback('Thermal Image',mouse_click)
dispW=640
dispH=480
flip=2

cam=cv2.VideoCapture(1)

# def rescale_frame(frame, percent=25):
#     width = int(frame.shape[1] * percent/ 15)
#     height = int(frame.shape[0] * percent/ 15)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def kelvin_to_celsius(val):
    return (val - 27315) / 1000

while True:
    ret, frame = cam.read()
    #cv2.imshow('nanoCam',frame)#to show the frame of the nanoCam
   
    # frame1= rescale_frame(frame, percent=25)
    frame1 = cv2.resize(frame, (700, 500))
    cv2.imshow('Thermal Image', frame1)

    if goFlag==1:
        frame1=cv2.rectangle(frame1,(x1,y1),(x2,y2),(255,0,0),3)
        roi=frame1[y1:y2,x1:x2]#position of the rectangle in ROI

        roi1 = cv2.resize(roi, (700, 500))
        cv2.imshow('New Selection',roi1)
        cv2.moveWindow('New Selection',705,0)
       
    cv2.moveWindow('Thermal Image',0,0) 
    if cv2.waitKey(1)==ord('q'):
        break
# IR_array = np.array(roi1)
# IR_array_C = kelvin_to_celsius(IR_array)
# print(IR_array_C)    
# print("The Maximum Temperature is:", IR_array_C.max(), "degree Celsius")

cam.release()
cv2.destroyAllWindows()
