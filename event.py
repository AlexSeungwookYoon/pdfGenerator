from tkinter import filedialog
import tkinter as tk
from PIL import Image
import json

from utils import pillow_to_tk_image

def start_event( root, label, json_dict, image_size):

    img = Image.new(mode = 'RGB', size = image_size)
    imgtk = pillow_to_tk_image(img)

    label.config(image=imgtk)
    label.image = imgtk


def load_event( root, label, json_dict, image_size):
    root.file = filedialog.askopenfile(
        initialdir = 'path',
        title = '사용자 정의 json 파일을 선택해주세요',
        filetypes = (('json files', '*.json'), ('all files', '*.*'))

    )
    json_dict['image'] = True
    print(json_dict)
    print(root.file.name)


    


def save_event( root, label, json_dict, image_size):
    with open('user_defined_layout.json', 'w') as f:
        json.dump(json_dict, f, indent ='\t')
        print("saved")
        popup_window = tk.Toplevel()
        popup_window.title("popup screen")
        popup_window.geometry("200x200")
        label = tk.Label(popup_window, text = "저장완료")
        label.pack()
        
        


