CREATE TABLE `news_t_table` (
	`seq`	int	NOT NULL	COMMENT 'AUTO INCREMENT',
	`title`	VARCHAR(30)	NOT NULL,
	`title_keywords`	VARCHAR(30)	NOT NULL,
	`text`	MEDIUMTEXT	NOT NULL,
	`addr`	VARCHAR(150)	NOT NULL,
	`thumbnail_addr`	VARCHAR(150)	NOT NULL,
	`date`	datetime	NOT NULL	COMMENT '중복 가능',
	`tag`	VARCHAR(40)	NULL	COMMENT '중복 가능',
	`author`	CHAR(10)	NOT NULL	COMMENT '중복 가능',
	`news_site`	VARCHAR(20)	NOT NULL	COMMENT '중복 가능 (통합 테이블 한정)'
);

CREATE TABLE `news_articles` (
	`seq`	int	NOT NULL	COMMENT 'AUTO INCREMENT',
	`news_site2`	VARCHAR(30)	NOT NULL	COMMENT '외래키, 중복 가능',
	`title`	VARCHAR(30)	NOT NULL,
	`title_keywords`	VARCHAR(30)	NOT NULL,
	`news_text_sm`	MEDIUMTEXT	NOT NULL,
	`addr`	VARCHAR(150)	NOT NULL,
	`thumbnail_addr`	VARCHAR(150)	NOT NULL,
	`news_date`	DATETIME	NOT NULL,
	`tag`	VARCHAR(40)	NULL	COMMENT '중복 가능',
	`author`	CHAR(10)	NOT NULL	COMMENT '중복 가능'
);

CREATE TABLE `news_sites` (
	`news_site`	VARCHAR(30)	NOT NULL	COMMENT '기본키',
	`site_code`	VARCHAR(30)	NOT NULL	COMMENT '임의 지정'
);

ALTER TABLE `news_t_table` ADD CONSTRAINT `PK_NEWS_T_TABLE` PRIMARY KEY (
	`seq`,
	`title`
);

ALTER TABLE `news_articles` ADD CONSTRAINT `PK_NEWS_ARTICLES` PRIMARY KEY (
	`seq`,
	`news_site2`
);

ALTER TABLE `news_sites` ADD CONSTRAINT `PK_NEWS_SITES` PRIMARY KEY (
	`news_site`
);

ALTER TABLE `news_articles` ADD CONSTRAINT `FK_news_sites_TO_news_articles_1` FOREIGN KEY (
	`news_site2`
)
REFERENCES `news_sites` (
	`news_site`
);

