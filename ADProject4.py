import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Student/Desktop/YearUp/CIS 403 - Adv Topics in App Development/Week 18 - CIS 403/AD Project 4 - CIS 403/chromedriver.exe")
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='css-1rz2iog e1nywbhn4'):
    name = element.find('h5')
    if name not in results:
        print(results)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
