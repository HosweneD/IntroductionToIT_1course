import datetime
from datetime import date, time
def now():
    f = datetime.datetime.now()
    dtd = date.today()
    tmd = f.time()
    s = f"Дата: {dtd} |  время: {tmd}"
    return s
