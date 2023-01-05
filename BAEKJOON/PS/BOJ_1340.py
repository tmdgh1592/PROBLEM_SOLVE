month, day, year, hhmm = input().split()
day = int(day[:-1])
year = int(year)
hh, mm = map(int, hhmm.split(':'))
month_name_li = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_day_li[1] += 1
total_time = sum(month_day_li) * 24 * 60

last_month_idx = month_name_li.index(month)
current_time = (sum(month_day_li[:last_month_idx]) + day-1)*24*60 + hh*60 + mm
print(current_time/total_time * 100)
