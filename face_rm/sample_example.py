# Detecting faces at the image file and Pointing randmarks

import cv2
import numpy as np
from insightface.app import FaceAnalysis
# from insightface.data import get_image

if __name__ == '__main__':
    # 기본 모델로 buffalo_1 사용
    # options: 감지, 2d이미지에 106개 랜드마크 지정
    app = FaceAnalysis(allowed_modules=['detection', 'landmark_2d_106'])

    # 검출 사이즈 지정
    app.prepare(ctx_id=0, det_size=(640, 640))

    # package에 있는 이미지 가져오기
    # img = get_image("t1")
    img = cv2.imread("sample_img.jpg")

    # 얼굴 분류기 사용을 위한 모델로 부터 얼굴 검출
    faces = app.get(img)

    # 결과물을 위해 이미지 복사
    tim = img.copy()

    # 랜드마크 생상 지정
    color = (200, 160, 75)

    # 검출 된 얼굴 별로 랜드마크 포인팅
    for face in faces:
        # 좌표 정보 받아오기(float32)
        lmk = face.landmark_2d_106

        # 정수형태(np.int32)로 좌표값들 타입 변환
        lmk = np.round(lmk).astype(np.int32)

        # 좌표값들이 모인 데이터 looping
        for i in range(lmk.shape[0]):
            # 점 하나에 대한 좌표 정보
            p = tuple(lmk[i])

            # 위 좌표 정보를 이용하여 점 찍기
            cv2.circle(tim, p, 1, color, 1, cv2.LINE_AA)

    # 검출된 얼굴에 랜드마크를 찍은 이미지 저장
    cv2.imwrite('sample_out.jpg', tim)