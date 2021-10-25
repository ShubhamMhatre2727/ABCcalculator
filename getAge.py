from datetime import date, datetime
import calendar


def calculateAge(birthDate):
    
    # converting string to date 
    birthDate = datetime.strptime(birthDate, "%Y-%m-%d")
    birthDate = birthDate.date()

    # print(type(birthDate))
    # print(birthDate)

    # getting current date
    today = date.today()

    years = today.year - birthDate.year
    months = today.month - birthDate.month
    days = today.day - birthDate.day 

    end_date = today
    start_date = birthDate
    
    # persons birth months
    birth_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # persons birth days
    delta = end_date - start_date
    birth_days = delta.days

    # persons birth weeks
    birth_weeks = abs(birth_days//7)

    # persons birth Hours
    birth_hours = birth_days*24

    # persons birth minutes
    birth_minutes = birth_hours*60

    

    # print(years, months, days, birth_months, birth_weeks,birth_days, birth_hours, birth_minutes)
    return {
        'years': years,
        'months': months,
        'days': days,
        'birth_months': birth_months,
        'birth_week': birth_weeks,
        'birth_days': birth_days,
        'birth_hours': birth_hours,
        'birth_minutes': birth_minutes,
    }


# print(calculateAge('2001-06-22'))