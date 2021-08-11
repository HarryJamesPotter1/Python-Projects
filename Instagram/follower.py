from var import password # privacy purposes
from selenium import webdriver
import time
import math

USERNAME = ''
PATH = 'D:/chromedriver'

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
# input password and username
username_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input") # button

username_input.send_keys(USERNAME)

password_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")

password_input.send_keys(password)

button = driver.find_element_by_css_selector("button[type=submit]")
button.click()

time.sleep(6)

profile_click = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
profile_click.click()
time.sleep(2)

profile_word_click = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div')
profile_word_click.click()
time.sleep(5)

open_followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
open_followers.click()
time.sleep(3)

follower_num = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title").replace(".","")

print(f"You have {follower_num} followers.") #edge cases: 999+ -> 1,000. Our assumption: <1000

scroll_time = math.floor(int(follower_num)/12)+1

for i in range(scroll_time):
    follower_names = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
    # [<span>ijosad</span>, <span>ajsdoads</span>, .......]
    follower_usernames = [x.text for x in follower_names]
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight;
    ''')
    time.sleep(2)

print(f"The collected number of followers is {len(follower_usernames)}")
xclose = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
xclose.click()
time.sleep(3)

following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
following.click()
time.sleep(3)

following_num = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text()

print(f"You are following {len(following_num)} number of people")

scroll_time = math.floor(int(following_num)/12)+1

for i in range(scroll_time):
    following_names = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
    # [<span>ijosad</span>, <span>ajsdoads</span>, .......]
    following_usernames = [x.text for x in following_names]
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight;
    ''')
    time.sleep(2)

print(f"The collected number of followers is {len(following_usernames)}")


# Followers and Following Usernames
# Who is in the following but not in the follower list

not_following_back = []

for i in range(len(following_num)):
    if following_usernames[i] not in follower_usernames:
        not_following_back.append(following_names[i])
print(not_following_back)

