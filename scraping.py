from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from utils import scrap_url

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

# Prepare webdriver with a valid user-agent
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)

table = []
nimages = 0

#################### CONNECTION TO FIRST LINK #######################################################################
driver = webdriver.Chrome(options=chrome_options)
# As a default, done with flat rental in Valencia
URL1 = "https://www.fotocasa.es/es/alquiler/viviendas/valencia-capital/todas-las-zonas/l"
print("User agent: " + driver.execute_script("return navigator.userAgent"))
driver.get(URL1)

### LOAD DYNAMIC CONTENT FROM JS TO ACCESS LINKS TO OTHER PAGES
js_url = 'https://frtassets.fotocasa.es/SearchPage.735b5311.js'
driver.execute_script(f"var script = document.createElement('script');script.src = '{js_url}';document.head.appendChild(script);")
driver.implicitly_wait(3)
print("Page 1")

# INITIAL SCRAPING
nimages = scrap_url(driver, table, nimages)

# Extract link to "next page"
a = driver.find_element(By.CSS_SELECTOR,
                         'a.sui-AtomButton.sui-AtomButton--neutral.sui-AtomButton--outline.sui-AtomButton--center.sui-AtomButton--small.sui-AtomButton--link.sui-AtomButton--rounded')
next_url = a.get_attribute('href')

############################ LOOP TO SCRAPE NEXT PAGES ##################################################
for i in range(30):
    print("Page " + str(i+2))
    # Accessing next page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(next_url)

    # Load new dynamic content with JS
    js_url = 'https://frtassets.fotocasa.es/SearchPage.735b5311.js'
    driver.execute_script(f"var script = document.createElement('script');script.src = '{js_url}';document.head.appendChild(script);")
    driver.implicitly_wait(1)

    # Launch scraping
    print("SCRAPING")
    nimages = scrap_url(driver, table, nimages)
    print("END SCRAPING")

    # Extract link to "next page"
    a = driver.find_elements(By.CSS_SELECTOR,
                             'a.sui-AtomButton.sui-AtomButton--primary.sui-AtomButton--outline.sui-AtomButton--center.sui-AtomButton--small.sui-AtomButton--link.sui-AtomButton--empty.sui-AtomButton--rounded')
    try:
        a_next_page = a[1]
        next_url = a_next_page.get_attribute('href')
    except:
        break
        
############## DATA EXPORT ############################################
# Export to Pandas DataFrame and CSV
df = pd.DataFrame(table, columns=['Price','Location','Area','Rooms','Bathrooms','Floor','Contact', 'Link'])
df.to_csv('data.csv', index=False)
print("Process ended...")
print(df.head(10))
