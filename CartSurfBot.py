import cv2, pyautogui, time, numpy as np
from PIL import ImageGrab

pyautogui.FAILSAFE = False
YELLOW_LOWER = np.array([217, 174, 0], dtype="uint8")
YELLOW_UPPER = np.array([255, 255, 170], dtype="uint8")


def back_flip():  # performs a back flip
    pyautogui.press("down")
    pyautogui.press("space")
    print("back-flipping")


def cart_slam():  # performs a cart slam
    pyautogui.press("space")
    pyautogui.press("down")
    print("cart-slamming")


def drift(dir):  # performs a drift turn
    pyautogui.keyDown("down")
    pyautogui.keyDown(dir)
    print("drifting " + dir)
    time.sleep(1)
    pyautogui.keyUp("down")
    pyautogui.keyUp(dir)


def debug(grab):  # method to view what the program is seeing for bug testing
    cv2.imshow("Frame", grab)                                          # raw capture
    cv2.imshow("Mask", cv2.inRange(grab, YELLOW_LOWER, YELLOW_UPPER))  # yellow masked capture (what it's detecting)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_sign(dir, x1, y1, x2, y2):
    frame_grab = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # capture information on screen in XY region
    frame = np.array(frame_grab)                        # convert information to image
    # debug(frame)
    if 255 in cv2.inRange(frame, YELLOW_LOWER, YELLOW_UPPER):  # detect for yellow in captured image
        cart_slam()     # get some extra points and allow full 100 for next back flip
        time.sleep(.4)  # wait .4 seconds
        drift(dir)      # perform a drift in the necessary direction
        back_flip()     # perform a back flip after the drift/turn


while True:
    detect_sign("right", 400, 640, 1000, 955)
    detect_sign("left", 1500, 640, 2000, 955)
