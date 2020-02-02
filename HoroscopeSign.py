
from datetime import date

def get_sign(day, month):
    year = 2000
    tempDate = date(year, month, day)
    
    if date(year, 3, 21) <= tempDate <= date(year, 4, 20):
        return "aries"
    elif date(year, 4, 21) <= tempDate <= date(year, 5, 21):
        return "taurus"
    elif date(year, 5, 22) <= tempDate <= date(year, 6, 21):
        return "gemini"
    elif date(year, 6, 22) <= tempDate <= date(year, 7, 22):
        return "cancer"
    elif date(year, 7, 23) <= tempDate <= date(year, 8, 23):
        return "leo"
    elif date(year, 8, 24) <= tempDate <= date(year, 9, 22):
        return "virgo"
    elif date(year, 9, 23) <= tempDate <= date(year, 10, 23):
        return "libra"
    elif date(year, 10, 24) <= tempDate <= date(year, 11, 22):
        return "scorpio"
    elif date(year, 11, 23) <= tempDate <= date(year, 12, 21):
        return "sagittarius"
    elif date(year, 12, 22) <= tempDate <= date(year, 12, 31):
        return "capricorn"
    elif date(year, 1, 1) <= tempDate <= date(year, 1, 20):
        return "capricorn"
    elif date(year, 1, 21) <= tempDate <= date(year, 2, 18):
        return "aquarius"
    elif date(year, 2, 19) <= tempDate <= date(year, 3, 20):
        return "pisces"
