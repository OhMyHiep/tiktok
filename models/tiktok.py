from sqlite3 import Timestamp


class TikTok():
    def __init__(self,tk_link:str,date_added:Timestamp,downloaded_title:str):
        self.tk_link=tk_link
        self.date_added=date_added#use timestamp
        self.downloaded_title=downloaded_title
