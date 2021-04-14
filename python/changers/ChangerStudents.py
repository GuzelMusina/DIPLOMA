from numpy import math
import pandas as pd


class ChangerStudents(object):

    def __init__(self, df):
        self.df = df

    def changeBirthplace(self):
        # заменяем значени по месту рождения
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'BIRTHPLACE'] == 'РОССИЙСКАЯ ФЕДЕРАЦИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 0
            elif self.df.loc[i, 'BIRTHPLACE'] == 'ТУРКМЕНИСТАН':
                self.df.loc[i, 'BIRTHPLACE'] = 1
            elif self.df.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА УЗБЕКИСТАН':
                self.df.loc[i, 'BIRTHPLACE'] = 2
            elif self.df.loc[i, 'BIRTHPLACE'] == 'КИТАЙСКАЯ НАРОДНАЯ РЕСПУБЛИКА':
                self.df.loc[i, 'BIRTHPLACE'] = 3
            elif self.df.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА КАЗАХСТАН':
                self.df.loc[i, 'BIRTHPLACE'] = 4
            elif self.df.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА ТАДЖИКИСТАН':
                self.df.loc[i, 'BIRTHPLACE'] = 5
            elif self.df.loc[i, 'BIRTHPLACE'] == 'КЫРГЫЗСКАЯ РЕСПУБЛИКА':
                self.df.loc[i, 'BIRTHPLACE'] = 6
            elif self.df.loc[i, 'BIRTHPLACE'] == 'ИНДОНЕЗИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 7
            elif self.df.loc[i, 'BIRTHPLACE'] == 'МОЛДОВА':
                self.df.loc[i, 'BIRTHPLACE'] = 8
            elif self.df.loc[i, 'BIRTHPLACE'] == 'АЗЕРБАЙДЖАНСКАЯ РЕСПУБЛИКА':
                self.df.loc[i, 'BIRTHPLACE'] = 9
            elif self.df.loc[i, 'BIRTHPLACE'] == 'УКРАИНА':
                self.df.loc[i, 'BIRTHPLACE'] = 10
            elif self.df.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА АРМЕНИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 11
            elif self.df.loc[i, 'BIRTHPLACE'] == 'ГВАТЕМАЛА':
                self.df.loc[i, 'BIRTHPLACE'] = 12
            elif self.df.loc[i, 'BIRTHPLACE'] == 'ГРУЗИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 13
            elif self.df.loc[i, 'BIRTHPLACE'] == 'ЧАД':
                self.df.loc[i, 'BIRTHPLACE'] = 14
            elif self.df.loc[i, 'BIRTHPLACE'] == 'НИГЕРИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 15
            elif self.df.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА ЗАМБИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 16
            elif self.df.loc[i, 'BIRTHPLACE'] == 'КОЛУМБИЯ':
                self.df.loc[i, 'BIRTHPLACE'] = 17
            elif self.df.loc[i, 'BIRTHPLACE'] == 'АФГАНИСТАН':
                self.df.loc[i, 'BIRTHPLACE'] = 18
        print("BIRTHPLACE", self.df['BIRTHPLACE'])

    def changeIsMedale(self):
        #заменяем наличие медали медали
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'MEDALE'] == 'Нет':
                self.df.loc[i, 'MEDALE']=0
            elif self.df.loc[i, 'MEDALE'] == 'Диплом с отличием':
                self.df.loc[i, 'MEDALE']=1

    def changeInstitute(self):
        #заменяем по институту
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'INSTITUTEID'] == 9483:
                self.df.loc[i, 'INSTITUTEID']=0
            elif self.df.loc[i, 'INSTITUTEID'] == 9500:
                self.df.loc[i, 'INSTITUTEID']=1
            elif self.df.loc[i, 'INSTITUTEID'] == 9499:
                self.df.loc[i, 'INSTITUTEID']=2
            elif self.df.loc[i, 'INSTITUTEID'] == 9549:
                self.df.loc[i, 'INSTITUTEID']=3
            elif self.df.loc[i, 'INSTITUTEID'] == 9579:
                self.df.loc[i, 'INSTITUTEID']=4

    def changeKindtraining(self):
        #заменяем по KINDTRAINING
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'KINDTRAINING'] == 49:
                self.df.loc[i, 'KINDTRAINING']=4

    def changeTypeOfTraining(self):
        #заменяем по TYPETRAINIG
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'TYPETRAINING'] == 1.0:
                self.df.loc[i, 'TYPETRAINING']=1
            elif self.df.loc[i, 'TYPETRAINING'] == 3.0:
                self.df.loc[i, 'TYPETRAINING']=2
            elif self.df.loc[i, 'TYPETRAINING'] == 29.0:
                self.df.loc[i, 'TYPETRAINING']=3
            elif self.df.loc[i, 'TYPETRAINING'] == 2.0:
                self.df.loc[i, 'TYPETRAINING']=4
            elif self.df.loc[i, 'TYPETRAINING'] == 28.0:
                self.df.loc[i, 'TYPETRAINING']=5
            elif math.isnan(self.df.loc[i, 'TYPETRAINING']):
                self.df.loc[i, 'TYPETRAINING']=0

    def changeQualification(self):
        #заменяем по QUALIFICATIONTYPE
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'QUALIFICATIONTYPE'] == 1.0:
                self.df.loc[i, 'QUALIFICATIONTYPE']=1
            elif self.df.loc[i, 'QUALIFICATIONTYPE'] == 2.0:
                self.df.loc[i, 'QUALIFICATIONTYPE']=2
            elif self.df.loc[i, 'QUALIFICATIONTYPE'] == 3.0:
                self.df.loc[i, 'QUALIFICATIONTYPE']=3
            elif math.isnan(self.df.loc[i, 'QUALIFICATIONTYPE']):
                self.df.loc[i, 'QUALIFICATIONTYPE']=0
    def changeCategoryId(self):
        #заменяем по CATEGORYID
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'CATEGORYID'] == 1.0:
                self.df.loc[i, 'CATEGORYID']=1
            elif self.df.loc[i, 'CATEGORYID'] == 49.0:
                self.df.loc[i, 'CATEGORYID']=2
            elif self.df.loc[i, 'CATEGORYID'] == 3.0:
                self.df.loc[i, 'CATEGORYID']=3
            elif math.isnan(self.df.loc[i, 'CATEGORYID']):
                self.df.loc[i, 'CATEGORYID']=0

    def changeCreativeActive(self):
        #заменяем по CREATICEACTIVE
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'CREATICEACTIVE'] == 1.0:
                self.df.loc[i, 'CREATICEACTIVE']=1
            elif self.df.loc[i, 'CREATICEACTIVE'] == 2.0:
                self.df.loc[i, 'CREATICEACTIVE']=2
            elif self.df.loc[i, 'CREATICEACTIVE'] == 3.0:
                self.df.loc[i, 'CREATICEACTIVE']=3
            elif math.isnan(self.df.loc[i, 'CREATICEACTIVE']):
                self.df.loc[i, 'CREATICEACTIVE']=0

    def changeOlimpiade(self):
        #заменяем по OLIMPIADE
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'OLIMPIADE'] == 1.0:
                self.df.loc[i, 'OLIMPIADE']=1
            elif math.isnan(self.df.loc[i, 'OLIMPIADE']):
                self.df.loc[i, 'OLIMPIADE']=0

    # change type of school
    # 0 - Школа (school), пусто (empty)
    # 1 - Вуз (university)
    # 2 - Лицей (lyceum)
    # 3 - Гимназия (gymnasium)
    # 4 - Колледж (college)
    # 5 - Техникум (technical college,)
    # 6 - прочее (other)
    # 7 - школа-интернат (boarding school)
    # 8 - Гимназия-интернат (boarding gymnasium)
    # 9 - Училище (college)
    # 10 - Лицей-интернат (boarding lyceum)
    # 11 - АО Ямало-Ненецкий (AO Yamalo-Nenezkii)
    def changeSchool(self):
        #заменяем значени по школе
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'TYPEOFSCHOOL'] == 'Школа':
                self.df.loc[i, 'TYPEOFSCHOOL']=0
            elif self.df.loc[i, 'TYPEOFSCHOOL'] == 'Вуз':
                self.df.loc[i, 'TYPEOFSCHOOL']=1
            elif self.df.loc[i, 'TYPEOFSCHOOL'] == 'Лицей':
                self.df.loc[i, 'TYPEOFSCHOOL']=2
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Гимназия':
                self.df.loc[i, 'TYPEOFSCHOOL']=3
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Колледж':
                self.df.loc[i, 'TYPEOFSCHOOL']=4
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Техникум':
                self.df.loc[i, 'TYPEOFSCHOOL']=5
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Прочее':
                self.df.loc[i, 'TYPEOFSCHOOL']=6
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Школа-интернат':
                self.df.loc[i, 'TYPEOFSCHOOL']=7
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Гимназия-интернат':
                self.df.loc[i, 'TYPEOFSCHOOL']=8
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Училище':
                self.df.loc[i, 'TYPEOFSCHOOL']=9
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'Лицей-интернат':
                self.df.loc[i, 'TYPEOFSCHOOL']=10
            elif self.df.loc[i, 'TYPEOFSCHOOL']== 'АО Ямало-Ненецкий':
                self.df.loc[i, 'TYPEOFSCHOOL']=11
            else:
                self.df.loc[i, 'TYPEOFSCHOOL']=0

    # change study type
    def changeStudyType(self):
        #заменяем по STUDTYPE_ID
        for i in range(0, len(self.df)):
            if self.df.loc[i, 'STUDTYPE_ID'] == 1.0:
                self.df.loc[i, 'STUDTYPE_ID']=1
            elif math.isnan(self.df.loc[i, 'STUDTYPE_ID']):
                self.df.loc[i, 'STUDTYPE_ID']=0

    # drop columns
    def dropColumns(self):
        self.df.drop(['NAME', 'FAMILIA', 'OTCHESTVO', 'BIRTHDATE', 'RESIDENCEPLACE', 'VKURL',
                               'FACEBOOK', 'INSTAURL', 'EMAIL', 'EMAILKPFU', 'FOTO', 'PLACEOFGRADUATION',
                               'COUNTRY', 'REGION','DISTRICT','CITY','LOCALITY', 'ORDERBEGIN', 'ORDEREND',
                               'PLACEOFGRADUATION', 'YEAROFGRADUATION','REASONFORLEAVING', 'DATEADMISION',
                               'STUDSTATUS', 'GROUPID','CITIZENSHIP_COUNTRY_ID', 'CITIZENSHIP_ID', 'SPECIALLITYID','SPECIALISATIONID', 'STUDY_PLAN_ID'], axis='columns', inplace=True)

    #union NAME FAMILIA and OTCHESTVO into one string FIO
    def addFIO(self):
        fio_arr = []
        for j in range(0, len(self.df)):
            st = str(str(self.df['FAMILIA'][j]) + str(' ') + str(self.df['NAME'][j])) + str(' ') + str(
                self.df['OTCHESTVO'][j])
            fio_arr.append(st)
        self.df.insert(1, 'FIO', fio_arr, True)

    #union NAME FAMILIA
    def addFI(self):
        fio_arr = []
        for j in range(0, len(self.df)):
            st = str(str(self.df['FAMILIA'][j]) + str(' ') + str(self.df['NAME'][j]))
            fio_arr.append(st)
        self.df.insert(1, 'FI', fio_arr, True)

    # convert columns from float to integer
    def toNumeric(self):
        self.df["TYPETRAINING"] = pd.to_numeric(self.df["TYPETRAINING"], downcast='integer')
        self.df["QUALIFICATIONTYPE"] = pd.to_numeric(self.df["QUALIFICATIONTYPE"], downcast='integer')
        self.df["CATEGORYID"] = pd.to_numeric(self.df["CATEGORYID"], downcast='integer')
        self.df["CREATICEACTIVE"] = pd.to_numeric(self.df["CREATICEACTIVE"], downcast='integer')
        self.df["STUDTYPE_ID"] = pd.to_numeric(self.df["STUDTYPE_ID"], downcast='integer')
        self.df["OLIMPIADE"] = pd.to_numeric(self.df["OLIMPIADE"], downcast='integer')

    # save to csv
    def saveAs(self):
        print("BIRTHPLACE", self.df['BIRTHPLACE'])
        self.df.to_csv(r'..\data\Students_new.csv')


