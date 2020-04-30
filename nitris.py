from selenium import webdriver
from time import sleep
import requests
import os


class NitrisBot():
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(executable_path ="F:/Environments/project1_env/lib/site-packages/chromedriver/chromedriver.exe")
        #Opening the nitris site.
        self.driver.get("https://eapplication.nitrkl.ac.in/nitris/Login.aspx")  
        self.username = username
        self.password = pw
        #Passing the username and password to log in to the nitris website.
        self.driver.find_element_by_xpath("//*[@id='txtUserName']").send_keys(self.username) 
        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        #Closing any news pop ups that come in.
        self.driver.find_element_by_xpath('//*[@id="modalevent"]/div/div/div[3]/button').click()
        if (self.driver.find_element_by_xpath('//*[@id="wrapper"]/nav[1]/div[3]/div/a/i')):
            self.get_pdfs()
        
        else:
            
            self.driver.find_element_by_xpath('//*[@id="messageShow"]/div/div/div[2]/button').click()
            self.get_pdfs()
        


    def get_pdfs(self):
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/nav[1]/div[3]/div/a/i').click()
        string = self.driver.find_element_by_xpath('//*[@id="wrapper"]/nav[1]/div[3]/div/ul/li[1]/p')
        
        string_text = string.get_attribute("innerHTML")
        string_text = string_text.split(" ")
        if "You" in string_text: string_text.remove("You") 
        if "have" in string_text: string_text.remove("have") 
        if "new" in string_text: string_text.remove("new") 
        if "message(s)" in string_text: string_text.remove("message(s)") 

        # print(string_text)
        #no of potential files needed to be downloaded
        no_of_pd = int(string_text[0])

        if no_of_pd == 0: 
            print("No downloadable files present.")
            
            
            
        else:
            for i in range(1,no_of_pd+1):
                self.driver.find_element_by_xpath('//*[@id="wrapper"]/nav[1]/div[3]/div/ul/li[{}]/a'.format(2*i)).click()
        #self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder2_hypPreview"]').click()
                sleep(2)
                url = self.driver.find_element_by_xpath('//*[@id="ContentPlaceHolder2_hypPreview"]').get_attribute("href")
                myfile = requests.get(url)

                open('path_to_desired_folder/download{}.pdf'.format(i), 'wb').write(myfile.content)
                
                self.driver.get('https://eapplication.nitrkl.ac.in/nitris/Student/Home/Home.aspx')
                self.driver.find_element_by_xpath('//*[@id="modalevent"]/div/div/div[3]/button').click()
                self.driver.find_element_by_xpath('//*[@id="wrapper"]/nav[1]/div[3]/div/a/i').click()
        
        self.log_out()
        
        

    def log_out(self):
        self.driver.find_element_by_xpath('//*[@id="lnkLogout"]').click()
        os.startfile("path_to_desired_folder")
        
        
        exit(1)
        
        

my_bot = NitrisBot(#username,#password)
