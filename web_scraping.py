from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Load secret .env file
load_dotenv("local.env")

#env variables
url = os.getenv('WEB_URL')
local_folder = os.getenv('LOCAL_FOLDER')
class_name = os.getenv('CLASS_NAME')

#File extension, used jpg for commodity, dont know the best one, probably incorrect ext
image_ext = "jpg"

#html request
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#get all tags with expecific class
cards = doc.find_all("img", {"class":class_name})

for card in cards:
    #get attr value
    imgURL = card['src']
    #expecific possition at the url where its the name of the image
    card_number = imgURL[66:69]
    #get image
    img = requests.get(imgURL,allow_redirects=True)
    #save image
    open(local_folder + card_number + image_ext,'wb').write(img.content)