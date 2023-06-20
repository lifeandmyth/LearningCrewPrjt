#==============================
# mySQL db에 업로드하기

import pymysql
from mydb_local_env import *
conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset)

with conn:
  cur = conn.cursor()
  # DB 만들기
  sql_db_drop = """
    DROP DATABASE IF EXISTS cwn_cwl_db;
  """
  sql_db = """
    CREATE DATABASE cwn_cwl_db DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
  """
  cur.execute(sql_db_drop)
  cur.execute(sql_db)
  conn.commit()
  # 해당 연결의 현존하는 db 목록 뽑기
  cur.execute("SHOW DATABASES")
  # for data in cur:
  #   print(data)

db = "cwn_cwl_db"
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
# 커서 만들기
cur = conn.cursor()

# table 만들기
# news_t_list.append([news_date, news_title, news_text_sm, url_in, news_writer, tags_string])
sql_cwn_data_t ="""
CREATE TABLE IF NOT EXISTS cwn_cwl_data(
idx INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
news_date VARCHAR(20) NOT NULL, 
news_title VARCHAR(80) NOT NULL, 
news_text_sm MEDIUMTEXT NOT NULL, 
url_in VARCHAR(100) NOT NULL,
news_writer CHAR(10) NOT NULL,
tags_string VARCHAR(150) 
)
"""
cur.execute(sql_cwn_data_t)


# csv파일을 넣기
import csv

f = open('/data_crawling_D/data_crawling_김경민/cwn.kr/2023-06-19-20.csv','r')
rdr = csv.reader(f)

# 2차원 리스트 만들기
total_news_list = []
for line in rdr:
    total_news_list.append(line)
    print(total_news_list)
f.close()


# total_news_list = []
# for a in news_t_list:
#     # a.append(now_t)
#     total_news_list.append(a)
# # print(total_news_list) 

cur.executemany("INSERT INTO cwn_cwl_data(news_date, news_title, news_text_sm, url_in, news_writer, tags_string) VALUES (%s,%s,%s,%s,%s,%s)", total_news_list)

# db 적용, 트랜젝션 종료
conn.commit()