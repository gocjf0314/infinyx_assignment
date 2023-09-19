# Infinyx_assignment

- Assignment for joining infinyx
- Developed in Window environment
- Execution directory is 'face_rm' or 'face_swap'

## Ref-Links

[python development ref with CV](https://datascienceschool.net/intro.html)
[data set link](https://www.kaggle.com/datasets/selfishgene/youtube-faces-with-facial-keypoints)

### Face Detection

- [model: buffalo_l](https://drive.google.com/file/d/13Pz8mH-a1s7RXpq_jFUXxaqCpDUE0oSr/view)
- [source code](https://github.com/deepinsight/insightface/tree/master/alignment)

### Swap faces

- [model: inswap_128](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view)
- [source code](https://github.com/deepinsight/insightface/tree/master/examples/in_swapper)

### Python packages

- [numpy official docs](https://numpy.org/doc/stable/user/index.html)
- [Reason about using numpy](https://blog.naver.com/nackji80/222988466129)
- [openCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [scikit-image](https://scikit-image.org/docs/stable/)
- [matplolib official docs](https://matplotlib.org/stable/index.html)
- [matplolib post](https://wikidocs.net/124976)
- [insightface](https://github.com/deepinsight/insightface)

### Other concepts

- [Image Preprocessing](https://datascienceschool.net/03%20machine%20learning/03.02.01%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%B2%98%EB%A6%AC%20%EA%B8%B0%EC%B4%88.html#)
- [KMeans algorithm](https://velog.io/@jhlee508/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-K-%ED%8F%89%EA%B7%A0K-Means-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
- [Affine transformation](https://kr.mathworks.com/discovery/affine-transformation.html)
- [Image rotate and affine transformation](https://aliencoder.tistory.com/57)
- [Image Blending](https://dsbook.tistory.com/155)

## Version Checking

NVIDIA GPU Version

```powershell
nvidia-smi
```

CUDA Version

```powershell
nvcc -V
nvcc --version
```

## Activate conda

- Run 'Anaconda Pormpt'
- Run below CLI

```powershell
conda activate name
```

## Install python dependencies

```powershell
pip install -r requirements.txt
```
