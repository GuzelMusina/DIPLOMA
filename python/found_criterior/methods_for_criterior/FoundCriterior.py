W = [1, 0.1, 0.1, 0.1, 0.5,
     0.1, 0.1, 0.1, 0.5, 0.1, 0.5
    , 0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5
    , 0.1, 0.5, 0.5, 1, 0.5, 0.5, 0.1, 0.1, 0.1, 1]


def algorithmFoundCriterio(df, K, PERCENTAGE):
    x = 0
    K = 4
    P = df.columns
    matrix = []
    for i in range(len(df)):
        for p in range(P):
            for k in K:
                if len(K[k][K[k][P[p]] >= x]) / len(K[k]) == PERCENTAGE:
                    matrix[p][k] = x
                else:
                    x = x + 1

    success = []
    for i in range(len(df)):
        stud_class = df.loc[i, 'CLASS']
        stud_sum = 0
        if stud_class == -1:
            k = 0
        elif stud_class == 0:
            k = 1
        else:
            k = 2
        for p in range(P):
            if df.loc[i, P[p]] >= matrix[p][k]:
                stud_sum = stud_sum + 1 * W[p]
            else:
                stud_sum = stud_sum + 0 * W[p]
        if stud_sum >= 7:
            success.append('success')
        else:
            success.append('not success')
