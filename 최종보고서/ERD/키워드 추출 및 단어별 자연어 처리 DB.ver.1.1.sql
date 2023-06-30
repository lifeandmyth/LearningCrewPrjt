CREATE TABLE `news_t_table` (
	`seq`	int	NOT NULL	COMMENT 'AUTO INCREMENT',
	`title`	VARCHAR(30)	NOT NULL,
	`title_keywords`	VARCHAR(30)	NOT NULL,
	`text`	MEDIUMTEXT	NOT NULL,
	`addr`	VARCHAR(50)	NOT NULL,
	`thumbnail_addr`	VARCHAR(100)	NOT NULL,
	`date`	datetime	NOT NULL	COMMENT '중복 가능',
	`tag`	VARCHAR(40)	NULL	COMMENT '중복 가능',
	`author`	CHAR(4)	NOT NULL	COMMENT '중복 가능'
);

CREATE TABLE `author` (
	`seq`	int	NOT NULL,
	`author`	CHAR(4)	NOT NULL
);

CREATE TABLE `news_article` (
	`seq`	int	NOT NULL,
	`title_id`	int	NOT NULL,
	`seq2`	int	NOT NULL,
	`addr`	VARCHAR(50)	NOT NULL,
	`thumbnail_addr`	VARCHAR(100)	NOT NULL,
	`date`	DATETIME	NOT NULL,
	`text`	MEDIUMTEXT	NOT NULL,
	`tag`	VARCHAR(40)	NULL
);

CREATE TABLE `title_n_key` (
	`title_id`	int	NOT NULL,
	`title`	VARCHAR(30)	NOT NULL,
	`title_keys`	VARCHAR(30)	NOT NULL,
	`text`	MEDIUMTEXT	NOT NULL
);

ALTER TABLE `news_t_table` ADD CONSTRAINT `PK_NEWS_T_TABLE` PRIMARY KEY (
	`seq`,
	`title`
);

ALTER TABLE `author` ADD CONSTRAINT `PK_AUTHOR` PRIMARY KEY (
	`seq`
);

ALTER TABLE `news_article` ADD CONSTRAINT `PK_NEWS_ARTICLE` PRIMARY KEY (
	`seq`,
	`title_id`,
	`seq2`
);

ALTER TABLE `title_n_key` ADD CONSTRAINT `PK_TITLE_N_KEY` PRIMARY KEY (
	`title_id`
);

ALTER TABLE `news_article` ADD CONSTRAINT `FK_title_n_key_TO_news_article_1` FOREIGN KEY (
	`title_id`
)
REFERENCES `title_n_key` (
	`title_id`
);

ALTER TABLE `news_article` ADD CONSTRAINT `FK_author_TO_news_article_1` FOREIGN KEY (
	`seq2`
)
REFERENCES `author` (
	`seq`
);

