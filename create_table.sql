
CREATE database db_finance DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci

CREATE TABLE `t_finance_research_report` (
  `report_id` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `publish_date` datetime DEFAULT NULL COMMENT '发表时间',
  `report_type_id` int(11) DEFAULT NULL COMMENT '报告类型ID',
  `report_type` varchar(40) DEFAULT NULL COMMENT '报告类型',
  `report_title` varchar(500) DEFAULT NULL COMMENT '研报标题',
  `report_organization` varchar(40) DEFAULT NULL COMMENT '研报机构',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `page_count` int(11) DEFAULT NULL COMMENT '页数',
  `file_url` varchar(200) DEFAULT NULL COMMENT '文件地址',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT 'pdf地址',
  `report_content` text COMMENT '报告内容',
  `file_local_path` varchar(400) DEFAULT NULL COMMENT '文件本地路径'
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `t_finance_history_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8



#预披露
CREATE TABLE `t_finance_pre_disclosure_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8

#股份装让
CREATE TABLE `t_finance_neeq_company_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8

#香港公告
CREATE TABLE `t_finance_hke_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8

#基金公告fund

CREATE TABLE `t_finance_fund_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8



#监管机制公告
CREATE TABLE `t_finance_regulator_report` (
  `hid` varchar(40) DEFAULT NULL COMMENT '报告ID',
  `sec_code` varchar(20) DEFAULT NULL COMMENT '代码',
  `sec_name` varchar(40) DEFAULT NULL COMMENT '简称',
  `notice_title` varchar(500) DEFAULT NULL COMMENT '公告标题',
  `file_type` varchar(20) DEFAULT NULL COMMENT '文件类型',
  `file_size` int(11) DEFAULT NULL COMMENT '文件大小',
  `pdf_url` varchar(200) DEFAULT NULL COMMENT '文件网址字段pdf地址',
  `notice_id` int DEFAULT NULL COMMENT '公告类型id',
  `notice_type` varchar(40) DEFAULT NULL COMMENT '公告类别',
  `notice_date` datetime DEFAULT NULL COMMENT '公告时间',
  `page_count` int(11) DEFAULT NULL COMMENT '文件页数',
  `local_file` varchar(400) DEFAULT NULL COMMENT '本地文件名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
