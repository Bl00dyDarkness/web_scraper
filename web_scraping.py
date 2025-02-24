from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os

# Load secret .env file
load_dotenv("local.env")

#env variables
url = os.getenv('WEB_URL')
local_folder = os.getenv('LOCAL_FOLDER')
class_name = os.getenv('CLASS_NAME')

#File extension, used jpg for commodity, dont know the best one, probably incorrect ext
image_ext = ".jpg"

#html request
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#get all tags with expecific class
cards = doc.find_all("img", {"class":class_name})

for card in cards:
    #get attr value
    imgURL = card['src']
    file_name = card['alt']
    
    #get image
    img = requests.get(imgURL,allow_redirects=True)
    #save image
    img_name = local_folder + file_name + image_ext 

    #Check if file exist
    #if not os.path.isfile(img_name):

    open(img_name,'wb').write(img.content)
    print(img_name)