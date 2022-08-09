from selenium import webdriver
from POM.snaptik import SnapTikPage
from hashlib import sha256
from models.tiktok import TikTok
from service.tiktok_service import TiktokService
import datetime
import os



driver_path="/Users/hiephuynh/Documents/apps/TikTokScraper/driver/chromedriver"
driver=webdriver.Chrome(driver_path)
driver.implicitly_wait(2)

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


def change_file_name(link:str,folder_path:str):
    """rename file to its hashed link"""
    file_name_list = os.listdir(folder_path)
    try:
        for file in file_name_list:
            if file.__contains__("SnapTik"):
                new_name=sha256(link.encode()).hexdigest()[:20]
                os.rename(folder_path+file,folder_path+new_name+".mp4")
    except (Exception) as e:
        print(e)



def map_video_to_link(link:str,folder_path:str,name_list:dict):
    file_name_list = os.listdir(folder_path)
    try:
        for file in file_name_list:
            if file.__contains__("SnapTik") and file not in name_list.values():
                name_list[link]=file
                tiktok=TikTok(link,datetime.now(),file)
                # TiktokService.add_tiktok(tiktok) #this should be changed to update as the link should already exist in the database

    except (Exception) as e:
        print(e)


def persist_video_link():
    pass


if __name__=="__main__":
    f=open("tiktok.txt","r")
    name_list={}
    for link in f:
        download_tiktok(link)
        # change_file_name(link,"/Users/hiephuynh/downloads/")
        # map_video_to_link(link,"/Users/hiephuynh/downloads/",name_list)
        if link not in name_list:
            print (link+" does not have video")
    driver.quit()

