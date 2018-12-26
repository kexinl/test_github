from datetime import datetime
def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or ((year % 100 !=0) and (year % 400 == 0)):
        is_leap = True
    return is_leap
def main():
    input_date_str = input('请输入日期(yyyy/mm/dd/): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month - 1]) + day
    print('这是第几{}天.'.format(days))
if __name__ == '__main__':
    main()