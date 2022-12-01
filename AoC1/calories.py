f = open("calories.txt")
lines = f.readlines()

sum_cal = []
calorie = 0

for line in lines:
    if line != '\n':
        calorie += int(line)
    else:
        sum_cal += [calorie]
        calorie = 0

for i, val in enumerate(sum_cal):
    if val == max(sum_cal): print(i, max(sum_cal))

# sum of top 3 calories
sum_cal.sort(reverse=True)
top3 = 0
for i in range(3):
    top3 += sum_cal[i]

print(top3)