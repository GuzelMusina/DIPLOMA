W = [1, 0.1, 0.1, 0.1, 0.5,
     0.1, 0.1, 0.1, 0.5, 0.1, 0.5
    , 0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5
    , 0.1, 0.5, 0.5, 1, 0.5, 0.5, 0.1, 0.1, 0.1, 2]

matrix = {'COUNT_ACTIVITIES': [45, 57, 50, 50], 'SEX': [1, 1, 1, 1],
          'BIRTHPLACE': [0, 0, 0, 0], 'INSTITUTEID': [1, 1, 1, 1],
          'ISOBCHAGA': [0, 0, 0, 0], 'MARTIALSTATUSID': [0, 0, 0, 0],
          'PUBLICATIONS': [0, 0, 0, 0], 'CONFERENCE': [0, 0, 0, 0],
          'STUDACTIVE': [0, 0, 0, 0], 'CREATICEACTIVE': [0, 0, 0, 0],
          'SOCIALACTIVE': [0, 0, 0, 0], 'MEDALE': [0, 0, 0, 0],
          'OLIMPIADE': [0, 0, 0, 0], 'TYPEOFSCHOOL': [0, 0, 0, 0],
          'COUNT_METTINGS': [3, 12, 15, 4], 'TIME_AUDIO_MINUTES': [280, 650, 850, 300],
          'TIME_VIDEO_MINUTES': [50, 190, 250, 60], 'SHARE_SCREEN_MINUTES': [0, 1, 1, 0],
          'TET_A_TET_CALLS': [0, 0, 0, 0], 'MS_MESSAGES': [0, 4, 5, 1], 'BALLSTOTAL': [56, 71, 86, 100]
          }


