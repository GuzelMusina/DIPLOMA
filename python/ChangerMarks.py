import pandas as pd

#Data mining marks.csv file
class ChangerMarks(object):
    def __init__(self, dataset_marks):
        self.dataset_marks = dataset_marks

    # change discipline type (string) to number
    # 0 - зачет (pass), пусто (empty)
    # 1 - экзамен (exam)
    # 2 - диф.зачет (pass with mark)
    def changeDisciplineType(self):
        for i in range(0, len(self.dataset_marks)):
            print(self.dataset_marks.loc[i, 'DISCIPLINETYPE'])
            if self.dataset_marks.loc[i, 'DISCIPLINETYPE'] == 'зачет':
                self.dataset_marks.loc[i, 'DISCIPLINETYPE'] = 0
            elif self.dataset_marks.loc[i, 'DISCIPLINETYPE'] == 'экзамен':
                self.dataset_marks.loc[i, 'DISCIPLINETYPE'] = 1
            elif self.dataset_marks.loc[i, 'DISCIPLINETYPE'] == 'диф.зачет':
                self.dataset_marks.loc[i, 'DISCIPLINETYPE'] = 2
            else:
                self.dataset_marks.loc[i, 'DISCIPLINETYPE'] = 0

        print(self.dataset_marks['DISCIPLINETYPE'])

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
        for i in range(0, len(self.dataset_marks)):
            print(self.dataset_marks.loc[i, 'MARK'])
            if self.dataset_marks.loc[i, 'MARK'] == 'не сдает':
                self.dataset_marks.loc[i, 'MARK'] = 0
            elif self.dataset_marks.loc[i, 'MARK'] == 'отсут. по неув.':
                self.dataset_marks.loc[i, 'MARK'] = 1
            elif self.dataset_marks.loc[i, 'MARK'] == 'неудовлетворительно':
                self.dataset_marks.loc[i, 'MARK'] = 2
            elif self.dataset_marks.loc[i, 'MARK'] == 'удовлетворительно':
                self.dataset_marks.loc[i, 'MARK'] = 3
            elif self.dataset_marks.loc[i, 'MARK'] == 'хорошо':
                self.dataset_marks.loc[i, 'MARK'] = 4
            elif self.dataset_marks.loc[i, 'MARK'] == 'отлично':
                self.dataset_marks.loc[i, 'MARK'] = 5
            elif self.dataset_marks.loc[i, 'MARK'] == 'зачтено':
                self.dataset_marks.loc[i, 'MARK'] = 6
            elif self.dataset_marks.loc[i, 'MARK'] == 'не зачтено':
                self.dataset_marks.loc[i, 'MARK'] = 7
            elif self.dataset_marks.loc[i, 'MARK'] == '0':
                self.dataset_marks.loc[i, 'MARK'] = 8
            else:
                self.dataset_marks.loc[i, 'DISCIPLINETYPE'] = 0

    # drop column hours and passdate
    def dropColumns(self):
        self.dataset_marks.drop(['HOURS', 'PASSDATE'], axis='columns', inplace=True)

    # convert columns from float to integer
    def toNumeric(self):
        self.dataset_marks["BALLSTOTAL"] = pd.to_numeric(self.dataset_marks["BALLSTOTAL"], downcast='integer')
        self.dataset_marks["MARK"] = pd.to_numeric(self.dataset_marks["MARK"], downcast='integer')

    #save to csv
    def saveAs(self):
        print("SAVEEEEEEE_____________________________________________________")
        self.dataset_marks.to_csv(r'..\data\Marks_new.csv')

