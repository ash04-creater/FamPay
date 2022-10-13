from datetime import datetime
from flask import jsonify,request
from app.yt_data.models import VideoDetails
from datetime import datetime
from app import db
import numpy as np

VIDEO_SUGGESTIONS = 5 #top 5 videos will be fected on search
video_per_page=5      # 5 videos per page will be displayed

def get(page_number):

    from app import Session

    session=Session()

    offset=(page_number-1)*video_per_page

    videos=[]

    pagination_object=session.query(VideoDetails).offset(offset).limit(video_per_page)
    videos=pagination_object

    video_dict={}

    video_dict['items']=[]

    for video in videos:

        v_dict={}
        v_dict['title']=video.title
        v_dict['description']=video.description
        v_dict['thumbnail_url']=video.thumbnail_url
        v_dict['publishtime']=video.publishtime

        video_dict['items'].append(v_dict)

    return jsonify(video_dict)

def search_video(key):

    from app import Session
    session=Session()

    videos=session.query(VideoDetails)

    list_key=set(key.split())
    lower_list_key= list(map(lambda x:x.lower(), list_key))

    score_array = []
    for video in videos:
        curr_score = 0

        list_title = video.title.split()
        lower_list_title= list(map(lambda x:x.lower(), list_title))

        for word in lower_list_title:
            if len(word)> 2 and word in lower_list_key:
                curr_score += 1

        list_desc = video.description.split()
        lower_list_desc= list(map(lambda x:x.lower(), list_desc))

        for word in lower_list_desc:
            if len(word)> 2 and word in lower_list_key:
                curr_score += 1
        score_array.append(curr_score)
    
    fin_videos = np.argsort(score_array)[-VIDEO_SUGGESTIONS:]
    final_videos=fin_videos.tolist()

    final_videos.reverse()
    video_dict={}

    video_dict['items']=[]

    for i in final_videos :
        if(score_array[i] < 1):
            break
        v_dict={}
        v_dict['title']=videos[i].title
        v_dict['description']=videos[i].description
        v_dict['thumbnail_url']=videos[i].thumbnail_url
        v_dict['publishtime']=videos[i].publishtime

        video_dict['items'].append(v_dict)
    
    return jsonify(video_dict)

    









    



