import os
import time
import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#####################Function to extract images from selected housing offer
def extract_image(element, nimages):
    if not os.path.exists("images"):
        os.makedirs("images")

    image = element.find_element(By.CLASS_NAME, "re-CardMultimediaSlider-image")
    url_image = image.get_attribute("src")
    img_download = requests.get(url_image)
    rel_path = "images/image" + str(nimages) + ".jpg"
    nimages += 1
    abs_path = os.path.abspath(rel_path)
    print("Downloading image in : " + abs_path)
    f = open(abs_path, "wb")
    f.write(img_download.content)
    f.close()

    return nimages
    

##################### Function to scrape the webpage  
def scrap_url(driver, table, nimages):

  # A LIST FOR EACH CARD TYPE (PREMIUM, ADVANCE, BASIC MINIMAL)
    cards = []
    cards2 = []
    cards3 = []
    cards4 =[]
    old_card_size = len(cards)
    old_card2_size = len(cards2)
    old_card3_size = len(cards3)
    old_card4_size = len(cards4)

    print("Loading dynamic content")
    while True:

        for _ in range(10):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)

        cards = driver.find_elements(By.CSS_SELECTOR, 'article.re-CardPackPremium')
        cards2 = driver.find_elements(By.CSS_SELECTOR, 'article.re-CardPackAdvance')
        cards3 = driver.find_elements(By.CSS_SELECTOR, 'article.re-CardPackBasic')
        cards4 = driver.find_elements(By.CSS_SELECTOR, 'article.re-CardPackMinimal')

        # STOP SCROLLING DOWN IF NO MORE CARDS ARE LOADED
        if (old_card_size == len(cards) and old_card2_size == len(cards2) and old_card3_size == len(cards3) and old_card4_size == len(cards4)):
            print("END of dynamic loading.")
            break

        old_card_size = len(cards)
        old_card2_size = len(cards2)
        old_card3_size = len(cards3)
        old_card4_size = len(cards4)

    # EXTRACT INFORMATION FROM PREMIUM CARDS
    print("EXTRACTING DATA FROM PREMIUM CARDS")
    print(len(cards))
    for el in cards:
        print("-----------------------------------------------------")
        try:
            link = el.find_element(By.CLASS_NAME, "re-CardPackPremium-carousel").get_attribute("href")
        except:
            link = ""

        try:
            price = el.find_element(By.CSS_SELECTOR, "span.re-CardPrice").text
        except:
            price = ""

        try:
            location = el.find_element(By.CSS_SELECTOR, "span.re-CardTitle.re-CardTitle--big").text
        except:
            location = ""

        try:
            area = el.find_element(By.CSS_SELECTOR, "span.re-CardFeaturesWithIcons-feature-icon.re-CardFeaturesWithIcons-feature-icon--surface").text
        except:
            area = ""

        try:
            rooms = el.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon").text
        except:
            rooms = ""

        try:
            bathrooms = el.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--bathrooms").text
        except:
            bathrooms = ""

        try:
            floor = el.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--floor").text
        except:
            floor = ""

        try:
            contact_number = el.find_element(By.CLASS_NAME, "re-CardContact-appendix").text
            contact_number = contact_number.split("Contactar\n")[1]
        except:
            contact_number = ''

        index = [price, location, area, rooms, bathrooms, floor, contact_number, link]
        table.append(index)

        nimages = extract_image(el, nimages)

    # EXTRACT INFORMATION FROM ADVANCED CARDS
    print("EXTRACTING DATA FROM ADVANCED CARDS")
    print(len(cards2))
    for el2 in cards2:
        print("-----------------------------------------------------")
        try:
            link = el2.find_element(By.CLASS_NAME, "re-CardPackAdvance-slider").get_attribute("href")
        except:
            link = ""

        try:
            price = el2.find_element(By.CSS_SELECTOR, "span.re-CardPrice").text
        except:
            price = ""

        try:
            location = el2.find_element(By.CSS_SELECTOR, "span.re-CardTitle.re-CardTitle--big").text
        except:
            location = ""

        try:
            area = el2.find_element(By.CSS_SELECTOR, "span.re-CardFeaturesWithIcons-feature-icon.re-CardFeaturesWithIcons-feature-icon--surface").text
        except:
            area = ""

        try:
            rooms = el2.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon").text
        except:
            rooms = ""

        try:
            bathrooms = el2.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--bathrooms").text
        except:
            bathrooms = ""

        try:
            floor = el2.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--floor").text
        except:
            floor = ""

        try:
            contact_number = el2.find_element(By.CLASS_NAME, "re-CardContact-appendix").text
            contact_number = contact_number.split("Contactar\n")[1]
        except:
            contact_number = ''

        index = [price, location, area, rooms, bathrooms, floor, contact_number, link]
        table.append(index)

        nimages = extract_image(el2, nimages)

    # EXTRACT INFORMATION FROM BASIC CARDS
    print("EXTRACTING DATA FROM BASIC CARDS")
    print(len(cards3))
    for el3 in cards3:
        print("-----------------------------------------------------")
        try:
            link = el3.find_element(By.CLASS_NAME, "re-CardPackBasic-slider").get_attribute("href")
        except:
            link = ""

        try:
            price = el3.find_element(By.CSS_SELECTOR, "span.re-CardPrice").text
        except:
            price = ""

        try:
            location = el3.find_element(By.CSS_SELECTOR, "span.re-CardTitle").text
        except:
            location = ""

        try:
            area = el3.find_element(By.CSS_SELECTOR, "span.re-CardFeaturesWithIcons-feature-icon.re-CardFeaturesWithIcons-feature-icon--surface").text
        except:
            area = ""

        try:
            rooms = el3.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon").text
        except:
            rooms = ""

        try:
            bathrooms = el3.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--bathrooms").text
        except:
            bathrooms = ""

        try:
            floor = el3.find_element(By.CLASS_NAME, "re-CardFeaturesWithIcons-feature-icon--floor").text
        except:
            floor = ""

        try:
            contact_number = el3.find_element(By.CLASS_NAME, "re-CardContact-appendix").text
            contact_number = contact_number.split("Contactar\n")[1]
        except:
            contact_number = ''

        index = [price, location, area, rooms, bathrooms, floor, contact_number, link]
        table.append(index)

        nimages = extract_image(el3, nimages)

    # EXTRACT INFORMATION FROM MINIMAL CARDS
    print("EXTRACTING DATA FROM MINIMAL CARDS")
    print(len(cards4))
    for el4 in cards4:
        print("-----------------------------------------------------")
        try:
            link = el4.find_element(By.CLASS_NAME, "re-CardPackMinimal-slider").get_attribute("href")
        except:
            link = ""

        try:
            price = el4.find_element(By.CSS_SELECTOR, "span.re-CardPrice").text
        except:
            price = ""

        try:
            location = el4.find_element(By.CSS_SELECTOR, "span.re-CardTitle").text
        except:
            location = ""

        try:
            features = el4.find_elements(By.CLASS_NAME, "re-CardFeatures-feature")
        except:
            pass

        try:
            area = features[2].text
        except:
            area = ""

        try:
            rooms = features[0].text
        except:
            rooms = ""

        try:
            bathrooms = features[1].text
        except:
            bathrooms = ""

        try:
            floor = features[3].text
        except:
            floor = ""

        try:
            contact_number = el4.find_element(By.CLASS_NAME, "re-CardContact-appendix").text
            contact_number = contact_number.split("Contactar\n")[1]
        except:
            contact_number = ''

        index = [price, location, area, rooms, bathrooms, floor, contact_number, link]
        table.append(index)

        nimages = extract_image(el4, nimages)

    return nimages