def algorithmFoundCriterio(df, PERCENTAGE):
    x = 0
    P = df.columns
    print("priznaki: ", P)

    classes = []
    classes.append(df[df['CLASS'] == 0])
    classes.append(df[df['CLASS'] == 1])
    classes.append(df[df['CLASS'] == 2])
    classes.append(df[df['CLASS'] == 3])
    k = 0
    # for i in range(10):
    #     for p in range(len(P)):
    #             # print(len(classes[k][classes[k][P[p]] >= 45]) / len(classes[k]))
    #             while format(len(classes[k][classes[k][P[p]]> x ]) / len(classes[k]), '.1f') != PERCENTAGE:
    #                 print(x, ' ', k)
    #                 x = x + 1
    #             else:
    #                 print(x)
    #                 matrix[p][k] = x
    #                 x = 0
    #                 if(k!=3):
    #                     k = k+1
    #                 else:
    #                     k=0

    print(matrix)

    parametrs = 0
    success = []
    for i in range(len(df)):
        student = df.loc[i]
        stud_sum = 0
        if student['CLASS'] == 0:
            k = 0
        elif student['CLASS'] == 1:
            k = 1
        elif student['CLASS'] == 2:
            k = 2
        else:
            k = 3

        if student['COUNT_ACTIVITIES'] >= matrix['COUNT_ACTIVITIES'][k]:
            # print('TRUE COUNT_ACTIVITIES')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['SEX'] == matrix['SEX'][k]:
            # print('TRUE SEX')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['BIRTHPLACE'] == matrix['BIRTHPLACE'][k]:
            # print('TRUE BIRTHPLACE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['INSTITUTEID'] == 4:
            # print('VERY TRUE INSTITUTEID')
            stud_sum = stud_sum + 1 * 0.2
            parametrs = parametrs + 1
        elif student['INSTITUTEID'] == matrix['INSTITUTEID'][k]:
            # print('TRUE INSTITUTEID')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['ISOBCHAGA'] == matrix['ISOBCHAGA'][k]:
            # print('TRUE ISOBCHAGA')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['MARTIALSTATUSID'] == matrix['MARTIALSTATUSID'][k]:
            # print('TRUE MARTIALSTATUSID')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['PUBLICATIONS'] > 0:
            # print('VERY TRUE PUBLICATIONS')
            stud_sum = stud_sum + 1 * 0.5
            parametrs = parametrs + 1
        elif student['PUBLICATIONS'] == matrix['PUBLICATIONS'][k]:
            # print('TRUE PUBLICATIONS')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['CONFERENCE'] > 0:
            # print('VERY TRUE CONFERENCE')
            stud_sum = stud_sum + 1 * 0.5
            parametrs = parametrs + 1
        elif student['CONFERENCE'] == matrix['CONFERENCE'][k]:
            # print('TRUE CONFERENCE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['STUDACTIVE'] == 1:
            # print('VERY TRUE STUDACTIVE')
            stud_sum = stud_sum + 1 * 0.2
            parametrs = parametrs + 1
        elif student['STUDACTIVE'] == matrix['STUDACTIVE'][k]:
            # print('TRUE STUDACTIVE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['CREATICEACTIVE'] == 1:
            # print('VERY TRUE CREATICEACTIVE')
            stud_sum = stud_sum + 1 * 0.2
            parametrs = parametrs + 1
        elif student['CREATICEACTIVE'] == matrix['CREATICEACTIVE'][k]:
            # print('TRUE CREATICEACTIVE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['SOCIALACTIVE'] == 1:
            # print('VERY TRUE SOCIALACTIVE')
            stud_sum = stud_sum + 1 * 0.2
            parametrs = parametrs + 1
        elif student['SOCIALACTIVE'] == matrix['SOCIALACTIVE'][k]:
            # print('TRUE SOCIALACTIVE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['MEDALE'] > 0:
            # print('VERY TRUE MEDALE')
            stud_sum = stud_sum + 1 * 0.5
            parametrs = parametrs + 1
        elif student['MEDALE'] == matrix['MEDALE'][k]:
            # print('TRUE MEDALE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['OLIMPIADE'] == 1:
            # print('VERY TRUE OLIMPIADE')
            stud_sum = stud_sum + 1 * 0.5
            parametrs = parametrs + 1
        elif student['OLIMPIADE'] == matrix['OLIMPIADE'][k]:
            # print('TRUE OLIMPIADE')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['TYPEOFSCHOOL'] == 1:
            # print('VERY TRUE TYPEOFSCHOOL')
            stud_sum = stud_sum + 1 * 0.5
            parametrs = parametrs + 1
        elif student['TYPEOFSCHOOL'] == matrix['TYPEOFSCHOOL'][k]:
            # print('TRUE TYPEOFSCHOOL')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['COUNT_METTINGS'] >= matrix['COUNT_METTINGS'][k]:
            # print('TRUE COUNT_METTINGS')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['TIME_AUDIO_MINUTES'] >= matrix['TIME_AUDIO_MINUTES'][k]:
            # print('TRUE TIME_AUDIO_MINUTES')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        if student['TIME_VIDEO_MINUTES'] >= matrix['TIME_VIDEO_MINUTES'][k]:
            # print('TRUE TIME_VIDEO_MINUTES')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['SHARE_SCREEN_MINUTES'] >= matrix['SHARE_SCREEN_MINUTES'][k]:
            # print('TRUE SHARE_SCREEN_MINUTES')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['TET_A_TET_CALLS'] >= matrix['TET_A_TET_CALLS'][k]:
            # print('TRUE TET_A_TET_CALLS')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['MS_MESSAGES'] >= matrix['MS_MESSAGES'][k]:
            # print('TRUE MS_MESSAGES')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1
        if student['BALLSTOTAL'] <= matrix['BALLSTOTAL'][k]:
            # print('TRUE BALLSTOTAL')
            stud_sum = stud_sum + 1 * W[parametrs]
            parametrs = parametrs + 1

        parametrs = 0
        # print(stud_sum)

        if stud_sum >= 6:
            success.append('success')
        elif stud_sum>=5:
            success.append('partly success')
        else:
            success.append('-')

    df.insert(1, 'SUCCESS', success, True)
    df.to_csv('Success_data.csv')
    # print(success)

