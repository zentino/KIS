# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from actions import Actions
from QLearningAgent import QLearningAgent
from color_detector import ColorDetector

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

def start():
    a = Actions()
    c = ColorDetector()
    states = 2
    actions = 3
    action = 0
    state = 0
    nextState = 0
    ballvisible = True
    q = QLearningAgent(3, 2)
    # allow the camera to warmup
    time.sleep(0.1)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    res = c.prepareImage(image)
    redPixel = c.isCenter(res)[1]

    if redPixel > 0:
        state = 0
    else:
        state = 1

    while True:
        action = q.chooseAction(state)
        if action == 0:
            a.rotateRight()
        elif action == 1:
            a.rotateLeft()
        else:
            a.walkStraight()

        time.sleep(0.1)
	rawCapture.truncate(0)
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        res = c.prepareImage(image)
        isCenter, pixelCount = c.isCenter(res)

        if pixelCount > 0:
            nextState = 0
            ballVisible = True
        else:
            nextState = 1
            ballVisible = False

        if isCenter and pixelCount > redPixel:
            q.learn(state, nextState, action, 3)
        elif isCenter:
            q.learn(state, nextState, action, 2)
        elif ballVisible:
            q.learn(state, nextState, action, 1)
        else:
            q.learn(state, nextState, action, -1)


        state = nextState
        redPixel = pixelCount


start()
