#coding=utf-8
__author__ = 'shifx'
import MySQLdb
import datetime

def mysql_connect():
    try:
        # mysql_conn = MySQLdb.connect("127.0.0.1","root","123456","db_finance",charset="utf8")
        mysql_conn = MySQLdb.connect("192.168.2.168","root","123456","db_finance",charset="utf8")
        # mysql_conn = MySQLdb.connect("192.168.0.106","report","report2018","db_finance",charset="utf8")
    except:
        print "connect mysql error"
        return 0
    return mysql_conn

#写入mysql mysql数据库需要将unnicode转换成str
def insert_mysql_t_finance_report(mysql_conn,*args):
    # print args
    # print len(args)
    if len(args) == 12:
        hid = args[0]
        sec_code = args[1]
        sec_name = args[2].encode('utf-8')
        notice_title = args[3].encode('utf-8')
        file_type = args[4]
        file_size = int(args[5])
        pdf_url = args[6]
        notice_id = int(args[7])
        notice_type = args[8]
        notice_date = args[9]
        page_count = int(args[10])
        local_file = args[11].encode('utf-8')

    try:
        mysql_cursor = mysql_conn.cursor()
        sql = '''insert into db_finance.t_finance_history_report (hid, sec_code, sec_name, notice_title, file_type, \
                  file_size, pdf_url, notice_id, notice_type, notice_date, page_count, local_file) values('%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s', '%s', '%d', '%s')''' \
                    %(hid, sec_code, sec_name, notice_title, file_type,file_size, pdf_url, notice_id, notice_type, notice_date, page_count, local_file)

        # write_file(sql)
        mysql_cursor.execute(sql)
        mysql_conn.commit()
    except:
        print "insert article into faild!"
    # time.sleep(3)
    return 0


def get_mysql_record(mysql_conn, start_date, last_date):
    mysql_cursor = mysql_conn.cursor()
    sql1 = "SELECT notice_date FROM db_finance.t_finance_history_report WHERE notice_date >= '%s' and notice_date<= '%s' order by notice_date asc limit 1;" % (start_date,last_date)
    mysql_cursor.execute(sql1)
    data = mysql_cursor.fetchone()
    try:
        last_publish_date = data[0]
    except:
        last_publish_date = last_date

    return last_publish_date

def write_file(sql):
    f = open("sql.sql",'w')
    f.write(sql)
    f.close()