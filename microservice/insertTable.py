import psycopg2
from datetime import datetime
from config import config
import googleapiclient.discovery
import threading
from configparser import ConfigParser

ytConfig=[]

def insert_video_list(video_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO video_details(title, description, thumbnail_url, publishtime) VALUES (%s, %s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,video_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def fetchVideo(publishAfter):
    print("Function called on ", datetime.now())
    #fetching videos from YT
    global ytConfig
    youtube = googleapiclient.discovery.build(ytConfig[0][1], ytConfig[1][1], developerKey = ytConfig[2][1])
    request = youtube.search().list(
        part="snippet",
        fields="items(snippet(title,description,thumbnails(default(url)),publishTime))",
        type="video",
        publishedAfter=publishAfter,
        order="date",
        q="cricket",
        maxResults="30"
    )
    response = request.execute()

    # insert videos to db
    video_list=[]
    for video in response["items"]:
        videoParams=[video["snippet"]["title"], video["snippet"]["description"], video["snippet"]["thumbnails"]["default"]["url"], video["snippet"]["publishTime"]]
        video_list.append(videoParams)
    insert_video_list(video_list)
    publishAfter=response["items"][0]["snippet"]["publishTime"]
    threading.Timer(10,fetchVideo, [publishAfter]).start()


if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('variables.ini')
    if parser.has_section('youTube'):
        ytConfig = parser.items('youTube')
    publishAfter="2010-01-01T00:00:00Z"
    fetchVideo(publishAfter)