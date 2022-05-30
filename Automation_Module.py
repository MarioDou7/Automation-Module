from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys


class automation():
    def __init__(self):
        self.options =Options()
        self.options.add_argument("user-data-dir=C:\\Users\\Mario\\AppData\\Local\\Google\\Chrome\\User Data")
        self.driver = webdriver.Chrome(executable_path='D:\projects\python\chromedriver_win32\chromedriver.exe',options=self.options)
        


    def facebook(self):
        self.driver.get('https://www.facebook.com')

        element_email = self.driver.find_elements_by_xpath('//*[@id="email"]')
        element_email[0].send_keys('FACEBOOK USERNAME')

        element_password = self.driver.find_elements_by_xpath('//*[@id="pass"]')
        element_password[0].send_keys('FACEBOOK PASSWORD')
        element_password[0].send_keys(Keys.RETURN)

    def google(self,search):
        self.driver.get('https://www.google.com')

        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        element.send_keys(search)
        element.send_keys(Keys.RETURN)

    def youtube(self,search):
        self.driver.get('https://www.youtube.com')

        element = self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
        element.click()
        element.send_keys(search)
        element = self.driver.find_element_by_id('search-icon-legacy').click()

    def announcment(self):
        people = []
        people_number = int(input('how many people do you want to message: '))
        message = input("what do you want to say?\n")

        print("Enter " + str(people_number) + " names \n")
        for i in range(0,people_number):
            name = input("")
            people.append(name)

        self.driver.maximize_window()

        self.driver.get('https://web.whatsapp.com/')    
    

        xpath_search = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]'
        xpath_message = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'

        for name in people:
            search_bar = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath_search))
                )

            search_bar.click()
            search_bar.send_keys(name)
            search_bar.send_keys(Keys.RETURN)

            message_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath_message))
            )

            message_field.click()
            message_field.send_keys(message)
            message_field.send_keys(Keys.RETURN)

    def texting(self):
        want_to_text = input("who do you want to text: ")
        message = input("what do you want to say?\n")

        self.driver.maximize_window()

        self.driver.get('https://web.whatsapp.com/')    


        xpath_search = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]'
        xpath_message = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'

        search_bar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath_search))
        )

        search_bar.click()
        search_bar.send_keys(want_to_text)
        search_bar.send_keys(Keys.RETURN)

        try:
            message_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath_message))
            )

            message_field.click()
            message_field.send_keys(message)
            message_field.send_keys(Keys.RETURN)
        
        except :
            pass

    def status(self):

        self.driver.maximize_window()

        self.driver.get('https://web.whatsapp.com/')    

        xpath_status = '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[1]/div/span'

        status = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, xpath_status))
        )

        status.click()

    def whatsapp(self):
        want_To_do = input("what do you want to do?(texting, status, announcment)\n")
        
        if want_To_do == "texting":
            self.texting()
        elif want_To_do == "status":
            self.status()
        elif want_To_do == "announcment":
            self.announcment()

    def egybest(self,movie):

        wantWatch = movie               # TO search for the movie using his name
        xpath_search = '/html/body/div[3]/div/div[2]/form/input[2]'
        self.driver.get('https://amer.egybest.online/')

        search = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH, xpath_search))
        )
        search.click()

        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

        search.send_keys(movie)
        search.send_keys(Keys.RETURN)
    
        movie = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, wantWatch))
        )
        movie.click()

        download = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "تحميل"))
        )
        download.click()

        self.driver.switch_to_window(self.driver.window_handles[1])

        finalDownload = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/p[2]/a[1]"))
        )
        finalDownload.click()

        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[1])

        sleep(1)

        WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/p[2]/a[1]"))
        ).click()    

    def translate(self,text):

        xpath_textbox = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea'
        xpath_arabic = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]'

        self.driver.get('https://translate.google.com/')

        textbox = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH, xpath_textbox))
        )
        textbox.click()
        WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH, xpath_arabic))
        ).click()
        textbox.send_keys(text)


def main():

    automate = automation()

    while True:
        
        website = input("Enter the website you want: ")

        if website == "facebook":
            automate.facebook()

        elif website == "google":
            search = input("What are you searching for: ")
            automate.google(search)

        elif website == "youtube":
            search = input("What are you searching for: ")
            automate.youtube(search)
        
        elif website == "whatsapp":
            automate.whatsapp()
        
        elif website == "egybest":
            wantWatch = input("What do you want to watch?\n")
            automate.egybest(wantWatch)

        elif website == "translate":
            want_translate = input("Enter the word you want to translate:\n")
            automate.translate(want_translate)

        else:
            print("I only provide facebook, google, youtube, whatsapp, egybest and translate")



if __name__ == "__main__":
    main()