import numpy as np
import pyautogui
import cv2

image = pyautogui.screenshot(region=(0,0, 1920, 1080))

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("pic.png", image)
