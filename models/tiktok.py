from datetime import datetime
from sqlite3 import Timestamp


class TikTok():
    def __init__(self,tk_link:str,date_added,downloaded_title:str):
        self.tk_link=tk_link
        self.date_added=date_added
        self.downloaded_title=downloaded_title

            
