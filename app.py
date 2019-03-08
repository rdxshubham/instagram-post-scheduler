from InstagramAPI import InstagramAPI
from config import Config
import os
from random import randrange

InstagramAPI = InstagramAPI(Config.USERNAME, Config.PASSWORD)
InstagramAPI.login()

list_of_images = os.listdir(Config.IMAGE_FOLDER_PATH)
random_image_to_upload = Config.IMAGE_FOLDER_PATH + list_of_images[randrange(0, len(list_of_images))]
random_caption = Config.CAPTION_LIST[randrange(0, len(Config.CAPTION_LIST))]

InstagramAPI.uploadPhoto(random_image_to_upload, random_caption)