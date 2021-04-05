import pandas as pd
class Union(object):

    #ds - modified dataset_students from Online Uni
    #dm - modified dataset_marks from Online Uni
    def __init__(self, ds, dm):
        self.ds=ds
        self.dm=dm
        self.data=0

    def unionStudAndMarks(self):
        self.ds["STUDENTID"] = self.ds["STUDENTID"].apply(pd.to_numeric, errors='ignore')

        # dm["BALLSTOTAL"] = pd.to_numeric(dm["BALLSTOTAL"], downcast='integer')
        # dm["MARK"] = pd.to_numeric(dm["MARK"], downcast='integer')

        # merge by STUDENTID
        self.data = pd.merge(self.ds, self.dm, on='STUDENTID')