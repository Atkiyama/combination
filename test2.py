
team = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

for i in range(20):
    print(team[i], end='->')
    print(team[(i+6)%20])
