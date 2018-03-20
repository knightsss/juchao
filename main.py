#coding=utf-8
__author__ = 'shifx'

import json,urllib2,urllib
import requests,simplejson
import datetime,time
from base_data_message import get_base_report_type_url

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
    r = requests.post(url, data = textmod, headers = header_dict)
    return r.content


if __name__ == '__main__':
    # test_url()
    #构造日期
    current_year = 2017
    next_year = current_year + 1
    current_date = datetime.datetime(current_year, 1, 1)
    next_year_date = datetime.datetime(next_year, 1, 1)
    last_date = next_year_date - datetime.timedelta(days=1)

    announcement_msg_list = get_base_report_type_url()

    #重启后按日期过滤，定位到某一天，从大到小
    #遍历当年的每一天
    while(last_date >= current_date):
        search_date = last_date.strftime('%Y-%m-%d')
        #遍历每个类别
        for announcement_msg in announcement_msg_list:
            announcement_type = announcement_msg['category']
            announcement_type_desc = announcement_msg['show_title'].split('/')[-1]
            #获取第一页信息,求出总页数
            contens = juchao_request(search_date, 1, announcement_type)
            json_content = simplejson.loads(contens)
            total_count = json_content['totalRecordNum']
            page_count = (total_count+29)/30
            print "search_date:",search_date," total_count:",total_count," page_count:",page_count," announcement_type_desc:",announcement_type_desc, " announcement_type:",announcement_type

            #遍历当天的所有page
            for i in range(page_count):
                page_number = i + 1
                search_content = juchao_request(search_date, page_number, announcement_type)
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
                    file_name = sec_code + sec_name + search_date + '#' + adjunct_url.split('/')[-1]
                    #获取pdf大小、页数
                    if(download_pdf(pdf_url,file_name)):
                        page_count = reload_pdf(file_name)
                        print announcement_id, '  ',sec_code,'   ',sec_name,' ' ,announcement_title,'   ',adjunct_type,' ',adjunct_size,' ',pdf_url,' ', announcement_type_desc,' ',search_date,' ',page_count ,'  ',file_name
                        #写入mysql
                    else:
                        print "download pdf error:",pdf_url
                break
            #break
        time.sleep(2)
        last_date = last_date - datetime.timedelta(days=1)