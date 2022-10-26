year = int(input())

def number_of_days(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 366
    else:
        return 365

print(number_of_days(year))