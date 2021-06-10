import pandas as pd
from numpy import math


# класс для обработки данных из сайта дистанционного оразования кфу
class ChangerMarks(object):
    def __init__(self, df):
        self.df = df

    # удаление признаков
    def dropColumns(self):
        self.df.drop(['HOURS', 'PASSDATE', 'SEMESTR', 'DISCIPLINEID', 'DISCIPLINETYPE', 'SOURCETYPE',
                      'BALLSSEMESTER', 'BALLSPASS', 'MARK'],
                     axis='columns', inplace=True)

    # сортировака по Studentid
    def sortByStudentID(self):
        sorted_data = self.df.sort_values(by='STUDENTID')
        return sorted_data

    # трансформирование из категориальных признаков в числовые
    def refactorBalls(self):
        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'зачтено' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_zachot = sum(arr) / len(arr)

        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'не зачтено' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_ne_zachot = sum(arr) / len(arr)

        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'удовлетворительно' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_udov = sum(arr) / len(arr)

        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'хорошо' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_horosho = sum(arr) / len(arr)

        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'отлично' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_otlich = sum(arr) / len(arr)

        arr = []
        for i in range(len(self.df)):
            if self.df.loc[i, 'MARK'] == 'неудовлетворительно' and math.isnan(self.df.loc[i, 'BALLSTOTAL']) == False:
                arr.append(self.df.loc[i, 'BALLSTOTAL'])
        ave_ne_udov = sum(arr) / len(arr)
        print(ave_zachot, ave_ne_zachot, ave_udov, ave_horosho, ave_otlich, ave_ne_udov)

        for i in range(len(self.df)):
            if self.df.loc[i, 'BALLSTOTAL'] == '' or math.isnan(self.df.loc[i, 'BALLSTOTAL']):
                if self.df.loc[i, 'MARK'] == 'отсут. по неув.':
                    self.df.loc[i, 'BALLSTOTAL'] = 0
                elif self.df.loc[i, 'MARK'] == 'зачтено':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_zachot)
                elif self.df.loc[i, 'MARK'] == 'не зачтено':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_zachot)
                elif self.df.loc[i, 'MARK'] == 'удовлетворительно':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_udov)
                elif self.df.loc[i, 'MARK'] == 'хорошо':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_horosho)
                elif self.df.loc[i, 'MARK'] == 'отлично':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_otlich)
                elif self.df.loc[i, 'MARK'] == 'неудовлетворительно':
                    self.df.loc[i, 'BALLSTOTAL'] = int(ave_ne_udov)


        self.df.drop(self.df[self.df.BALLSTOTAL == -1].index, inplace=True)
        print(self.df.tail())
        # return df

    # метод формирует словарь из id студента и его среднего балла
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

        return diction
