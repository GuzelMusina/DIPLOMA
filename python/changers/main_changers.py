import pandas as pd

from python.changers.ChangerStudents import ChangerStudents
from python.changers.ChangerMarks import ChangerMarks
from python.changers.ChangeMSTeams import ChangeMSTeams
from python.changers.ChangeMoodle import ChangeMoodle
from python.changers.ChangerMoodleStud import ChangerMoodleStud
from python.found_criterior.Refactor import Refactor

from python.helpers.Merger import Merger
from python.helpers.Saver import Saver
from python.helpers.Reader import Reader

saver = Saver()
reader = Reader()
merger = Merger()

# refactor Students.csv
def refactorStudentsCSV(dataset_students):
    changer_students_eor = ChangerStudents(dataset_students)
    changer_students_eor.changeBirthplace()
    changer_students_eor.changeCategoryId()
    changer_students_eor.changeInstitute()
    changer_students_eor.changeIsMedale()
    changer_students_eor.changeCreativeActive()
    changer_students_eor.changeKindtraining()
    changer_students_eor.changeOlimpiade()
    changer_students_eor.changeQualification()
    changer_students_eor.changeSchool()
    changer_students_eor.changeStudyType()
    changer_students_eor.changeTypeOfTraining()
    changer_students_eor.addFIO()
    changer_students_eor.addFI()
    changer_students_eor.dropColumns()
    changer_students_eor.toNumeric()
    # cs.saveAs()
    saver.saveToCSV(changer_students_eor.df, r'..\data\Middle Wave\Students_new.csv')


# refactor Marks.csv
def refactorMarksCSV(dataset_marks):
    changer_marks_eor = ChangerMarks(dataset_marks_eor)
    # changer_marks_eor.toNumeric()
    changer_marks_eor.refactorBalls()
    changer_marks_eor.dropColumns()

    sorted_data = changer_marks_eor.sortByStudentID()
    pd.DataFrame(sorted_data).to_csv('../../data/Middle Wave/Sorted_marks.csv', index=None)

    new_data = pd.read_csv('../../data/Middle Wave/Sorted_marks.csv')
    diction = changer_marks_eor.analyzeMarks(new_data)

    data = pd.DataFrame(diction)
    saver.saveToCSV(data, '../../data/Middle Wave/Marks_FINAL.csv')


def refactorMSTeamsCSV(dms):
    changer_msteams = ChangeMSTeams(dms)
    changer_msteams.dropColumns()
    saver.saveToCSV(changer_msteams.dms, r'..\data\Middle Wave\Refactor_MSTeams_new.csv')


def refactorMoodle(dml):
    changer_moodle_logs = ChangeMoodle(dml)
    changer_moodle_logs.dropColumns()
    sorted_data = changer_moodle_logs.sorted_by_userid()
    pd.DataFrame(sorted_data).to_csv('..\data\Sorted_moodle.csv', index=None)
    new_data = pd.read_csv('..\data\Sorted_moodle.csv')
    diction = changer_moodle_logs.analyzeLogs(new_data)
    data = pd.DataFrame(diction)
    # print(data)
    saver.saveToCSV(data, '..\data\Moodle_final.csv')

def refactorStudentsMoodle(dataset_studnets_moodle):
    changer_moodle_stud = ChangerMoodleStud(dataset_studnets_moodle)
    changer_moodle_stud.addFI()
    changer_moodle_stud.dropColumns()
    saver.saveToCSV(changer_moodle_stud.df, '../data/Middle Wave/Student_moodle.csv')
    
def refactorFinalMoodle(dataset_final_moodle):
    final_changer = ChangerMoodleStud(dataset_final_moodle)
    sorted_data = final_changer.sortData()
    pd.DataFrame(sorted_data).to_csv('../data/Middle Wave/Sorted_final_moodle.csv', index=None)
    new_data = pd.read_csv('../../data/Middle Wave/Sorted_final_moodle.csv')
    diction = final_changer.analyzeData(new_data)
    data = pd.DataFrame(diction)
    saver.saveToCSV(data, r'..\data\Final Wave\MoodleFinalFinal.csv')

