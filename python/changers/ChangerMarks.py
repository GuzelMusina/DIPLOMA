import pandas as pd
from numpy import math


# Data mining marks.csv file
class ChangerMarks(object):
    def __init__(self, df):
        self.df = df

    # change discipline type (string) to number
    # 0 - зачет (pass), пусто (empty)
    # 1 - экзамен (exam)
    # 2 - диф.зачет (pass with mark)
    def changeDisciplineType(self):
        for i in range(0, len(self.df)):
            # print(self.df.loc[i, 'DISCIPLINETYPE'])
            if self.df.loc[i, 'DISCIPLINETYPE'] == 'зачет':
                self.df.loc[i, 'DISCIPLINETYPE'] = 0
            elif self.df.loc[i, 'DISCIPLINETYPE'] == 'экзамен':
                self.df.loc[i, 'DISCIPLINETYPE'] = 1
            elif self.df.loc[i, 'DISCIPLINETYPE'] == 'диф.зачет':
                self.df.loc[i, 'DISCIPLINETYPE'] = 2
            else:
                self.df.loc[i, 'DISCIPLINETYPE'] = 0

        # print(self.df['DISCIPLINETYPE'])

    # change marks (string) to number
    # 0 - не сдает (doesn't pass), пусто (empty)
    # 1 - отсут. по неув. (missing for a disrespectful reason)
    # 2 - неудовлетворительно (failing grade)
    # 3 - удовлетворительно (middle-level mark)
    # 4 - хорошо (good-level mark)
    # 5 - отлично (excellent-level mark)
    # 6 - зачтено (pass)
    # 7 - не зачтено (not pass)
    def changeMark(self):
        for i in range(0, len(self.df)):
            print(self.df.loc[i, 'MARK'])
            if self.df.loc[i, 'MARK'] == 'не сдает':
                self.df.loc[i, 'MARK'] = 0
            elif self.df.loc[i, 'MARK'] == 'отсут. по неув.':
                self.df.loc[i, 'MARK'] = 1
            elif self.df.loc[i, 'MARK'] == 'неудовлетворительно':
                self.df.loc[i, 'MARK'] = 2
            elif self.df.loc[i, 'MARK'] == 'удовлетворительно':
                self.df.loc[i, 'MARK'] = 3
            elif self.df.loc[i, 'MARK'] == 'хорошо':
                self.df.loc[i, 'MARK'] = 4
            elif self.df.loc[i, 'MARK'] == 'отлично':
                self.df.loc[i, 'MARK'] = 5
            elif self.df.loc[i, 'MARK'] == 'зачтено':
                self.df.loc[i, 'MARK'] = 6
            elif self.df.loc[i, 'MARK'] == 'не зачтено':
                self.df.loc[i, 'MARK'] = 7
            elif self.df.loc[i, 'MARK'] == '0':
                self.df.loc[i, 'MARK'] = 8
            else:
                self.df.loc[i, 'DISCIPLINETYPE'] = 0

    # drop column hours and passdate
    def dropColumns(self):
        self.df.drop(['HOURS', 'PASSDATE', 'SEMESTR', 'DISCIPLINEID', 'DISCIPLINETYPE', 'SOURCETYPE',
                      'BALLSSEMESTER', 'BALLSPASS', 'MARK'],
                     axis='columns', inplace=True)

    # convert columns from float to integer
    def toNumeric(self):
        self.df["BALLSTOTAL"] = pd.to_numeric(self.df["BALLSTOTAL"], downcast='integer')
        for i in range(len(self.df)):
            if math.isnan(self.df.loc[i, 'BALLSTOTAL']):
                self.df.loc[i, 'BALLSTOTAL'] = 0
        # self.df["MARK"] = pd.to_numeric(self.df["MARK"], downcast='integer')

    def sortByStudentID(self):
        sorted_data = self.df.sort_values(by='STUDENTID')
        return sorted_data

    # def summarizeBallsSem(self, df):
    #     count_sem = df['BALLSSEMESTER'][0]
    #     # count_pass = df['BALLSPASS'][0]
    #     # count_total = df['BALLSTOTAL'][0]
    #
    #     arr_balls_semester = []
    #     # arr_balls_pass = []
    #     # arr_balls_total = []
    #
    #     for i in range(1, len(df)):
    #         if df['STUDENTID'][i - 1] == df['STUDENTID'][i]:
    #             # то увеличиваем counts
    #             count_sem = count_sem + df['BALLSSEMESTER'][i]
    #             # count_pass = count_pass + df['BALLSPASS'][i]
    #             # count_total = count_total + df['BALLSTOTAL'][i]
    #
    #         elif df['STUDENTID'][i - 1] != df['STUDENTID'][i]:
    #             print('count sem', count_sem,  'STUDENT ID i-1 ', df['STUDENTID'][i - 1],
    #                   ' STUDENT ID i-1 ' ,df['STUDENTID'][i])
    #
    #             arr_balls_semester.append(count_sem)
    #             # arr_balls_pass.append(count_pass)
    #             # arr_balls_total.append(count_total)
    #
    #             count_sem = df['BALLSSEMESTER'][i]
    #             # count_pass = df['BALLSPASS'][i]
    #             # count_total = df['BALLSTOTAL'][i]
    #
    #     return count_sem
    #
    # def summarizeBallsPass(self, df):
    #
    #     count_pass = df['BALLSPASS'][0]
    #     arr_balls_pass = []
    #
    #     for i in range(1, len(df)):
    #         if df['STUDENTID'][i - 1] == df['STUDENTID'][i]:
    #             # то увеличиваем counts
    #             count_pass = count_pass + df['BALLSPASS'][i]
    #
    #         elif df['STUDENTID'][i - 1] != df['STUDENTID'][i]:
    #             print('count pass', count_pass, 'STUDENT ID i-1 ', df['STUDENTID'][i - 1],
    #                   ' STUDENT ID i-1 ', df['STUDENTID'][i])
    #
    #             arr_balls_pass.append(count_pass)
    #             count_pass = df['BALLSPASS'][i]
    #             # count_total = df['BALLSTOTAL'][i]
    #
    #     return count_pass

    def analyzeMarks(self, df):
        count_total = df['BALLSTOTAL'][0]
        arr_balls_total = [count_total]
        arr_studentid = df.STUDENTID.unique()
        count_subjects = 1

        for i in range(1, len(df)):
            if df['STUDENTID'][i - 1] == df['STUDENTID'][i]:
                # то увеличиваем counts
                count_total = count_total + df['BALLSTOTAL'][i]
                count_subjects = count_subjects + 1

            elif df['STUDENTID'][i - 1] != df['STUDENTID'][i]:
                print('count total', count_total, 'STUDENT ID i-1 ', df['STUDENTID'][i - 1],
                      ' STUDENT ID i-1 ', df['STUDENTID'][i])

                arr_balls_total.append(count_total/count_subjects)
                count_subjects=1
                count_total = df['BALLSTOTAL'][i]

        if len(arr_studentid) > len(arr_balls_total):
            print('БОЛЬШЕ длина userid = ', len(arr_studentid), 'длина count = ', len(arr_balls_total))
        elif len(arr_studentid) < len(arr_balls_total):
            print('МЕНЬШЕ длина userid = ', len(arr_studentid), 'длина count = ', len(arr_balls_total))
        else:
            print('РАВНО длина userid = ', len(arr_studentid), 'длина count = ', len(arr_balls_total))

        diction = {'STUDENTID': arr_studentid, 'BALLSTOTAL': arr_balls_total}
        print(diction)
        data = pd.DataFrame(diction)
        # data.to_csv('..\data\MARKS_FINAL.csv', index=False)
        return diction

    # save to csv
    def saveAs(self):
        print("SAVEEEEEEE_____________________________________________________")
        self.df.to_csv(r'..\data\Marks_new.csv')
