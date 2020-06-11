import yadisk
import os

token = 'AgAAAAAmaJOdAAZk1uxHxyasKkedh5gkVD-fJsE'
y = yadisk.YaDisk(token=token)

te = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\test.csv'
tr = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed\train.csv'
sub = os.path.dirname(os.getcwd()[0:-7]) + r'\data\external\sample_submission.csv'
a = os.path.dirname(os.getcwd()[0:-7]) + r'\data\processed'
b = os.path.dirname(os.getcwd()[0:-7]) + r'\data\external'


def downld():
    y.download("/Netology/test.csv", te)
    y.download("/Netology/train.csv", tr)
    y.download("/Netology/sample_submission.csv", sub)

if os.path.isdir(a) and os.path.isdir(b):
    downld()
    print('Success')
elif os.path.isdir(a)==True and os.path.isdir(b)==False:
    os.mkdir(b)
    downld()
    print('Success')
elif os.path.isdir(a) == False and os.path.isdir(b) == False:
    os.mkdir(a)
    os.mkdir(b)
    downld()
    print('Success')
elif os.path.isdir(a) == False and os.path.isdir(b) == True:
    os.mkdir(a)
    downld()
    print('Success')
elif os.path.isfile(te) and os.path.isfile(tr) and os.path.isfile(sub):
    print('Файлы train.csv, test,csv, sample_submission.csv уже есть на ПК.')
else:
    print('Ошибка')