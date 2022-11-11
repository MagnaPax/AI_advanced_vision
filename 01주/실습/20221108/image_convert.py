import PySimpleGUI as sg
import shutil
from PIL import Image
import tempfile
import io

def grayscale(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert(mode = "L")
    gray_scale.save(output_image_path)    

def black_and_white(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert(mode = "1")
    gray_scale.save(output_image_path)    

def sepia(input_image_path, output_image_path):
    whitish = (255, 240, 192)
    palette = []
    r, g, b = whitish
    for i in range(255):
        new_red = r * i // 255
        new_green = g * i // 255
        new_blue = b * i // 255
        palette.extend( (new_red, new_green, new_blue) )

    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert(mode = "L")

    gray_scale.putpalette(palette)

    # gray_scale.show()

    sepia_image = gray_scale.convert("RGB")
    sepia_image.save(output_image_path)   

file_types = [
    ("JPEG (*.jpg)", "*.jpg"),
    ("모든 파일 (*.*)", "*.*")
]

effects = {
    "Normal": shutil.copy,
    "Black and White": black_and_white,
    "Grayscale": grayscale,
    "Sepia": sepia
}

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

def main():
    effect_name = list(effects.keys())

    layout = [
        [ sg.Image(key = "-IMAGE-", size = (400, 400))],
        [
            sg.Text("이미지 파일"),
            sg.Input(size = (25, 1), key = "-FILENAME-"),
            sg.FileBrowse(file_types = file_types),
            sg.Button("이미지 불러오기")
        ],
        [
            sg.Text("효과"),
            sg.Combo(
                effect_name, 
                default_value = "Normal", 
                key = "-EFFECTS-", 
                enable_events=True, 
                readonly=True
            )
        ],
        [sg.Button("저장")]
    ]

    window = sg.Window("이미지 변환기", layout, size = (450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event in ["이미지 불러오기", "-EFFECTS-"]:
            selected_effect = values["-EFFECTS-"]
            image_file = values["-FILENAME-"]
            if image_file:
                effects[selected_effect](image_file, tmp_file)
                image = Image.open(tmp_file)
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format = "PNG")
                window["-IMAGE-"].update(data=bio.getvalue(), size = (400, 400))

        if event == "저장" and values["-FILENAME-"]:
            save_filename = sg.popup_get_file(
                "File", file_types = file_types, save_as=True, no_window=True
            )
            if save_filename == values["-FILENAME-"]:
                sg.popup_error("원본 이미지에 덮여쓰여집니다!")
            else:
                if save_filename:
                    shutil.copy(tmp_file, save_filename)
                    sg.popup(f"저장됨: {save_filename}")

    window.close()

if __name__ == "__main__":
    main()