# подгрузим модули
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

from python.ChangerStudents import ChangerStudents

# загрузим данные
def readCSVStudents():
    # dataset_marks = pd.read_csv('../data/Marks.csv')
    dataset_students = pd.read_csv('../data/Students.csv')
    return dataset_students
    # print(dataset_students.head())

def refactorStudentsCSV(dataset_students):
    cs = ChangerStudents(dataset_students)
    cs.changeBirthplace()
    cs.changeCategoryId()
    cs.changeInstitute()
    cs.changeIsMedale()
    cs.changeCreativeActive()
    cs.changeKindtraining()
    cs.changeOlimpiade()
    cs.changeQualification()
    cs.changeSchool()
    cs.changeStudyType()
    cs.changeTypeOfTraining()
    cs.addFIO()
    cs.dropColumns()
    cs.saveAs()
    print("2nd ---------", cs.dataset_students.head())



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



# dataset_students["STUDENTID"] = dataset_students["STUDENTID"].apply(pd.to_numeric, errors='ignore')
# data = pd.merge(dataset_students, dataset_marks, on='STUDENTID')
# data.to_csv('Data.csv')


if __name__ == '__main__':
    dataset_students = readCSVStudents()
    print("1st---------", dataset_students.head())
    refactorStudentsCSV(dataset_students)

