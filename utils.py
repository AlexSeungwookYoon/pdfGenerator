import json
from PIL import Image, ImageTk
#프로그램의 가장 처음화면 로고를 load 하는 함수
def load_main_image():
    image = Image.open('img/main_image.png')
    return image 
#pillow type image를 tk type image 로 convert 하는 함수 
def pillow_to_tk_image(pillow_image):
    imgtk = ImageTk.PhotoImage(image= pillow_image)
    return imgtk