CREATE TABLE youtube_channels (
channel_id        VARCHAR2(50) PRIMARY KEY,
channel_name      VARCHAR2(100) NOT NULL,
lean              VARCHAR2(20)  NOT NULL,
description       VARCHAR2(500),
published_at      DATE,
subscriber_count  NUMBER,
total_view_count  NUMBER,
total_video_count NUMBER
)

CREATE TABLE youtube_videos (
video_id      VARCHAR2(50) PRIMARY KEY,
channel_id    VARCHAR2(50) NOT NULL,
title         VARCHAR2(200),
lean          VARCHAR2(20) NOT NULL,
published_at  DATE,
year          NUMBER(4),
month         NUMBER(2),
view_count    NUMBER,
like_count    NUMBER,
comment_count NUMBER,
CONSTRAINT fk_video_channel FOREIGN KEY (channel_id)
    REFERENCES youtube_channels(channel_id)
    )

CREATE TABLE youtube_comments (
comment_id   VARCHAR2(100) PRIMARY KEY,
video_id     VARCHAR2(50) NOT NULL,
text         VARCHAR2(500),
like_count   NUMBER,
published_at DATE,
CONSTRAINT fk_comment_video FOREIGN KEY (video_id)
    REFERENCES youtube_videos(video_id)
)