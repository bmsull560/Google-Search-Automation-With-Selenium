from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com") #to navigate to google.com
search_box = driver.find_element(By.NAME, 'q') # finding the search bar
search_query = "Python programming"  #input 
search_box.send_keys(search_query)   #typing input
search_box.send_keys(Keys.RETURN)       #pressing enter
time.sleep(2)                       #waiting
search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')  #finding title and link
results = []
for result in search_results[:10]:
    title = result.text
    link = result.find_element(By.XPATH, '..').get_attribute('href')
    results.append({'title': title, 'link': link})
with open('google_search_results.txt', 'w') as file:
    for i, result in enumerate(results, 1):
        file.write(f"{i}. Title: {result['title']}\n")
        file.write(f"   URL: {result['link']}\n")
        file.write("\n")
driver.quit()
print("Search results saved to google_search_results.txt")
