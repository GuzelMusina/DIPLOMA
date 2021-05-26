import pandas as pd
class ChangerMoodleStud(object):
    def __init__(self, df):
        self.df = df

    # union NAME FAMILIA  into one string FI
    def addFI(self):
        fio_arr = []
        for j in range(0, len(self.df)):
            st = str(str(self.df['FAMILIA'][j]) + str(' ') + str(self.df['NAME'][j]))
            fio_arr.append(st)
        self.df.insert(1, 'FI', fio_arr, True)

    def dropColumns(self):
        self.df.drop(['NAME', 'FAMILIA', 'Unnamed: 3'], axis='columns', inplace=True)

    def sortData(self):
        sorted_data = self.df.sort_values(by='FI')
        return sorted_data

    def analyzeData(self, df):
        count_total = df['COUNT_ACTIVITIES'][0]
        arr_balls_total = [count_total]
        arr_fio = df.FI.unique()

        for i in range(1, len(df)):
            if df['FI'][i - 1] == df['FI'][i]:
                # то увеличиваем counts
                count_total = count_total + df['COUNT_ACTIVITIES'][i]
            elif df['FI'][i - 1] != df['FI'][i]:
                print('COUNT_ACTIVITIES', count_total, 'FI ID i-1 ', df['FI'][i - 1],
                      ' FI ID i-1 ', df['FI'][i])
                arr_balls_total.append(count_total)
                count_total = df['COUNT_ACTIVITIES'][i]

        if len(arr_fio) > len(arr_balls_total):
            print('БОЛЬШЕ длина userid = ', len(arr_fio), 'длина count = ', len(arr_balls_total))
        elif len(arr_fio) < len(arr_balls_total):
            print('МЕНЬШЕ длина userid = ', len(arr_fio), 'длина count = ', len(arr_balls_total))
        else:
            print('РАВНО длина userid = ', len(arr_fio), 'длина count = ', len(arr_balls_total))

        diction = {'FI': arr_fio, 'COUNT_ACTIVITIES': arr_balls_total}
        print(diction)
        data = pd.DataFrame(diction)
        # data.to_csv('..\data\MARKS_FINAL.csv', index=False)
        return diction
