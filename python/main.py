import pandas as pd

from python.ChangerStudents import ChangerStudents
from python.ChangerMarks import ChangerMarks
from python.ChangeMSTeams import ChangeMSTeams

from python.helpers.Union import Union
from python.helpers.Saver import Saver
from python.helpers.Reader import Reader

saver = Saver()
reader = Reader()
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

#union two csv Marks and Students
def uniStudentAndMarks(dataset_students, dataset_marks):
    unifier = Union(dataset_students, dataset_marks)
    unifier.unionStudAndMarks()
    saver.saveToCSV(unifier.data,r'..\data\Data.csv')


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
    # uniStudentAndMarks(ds, dm)

    dms = readCSVMSTeams()
    refactorMSTeamsCSV(dms)



