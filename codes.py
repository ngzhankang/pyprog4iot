# import the necessary packages
import cv2
import time
import imutils
import argparse
import datetime
from imutils.video import VideoStream
from webcamvideostream import WebcamVideoStream


# defining VideoStream so that we can use our webcamera
class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240),
                 framerate=32):
        # check to see if the picamera module should be used
        if usePiCamera:
            # only import the picamera packages unless we are
            # explicity told to do so -- this helps remove the
            # requirement of `picamera[array]` from desktops or
            # laptops that still want to use the `imutils` package
            from pivideostream import PiVideoStream
            # initialize the picamera stream and allow the camera
            # sensor to warmup
            self.stream = PiVideoStream(resolution=resolution,
                                        framerate=framerate)
        # otherwise, we are using OpenCV so initialize the webcam
        # stream
        else:
            self.stream = WebcamVideoStream(src=src)

    def start(self):
        # start the threaded video stream
        return self.stream.start()

    def update(self):
        # grab the next frame from the stream
        self.stream.update()

    def read(self):
        # return the current frame
        return self.stream.read()

    def stop(self):
        # stop the thread and release any resources
        self.stream.stop()


# main ideas come in here
# import the necessary packages
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	# draw the timestamp on the frame
	timestamp = datetime.datetime.now()
	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 0, 255), 1)
	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()



















# # import the necessary packages
# from imutils.video import VideoStream
# import argparse
# import datetime
# import imutils
# import time
# import cv2

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", help="path to the video file")
# ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
# args = vars(ap.parse_args())

# # if the video argument is None, then we are reading from webcam
# if args.get("video", None) is None:
# 	vs = VideoStream(src=0).start()
# 	time.sleep(2.0)

# # otherwise, we are reading from a video file
# else:
# 	vs = cv2.VideoCapture(args["video"])

# # initialize the first frame in the video stream
# firstFrame = None

# # loop over the frames of the video
# while True:
# 	# grab the current frame and initialize the occupied/unoccupied
# 	# text
# 	frame = vs.read()
# 	frame = frame if args.get("video", None) is None else frame[1]
# 	text = "Unoccupied"

# 	# if the frame could not be grabbed, then we have reached the end
# 	# of the video
# 	if frame is None:
# 		break

# 	# resize the frame, convert it to grayscale, and blur it
# 	frame = imutils.resize(frame, width=500)
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	gray = cv2.GaussianBlur(gray, (21, 21), 0)

# 	# if the first frame is None, initialize it
# 	if firstFrame is None:
# 		firstFrame = gray
# 		continue

# 	# compute the absolute difference between the current frame and
# 	# first frame
# 	frameDelta = cv2.absdiff(firstFrame, gray)
# 	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

# 	# dilate the thresholded image to fill in holes, then find contours
# 	# on thresholded image
# 	thresh = cv2.dilate(thresh, None, iterations=2)
# 	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 		cv2.CHAIN_APPROX_SIMPLE)
# 	cnts = imutils.grab_contours(cnts)

# 	# loop over the contours
# 	for c in cnts:
# 		# if the contour is too small, ignore it
# 		if cv2.contourArea(c) < args["min_area"]:
# 			continue

# 		# compute the bounding box for the contour, draw it on the frame,
# 		# and update the text
# 		(x, y, w, h) = cv2.boundingRect(c)
# 		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# 		text = "Occupied"

# 	# draw the text and timestamp on the frame
# 	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
# 		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# 	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
# 		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

# 	# show the frame and record if the user presses a key
# 	cv2.imshow("Security Feed", frame)
# 	cv2.imshow("Thresh", thresh)
# 	cv2.imshow("Frame Delta", frameDelta)
# 	key = cv2.waitKey(1) & 0xFF

# 	# if the `q` key is pressed, break from the loop
# 	if key == ord("q"):
# 		break

# # cleanup the camera and close any open windows
# vs.stop() if args.get("video", None) is None else vs.release()
# cv2.destroyAllWindows()
