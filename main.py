from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.tiktok_hashtag_page import TikTokHashtagPage
import time

driver_path="/Users/hiephuynh/Documents/apps/TikTokScraper/driver/chromedriver"
driver=webdriver.Chrome(driver_path)
driver.implicitly_wait(1)

def driver_function():
    try:
        hash_tag_page=TikTokHashtagPage(driver,"viral")
        hash_tag_page.go_to_hastag_page()

        link_Elements=hash_tag_page.get_video_links()
        while len(link_Elements)<10:
            for i in range(10):
                hash_tag_page.scroll_down()
                time.sleep(.05)
            link_Elements=hash_tag_page.get_video_links()
        print (len(link_Elements))
        # link_Elements=set(link_Elements)
        
        # print(link_Elements[len(link_Elements)-1].find_element(By.TAG_NAME,"a").get_attribute('href'))
        write_to_file(link_Elements)
    except (Exception) as e:
        print(e)
    finally:
        driver.quit()

# should persist link to database here 
def write_to_file(link_Elements):
    link_Elements=set(link_Elements)
    f=open("tiktok.txt","a")
    for link in link_Elements:
        f.write(link.find_element(By.TAG_NAME,"a").get_attribute('href')+"\n")
    f.close()

    # print(link.find_element(By.TAG_NAME,"a").get_attribute('href'))






if __name__=='__main__':
    driver_function()