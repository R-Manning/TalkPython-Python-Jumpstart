import datetime

def print_header():
    print('--------------------------------')
    print('     Birthday Countdown App     ')
    print('--------------------------------')


def get_birthday_from_user():
    print('When were you born?')

    while True:
        year = input('What year [YYYY]: ')
        if not year.isnumeric():
            print('Please enter an integer year')
        elif len(year) != 4:
            print('Please enter a 4 digit year')
        else:
            year = int(year)
            break
    while True:
        month = input('What month [MM]: ')
        if not month.isnumeric():
            print('Please enter an integer month')
        elif len(month) != 2:
            print('Please enter a 2 digit month')
        else:
            month = int(month)
            break
    while True:
        day = input('What day [DD]: ')
        if not day.isnumeric():
            print('Please enter an integer day')
        elif len(day) != 2:
            print('Please enter a 2 digit day')
        else:
            day = int(day)
            break

    bday = datetime.date(year, month, day)

    return bday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    diff = this_year - target_date
    return diff.days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday was {} days ago.'.format(-days))
    elif days > 0:
        print('Your birthday is coming up in {} days.'.format(days))
    else:
        print("It's your birthday, Happy Birthday!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.datetime.now().date()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()