# merge two csv Marks and Students
def mergeStudentAndMarks(dataset_students, dataset_marks, param):
    dataset_students["STUDENTID"] = dataset_students["STUDENTID"].apply(pd.to_numeric, errors='ignore')
    data = merger.merge(dataset_students, dataset_marks, param)
    saver.saveToCSV(data, '../../data/Middle Wave/StudAndMarksMerge.csv')

# merge MSTeams and Data (Students + Marks)
def mergeMSTeamsAndData(datset_studmarks, dataset_msteams, param):
    data = merger.merge(datset_studmarks, dataset_msteams, param)
    saver.saveToCSV(data, '../../data/Final Wave/StudMarksMSteams.csv')

def mergeMoodleLogsAndStudents(dataset_moodle_log, dataset_moodle_students, param):
    data = merger.merge(dataset_moodle_log, dataset_moodle_students, param)
    saver.saveToCSV(data, r'..\data\Final Wave\FinalMoodle.csv')

def mergeMoodleTeamsOnlineUni(dataset_moodle, dataset_msteams_student_marks, param):
    data = merger.merge(dataset_moodle, dataset_msteams_student_marks, param)
    saver.saveToCSV(data, '../../data/Final Wave/Final.csv')


class MainChangers(object):
    def __init__(self, dataset_students_eor, dataset_marks_eor, dataset_msteams,
                 dataset_logs_moodle, dataset_students_moodle):
        self.dataset_students_eor = dataset_students_eor
        self.dataset_marks_eor = dataset_marks_eor
        self.dataset_msteams = dataset_msteams
        self.dataset_logs_moodle = dataset_logs_moodle
        self.dataset_students_moodle = dataset_students_moodle

    def change(self):
        refactorStudentsCSV(self.dataset_students_eor)
        refactorMarksCSV(self.dataset_marks_eor)
        refactorMSTeamsCSV(self.dataset_msteams)

        dataset_marks_refact = pd.read_csv('../../data/Middle Wave/Marks_FINAL.csv')
        dataset_students_refact = pd.read_csv('../../data/Middle Wave/Students_new.csv')
        dataset_students_refact["STUDENTID"] = dataset_students_refact["STUDENTID"].apply(pd.to_numeric,
                                                                                          errors='ignore')
        dataset_marks_refact["BALLSTOTAL"] = pd.to_numeric(dataset_marks_refact["BALLSTOTAL"], downcast='integer')
        mergeStudentAndMarks(dataset_students_refact, dataset_marks_refact, 'STUDENTID')

        dataset_msteams = pd.read_csv('../../data/Middle Wave/Refactor_MSTeams_new.csv')
        dataset_student_and_marks = pd.read_csv('../../data/Middle Wave/StudAndMarksMerge.csv')
        mergeMSTeamsAndData(dataset_student_and_marks, dataset_msteams, 'FIO')

        # dataset_moodle_logs_rare = pd.read_csv('..\data\First Wave\Logs.csv', sep=';')
        # dataset_moodle_logs_rare.rename(columns=({'Действие': 'movements', 'Дата': 'date', 'Дата и время': 'date_and_time'}), inplace=True)
        # renamed_df = dataset_moodle_logs_rare.to_csv("..\data\First Wave\MoodleLogs.csv", index=None)

        refactorMoodle(self.dataset_logs_moodle)
        refactorStudentsMoodle(self.dataset_students_moodle)

        data_for_merge_moodle_logs = reader.readCSV('../data/Final Wave/Moodle_logs.csv')
        data_for_merge_moodle_students = reader.readCSV('../data/Middle Wave/Student_moodle.csv')

        mergeMoodleLogsAndStudents(data_for_merge_moodle_logs, data_for_merge_moodle_students, 'USERID')

        dataset_final_moodle = reader.readCSV('../data/Final Wave/FinalMoodle.csv')
        refactorFinalMoodle(dataset_final_moodle)

        dataset_final_moodle = reader.readCSV('../../data/Final Wave/MoodleFinalFinal.csv')
        dataset_final_msteams_eor = reader.readCSV('../../data/Final Wave/StudMarksMSteams.csv')

        mergeMoodleTeamsOnlineUni(dataset_final_moodle, dataset_final_msteams_eor, 'FI')

        df = reader.readCSV('../../data/Final Wave/Final.csv')
        df.drop(['GROUP_NUMBER'], axis='columns', inplace=True)
        df.drop(['STUDENTID', 'FI', 'FIO'], axis='columns', inplace=True)
        df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
        df["BALLSTOTAL"] = df["BALLSTOTAL"].astype(int)
        df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
        saver.saveToCSV(df, 'Data.csv')

        y_ = [0 for x in range(len(df))]
        for i in range(len(df)):
            if df.loc[i, 'BALLSTOTAL'] < 56:
                y_[i] = 0
            elif df.loc[i, 'BALLSTOTAL'] >= 56 and df.loc[i, 'BALLSTOTAL'] < 71:
                y_[i] = 1
            elif df.loc[i, 'BALLSTOTAL'] >= 71 and df.loc[i, 'BALLSTOTAL'] < 86:
                y_[i] = 2
            elif df.loc[i, 'BALLSTOTAL'] >= 86:
                y_[i] = 3
        df.insert(21, 'CLASS', y_, True)
        df.to_csv('Data_with_class.csv', index=False)

        refactor = Refactor()
        refactor

        return df

