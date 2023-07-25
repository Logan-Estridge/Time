
t = int(input('''Enter current military time (hours only, e.g. 5:00 PM == 17): '''))
n = int(input('Enter number of hours to wait: '))
print('')

t_new = t + n  # Problem: what if new time is >= 24?
day = t_new // 24  # Solution: add a day counter. E.g. t_new = 49 --> 49 // 24 = 2 days passed

# if new time is more than 1 day passed
# then subtract the number of days passed in hours.
# E.g. t_new = 49 hours - (24 hours * 2 days) = 49 - 48 = 1

if t_new >= 24:
    t_new = t_new-(24*day)

print(f'''Days passed: {day}
New time: {t_new}''')
