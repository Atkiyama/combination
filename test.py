#A-Zまでの配列

team = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

for i in range(20):
    for j in range(6):
        print(team[i], end='->')
        print(team[(i+j)%20])
