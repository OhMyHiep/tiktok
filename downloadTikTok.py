from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.snaptik import SnapTikPage


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


if __name__=="__main__":
    f=open("tiktok.txt","r")
    for link in f:
        download_tiktok(link)
    driver.quit()