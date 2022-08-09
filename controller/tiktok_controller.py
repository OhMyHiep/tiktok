from select import select
from models.tiktok import TikTok
from service.tiktok_service import TiktokService

class TikTokController():

    def __init__(self,tiktok_service:TiktokService) -> None:
        self.tiktok_service=tiktok_service

    def add_tiktok(self,tiktok):
        return self.tiktok_service.add_tiktok(tiktok)

    def get_all(self):
        return self.tiktok_service.get_all(())

    def update(self,tk:TikTok):
        return self.tiktok_service.update(tk)