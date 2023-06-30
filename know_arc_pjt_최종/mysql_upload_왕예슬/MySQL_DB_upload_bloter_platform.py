#==============================
# mySQL db에 업로드하기

import pymysql
from mydb_local_env import *
conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset)
cur = conn.cursor()

# with conn:
#   cur = conn.cursor()
  # DB 만들기
  # sql_db_drop = """
  #   DROP DATABASE IF EXISTS news_cwl_data;
  # """
  # sql_db = """
  #   CREATE DATABASE news_cwl_data DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
  # # """
  # cur.execute(sql_db_drop)
  # cur.execute(sql_db)
  # conn.commit()
  # 해당 연결의 현존하는 db 목록 뽑기
  # cur.execute("SHOW DATABASES")
  # for data in cur:
  #   print(data)

db = "news_cwl_data"
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
# 커서 만들기
cur = conn.cursor()

# table 만들기
# news_t_list.append([news_date, news_title, news_text_sm, url_in, news_writer, tags_string])

# cwn_cwl_data 테이블 만들기
sql_bloter_p_data_t ="""
CREATE TABLE IF NOT EXISTS sql_bloter_p_data(
idx INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
news_date VARCHAR(20) NOT NULL, 
news_title VARCHAR(80) NOT NULL, 
news_text_sm MEDIUMTEXT NOT NULL, 
url_in VARCHAR(100) NOT NULL,
news_writer CHAR(20) NOT NULL,
tags_string VARCHAR(150),
thumb_addr VARCHAR(100) NOT NULL
)
"""
# sql_bloter_p_data 테이블 만들기


# sql_bloter_p_data_t 실행하기
cur.execute(sql_bloter_p_data_t)


# csv파일을 넣기
import csv


# bloter csv platform 
f = open('know_arc_pjt/data_crawling_D/data_crawling_왕예슬/bloter_portal_platform.csv','r', encoding='utf8')
rdr = csv.reader(f)
next(rdr)

# 2차원 리스트 만들기
total_news_list = []
for line in rdr:
    total_news_list.append(line)
    # print(total_news_list)
f.close()


# itbz_cwl_data에 데이터 입력하기
cur.executemany("INSERT INTO sql_bloter_p_data(news_date, news_title, news_text_sm, url_in, news_writer, tags_string, thumb_addr) VALUES (%s,%s,%s,%s,%s,%s,%s)", total_news_list)

# db 적용, 트랜젝션 종료
conn.commit()