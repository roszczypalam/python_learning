teams = [
    'Real Madryt',
    'Fc Barcelona',
    'Legia Warszawa',
    'Bayern Monachium',
    'Widzew Łódź',
    'Atletico Madrid',
    'Ajax Amsterdam'
]

#===================================== 
# for x in [1,2,3]:
    # for y in [4,5,6]:
        # print(x, y)

# print(lista_meczy)

# lista_meczy = []

# pierwsza_druzyna = teams[0]

# for team in teams[1:]:
    # para = [pierwsza_druzyna, team]

    # lista_meczy.append(para)
    

# print(lista_meczy)


# ========================================

lista_meczy = []

for team in teams:

    for team2 in teams:
        if team != team2:
            para = [team , team2]
            lista_meczy.append(para)

teams = [
    'Real Madryt',
    'Fc Barcelona',
    'Legia Warszawa',
    'Bayern Monachium',
    'Widzew Łódź',
    'Atletico Madrid',
    'Ajax Amsterdam'
]


# print(lista_meczy)


# ========================================

# for team in teams:
    # print(team)


# [['druzynaA', 'druzynaB'], ['druzynaA', 'druzynaC']]


