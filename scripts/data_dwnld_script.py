import yadisk
import os

token = 'AgAAAAAmaJOdAAZk1uxHxyasKkedh5gkVD-fJsE'
y = yadisk.YaDisk(token=token)
te = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\test.csv'
tr = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\train.csv'
s = os.path.dirname(os.getcwd()[0:-7]) + r'\data\external\sample_submission.csv'
y.download("/Netology/test.csv", te)
y.download("/Netology/train.csv", tr)
y.download("/Netology/sample_submission.csv", s)
print('Success')