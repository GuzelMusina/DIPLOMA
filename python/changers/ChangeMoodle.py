import pandas as pd

# класс для обработки данных (логов) из мудл
class ChangeMoodle(object):
    def __init__(self, df):
       self.df=df

    #сортировка по userid
    def sorted_by_userid(self):
        sorted_data = self.df.sort_values(by='userid')
        return sorted_data

    # удаление признаков
    def dropColumns(self):
        self.df.drop(['component', 'action', 'target', 'objecttable', 'courseid',
                      'timecreated', 'movements', 'date', 'date_and_time'], axis='columns', inplace=True)

    # метод поодсчитывает количество активностей у каждого пользователя
    def analyzeLogs(self, df):
        count = 1
        # создано два массива с id студентов и count - количество их движений в moodle
        arr_userid = df.userid.unique()
        arr_count = [1]
        print(df)
        # массив отсортирован по возрастанию
        # циклом проверяю если предыдущий id равен текщему id,
        for i in range(1, len(df)):
            if df['userid'][i-1] == df['userid'][i]:
                    # то увеличиваем count
                count = count + 1
            elif df['userid'][i-1] != df['userid'][i]:
                print('count', count, ' user id i+1 ',df['userid'][i-1],
                        ' user id i ', df['userid'][i])
                    # иначе, если id не совпадают, то записываю count с прошлого id в массив
                arr_count.append(count)
                count = 1

        if len(arr_userid)>len(arr_count):
            print('БОЛЬШЕ длина userid = ', len(arr_userid), 'длина count = ', len(arr_count))
        elif len(arr_userid)<len(arr_count):
            print('МЕНЬШЕ длина userid = ', len(arr_userid), 'длина count = ', len(arr_count))
        else:
            print('РАВНО длина userid = ', len(arr_userid), 'длина count = ', len(arr_count))
        diction = {'userid': arr_userid, 'count': arr_count}

        return diction




