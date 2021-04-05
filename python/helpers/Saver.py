#class which save into different files
class Saver(object):

    def saveToCSV(self, data, path):
        data.to_csv(path)