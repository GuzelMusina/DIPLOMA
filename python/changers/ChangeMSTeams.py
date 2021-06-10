# класс для обработки данных Microsoft Teams
class ChangeMSTeams(object):

    # df - dataset from Microsoft Teams
    def __init__(self, df):
        self.df = df

    # удаление признаков
    def dropColumns(self):
        self.df.drop(['UNI_NAME', 'FACULTY'], axis='columns', inplace=True)