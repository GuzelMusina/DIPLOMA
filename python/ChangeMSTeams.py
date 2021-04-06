class ChangeMSTeams(object):
    # dms - dataset from Microsoft Teams
    def __init__(self, dms):
        self.dms = dms

    # drop column UNI_NAME, FACULTY,  because it is only one
    def dropColumns(self):
        self.dms.drop(['UNI_NAME', 'FACULTY'], axis='columns', inplace=True)