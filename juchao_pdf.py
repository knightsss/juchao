#coding=utf-8
__author__ = 'shifx'
import os
import time
import urllib2
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfrw import PdfReader
def get_page(url):
    # page = urllib2.request.urlopen(url)
    get_html_flag = True
    count = 0
    while get_html_flag:
        try:
            req = urllib2.Request(url = url)
            page = urllib2.urlopen(req)
            get_html_flag = False
        except:
            print "spider page again..."
            if count > 0:
                get_html_flag = False
                print "spider error..."
                page = ''
        count = count + 1
    return page

def get_pdf_path():
    pwd = os.getcwd()
    print pwd
    father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    print father_path
    return father_path

#返回是否成功下载
def download_pdf(url, file_name, current_year, request_column):

    path_file_name =  '/home/user1/python/common/file/' + str(request_column) + '/' + str(current_year) + '/' + file_name
    path_file_name = file_name
    page = get_page(url)
    if page == '':
        print ("faild to download" + " " + path_file_name)
        return False
    else:
        f = open(path_file_name, 'wb')
        block_sz = 8192
        while True:
            buffer = page.read(block_sz)
            if not buffer:
                break
            f.write(buffer)
        f.close()
        # print ("Sucessful to download" + " " + path_file_name)
        return True


#通过文件名 获取文件页数，文件大小 旧版
def reload_pdf_page_size(file_name):
    # 获取一个 PdfFileReader 对象
    page_count = 0
    file_size = 0
    # path_file_name = 'home/user1/python/report/file/' + file_name
    path_file_name = file_name
    try:
        pdf_input = PdfFileReader(open(path_file_name, 'rb'))
        # 获取 PDF 的页数
        page_count = pdf_input.getNumPages()
    except:
        page_count = 0
    try:
        file_size = get_FileSize(path_file_name)
    except:
        file_size = 0
    return page_count,file_size


#通过文件名 获取文件页数，文件大小
def reload_pdf(file_name, current_year, request_column):
    # 获取一个 PdfFileReader 对象
    page_count = 0
    file_size = 0

    path_file_name = '/home/user1/python/common/file/' + str(request_column) + '/' + str(current_year) + '/' + file_name
    path_file_name = file_name
    try:
        pdf_input = PdfFileReader(open(path_file_name, 'rb'))
        # 获取 PDF 的页数
        page_count = pdf_input.getNumPages()
    except:
        print "get pdf count error!"
        page_count = 0
        # try:
        #     page_count = len(PdfReader(path_file_name).pages)
        #     print 'pdf File has not been decrypted '
        # except:

    return page_count

def get_FileSize(filePath):
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)
    return round(fsize)