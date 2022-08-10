from selenium import webdriver
from POM.snaptik import SnapTikPage
from hashlib import sha256
from dao.tiktok_dao import TikTokDao
from models.tiktok import TikTok
from service.tiktok_service import TiktokService
from controller.tiktok_controller import TikTokController
import datetime
import os

tk_controller= TikTokController(TiktokService(TikTokDao()))

# driver_path="/Users/hiephuynh/Documents/apps/TikTokScraper/driver/chromedriver"
# driver=webdriver.Chrome(driver_path)
# driver.implicitly_wait(2)

def download_tiktok(link:str):
    try:
        snaptik=SnapTikPage(driver)
        snaptik.go_to_snaptik()
        snaptik.input_link(link)
        snaptik.click_download()
        snaptik.click_another_download_btn()
        snaptik.close_ads()
    except (Exception) as e:
        print (e)


def map_video_to_link(link:str,folder_path:str,name_list:dict):
    file_name_list = os.listdir(folder_path)
    try:
        for file in file_name_list:
            if file.__contains__("SnapTik") and file not in name_list.values():
                name_list[link]=file
                tiktok=TikTok(link,datetime.datetime.now(),file)
                tk_controller.update(tiktok) 
    except (Exception) as e:
        print(e)


if __name__=="__main__":
    tiktoks=tk_controller.get_tiktoks_by_null_title()
    name_list={}
    for tk in tiktoks:
        # download_tiktok(tk.yt_link)
        map_video_to_link(tk.tk_link,"/Users/hiephuynh/downloads/",name_list)
        if tk.tk_link not in name_list:
            print (tk.tk_link+" does not have video")
    # driver.quit()

