import numpy as np
import cv2
from insightface.app import FaceAnalysis

# haarcascade_frontalface_default.xml 파일을 Classifier로 사용
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

app = FaceAnalysis(allowed_modules=['detection', 'landmark_2d_106'])
app.prepare(ctx_id=0, det_size=(640, 480))

# Video Capture 기본 카메라 모드(0)로 생성
cap = cv2.VideoCapture(0)

# captture 높이, 너비 지정
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

# 랜드마크 색상 지정
color = (200, 160, 75)

while True:
    # cap.read() - 카메라 영상 동작 시 프레임과 동작 성공여부 read
    # img: 영상 프레임
    # ret: 동작 성공 여부
    ret, img = cap.read()
    if ret is False:
        print("Error: Faile to capture image")
        break
    
    # cv2.flip() - 이미지 반전 및 회전
    # 1: 좌우 반전
    # 0: 상하 반전
    img = cv2.flip(img, 1)

    # 이미지 지정 후 랜드마크를 표시할 얼굴 정보 가져오기
    faces = app.get(img)

    for face in faces:
        # 한 얼굴에 대한 랜드마크 정보 할당
        # [[a, b], [c, d], ....]
        lmk = face.landmark_2d_106

        # 위 랜드마크 좌표 값들을 정수로 변환
        lmk = np.round(lmk).astype(np.int32)
        for i in range(lmk.shape[0]):
            # 좌표값 할당: [a, b]
            p = tuple(lmk[i])

            # 이미지에 해당하는 좌표값에 랜드마크 표시
            # 원을 찍을 이미지, 중심, 색, 반지름, 선 굵기, 선 스타일
            cv2.circle(img, p, 1, color, 1, cv2.LINE_AA)

    # video라는 이름으로 화면에 가공된 이미지 출력
    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit # ESC를 누르면 종료
        break

# 캡쳐 도구 dispose
cap.release()

# 비디오 스트림 및 모든 화면 dispose
cv2.destroyAllWindows()
