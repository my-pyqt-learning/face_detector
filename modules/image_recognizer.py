import cv2
import settings

cascade = cv2.CascadeClassifier(str(settings.CASCADE_CLASSIFIER_PATH))


# 引数imgで与えられた画像から顔を検出
# scale_factorで画像の縮小率を、min_sizeで検出する顔の最小サイズをそれぞれ指定
# 両方とも数字を大きくすると検出率が下がるが、検出にかかる時間が短くなる
def recognize_face(img, scale_factor=1.5, min_size=50):
    return cascade.detectMultiScale(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
        scaleFactor=scale_factor,
        minSize=(min_size, min_size)
    )


# 顔と認識された部分facesを長方形で囲む
# 顔が認識されなければ何も描画されない
def draw_rectangles(img, faces):
    for (face_x, face_y, width, height) in faces:
        cv2.rectangle(img, (face_x, face_y), (face_x + width, face_y + height), (255, 0, 0), 2)