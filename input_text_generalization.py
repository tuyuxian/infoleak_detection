"""
Author: Yu-Hsien,Tu
Date: 2020/07/30
Input Text Cleaning
Version 1.2
"""


class Input_text(object):
    def __init__(self, texts):
        self.texts = texts

    def text_cleaning(self):
        texts = self.texts
        if (texts.strip(' ') == '--' or texts.strip(' ') == '{}' or texts.strip(' ') == '[]'
            or texts.strip(' ') == '' or texts.strip(' ') == 'int' or texts.strip(' ') == 'list' or texts.strip(' ') == 'dict'
                or texts.strip(' ') == '=' or texts.strip(' ') == '=='):
            texts = ''

        lines = texts.split('\n')
        text_lst = []
        for text in lines:
            if (text != '' and text != ' '):
                text = text.replace("'", '"')
                text_lst.append(text)
        return text_lst
