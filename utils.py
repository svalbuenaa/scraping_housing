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