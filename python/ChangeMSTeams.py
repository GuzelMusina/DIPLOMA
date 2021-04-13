class ChangeMSTeams(object):
    # dms - dataset from Microsoft Teams
    def __init__(self, df):
        self.df = df

    # drop column UNI_NAME, FACULTY,  because it is only one
    def dropColumns(self):
        self.df.drop(['UNI_NAME', 'FACULTY'], axis='columns', inplace=True)