# подгрузим модули
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

from python.changer import ChangerStudents


# загрузим данные
def readCSV():
    dataset_marks = pd.read_csv('../data/Marks.csv')
    dataset_students = pd.read_csv('../data/Students.csv')

    print(dataset_students.head())

def refactorStudentsCSV(dataset_students):
    cs = ChangerStudents(dataset_students)
    cs.changeStudyType()

# fio_arr = []
# for j in range(0,len(dataset_students)):
#     st = str(dataset_students['NAME'][j]) + str(' ') + str(dataset_students['FAMILIA'][j]) + str(' ') + str(dataset_students['OTCHESTVO'][j])
#     fio_arr.append(st)
#
# dataset_students.drop(['NAME', 'FAMILIA', 'OTCHESTVO','BIRTHDATE', 'RESIDENCEPLACE','VKURL',
#                        'FACEBOOK', 'INSTAURL', 'EMAIL', 'EMAILKPFU', 'FOTO', 'PLACEOFGRADUATION',
#                        'COUNTRY', 'REGION','DISTRICT','CITY','LOCALITY', 'ORDERBEGIN', 'ORDEREND',
#                        'PLACEOFGRADUATION', 'YEAROFGRADUATION','REASONFORLEAVING', 'DATEADMISION',
#                        'STUDSTATUS', 'CITIZENSHIP_COUNTRY_ID', 'CITIZENSHIP_ID'], axis='columns', inplace=True)
# dataset_students.insert(1, 'FIO', fio_arr, True)

# dataset_students.KINDTRAINING.unique()
# dataset_students.TYPETRAINING.unique()
# dataset_students.QUALIFICATIONTYPE.unique()
# dataset_students.CATEGORYID.unique()
# dataset_students.ISOBCHAGA.unique() --ok
# dataset_students.MARTIALSTATUSID.unique() --ok
# dataset_students.CREATICEACTIVE.unique()
# dataset_students.OLIMPIADE.unique()
# dataset_students.STUDSTATUS.unique() --?
# dataset_students.TYPEOFSCHOOL.unique()
# dataset_students.STUDTYPE_ID.unique()
#dataset_students.STUDY_PLAN_ID.unique()


# dataset_students.to_csv('Students_new.csv')
# dataset_students["STUDENTID"] = dataset_students["STUDENTID"].apply(pd.to_numeric, errors='ignore')
# data = pd.merge(dataset_students, dataset_marks, on='STUDENTID')
# data.to_csv('Data.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readCSV()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
