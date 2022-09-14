import time
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

url = "https://prosettings.net/valorant-pro-settings-gear-list/"


driver = webdriver.Chrome(executable_path="4_Dependencies/chromedriver.exe")

driver.maximize_window()
driver.get(url)
driver.execute_script("window.scrollTo(0,10000)")
time.sleep(5)

page = driver.page_source
soup = BeautifulSoup(page,"html.parser")
season_stats = soup.find(id="table_1")

df = pd.read_html(str(season_stats))[0]
df.to_csv("2_Dataset/Pro_Settings.csv")