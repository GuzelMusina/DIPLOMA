
class ChangerStudents(object):

    def __init__(self, dataset_students):
        self.dataset_students = dataset_students

    def changeBirthplace(self):
        # заменяем значени по месту рождения
        for i in range(0, len(self.dataset_students)):
            if self.dataset_students.loc[i, 'BIRTHPLACE'] == 'РОССИЙСКАЯ ФЕДЕРАЦИЯ':
                self.dataset_students.loc[i, 'BIRTHPLACE'] = 0
            elif self.dataset_students.loc[i, 'BIRTHPLACE'] == 'ТУРКМЕНИСТАН':
                self.dataset_students.loc[i, 'BIRTHPLACE'] = 1
            elif self.dataset_students.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА УЗБЕКИСТАН':
                self.dataset_students.loc[i, 'BIRTHPLACE'] = 2
            elif self.dataset_students.loc[i, 'BIRTHPLACE'] == 'КИТАЙСКАЯ НАРОДНАЯ РЕСПУБЛИКА':
                self.dataset_students.loc[i, 'BIRTHPLACE'] = 3
            elif self.dataset_students.loc[i, 'BIRTHPLACE'] == 'РЕСПУБЛИКА КАЗАХСТАН':
                self.dataset_students.loc[i, 'BIRTHPLACE'] = 4
        print("BIRTHPLACE", self.dataset_students['BIRTHPLACE'])

    def changeIsMedale(self):
        #заменяем наличие медали медали
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'MEDALE'] == 'Нет':
                self.dataset_students.loc[i,'MEDALE']=0
            elif self.dataset_students.loc[i,'MEDALE'] == 'Диплом с отличием':
                self.dataset_students.loc[i,'MEDALE']=1

    def changeInstitute(self):
        #заменяем по институту
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'INSTITUTEID'] == 9483:
                self.dataset_students.loc[i,'INSTITUTEID']=0
            elif self.dataset_students.loc[i,'INSTITUTEID'] == 9500:
                self.dataset_students.loc[i,'INSTITUTEID']=1
            elif self.dataset_students.loc[i,'INSTITUTEID'] == 9499:
                self.dataset_students.loc[i,'INSTITUTEID']=2
            elif self.dataset_students.loc[i,'INSTITUTEID'] == 9549:
                self.dataset_students.loc[i,'INSTITUTEID']=3
            elif self.dataset_students.loc[i,'INSTITUTEID'] == 9579:
                self.dataset_students.loc[i,'INSTITUTEID']=4

    def changeKindtraining(self):
        #заменяем по KINDTRAINING
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'KINDTRAINING'] == 49:
                self.dataset_students.loc[i,'KINDTRAINING']=4

    def changeTypeOfTraining(self):
        #заменяем по TYPETRAINIG
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'TYPETRAINING'] == 1.:
                self.dataset_students.loc[i,'TYPETRAINING']=1
            elif self.dataset_students.loc[i,'TYPETRAINING'] == 3.:
                self.dataset_students.loc[i,'TYPETRAINING']=2
            elif self.dataset_students.loc[i,'TYPETRAINING'] == 29.:
                self.dataset_students.loc[i,'TYPETRAINING']=3
            elif self.dataset_students.loc[i,'TYPETRAINING'] == 2.:
                self.dataset_students.loc[i,'TYPETRAINING']=4
            elif self.dataset_students.loc[i,'TYPETRAINING'] == 28.:
                self.dataset_students.loc[i,'TYPETRAINING']=5
            elif self.dataset_students.loc[i,'TYPETRAINING'] == '':
                self.dataset_students.loc[i,'TYPETRAINING']=0

    def changeQualification(self):
        #заменяем по QUALIFICATIONTYPE
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'QUALIFICATIONTYPE'] == 1.:
                self.dataset_students.loc[i,'QUALIFICATIONTYPE']=1
            elif self.dataset_students.loc[i,'QUALIFICATIONTYPE'] == 2.:
                self.dataset_students.loc[i,'QUALIFICATIONTYPE']=2
            elif self.dataset_students.loc[i,'QUALIFICATIONTYPE'] == 3.:
                self.dataset_students.loc[i,'QUALIFICATIONTYPE']=3
            elif self.dataset_students.loc[i,'QUALIFICATIONTYPE'] == '':
                self.dataset_students.loc[i,'QUALIFICATIONTYPE']=0
    def changeCategoryId(self):
        #заменяем по CATEGORYID
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'CATEGORYID'] == 1.:
                self.dataset_students.loc[i,'CATEGORYID']=1
            elif self.dataset_students.loc[i,'CATEGORYID'] == 49.:
                self.dataset_students.loc[i,'CATEGORYID']=2
            elif self.dataset_students.loc[i,'CATEGORYID'] == 3.:
                self.dataset_students.loc[i,'CATEGORYID']=3
            elif self.dataset_students.loc[i,'CATEGORYID'] == '':
                self.dataset_students.loc[i,'CATEGORYID']=0

    def changeCreativeActive(self):
        #заменяем по CREATICEACTIVE
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'CREATICEACTIVE'] == 1.:
                self.dataset_students.loc[i,'CREATICEACTIVE']=1
            elif self.dataset_students.loc[i,'CREATICEACTIVE'] == 2.:
                self.dataset_students.loc[i,'CREATICEACTIVE']=2
            elif self.dataset_students.loc[i,'CREATICEACTIVE'] == 3.:
                self.dataset_students.loc[i,'CREATICEACTIVE']=3
            elif self.dataset_students.loc[i,'CREATICEACTIVE'] == '':
                self.dataset_students.loc[i,'CREATICEACTIVE']=0

    def changeOlimpiade(self):
        #заменяем по OLIMPIADE
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'CREATICEACTIVE'] == 1.:
                self.dataset_students.loc[i,'CREATICEACTIVE']=1
            elif self.dataset_students.loc[i,'CREATICEACTIVE'] == '':
                self.dataset_students.loc[i,'CREATICEACTIVE']=0

    def changeSchool(self):
        #заменяем значени по школе
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'TYPEOFSCHOOL'] == 'Школа':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=0
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL'] == '':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=0
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL'] == 'Вуз':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=1
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL'] == 'Лицей':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=2
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Гимназия':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=3
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Колледж':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=4
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Техникум':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=5
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Прочее':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=6
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Школа-интернат':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=7
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Гимназия-интернат':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=8
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Училище':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=9
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'Лицей-интернат':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=10
            elif self.dataset_students.loc[i,'TYPEOFSCHOOL']== 'АО Ямало-Ненецкий':
                self.dataset_students.loc[i,'TYPEOFSCHOOL']=11

    def changeStudyType(self):
        #заменяем по STUDTYPE_ID
        for i in range(0,len(self.dataset_students)):
            if self.dataset_students.loc[i,'STUDTYPE_ID'] == 1.:
                self.dataset_students.loc[i,'STUDTYPE_ID']=1
            elif self.dataset_students.loc[i,'STUDTYPE_ID'] == '':
                self.dataset_students.loc[i,'STUDTYPE_ID']=0

    def dropColumns(self):
        self.dataset_students.drop(['NAME', 'FAMILIA', 'OTCHESTVO','BIRTHDATE', 'RESIDENCEPLACE','VKURL',
                               'FACEBOOK', 'INSTAURL', 'EMAIL', 'EMAILKPFU', 'FOTO', 'PLACEOFGRADUATION',
                               'COUNTRY', 'REGION','DISTRICT','CITY','LOCALITY', 'ORDERBEGIN', 'ORDEREND',
                               'PLACEOFGRADUATION', 'YEAROFGRADUATION','REASONFORLEAVING', 'DATEADMISION',
                               'STUDSTATUS', 'CITIZENSHIP_COUNTRY_ID', 'CITIZENSHIP_ID'], axis='columns', inplace=True)

    def addFIO(self):
        fio_arr = []
        for j in range(0, len(self.dataset_students)):
            st = str(self.dataset_students['NAME'][j]) + str(' ') + str(self.dataset_students['FAMILIA'][j]) + str(' ') + str(
                self.dataset_students['OTCHESTVO'][j])
            fio_arr.append(st)
        self.dataset_students.insert(1, 'FIO', fio_arr, True)

    def saveAs(self):
        print("BIRTHPLACE", self.dataset_students['BIRTHPLACE'])
        self.dataset_students.to_csv('Students_new.csv')
