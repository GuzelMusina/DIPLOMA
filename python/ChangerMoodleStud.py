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
