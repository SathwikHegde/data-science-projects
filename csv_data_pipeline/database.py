import cx_Oracle

def run_select_query():
    conn_str = ''
    try:
        con = cx_Oracle.connect(conn_str)
        cur = con.cursor()
        cur.execute("SELECT * FROM file_name")
        row = cur.fetchone()
        print("First row:", row)
        cur.close()
        con.close()
    except Exception as e:
        print("Database error:", e)

if __name__ == "__main__":
    run_select_query()
