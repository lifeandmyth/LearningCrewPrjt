CREATE TABLE `news_t_table` (
	`seq`	int	NOT NULL	COMMENT 'AUTO INCREMENT',
	`Key`	VARCHAR(30)	NOT NULL,
	`title_keywords`	VARCHAR(30)	NOT NULL,
	`text`	VARCHAR(100)	NOT NULL,
	`addr`	VARCHAR(50)	NOT NULL,
	`thumbnail_addr`	VARCHAR(100)	NOT NULL,
	`date`	datetime	NOT NULL	COMMENT '중복 가능',
	`tag`	VARCHAR(40)	NULL	COMMENT '중복 가능',
	`author`	CHAR(4)	NOT NULL	COMMENT '중복 가능'
);

CREATE TABLE `title_n_key` (
	`seq`	int	NOT NULL,
	`title`	VARCHAR(30)	NOT NULL,
	`title_keywords`	VARCHAR(30)	NOT NULL	COMMENT '전체 목록을 하나의 string으로',
	`text`	VARCHAR(100)	NOT NULL,
	`addr`	VARCHAR(50)	NOT NULL,
	`thumbnail_addr`	VARCHAR(100)	NOT NULL	COMMENT '썸네일 이미지 주소',
	`date`	datetime	NOT NULL	COMMENT '작성일자'
);

CREATE TABLE `title_n_tag` (
	`seq`	int	NOT NULL,
	`title`	VARCHAR(30)	NOT NULL,
	`tag`	VARCHAR(40)	NULL	COMMENT '중복 가능'
);

CREATE TABLE `title_n_author` (
	`seq`	int	NOT NULL,
	`title`	VARCHAR(30)	NOT NULL,
	`author`	CHAR(4)	NOT NULL	COMMENT '중복 가능',
	`date`	DATETIME	NOT NULL	COMMENT '중복 가능'
);

ALTER TABLE `news_t_table` ADD CONSTRAINT `PK_NEWS_T_TABLE` PRIMARY KEY (
	`seq`,
	`Key`
);

ALTER TABLE `title_n_key` ADD CONSTRAINT `PK_TITLE_N_KEY` PRIMARY KEY (
	`seq`,
	`title`
);

ALTER TABLE `title_n_tag` ADD CONSTRAINT `PK_TITLE_N_TAG` PRIMARY KEY (
	`seq`,
	`title`
);

ALTER TABLE `title_n_author` ADD CONSTRAINT `PK_TITLE_N_AUTHOR` PRIMARY KEY (
	`seq`,
	`title`
);

ALTER TABLE `title_n_tag` ADD CONSTRAINT `FK_title_n_key_TO_title_n_tag_1` FOREIGN KEY (
	`title`
)
REFERENCES `title_n_key` (
	`title`
);

ALTER TABLE `title_n_author` ADD CONSTRAINT `FK_title_n_key_TO_title_n_author_1` FOREIGN KEY (
	`title`
)
REFERENCES `title_n_key` (
	`title`
);

