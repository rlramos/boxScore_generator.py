teamNBA = {}

statsPG = {}
statsSG = {}
statsSF = {}
statsPF = {}
statsC = {}
print()
print("Hello, welcome to the NBA score generator.")
print()
print('-' * 90)
print('POINT GUARD: ')
print('-' * 90)
namePG = input('Enter the point guard\'s name:   ')
statsPG['Points'] = input('How many points did he score?  ')
statsPG['Rebounds'] = input('How many rebounds did he end with? ')
statsPG['Assists'] = input('How many assists did he end with?   ')
teamNBA[namePG] = statsPG
print('-' * 90)
print('SHOOTING GUARD:  ')
print('-' * 90)
nameSG = input('Enter the shooting guard\'s name:   ')
statsSG['Points'] = input('How many points did he score?  ')
statsSG['Rebounds'] = input('How many rebounds did he end with? ')
statsSG['Assists'] = input('How many assists did he end with?   ')
teamNBA[nameSG] = statsSG
print('-' * 90)
print('SMALL FORWARD:   ')
print('-' * 90)
nameSF = input('Enter the small forward\'s name:   ')
statsSF['Points'] = input('How many points did he score?  ')
statsSF['Rebounds'] = input('How many rebounds did he end with? ')
statsSF['Assists'] = input('How many assists did he end with?   ')
teamNBA[nameSF] = statsSF
print('-' * 90)
print('POWER FORWARD:   ')
print('-' * 90)
namePF = input('Enter the power forward\'s name:   ')
statsPF['Points'] = input('How many points did he score?  ')
statsPF['Rebounds'] = input('How many rebounds did he end with? ')
statsPF['Assists'] = input('How many assists did he end with?   ')
teamNBA[namePF] = statsPF
print('-' * 90)
print('CENTER:  ')
print('-' * 90)
nameC = input('Enter the center\'s name:   ')
statsC['Points'] = input('How many points did he score?  ')
statsC['Rebounds'] = input('How many rebounds did he end with? ')
statsC['Assists'] = input('How many assists did he end with?   ')
teamNBA[nameC] = statsC
print('-' * 90)
print()
print('-' * 90)

def totalCat(team, stats):
    num = 0
    for k, v in team.items():
        num = num + int(v.get(stats, 0))
    return num

print('{:^90}'.format('Total Team Box Scores:'))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format('Player Name', 'Points', 'Rebounds', 'Assists'))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format(namePG, statsPG['Points'], statsPG['Rebounds'], statsPG['Assists']))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format(nameSG, statsSG['Points'], statsSG['Rebounds'], statsSG['Assists']))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format(nameSF, statsSF['Points'], statsSF['Rebounds'], statsSF['Assists']))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format(namePF, statsPF['Points'], statsPF['Rebounds'], statsPF['Assists']))
print('-' * 90)
print("{:^22}{:^22}{:^22}{:^22}".format(nameC, statsC['Points'], statsC['Rebounds'], statsC['Assists']))
print('-' * 90)
print('Total Points:    ' + str(totalCat(teamNBA, 'Points')))
print('Total Rebounds:  ' + str(totalCat(teamNBA, 'Rebounds')))
print('Total Assists:   ' + str(totalCat(teamNBA, 'Assists')))
print('-' * 90)
