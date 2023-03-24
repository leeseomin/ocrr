# OCRR  : OCR gui software based on Tesseract OCR 


###  :o: Select Language -> Load Image -> Convert -> Save As 

### :o: Batch conversion support (배치 일괄 변환 지원)

![대표](https://github.com/leeseomin/ocrr/blob/main/pic/1.png)
 <br/>
![대표2](https://github.com/leeseomin/ocrr/blob/main/pic/3.png)


## Dependency (Tested on an M1 Mac) 필수설치 


```pip install pytesseract ```

```pip install requests``` 

```pip install Pillow```




## run code 앱실행  (Current version 0.37)

```python ocr_37.py```

 <br/>

## Language packs may take a while to download on first run. 
(최초실행시 언어팩다운으로 다소오래걸릴수있음)


## Key Features

individual image conversion.

Batch conversion feature. (select batch folder -> batch convert)

Support for 10 languages


## Supported languages 현재 지원 언어

"eng", "kor", "jpn", "deu", "spa", "fra", "Latin", "grc:old greek", "chi_sim", "chi_tra"

영어,한글, 일본, 독일, 스페인, 프랑스, 라틴어, 고대그리스어, 한문, 중국어간자.



## to do



With the mobile app 



## Credit

Tesseract OCR : https://github.com/tesseract-ocr/tesseract 
