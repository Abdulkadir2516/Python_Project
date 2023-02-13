import cv2
import numpy as np
import pyautogui as pg


def capture():
    pos = pg.position()

    s = pg.screenshot(region=(pos[0], pos[1], 1, 1))

    s = np.array(s)

    print(s[0, 0])


size = 20

while True:
    pos = pg.position()

    s = pg.screenshot(region=(pos[0] - size / 2, pos[1] - size / 2, size, size))

    im = cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR)

    im = cv2.resize(im, (size * 10, size * 10), interpolation=cv2.INTER_AREA)

    st = int((size * 10) / 2 - 5)
    ed = int((size * 10) / 2 + 5)

    im = cv2.rectangle(im, (st, st), (ed, ed), (0, 0, 0), 3)

    cv2.imshow("windows", im)

    if(cv2.waitKey(1) == ord("q")):
        capture()
    elif(cv2.waitKey(1) == ord("k")):
        break

cv2.destroyAllWindows()

