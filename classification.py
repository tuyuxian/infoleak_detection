"""
Author: Yu-Hsien,Tu
Date: 2020/07/30
Classification 
Version 1.1
"""
import os
import requests
import uuid
import json

from input_text_generalization import Input_text
from service import Classify
from database import lookup, feedback


def get_result(text_input):
    x = str(uuid.uuid1())
    contract = Input_text(text_input)
    sentence = contract.text_cleaning()
    uncheck = []
    result = []
    # check database first
    if sentence == []:
        body = {
            'text': '重新整理頁面再輸入條文內容',
            'uuid': x}
        print('---- precarious input ----')
        return body
    else:
        for item in sentence:
            target = lookup(item)
            if target == -1:
                uncheck.append(item)
            elif target == '1':
                result.append(item)

    # predict
    if len(uncheck) > 0:
        uncheck_sentence = Classify(uncheck)
        uncheck_sentence.sen_encode()
        result1, prob = uncheck_sentence.sen_predict()
        print(prob)
        # combine tow results
        for item in result1:
            result.append(item)

    # output text
    output = ''
    number = 0
    if result == []:
        output += '此份條款或合約無風險'
    else:
        for item in result:
            number += 1
            output += '%d. ' % number + item + '\n \n'

    # user database
    feedback(x, output, contract.texts)

    body = {
        'text': output,
        'uuid': x
    }

    return body
