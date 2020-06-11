import yadisk
import os

token = 'AgAAAAAmaJOdAAZk1uxHxyasKkedh5gkVD-fJsE'
y = yadisk.YaDisk(token=token)
te = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\test.csv'
tr = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\train.csv'
s = os.path.dirname(os.getcwd()[0:-7]) + r'\data\external\sample_submission.csv'
a = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed'
b = os.path.dirname(os.getcwd()[0:-7]) + r'\data\external'
if os.path.isdir(a) and os.path.isdir(b):
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", s)
    print('Success')
elif os.path.isdir(a)==True and os.path.isdir(b)==False:
    os.mkdir(b)
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", s)
    print('Success')
elif os.path.isdir(a) == False:
    os.mkdir(a)
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", s)
    print('Success')
elif os.path.isdir(b) == False:
    os.mkdir(b)
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", s)
    print('Success')
elif os.path.isdir(a) == False and os.path.isdir(b) == True:
    os.mkdir(a)
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", s)
    print('Success')