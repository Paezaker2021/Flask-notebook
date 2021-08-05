import cv2
import time, random
import os
import HandTrackingModule as htm
from DB_handler import DBModule

DB=DBModule()
Verify = False
uid = 'NONE'
randomint = random.randrange(1,6)

def activate(verify):
    DB.verify_notbot(Verify, uid)
    cv2.destroyAllWindows()
    exit()

while(True):
    print('자동가입 방지 프로그램입니다. 아이디와 비밀번호를 입력해주세요.')
    uid = input('ID :')
    pwd = input('PW :')

    if DB.login(uid, pwd):
        print('※※자동가입 방지 : 손으로 숫자', randomint, '를 5초 이상 만들어 보세요.※※\n(진행 창이 표시되지 않거나 인증이 되지 않을 수 있습니다. 그럴 땐 다시 진행해주세요.)')
        pass
    else:
        print('아이디가 존재하지 않거나, 아이디 또는 비밀번호가 일치하지 않습니다.')
        continue

    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, wCam)
    cap.set(4, hCam)

    # folderPath = "FingerImages"
    # myList = os.listdir(folderPath)
    # print(myList)
    # overlayList = []
    # for imPath in myList:
    # image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    # overlayList.append(image)

    # print(len(overlayList))
    pTime = 0
    before = -1
    before_t = time.time()

    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]
    start = time.time()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)

            current_t = time.time()
            sec = current_t - before_t

            if totalFingers == randomint and int(sec) >= 5:
                Verify = 'T'
                activate(Verify)

            if totalFingers != randomint and int(sec) >= 2:
                print('올바르지 않은 숫자를 인식했습니다.')

            if int(sec)>=60:
                print('60초가 지나서 종료되었습니다. 다시 진행해 주세요.')
                break

            if before != totalFingers:
                before = totalFingers
                before_t = current_t
            else:
                cv2.rectangle(img, (0, 470), (640, 480), (200, 200, 200), -1)
                cv2.rectangle(img, (0, 470), (int(sec / 5 * 640), 480), (0, 255, 0), -1)
            # h, w, c = overlayList[totalFingers-1].shape
            # img[0:h, 0:w] = overlayList[totalFingers-1]

            # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
        else:
            if int(time.time()-start) >= 50:
                print('10초 뒤에 자동 종료가 됩니다.')
                exit()
            if int(time.time()-start) >= 60:
                print('60초가 지나서 종료되었습니다. 다시 진행해 주세요.')
                exit()
            before_t = time.time()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        title = "Show number :\"" + str(randomint) + "\" in front of Camera"
        cv2.imshow(title, img)
        cv2.waitKey(1)

