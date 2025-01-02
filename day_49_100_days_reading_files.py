# day_49_100_days_reading_files

initials = None
max_score = 0

f = open(r'C:\Users\adame\OneDrive\Desktop\python_scripts\replit_100_days_of_code\day48_100days.txt', 'r')
contents = f.read().split('\n')
f.close()

for row in contents:
    data = row.split()

    if data != []:
        if int(data[1]) > max_score:
            max_score = int(data[1])
            initials = data[0]

print(f'Max score = {max_score} for player {initials}')
