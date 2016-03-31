def days_total(self):
    month = datetime.now().month
    year = datetime.now().year
    days_in_month = calendar.monthrange(year, month)[1]
    conn = None
    days_f = []
    month_f = []
    days_fest = []
    days_of_work = []
    days_total = []
    db_name = self.db_names()[1]

    try:
        conn = psycopg2.connect("dbname='%s' user='odoo' host='localhost' password='odoo'" % str(db_name))
    except:
        print "Failed to connect to database %s" % str(db_name)
    cur = conn.cursor()
    cur.execute("""SELECT date FROM hr_holidays_public WHERE employee_category_id = 4 ORDER BY 1""")

    for i in cur:
        days_f.append(i[0])
    for j in range(0, len(days_f)):
        if days_f[j].month == month:
            month_f.append(days_f[j])
    for i in range(0, len(month_f)):
        days_fest.append(month_f[i].day)
    conn.close()

    fromdate = date(year, month, 1)
    todate = date(year, month, days_in_month)
    daygenerator = (fromdate + timedelta(x)
                    for x in range((todate - fromdate).days + 1))
    for day in daygenerator:
        if day.weekday() < 5:
            days_of_work.append(day.day)
    for i in days_of_work:
        if i not in days_fest:
            days_total.append(i)
    return days_total