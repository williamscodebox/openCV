import cv2 as cv

# Re-Scaling 
#####################################################
# img = cv.imread("Photos/cat_large.jpg")

# cv.imshow("Cat", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)


# Reading Videos
######################################################
# capture = cv.VideoCapture(0) # Use this to open WebCam
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
