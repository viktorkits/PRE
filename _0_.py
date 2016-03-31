import calendar
import psycopg2
from  datetime import datetime

def days_total():
    month = datetime.now().month
    year = datetime.now().year
    days_in_month = calendar.monthrange(year, month)[1]

    days_f = []
    month_f = []
    days_fest = []
    days_of_work = []
    days_total = []

    try:
        conn = psycopg2.connect("dbname='odoo_01_2016' user='odoo' host='localhost' password=''")
    except:
        print "Failed to connect to database"
    cur = conn.cursor()
    cur.execute("""SELECT date FROM hr_holidays_public WHERE employee_category_id = 4 ORDER BY 1""")

    for i in cur:
        days_f.append(i[0])
    for j in range(0,len(days_f)):
        if days_f[j].month == month:
             month_f.append(days_f[j])
    for i in range(0, len(month_f)):
        days_fest.append(month_f[i].day)

    from datetime import date,timedelta
    fromdate = date(year,month, 1)
    todate = date(year,month,days_in_month)
    daygenerator = (fromdate + timedelta(x)
    for x in range((todate - fromdate).days + 1))
    for day in daygenerator:
        if day.weekday() < 5:
            days_of_work.append(day.day)
    for i in days_of_work:
        if i not in days_fest:
            days_total.append(i)
    return days_total, days_fest

x = days_total()
print x[1]





