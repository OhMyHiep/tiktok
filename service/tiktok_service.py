from dao.tiktok_dao import TikTokDao
from models.tiktok import TikTok

class TiktokService():

    def __init__(self,tiktok_dao:TikTokDao) -> None:
        self.tiktok_dao=tiktok_dao

    def add_tiktok(self,tikTok:TikTok):
        return self.tiktok_dao.add_tiktok(tikTok)

    def get_all(self):
        return self.tiktok_dao.get_all()

    def update(self,tk:TikTok):
        queried_tiktok=self.tiktok_dao.get_tiktok_by_id(tk)
        if queried_tiktok:
            if tk.date_added:
                queried_tiktok.date_added=tk.date_added
            if tk.downloaded_title:
                queried_tiktok.downloaded_title=tk.downloaded_title
            return self.tiktok_dao.update(queried_tiktok)
        return None

