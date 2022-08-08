from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By



class TikTokHashtagPage():
    def __init__(self, driver:WebDriver,hashtag:str):
        self.driver=driver
        self.hashtag=hashtag

    def go_to_hastag_page(self):
        self.driver.get(f"https://www.tiktok.com/tag/{self.hashtag}")

    def get_video_links(self):
        # elements = self.driver.find_element(By.CLASS_NAME,'tiktok-yz6ijl-DivWrapper')
        # print(elements)
        elements=self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[2]/div/div[contains(@class,"tiktok-x6y88p-DivItemContainerV2")]')
        # print(len(elements))
        return elements

    def set_hash_tag(self,hashtag:str):
        self.hashtag=hashtag

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    