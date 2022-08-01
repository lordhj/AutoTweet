#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#INPUTS
USERNAME = input("Enter your Twitter username without @: ") #YOUR USERNAME
PASSWD = input("Enter your password: ") #YOUR PASSWORD
TWEET = input("Enter your automated tweet: ") #YOUR TWEET

chrome_driver_path = "C:\Softwares\Develop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
wait = WebDriverWait(driver, 30)
driver.get("https://twitter.com/login")

#-------------------------LOGIN-------------------------------------

#USERNAME INPUT
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.ENTER)

#PASSWORD INPUT
password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys(PASSWD)
password_input.send_keys(Keys.ENTER)

#---------------------------COMPOSING TWEETS-------------------------------
compose_tweet_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))
compose_tweet_button.click()
compose_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "public-DraftStyleDefault-block")))
compose_box.send_keys(TWEET)
post_tweet_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')))
post_tweet_button.click()