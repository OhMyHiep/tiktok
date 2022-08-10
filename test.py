from dao.tiktok_dao import TikTokDao
from models.tiktok import TikTok
from service.tiktok_service import TiktokService
from controller.tiktok_controller import TikTokController
import datetime


sample_tiktok=TikTok("sample",datetime.datetime(2022, 8, 8, 13, 31, 50, 723203),"this is to see if it works")
tk=TikTok("sample",datetime.datetime(2022, 8, 8, 13, 31, 50, 723203),"SnapTik_7070128800683593006_Full_HD.mp4")
tk_dao=TikTokDao()
tk_controler=TikTokController(TiktokService(tk_dao))

# print(sample_tiktok.date_added)
# print(tk_dao.add_tiktok(sample_tiktok))
# print(tk_dao.tiktok_mapper(("sample",datetime.datetime(2022, 8, 8, 13, 31, 50, 723203),"title")))

# list=[TikTok("testing"," datetime.datetime(2022, 8, 8, 13, 31, 50, 723203)","title")]
# print(type(list[0]))

# print(tk_controler.update(sample_tiktok))
print(tk_controler.get_tiktoks_by_null_title()[1].tk_link)