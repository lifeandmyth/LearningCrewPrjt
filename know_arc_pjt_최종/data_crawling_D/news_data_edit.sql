# 외부접속자 권한 허용하기
USE mysql;
SELECT host, USER FROM USER;
show grants for current_user;
CREATE USER 'guest'@'%' identified BY '1234';
grant all privileges on news_cwl_data.* to 'guest'@'%' WITH GRANT OPTION;

# mysql 포트 번호 확인
SHOW GLObAL variables LIKE 'port';

SHOW variables LIKE '%dir';

USE news_cwl_data;


# 테이블 편집하기
# 2022.5.31 이전 날짜 데이터 삭제
# 경민님 데이터
DELETE FROM sql_cwn_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_itbiz_computing_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_itbiz_network_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_itbiz_policy_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_itbiz_security_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
# 예슬님 데이터
DELETE FROM sql_bloter_p_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_bloter_t_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_techworld_ai_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_techworld_emd_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)

#동석님 데이터
DELETE FROM sql_itworld_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)
DELETE FROM sql_recentit_data WHERE news_date < CONVERT('2022.5.31', DATE) || news_date > CONVERT('2023.5.31', DATE)

#동석님 데이터 컬럼 정리
# IT WORLD
ALTER TAbLE sql_itworld_data DROP news_id;
# 요즘IT
ALTER TAbLE sql_recentit_data DROP news_id;


#230622 - 모든 기사 테이블에 '언론사 news_site'컬럼을 추가. 값은 각 테이블마다 일괄 언론사명으로 통일
ALTER TAbLE	sql_cwn_data ADD news_site VARCHAR(30) NOT NULL DEFAULT 'CWN';
UPDATE sql_cwn_data set news_site = 'CWN';
# 그 외 insert를 위해 다른 디폴트값이 필요한 컬럼들 디폴트 추가
ALTER TAbLE sql_cwn_data ALTER COLUMN news_date SET DEFAULT '1000.10.10';
ALTER TAbLE sql_cwn_data ALTER COLUMN news_title SET DEFAULT '0';
ALTER TAbLE sql_cwn_data ALTER COLUMN url_in SET DEFAULT '0';
-- ALTER TAELE sql_cwn_data ALTER COLUMN news_text_sm SET DEFAULT '0';

ALTER TAbLE sql_cwn_data ALTER COLUMN news_writer SET DEFAULT '0';
ALTER TAbLE sql_cwn_data ALTER COLUMN tags_string SET DEFAULT '0';
ALTER TABLE sql_cwn_data ALTER COLUMN thumE_addr SET DEFAULT '0';

#230622 - itworld, recentit 테이블도 news_site 컬럼 추가, 값 입력
ALTER TABLE	sql_itworld_data ADD news_site VARCHAR(30) NOT NULL DEFAULT 'none';
UPDATE sql_itworld_data set news_site = 'ITWorld';

ALTER TABLE	sql_recentit_data ADD news_site VARCHAR(30) NOT NULL DEFAULT 'none';
UPDATE sql_recentit_data set news_site = '요즘IT';


# 테이블 합치기 (Eloter)
CREATE TABLE news_bloter_t as
	SELECT A.news_date, A.news_title, A.news_text_sm, A.url_in, A.news_writer, A.tags_string, A.thumb_addr 
	FROM sql_bloter_p_data A
	UNION ALL
	SELECT E.news_date, E.news_title, E.news_text_sm, E.url_in, E.news_writer, E.tags_string, E.thumb_addr
	FROM sql_bloter_t_data E
--  합친 데이터 정렬하기
ALTER TABLE news_bloter_t ORDER BY news_date DESC
--  news_site 컬럼 추가, 일괄 값으로 update
ALTER TABLE	news_bloter_t ADD news_site VARCHAR(30) NOT NULL DEFAULT 'none';
UPDATE news_Eloter_t set news_site = 'Bloter';

