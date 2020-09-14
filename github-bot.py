from githubUserinfo import username,password
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
#driver = webdriver.Chrome(ChromeDriverManager().install())
class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome(ChromeDriverManager().install())
        self.username=username
        self.password=password
        self.followers=[]

    def sigIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").send_keys(Keys.ENTER)#click
        time.sleep(1)
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        items=self.browser.find_elements_by_css_selector(".d-table.table-fixed.col-12.width-full.py-4.border-bottom.border-gray-light")
        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)

github=Github(username,password)
github.sigIn()
github.getFollowers()
print(github.followers)      
