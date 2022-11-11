# image_viewer.py

# PySimpleGUI로 프로그램을 만들 때 순서
# 1) layout을 먼저 구성
# 2) 이 layout으로 윈도우 생성
# 3) 이 윈도우에 로직 (logic)을 추가

import PySimpleGUI as sg
from PIL import Image
import io
import os

file_types = [
    ("JPEG (*.jpg)", "*.jpg"),
    ("모든 파일 (*.*)", "*.*")
]


def main():
    layout = [
        # 첫번째 행
        [sg.Image(key="-IMAGE-", size=(400, 400))],
        # 두번째 행
        [
            sg.Text("이미지 파일 이름"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("이미지 불러오기")
        ]
    ]

    window = sg.Window("이미지 뷰어", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "이미지 불러오기":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue(), size=(400, 400))

    window.close()


# 여기서부터 시작해라
if __name__ == "__main__":
    main()
