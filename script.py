# -*- coding: windows-1250 -*-

from PIL import Image
import pytesseract
import re
import sys
import datetime
from googletrans import Translator


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


def translate_text(list):
    translator = Translator()
    new_list = []
    text = ""
    for item in list:
        translation = translator.translate(item, dest='pl')
        try:
            print (translation.origin + ' \t\t\t ' + translation.text)
        except UnicodeEncodeError:
            print(translation.origin + ' \t\t\t ' + str(translation.text.encode('ascii', 'replace') ) )
        new_list.append(text)
    return new_list


def save_to_txt(list):
    now = datetime.datetime.now()
    name = now.strftime("%Y-%m-%d_%H-%M.txt")
    file = open('txt/'+'dict.txt', 'a')
    for item in list:
      file.write("%s\n" % item)





list_of_words_1 = [
    'Ttunaczenie','Ttumaczenie',
    'Ttunaczeni','Ttumaczeni',
    'Thumaczenie','Tlumaczenie','Ttunaczen','Ttumaczen',
    'Thumaczeni','Tlumaczeni','Ttunacze','Ttumacze','Tumaczenie',
    'Thumaczen','Tlumaczen','Ttunacz','Ttumacz','Tumaczeni',
    'Thumacze','Tlumacze','Ttunac','Ttumac','Tumaczen',
    'Thumacz','Tlumacz','Ttuna','Ttuma','Tumacze',
    'Thumac','Tlumac','Ttun','Ttum','Tumacz',
    '...','-','@','.','\n'
    ]

list_of_words_2 = [
    'p','po','pol','pols','a','an','ang','angi','end',
    'Tuma','Thur','Thum:','Thum','Thu','Thun','Tum'
    ]


def main():

    for i in range(12):
        iter = i+1
        path = 'media/test ('+str(iter)+').png'
        text_ocr = pytesseract.image_to_string(Image.open(path))
        text = text_ocr
        text = remove_non_ascii(text)
        words = convert_and_split(text)
        print(words)
        save_to_txt(words)

    #new_words = translate_text(words)
    #save_to_txt(words)

if __name__ == '__main__':
    main()