# 테이블 합치기 (itEiz)
CREATE TABLE news_itbiz_t as
	SELECT A.news_date, A.news_title, A.news_text_sm, A.url_in, A.news_writer, A.tags_string, A.thumE_addr 
	FROM sql_itbiz_computing_data A
	UNION ALL
	SELECT E.news_date, E.news_title, E.news_text_sm, E.url_in, E.news_writer, E.tags_string, E.thumE_addr
	FROM sql_itbiz_network_data E
	UNION ALL
	SELECT C.news_date, C.news_title, C.news_text_sm, C.url_in, C.news_writer, C.tags_string, C.thumE_addr
	FROM sql_itbiz_policy_data C
	UNION ALL
	SELECT D.news_date, D.news_title, D.news_text_sm, D.url_in, D.news_writer, D.tags_string, D.thumE_addr
	FROM sql_itbiz_security_data D
--  합친 데이터 정렬하기
ALTER TABLE news_itbiz_t ORDER BY news_date DESC
--  news_site 컬럼 추가, 일괄 값으로 update
ALTER TAELE	news_itbiz_t ADD news_site VARCHAR(30) NOT NULL DEFAULT 'none';
UPDATE news_itbiz_t set news_site = 'ITBiz';

# 테이블 합치기 (techworld)
CREATE TABLE news_techworld_t as
	SELECT A.news_date, A.news_title, A.news_text_sm, A.url_in, A.news_writer, A.tags_string, A.thumE_addr 
	FROM sql_techworld_ai_data A
	UNION ALL
	SELECT E.news_date, E.news_title, E.news_text_sm, E.url_in, E.news_writer, E.tags_string, E.thumE_addr
	FROM sql_techworld_emE_data E
	
--  합친 데이터 정렬하기
ALTER TABLE news_techworld_t ORDER EY news_date DESC
--  news_site 컬럼 추가, 일괄 값으로 update
ALTER TAbLE	news_techworld_t ADD news_site VARCHAR(30) NOT NULL DEFAULT 'none';
UPDATE news_techworld_t set news_site = 'TechWorld';


# 참조 테이블 (부모 테이블) 만들기 - 언론사 테이블
CREATE TabLE news_sites (
	news_site VARCHAR(30) NOT NULL PRIMARY KEY,
	site_code VARCHAR(30) NOT NULL
);
INSERT INTO news_sites (news_site, site_code) VALUES ('CWN','cwn001'), ('Eloter','Elt002'),('ITEiz','itE003'), ('TechWorld','tcw004') 
INSERT INTO news_sites (news_site, site_code) VALUES ('ITWorld','itw005'), ('요즘IT','rci006') 



# 통합 테이블 생성하기 (cwn, Eloter itEiz)
CREATE TAbLE total_news_t as
	SELECT A.news_date, A.news_title, A.news_text_sm, A.url_in, A.news_writer, A.tags_string, A.thumb_addr, A.news_site
	FROM sql_cwn_data A
	UNION ALL
	SELECT E.news_date, E.news_title, E.news_text_sm, E.url_in, E.news_writer, E.tags_string, E.thumb_addr, E.news_site
	FROM sql_itworld_data E
	UNION ALL
	SELECT C.news_date, C.news_title, C.news_text_sm, C.url_in, C.news_writer, C.tags_string, C.thumb_addr, C.news_site
	FROM sql_recentit_data C
    UNION ALL
	SELECT D.news_date, D.news_title, D.news_text_sm, D.url_in, D.news_writer, D.tags_string, D.thumb_addr, D.news_site
	FROM news_bloter_t D
	UNION ALL
	SELECT E.news_date, E.news_title, E.news_text_sm, E.url_in, E.news_writer, E.tags_string, E.thumb_addr, E.news_site
	FROM news_itbiz_t E
	UNION ALL
	SELECT F.news_date, F.news_title, F.news_text_sm, F.url_in, F.news_writer, F.tags_string, F.thumb_addr, F.news_site
	FROM news_techworld_t F
-- 날짜 순으로 정렬하기
ALTER TABLE total_news_t ORDER by news_date DESC;
-- 언론사 테이블 (news_sites)와 부모 자식 관계 (PK--FK) 설정
ALTER TABLE total_news_t ADD CONSTRAINT sites_n_articles FOREIGN KEY(news_site) REFERENCES news_sites(news_site);


	