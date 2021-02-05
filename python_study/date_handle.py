# from datetime import timedelta, date

# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2021, 1, 1)
# end_date = date(2021, 2, 1)

# date_list = []
# for single_date in daterange(start_date, end_date):
#     date_list.append(single_date.strftime("%Y%m%d"))

# print(date_list)

from datetime import date, timedelta

start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    print (start_date.strftime("%Y-%m-%d"))
    start_date += delta