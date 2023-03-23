import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import os
import requests

import os

# 환경 변수를 올바른 경로로 설정
tessdata_folder = os.path.join(os.getcwd(), 'tessdata')
os.environ['TESSDATA_PREFIX'] = tessdata_folder
os.makedirs(tessdata_folder, exist_ok=True)



class OCRApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")  # 창 크기를 변경
        self.image_file = None

        # 환경 변수를 현재 작업 폴더로 설정
        os.environ['TESSDATA_PREFIX'] = os.getcwd()

        # 영어 학습 데이터 파일 다운로드
        self.download_traineddata()

        self.init_ui()



import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import os
import requests

# 환경 변수를 올바른 경로로 설정
tessdata_folder = os.path.join(os.getcwd(), 'tessdata')
os.environ['TESSDATA_PREFIX'] = tessdata_folder
os.makedirs(tessdata_folder, exist_ok=True)

class OCRApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1100x900")  # 창 크기

        # 환경 변수를 현재 작업 폴더로 설정
        os.environ['TESSDATA_PREFIX'] = os.getcwd()

        # 영어 학습 데이터 파일 다운로드
        self.download_traineddata()

        self.init_ui()

    def init_ui(self):
        self.master.title('Tesseract OCR based GUI app')

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.text_edit = tk.Text(self.master, height=20, width=80)  # 텍스트 창 크기 변경
        self.text_edit.pack()

        load_button = tk.Button(self.master, text='Load', command=self.load_image)
        load_button.pack()

        self.lang_var = tk.StringVar(self.master)
        self.lang_var.set("eng")
        lang_options = ["eng", "kor", "jpn", "deu", "spa", "fra", "Latin", "grc", "chi_sim", "chi_tra"]
        lang_dropdown = tk.OptionMenu(self.master, self.lang_var, *lang_options)
        lang_dropdown.pack()

        convert_button = tk.Button(self.master, text='Convert', command=lambda: self.convert_image_to_text(self.lang_var.get()))
        convert_button.pack()

        save_button = tk.Button(self.master, text='Save as', command=self.save_text)
        save_button.pack()

    def download_traineddata(self, langs=["eng", "kor", "jpn", "deu", "spa", "fra", "Latin", "grc", "chi_sim", "chi_tra"]):
        # 언어별 URL 딕셔너리를 생성합니다.
        lang_urls = {
            "eng": "https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata",
            "kor": "https://github.com/tesseract-ocr/tessdata_best/raw/main/kor.traineddata",
            "jpn": "https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata",
            "deu": "https://github.com/tesseract-ocr/tessdata_best/raw/main/deu.traineddata",
            "spa": "https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata",
            "fra": "https://github.com/tesseract-ocr/tessdata_best/raw/main/fra.traineddata",
            "Latin": "https://github.com/tesseract-ocr/tessdata_best/raw/main/lat.traineddata",
            "grc": "https://github.com/tesseract-ocr/tessdata_best/raw/main/grc.traineddata",
            "chi_sim": "https://github.com/tesseract-ocr/tessdata_best/raw/main/chi_sim.traineddata",
            "chi_tra": "https://github.com/tesseract-ocr/tessdata_best/raw/main/chi_tra.traineddata"
        }

        for lang in langs:
            traineddata_file = os.path.join(os.environ['TESSDATA_PREFIX'], f"{lang}.traineddata")
            
            # 이미 파일이 존재하면 다운로드를 건너뜁니다.
            if os.path.exists(traineddata_file):
                print(f"{lang}.traineddata 파일이 이미 존재합니다. 다운로드를 건너뜁니다.")
                continue
            
            # 언어에 해당하는 URL을 사용합니다.
            url = lang_urls.get(lang)
            response = requests.get(url)

            if response.status_code == 200:
                with open(traineddata_file, "wb") as f:
                    f.write(response.content)
                print(f"{lang}.traineddata 파일이 {os.environ['TESSDATA_PREFIX']}에 저장되었습니다.")
            else:
                print(f"{lang}.traineddata 파일을 다운로드하지 못했습니다. 상태 코드: {response.status_code}")





    def load_image(self):
        filetypes = (
            ('이미지 파일', '*.png *.xpm *.jpg *.bmp'),
            ('모든 파일', '*.*')
        )
        self.image_file = filedialog.askopenfilename(title='이미지 파일 불러오기', filetypes=filetypes)
        if self.image_file:
            image = Image.open(self.image_file)

            # 이미지 크기 조절
            max_size = (500, 500)  # 원하는 최대 이미지 크기를 지정하세요.
            image.thumbnail(max_size, Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo




    def convert_image_to_text(self, lang='eng'):
        if self.image_file:
            text = pytesseract.image_to_string(self.image_file, lang=lang)
            self.text_edit.delete('1.0', tk.END)
            self.text_edit.insert('1.0', text)


    def save_text(self):
        save_file = filedialog.asksaveasfilename(title='텍스트 파일 저장', defaultextension='.txt', filetypes=[('텍스트 파일', '*.txt')])
        if save_file:
            with open(save_file, 'w', encoding='utf-8') as f:
                f.write(self.text_edit.get('1.0', tk.END))






if __name__ == '__main__':
    root = tk.Tk()
    app = OCRApp(master=root)
    app.mainloop()