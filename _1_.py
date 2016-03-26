import psycopg2
conn = None
def days_total():
    db_name_real = []
    db_names_res = ['template0', 'template', 'template1', 'postgres']
    try:
        conn = psycopg2.connect("dbname='postgres' user='odoo' password='Cnjnhb103'")
    except:
        print conn
    cur = conn.cursor()
    cur.execute("""SELECT datname from pg_database""")


    for row in cur:
        if row[0] not in db_names_res:
            db_name_real.append(row[0])
    return db_name_real
b = days_total()
print b



