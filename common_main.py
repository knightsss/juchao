#coding=utf-8
__author__ = 'shifx'

import json,urllib2,urllib
import requests,simplejson
import datetime,time
from db_mysql import get_mysql_record, mysql_connect, insert_mysql_t_finance_report

from juchao_pdf import reload_pdf,download_pdf
from base_data_message import get_base_report_type_url, get_pre_disclosure_report_type, get_neeq_company_report_type, get_hke_report_type, get_fund_report_type, get_regulator_report_type
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

#预披露
def juchao_request(request_column, page_number, search_date, category):

    if category == '':
        textmod={
            "column": request_column,
            "columnTitle":"历史公告查询",
            "pageNum":page_number,
            "pageSize": 30,
            "tabName":'fulltext',
            "seDate":search_date,
        }
    elif category == 'jgjg_sz' or category == 'jgjg_sh':
        textmod={
            "column": request_column,
            "columnTitle":"历史公告查询",
            "pageNum":page_number,
            "pageSize": 30,
            "tabName":'fulltext',
            "seDate":search_date,
            'plate':category,
        }
    else:
        textmod={
            "column": request_column,
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

def spider_page_report(current_year,table_name, request_column, announcement_msg_list):
    next_year = current_year + 1
    start_date = datetime.datetime(current_year, 1, 1)
    next_year_date = datetime.datetime(next_year, 1, 1)
    last_date = next_year_date - datetime.timedelta(days=1)


    today_date = datetime.datetime.today()
    if last_date > today_date:
        last_date = today_date
    #连接数据库，获取最新日期值
    db_conn = mysql_connect()
    if db_conn == 0:
        return 0
    start_date = get_mysql_record(db_conn, table_name, start_date, last_date)
    #重启后按日期过滤，定位到某一天，从大到小
    #遍历当年的每一天
    print "last date",last_date, ' start date:',start_date
    while(last_date >= start_date):
        search_date = start_date.strftime('%Y-%m-%d')
        #遍历每个类别
        for announcement_msg in announcement_msg_list:
            category_id = announcement_msg['category_id']
            announcement_type = announcement_msg['category']
            announcement_type_desc = announcement_msg['show_title'].split('/')[-1]
            #获取第一页信息,求出总页数
            contens = juchao_request(request_column, 1, search_date, announcement_type)
            #print "contents",contens
            if contens == '':
                continue
            try:
                json_content = simplejson.loads(contens)
            except:
                print "network error!!!"
                continue
            total_count = json_content['totalRecordNum']
            page_count = (total_count+29)/30
            print "time:", time.strftime("%Y%m%d %H:%M:%S", time.localtime())," search_date:",search_date," total_count:",total_count," page_count:",page_count," announcement_type_desc:",announcement_type_desc, " announcement_type:",announcement_type
            # time.sleep(500)
            #break
            #time.sleep(1)
            #遍历当天的所有page
            for i in range(page_count):
                page_number = i + 1
                search_content = juchao_request(request_column, page_number, search_date, announcement_type)
                if search_content == '':
                    continue
                json_search_content = simplejson.loads(search_content)
                #遍历每一个page的30条信息
                for message in json_search_content['announcements']:
                    announcement_id = message['announcementId']
                    adjunct_url = message['adjunctUrl']
                    #announcementTime = message['announcementTime']
                    adjunct_type = message['adjunctType']
                    sec_name = message['secName']
                    announcement_title = message['announcementTitle']
                    #org_id = message['orgId']
                    sec_code = message['secCode']
                    adjunct_size = message['adjunctSize']

                    #去除多余的code
                    try:
                        sec_code = sec_code.encode('utf-8').split(',')[0]
                    except:
                        sec_code = sec_code.encode('utf-8')

                    if adjunct_type == 'PDF' or adjunct_type == 'pdf':
                        pdf_url = 'http://www.cninfo.com.cn/' + adjunct_url
                        try:
                            file_name = sec_code + sec_name.replace('*','') + search_date + '#' + adjunct_url.split('/')[-1]
                        except:
                            file_name = announcement_title + search_date + '#' + adjunct_url.split('/')[-1]
                        #获取pdf大小、页数
                        if(download_pdf(pdf_url, file_name, current_year, request_column)):
                            page_count = reload_pdf(file_name, current_year, request_column)
                            #print announcement_id, '  ',sec_code,'   ',sec_name.encode('utf-8'),' ' ,announcement_title.encode('utf-8'),'   ',adjunct_type,' ',adjunct_size,' ',pdf_url,' ', announcement_type_desc,' ',search_date,' ',page_count ,'  ',file_name.encode('utf-8')
                            #print type(announcement_id), '  ',type(sec_code),'   ',type(sec_name),' ' ,type(announcement_title),'   ',type(adjunct_type),' ',type(adjunct_size),' ',type(pdf_url),' ', type(announcement_type_desc),' ',type(search_date),' ',type(page_count) ,'  ',type(file_name)
                            insert_mysql_t_finance_report(db_conn, table_name, announcement_id, sec_code, sec_name, announcement_title, adjunct_type, adjunct_size, pdf_url, category_id, announcement_type_desc, search_date, page_count, file_name)
                            #写入mysql
                        else:
                            print "download pdf error:",pdf_url
                    if request_column == 'regulator' and  (adjunct_type == 'TXT' or adjunct_type == 'txt') :
                        pdf_url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/regulator/bulletin_detail/true/' + announcement_id + '?announceTime=' + search_date
                        page_count = 0
                        file_name = ''
                        insert_mysql_t_finance_report(db_conn, table_name, announcement_id, sec_code, sec_name, announcement_title, adjunct_type, adjunct_size, pdf_url, category_id, announcement_type_desc, search_date, page_count, file_name)
                    #time.sleep(2)
            #break
        #time.sleep(1)
        start_date = start_date + datetime.timedelta(days=1)
import sys
if __name__ == '__main__':
    # test_url()
    #构造日期
    if len(sys.argv) == 3:
        if 1:
            current_year = int(sys.argv[1])
            index = int(sys.argv[2])
            if current_year>1999 and current_year<2018:

                if index == 0:
                    table_name = 't_finance_history_report'
                    request_column = "szse"
                    announcement_msg_list = get_base_report_type_url()
                    spider_page_report(current_year,table_name,request_column, announcement_msg_list)
                elif index == 1:
                    print index
                    #预披露公告 pre_disclosure
                    #current_year = 2017
                    table_name = 't_finance_pre_disclosure_report'
                    request_column = "pre_disclosure"
                    announcement_msg_list = get_pre_disclosure_report_type()
                    spider_page_report(current_year,table_name,request_column, announcement_msg_list)
                elif index == 2:
                    print index
                     #股份转让系统挂牌公司公告 neeq_company
                    # current_year = 2017
                    table_name = 't_finance_neeq_company_report'
                    request_column = "neeq_company"
                    announcement_msg_list = get_neeq_company_report_type()
                    spider_page_report(current_year, table_name, request_column, announcement_msg_list)
                elif index == 3:
                    print index
                    #香港公告hke
                    # current_year = 2017
                    table_name = 't_finance_hke_report'
                    request_column = "hke"
                    announcement_msg_list = get_hke_report_type()
                    spider_page_report(current_year, table_name, request_column, announcement_msg_list)
                elif index == 4:
                    print index
                     #基金公告 fund
                    #current_year = 2017
                    table_name = 't_finance_fund_report'
                    request_column = "fund"
                    announcement_msg_list = get_fund_report_type()
                    spider_page_report(current_year, table_name, request_column, announcement_msg_list)
                elif index == 5:
                    print index
                    #监管公告 bond
                    # current_year = 2017
                    table_name = 't_finance_regulator_report'
                    request_column = "regulator"
                    announcement_msg_list = get_regulator_report_type()
                    spider_page_report(current_year, table_name, request_column, announcement_msg_list)
                else:
                    print "编号 1-5"
            else:
                print "年份 2000-2017"
        else:
            print "格式 python common_main.py 2017 1"
    print "格式 python common_main 2017 1"

