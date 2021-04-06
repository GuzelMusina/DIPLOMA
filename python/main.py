import pandas as pd

from python.ChangerStudents import ChangerStudents
from python.ChangerMarks import ChangerMarks
from python.ChangeMSTeams import ChangeMSTeams

from python.helpers.Merger import Merger
from python.helpers.Saver import Saver
from python.helpers.Reader import Reader

saver = Saver()
reader = Reader()
merger = Merger()
# upload data
def readCSVStudents():
    return reader.readCSV('../data/Students.csv')

# upload data
def readCSVMarks():
    dataset_marks = pd.read_csv('../data/Marks.csv')
    return dataset_marks

def readCSVMSTeams():
    return reader.readCSV('../data/MicrosoftTeamsActivity.csv')

#refactor Students.csv
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
    cs.toNumeric()
    # cs.saveAs()
    saver.saveToCSV(cs.dataset_students, r'..\data\Students_new.csv')

#refactor Marks.csv
def refactorMarksCSV(dataset_marks):
    cm = ChangerMarks(dataset_marks)
    cm.changeDisciplineType()
    cm.changeMark()
    cm.dropColumns()
    cm.toNumeric()
    # cm.saveAs()
    saver.saveToCSV(cm.dataset_marks, r'..\data\Marks_new.csv')

#merge two csv Marks and Students
def mergeStudentAndMarks(dataset_students, dataset_marks, param):
    dataset_students["STUDENTID"] = dataset_students["STUDENTID"].apply(pd.to_numeric, errors='ignore')
    data = merger.merge(dataset_students, dataset_marks, param)
    saver.saveToCSV(data,r'..\data\Data.csv')

# merge MSTeams and Data (Students + Marks)
def mergeMSTeamsAndData(datset_studmarks, dataset_msteams, param):
    data = merger.merge(datset_studmarks, dataset_msteams, param)
    saver.saveToCSV(data, r'..\data\StudMarksMSteams.csv')

def refactorMSTeamsCSV(dms):
    changeMST = ChangeMSTeams(dms)
    changeMST.dropColumns()
    saver.saveToCSV(changeMST.dms, r'..\data\MSTeams_new.csv')


# проверка уникальных значений в столбце
# dataset_students.NAME_COLUMN.unique()

if __name__ == '__main__':
    # dataset_students = readCSVStudents()
    # refactorStudentsCSV(dataset_students)

    # dataset_marks=readCSVMarks()
    # refactorMarksCSV(dataset_marks)

    # dm = pd.read_csv('../data/Marks_new.csv')
    # ds = pd.read_csv('../data/Students_new.csv')
    # mergeMSTeamsAndData(ds, dm, 'STUDENTID')


    # dms = readCSVMSTeams()
    # refactorMSTeamsCSV(dms)

    # dmsteams = pd.read_csv('../data/MSTeams_new.csv')
    # dstudmarks=pd.read_csv('../data/Data.csv')
    # mergeMSTeamsAndData(dstudmarks, dmsteams, 'FIO')

    data = pd.read_csv('..\data\Логи.csv')
    print(data.columns)


