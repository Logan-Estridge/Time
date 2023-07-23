## Input Seconds Here
seconds = int(1*(10**15))
print(f'# of Seconds = {seconds:,}')
print('')

## Outputs of Hours, Minutes, Seconds
    # 1) Millennium: 10 centuries in a millennium = 31,556,952,000 (on average, removing leap seconds)
millennium = seconds // 31556952000 # seconds to millennia conversion
millennium_plus_one = millennium + 1 # convention: year 1 A.D. = 1st millennium
mod_millennium = seconds % 31556952000 # remainder_1 in seconds

    # 2) Century: 100 years in a century = 3,155,695,200 seconds on average (removing leap seconds)
centuries = seconds // 3155695200 # seconds to centuries conversion
centuries_plus_one = centuries + 1 # convention: year 1 A.D. = 1st century
mod_centuries = seconds % 3155695200 # remainder_2 in seconds

    # 3) Years: Assuming a Year has exactly 365 days, there are 31,536,000 seconds in 1 year
years = mod_centuries // 31536000 # seconds to years conversion
mod_years = mod_centuries % 31536000 # remainder_3 in seconds

    # 4) Days: There are 24 hours in 1 day = 86400 seconds
days = mod_years // 86400 # days in remainder_1
mod_days = mod_years % 86400 # remainder_4 in seconds

    # 5) Hours
hours = mod_days // 3600 # hours in remainder_2
mod_hours = mod_days % 3600 # remainder_5 in seconds

    # 6) Minutes
minutes = mod_hours // 60 # minutes in remainder_5

    # 7) Seconds
mod_minutes = mod_hours % 60 # remainder_6 of seconds leftover at end of conversion

## Converting to Strings with Relevant # of Digits
str_millennium = str(millennium)
str_millennium_plus_one = str(millennium_plus_one)
str_centuries = str(centuries)
str_centuries_plus_one = str(centuries_plus_one).zfill(2)
str_years = str(years).zfill(2)
str_days = str(days).zfill(3)
str_hours = str(hours).zfill(2)
str_minutes = str(minutes).zfill(2)
str_seconds = str(mod_minutes).zfill(2)

## Printing Outputs as Strings
print('In # of Seconds:')
print(f'''Millennium = {str_millennium_plus_one}
Century = {str_centuries_plus_one}
Year = {str_centuries + str_years}
Day = {str_days}
Hour = {str_hours}
Minute = {str_minutes}
Second = {str_seconds}''')