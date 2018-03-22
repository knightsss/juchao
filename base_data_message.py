#coding=utf-8
__author__ = 'shifx'

#获取最基础的报告类型url ---公司研究 行业研究
def get_base_report_type_url():
    base_report_type_url_list = []


    report_dict = {}
    report_dict['category_id'] = 1
    report_dict['category'] = 'category_ndbg_szsh;'
    report_dict['show_title'] = 'category_ndbg_szsh/category/年度报告'
    base_report_type_url_list.append(report_dict)


    report_dict = {}
    report_dict['category_id'] = 2
    report_dict['category'] = 'category_bndbg_szsh;'
    report_dict['show_title'] = 'category_bndbg_szsh/category/半年度报告'
    base_report_type_url_list.append(report_dict)


    report_dict = {}
    report_dict['category_id'] = 3
    report_dict['category'] = 'category_yjdbg_szsh;;'
    report_dict['show_title'] = 'category_yjdbg_szsh/category/一季度报告'
    base_report_type_url_list.append(report_dict)


    report_dict = {}
    report_dict['category_id'] = 4
    report_dict['category'] = 'category_sjdbg_szsh;;'
    report_dict['show_title'] = 'category_sjdbg_szsh/category/三季度报告'
    base_report_type_url_list.append(report_dict)


    report_dict = {}
    report_dict['category_id'] = 5
    report_dict['category'] = 'category_scgkfx_szsh;'
    report_dict['show_title'] = 'category_scgkfx_szsh/category/首次公开发行及上市'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 6
    report_dict['category'] = 'category_pg_szsh;'
    report_dict['show_title'] = 'category_pg_szsh/category/配股'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 7
    report_dict['category'] = 'category_zf_szsh;'
    report_dict['show_title'] = 'category_zf_szsh/category/增发'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 8
    report_dict['category'] = 'category_kzhz_szsh;'
    report_dict['show_title'] = 'category_kzhz_szsh/category/可转换债券'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 9
    report_dict['category'] = 'category_qzxg_szsh;'
    report_dict['show_title'] = 'category_qzxg_szsh/category/权证相关公告'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 10
    report_dict['category'] = 'category_qtrz_szsh;'
    report_dict['show_title'] = 'category_qtrz_szsh/category/其他融资'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 11
    report_dict['category'] = 'category_qyfpxzcs_szsh;'
    report_dict['show_title'] = 'category_qyfpxzcs_szsh/category/权益及限制出售股份'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 12
    report_dict['category'] = 'category_gqbd_szsh;'
    report_dict['show_title'] = 'category_gqbd_szsh/category/股权变动'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 13
    report_dict['category'] = 'category_jy_szsh;'
    report_dict['show_title'] = 'category_jy_szsh/category/交易'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 14
    report_dict['category'] = 'category_gddh_szsh;'
    report_dict['show_title'] = 'category_gddh_szsh/category/股东大会'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 15
    report_dict['category'] = 'category_cqfxyj_szsh;'
    report_dict['show_title'] = 'category_cqfxyj_szsh/category/澄清风险业绩预告'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 16
    report_dict['category'] = 'category_tbclts_szsh;'
    report_dict['show_title'] = 'category_tbclts_szsh/category/特别处理和退市'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 17
    report_dict['category'] = 'category_bcgz_szsh;'
    report_dict['show_title'] = 'category_bcgz_szsh/category/补充及更正'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 18
    report_dict['category'] = 'category_zjjg_szsh;'
    report_dict['show_title'] = 'category_zjjg_szsh/category/中介机构报告'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 19
    report_dict['category'] = 'category_ssgszd_szsh;'
    report_dict['show_title'] = 'category_ssgszd_szsh/category/上市公司制度'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 20
    report_dict['category'] = 'category_zqgg_szsh;'
    report_dict['show_title'] = 'category_zqgg_szsh/category/债券公告'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 21
    report_dict['category'] = 'category_qtzdsx_szsh;'
    report_dict['show_title'] = 'category_qtzdsx_szsh/category/其它重大事项'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 22
    report_dict['category'] = 'category_tzzgx_szsh;'
    report_dict['show_title'] = 'category_tzzgx_szsh/category/投资者关系信息'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 23
    report_dict['category'] = 'category_dshgg_szsh;'
    report_dict['show_title'] = 'category_dshgg_szsh/category/董事会公告'
    base_report_type_url_list.append(report_dict)

    report_dict = {}
    report_dict['category_id'] = 24
    report_dict['category'] = 'category_jshgg_szsh;'
    report_dict['show_title'] = 'category_jshgg_szsh/category/监事会公告'
    base_report_type_url_list.append(report_dict)

    return base_report_type_url_list

def get_pre_disclosure_report_type():
    base_report_type_url_list = []

    report_dict = {}
    report_dict['category_id'] = 0
    report_dict['category'] = ''
    report_dict['show_title'] = '/'
    base_report_type_url_list.append(report_dict)

    return base_report_type_url_list