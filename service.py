"""
Author: Yu-Hsien,Tu
Date: 2020/07/30
Connect to BertService
Version 1.1
"""

from bert_serving.client import BertClient
from joblib import load
from database import update


class Classify(object):
    def __init__(self, sentence):
        self.bc = BertClient()
        self.cls = load('./modelV1.joblib')
        self.sentence = sentence

    def sen_encode(self):
        self.sen_enc = self.bc.encode(self.sentence)

    def sen_predict(self):
        result = self.cls.predict(self.sen_enc)
        result_prob = self.cls.predict_proba(self.sen_enc)

        # update database simultaneously
        result_text = []
        for i in range(len(self.sentence)):
            if result[i] == '1':
                result_text.append(self.sentence[i])
                update(result[i], self.sentence[i])
            else:
                update(result[i], self.sentence[i])
        return result_text, result_prob
