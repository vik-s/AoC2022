f = open("rps.txt")
lines = f.readlines()
points = 0; points2 = 0
score_table = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
for line in lines:
    p, q = line.split()
    p = ord(p)-ord('A')
    q = ord(q)-ord('X')  
    points+=score_table[p][q] # part1   
    points2+=sorted(score_table[p])[q] # part2
print(points, points2)