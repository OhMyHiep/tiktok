from sqlite3 import Timestamp


class YoutubeCompilation():
    def __init__(self,yt_link:str,date_added:Timestamp, title:str):
        self.yt_link=yt_link
        self.date_added=date_added
        self.title=title