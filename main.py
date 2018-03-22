#coding=utf-8
__author__ = 'shifx'

import json,urllib2,urllib
import requests,simplejson
import datetime,time
from base_data_message import get_base_report_type_url
from db_mysql import get_mysql_record, mysql_connect, insert_mysql_t_finance_report

from juchao_pdf import reload_pdf,download_pdf
#定义请求头
header_dict = {
        'Host':'www.cninfo.com.cn',
        'Referer':'http://www.cninfo.com.cn/cninfo-new/announcement/show',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": 'http://www.cninfo.com.cn',
        "Proxy-Connection":'keep-alive',
    }

url='http://www.cninfo.com.cn/cninfo-new/announcement/query'

def juchao_request(search_date, page_number, category):
    textmod={
        "column": "szse",
        "columnTitle":"历史公告查询",
        "pageNum":page_number,
        "pageSize": 30,
        "tabName":'fulltext',
        "seDate":search_date,
        'category':category,
    }
    spider_result = ''
    spider_flag = True
    spider_count = 0
    while(spider_flag):
        try:
            r = requests.post(url, data = textmod, headers = header_dict, timeout=10)
            spider_result = r.content
            spider_flag = False
        except:
            if spider_count > 2:
                print "spider error...."
                spider_flag = False
            print "spider again...."
            time.sleep(1)
    return spider_result

def spider_page_report(current_year):
    next_year = current_year + 1
    start_date = datetime.datetime(current_year, 1, 1)
    next_year_date = datetime.datetime(next_year, 1, 1)
    last_date = next_year_date - datetime.timedelta(days=1)

    announcement_msg_list = get_base_report_type_url()

    #连接数据库，获取最新日期值
    db_conn = mysql_connect()
    last_date = get_mysql_record(db_conn, start_date, last_date)
    #重启后按日期过滤，定位到某一天，从大到小
    #遍历当年的每一天
    print "last date",last_date, ' start date:',start_date
    while(last_date >= start_date):
        search_date = last_date.strftime('%Y-%m-%d')
        #遍历每个类别
        for announcement_msg in announcement_msg_list:
            category_id = announcement_msg['category_id']
            announcement_type = announcement_msg['category']
            announcement_type_desc = announcement_msg['show_title'].split('/')[-1]
            #获取第一页信息,求出总页数
            contens = juchao_request(search_date, 1, announcement_type)
            if contens == '':
                continue
            json_content = simplejson.loads(contens)
            total_count = json_content['totalRecordNum']
            page_count = (total_count+29)/30
            print "time:",  , "search_date:",search_date," total_count:",total_count," page_count:",page_count," announcement_type_desc:",announcement_type_desc, " announcement_type:",announcement_type
            time.sleep(1)
            #遍历当天的所有page
            for i in range(page_count):
                page_number = i + 1
                search_content = juchao_request(search_date, page_number, announcement_type)
                if search_content == '':
                    continue
                json_search_content = simplejson.loads(search_content)
                #遍历每一个page的30条信息
                for message in json_search_content['announcements']:
                    announcement_id = message['announcementId']
                    adjunct_url = message['adjunctUrl']
                    announcementTime = message['announcementTime']
                    adjunct_type = message['adjunctType']
                    sec_name = message['secName']
                    announcement_title = message['announcementTitle']
                    org_id = message['orgId']
                    sec_code = message['secCode']
                    adjunct_size = message['adjunctSize']
                    pdf_url = 'http://www.cninfo.com.cn/' + adjunct_url
                    file_name = sec_code + sec_name.replace('*','') + search_date + '#' + adjunct_url.split('/')[-1]
                    #获取pdf大小、页数
                    if(download_pdf(pdf_url, file_name, current_year)):
                        page_count = reload_pdf(file_name, current_year)
                        print announcement_id, '  ',sec_code,'   ',sec_name,' ' ,announcement_title,'   ',adjunct_type,' ',adjunct_size,' ',pdf_url,' ', announcement_type_desc,' ',search_date,' ',page_count ,'  ',file_name
                        insert_mysql_t_finance_report(db_conn, announcement_id, sec_code, sec_name, announcement_title, adjunct_type, adjunct_size, pdf_url, category_id, announcement_type_desc, search_date, page_count, file_name)
                        #写入mysql
                    else:
                        print "download pdf error:",pdf_url
        time.sleep(2)
        last_date = last_date - datetime.timedelta(days=1)

if __name__ == '__main__':
    # test_url()
    #构造日期
    current_year = 2017
    spider_page_report(current_year)
