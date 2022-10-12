from flask import Blueprint
from app.yt_data import controller

search_api=Blueprint('search',__name__)
get_api=Blueprint('get',__name__)

get_api.add_url_rule(rule='/get/<int:page_number>',view_func=controller.get,methods=["GET"])
search_api.add_url_rule(rule='/search/video/<key>',view_func=controller.search_video,methods=["GET"])

