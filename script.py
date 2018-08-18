from PIL import Image
import pytesseract
import re
import datetime


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

list_of_words_1 = []
list_of_words_2 = []

def read_lists():
    with open('list_of_words_1.txt', 'r') as f:
        list_of_words_1 = [line.strip() for line in f]

    with open('list_of_words_2.txt', 'r') as f:
        list_of_words_2 = [line.strip() for line in f]

def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])


def convert_and_split(text):
    for item in list_of_words_1:
        text = text.replace(item,'')
    # print(text)
    words = text.split()
    for i in range(2):
        for item in words:
            if len(item)<4 or (item in list_of_words_2):
                words.remove(item)

    return words

def save_to_txt(list):
    now = datetime.datetime.now()
    name = now.strftime("%Y-%m-%d_%H-%M.txt")
    file = open(name, 'w')
    for item in list:
      file.write("%s\n" % item)


path = 'media/test2.png'
text_ocr = pytesseract.image_to_string(Image.open(path))


list_of_words_1 = [
    'Thumac','Tlumac','Ttun','Ttum','Tumacz',
    '...','-','@','.','\n'
    ]

list_of_words_2 = [
    'p','po','pol','pols','a','an','ang','angi','end',
    'Tuma','Thur','Thum:','Thum','Thu','Thun','Tum'
    ]


def main():
    text = text_ocr
    text = remove_non_ascii(text)
    words = convert_and_split(text)
    print(words)
    save_to_txt(words)

if __name__ == '__main__':
    main()