# проверка уникальных значений в столбце
# dataset_students.NAME_COLUMN.unique()

if __name__ == '__main__':

    dataset_students_eor = reader.readCSV('../data/First Wave/Students.csv')
    refactorStudentsCSV(dataset_students_eor)

    dataset_marks_eor=reader.readCSV('../../data/First Wave/Marks.csv')
    refactorMarksCSV(dataset_marks_eor)

    dataset_msteams = reader.readCSV('../data/First Wave/MicrosoftTeamsActivity.csv')
    refactorMSTeamsCSV(dataset_msteams)

    dataset_marks_refact = pd.read_csv('../../data/Middle Wave/Marks_FINAL.csv')
    dataset_students_refact = pd.read_csv('../../data/Middle Wave/Students_new.csv')
    dataset_students_refact["STUDENTID"] = dataset_students_refact["STUDENTID"].apply(pd.to_numeric, errors='ignore')
    dataset_marks_refact["BALLSTOTAL"] = pd.to_numeric(dataset_marks_refact["BALLSTOTAL"], downcast='integer')
    mergeStudentAndMarks(dataset_students_refact, dataset_marks_refact, 'STUDENTID')

    dataset_msteams = pd.read_csv('../../data/Middle Wave/Refactor_MSTeams_new.csv')
    dataset_student_and_marks=pd.read_csv('../../data/Middle Wave/StudAndMarksMerge.csv')
    mergeMSTeamsAndData(dataset_student_and_marks, dataset_msteams, 'FIO')

    dataset_moodle_logs_rare = pd.read_csv('..\data\First Wave\Logs.csv', sep=';')
    dataset_moodle_logs_rare.rename(columns=({'Действие': 'movements', 'Дата': 'date', 'Дата и время': 'date_and_time'}), inplace=True)
    renamed_df = dataset_moodle_logs_rare.to_csv("..\data\First Wave\MoodleLogs.csv", index=None)

    dataset_logs_moodle = reader.readCSV('../data/Fist Wave/MoodleLogs.csv')
    refactorMoodle(dataset_logs_moodle)

    dataset_students_moodle = reader.readCSVWithSeparator('../data/First Wave/MoodleStudents.csv')
    refactorStudentsMoodle(dataset_students_moodle)

    data_for_merge_moodle_logs = reader.readCSV('../data/Final Wave/Moodle_logs.csv')
    data_for_merge_moodle_students = reader.readCSV('../data/Middle Wave/Student_moodle.csv')

    mergeMoodleLogsAndStudents(data_for_merge_moodle_logs, data_for_merge_moodle_students, 'USERID')

    dataset_final_moodle = reader.readCSV('../data/Final Wave/FinalMoodle.csv')
    refactorFinalMoodle(dataset_final_moodle)

    dataset_final_moodle = reader.readCSV('../../data/Final Wave/MoodleFinalFinal.csv')
    dataset_final_msteams_eor = reader.readCSV('../../data/Final Wave/StudMarksMSteams.csv')

    mergeMoodleTeamsOnlineUni(dataset_final_moodle,dataset_final_msteams_eor, 'FI')





