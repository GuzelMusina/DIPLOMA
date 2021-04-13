import pandas as pd

#Data mining marks.csv file
class ChangerMarks(object):
    def __init__(self, df):
        self.df = df

    # change discipline type (string) to number
    # 0 - зачет (pass), пусто (empty)
    # 1 - экзамен (exam)
    # 2 - диф.зачет (pass with mark)
    def changeDisciplineType(self):
        for i in range(0, len(self.df)):
            print(self.df.loc[i, 'DISCIPLINETYPE'])
            if self.df.loc[i, 'DISCIPLINETYPE'] == 'зачет':
                self.df.loc[i, 'DISCIPLINETYPE'] = 0
            elif self.df.loc[i, 'DISCIPLINETYPE'] == 'экзамен':
                self.df.loc[i, 'DISCIPLINETYPE'] = 1
            elif self.df.loc[i, 'DISCIPLINETYPE'] == 'диф.зачет':
                self.df.loc[i, 'DISCIPLINETYPE'] = 2
            else:
                self.df.loc[i, 'DISCIPLINETYPE'] = 0

        print(self.df['DISCIPLINETYPE'])

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
        self.df.drop(['HOURS', 'PASSDATE'], axis='columns', inplace=True)

    # convert columns from float to integer
    def toNumeric(self):
        self.df["BALLSTOTAL"] = pd.to_numeric(self.df["BALLSTOTAL"], downcast='integer')
        self.df["MARK"] = pd.to_numeric(self.df["MARK"], downcast='integer')

    #save to csv
    def saveAs(self):
        print("SAVEEEEEEE_____________________________________________________")
        self.df.to_csv(r'..\data\Marks_new.csv')

