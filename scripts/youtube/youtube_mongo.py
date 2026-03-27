import pandas as pd
import json
from pymongo import MongoClient 

channels_df = pd.read_csv("channels.csv")
videos_df = pd.read_csv("top_5_videos.csv")
comments_df = pd.read_csv("comments_with_sentiment.csv")

merged = comments_df.merge(videos_df, on="video_id")
merged = merged.merge(channels_df, on="channel_id")

# Build JSON file
channels = {}

# Iterate over the merged df, each row being one comments
for index, row in merged.iterrows():

    # Extract the corresponding channel and video
    ch_id = row["channel_id"]
    vid_id = row["video_id"]

    # Create channel if not exist
    if ch_id not in channels:
        channels[ch_id] = {
            "channel_id": ch_id,
            "channel_name": row["channel_name_y"],
            "lean": row["lean_y"], 
            "description": row["description"],
            "subscriber_count": int(row["subscriber_count"]),
            "total_view_count": int(row["total_view_count"]),
            "total_video_count": int(row["total_video_count"]),
            "videos": []
        }

    channel = channels[ch_id]

    # Create video if not exist
    video = None

    for v in channel["videos"]:
        if v["video_id"] == vid_id:
            video = v
            break

    if video is None:
        video = {
            "video_id": vid_id,
            "title": row["title"],
            "year": int(row["year"]),
            "month": int(row["month"]),
            "lean": row["lean_x"],
            "published_at": row["published_at_y"],  
            "view_count": int(row["view_count"]),
            "like_count": int(row["like_count_y"]),
            "comment_count": int(row["comment_count"]),
            "comments": []
        }
        channel["videos"].append(video)

    # Create comment
    comment = {
        "comment_id": row["comment_id"],
        "text": row["text"],
        "like_count": int(row["like_count_x"]),
        "published_at": row["published_at_x"], 
        "sentiment_score": float(row["sentiment_score"]),
        "sentiment_label": row["sentiment_label"]
    }

    video["comments"].append(comment)

# Convert to list (for iteration purpose)
documents = list(channels.values())

# Write to JSON file
with open("youtube.json", "w") as f:
    json.dump(documents, f, indent=2)

print("JSON file created")

# NOTE: Ensure MongoDB is installed and running locally on port 27017
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["channels"]

# Clear old data
collection.delete_many({})

# Insert documents
if documents:
    collection.insert_many(documents)

print("Data inserted into MongoDB")