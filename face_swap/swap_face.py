import datetime
import numpy as np
import os
import os.path as osp
import glob
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

assert insightface.__version__>='0.7'

if __name__ == '__main__':
    # 얼굴 분석 및 분류 모델 지정
    app = FaceAnalysis(name='buffalo_l')
    
    # 얼굴 프레임 사이즈 지정
    app.prepare(ctx_id=0, det_size=(640, 640))

    # 얼굴 합성 모델 지정
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx')

    # 이미지 가져오기
    # img = ins_get_image('t1')
    img = cv2.imread("test_img_2.jpg")

    # 받아온 이미지로 부터 얼굴 추출
    faces = app.get(img)
    faces = sorted(faces, key = lambda x : x.bbox[0])
    
    # 합성시킬 이미지 지정
    source_face = faces[0]
    res = img.copy()

    # 추출한 얼굴에 source_face 합성
    for face in faces:
        res = swapper.get(res, face, source_face, paste_back=True)
    cv2.imwrite("./test_swapped_img_full.jpg", res)

    # source_face 합성하고 얼굴만 따로 추출
    res = []
    for face in faces:
        _img, _ = swapper.get(img, face, source_face, paste_back=False)
        res.append(_img)
    res = np.concatenate(res, axis=1)
    cv2.imwrite("./test_swapped_img_faces.jpg", res)