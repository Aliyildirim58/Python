from instagramUserinfo import phone_number,password,username
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 

class Instagram:
    def __init__(self,phone_number,password,username):
        self.browser=webdriver.Chrome(ChromeDriverManager().install())
        self.phone_number=phone_number
        self.password=password
        self.username=username
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/?hl=tr")
        time.sleep(2)
        first=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        time.sleep(1)
        second=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        time.sleep(1)
        first.send_keys(self.phone_number)
        time.sleep(1)
        second.send_keys(self.password)
        time.sleep(2)
        second.send_keys(Keys.ENTER)
        time.sleep(2)
    
    def getFollowers(self):
        followerslist=[]
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followercount=len(dialog.find_elements_by_css_selector("li"))
        max=int(self.browser.find_element_by_class_name("k9GMp").find_elements_by_css_selector("li")[1].find_element_by_css_selector(".g47SY").text)
        print("Toplam Takipçi:",max)
        print(f"first count:{followercount}")
        action=webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newcount=len(dialog.find_elements_by_css_selector("li"))
            time.sleep(2)
            if (newcount != max):
                print(f"second count:{newcount}")
                time.sleep(1)
            else:
                break
        followers=dialog.find_elements_by_css_selector("li")
        time.sleep(2)
        
        for i in followers:
            link=i.find_element_by_css_selector("a").get_attribute("href")
            followerslist.append(link)
        with open("followerlist.txt","w",encoding='UTF-8') as file:
            for item in followerslist:
                file.write(item+"\n")

    def followUser(self,username):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/"+username+"/")
        time.sleep(2)
        followButton=self.browser.find_element_by_tag_name("button")
        time.sleep(2)
        if(followButton.text == "Takip Et" or followButton.text=="Following"):
            followButton.click()
            print("Takip Edildi(Following)")
            time.sleep(2)
        else:
            print("Zaten Takip ediyorsun")
    def Unfollow(self,username):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/"+username+"/")
        time.sleep(2)
        followButton=self.browser.find_element_by_tag_name("button")
        if(followButton.text == "Takip Et" or followButton.text=="Following"):
            print("Zaten Takip Etmiyorsunuz")
        else:
            followButton=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span").click()
            time.sleep(2)
            unfollow=self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
            time.sleep(2)
            print("Takipten Çıkarıldı(Unfollowing)")

        

instgrm=Instagram(phone_number,password,username)
instgrm.signIn()
instgrm.getFollowers()
instgrm.followUser("kod_evreni")
instgrm.Unfollow("kod_evreni")       