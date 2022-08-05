from tkinter import Button
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class SnapTikPage():

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def go_to_snaptik(self):
        self.driver.get("https://snaptik.app/en")

    def input_link(self,link:str):
        link_bar=self.driver.find_element(By.ID,"url")
        link_bar.send_keys(link)

    def click_download(self):
        # self.driver.find_element(By.ID,"submiturl").click()
        self.driver.execute_script("document.getElementById('submiturl').click();")
        WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.ID,"download-block")))

    def click_another_download_btn(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.ID,"progress-bar")))
        buttons=self.driver.find_element(By.CLASS_NAME,"abuttons").find_elements(By.TAG_NAME,"a")
        # print(buttons[1].tag_name,buttons[1].get_attribute("class"))
        buttons[1].click()
        # time.sleep(10)

    #add function to close ads

    def close_ads(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID,"ad-modal")))
            close_buttons=self.driver.find_element(By.XPATH,'//*[@id="dismiss-button"]')
            # self.driver.execute_script("document.getElementById('dismiss-button').click();")
            # alert = self.driver.switch_to_alert()
            # alert.dismiss
            for handle in close_buttons:
                handle.click()
        
        except (Exception) as e:
            print("did not find first layer ad")
            print(e)
            

