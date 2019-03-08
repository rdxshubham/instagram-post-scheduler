from config import Config
import os
from random import randrange
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
from time import sleep


def UploadPhoto():

    from InstagramAPI import InstagramAPI

    InstagramAPI = InstagramAPI(Config.USERNAME, Config.PASSWORD)
    InstagramAPI.login()

    list_of_images = os.listdir(Config.IMAGE_FOLDER_PATH)
    random_image_to_upload = Config.IMAGE_FOLDER_PATH + list_of_images[randrange(0, len(list_of_images))]
    random_caption = Config.CAPTION_LIST[randrange(0, len(Config.CAPTION_LIST))]

    InstagramAPI.uploadPhoto(random_image_to_upload, random_caption)
    status = InstagramAPI.LastJson.get('status')
    print(status)

    if status == 'ok':
        print('Uploaded Successfully')
        os.remove(random_image_to_upload)
    else:
        print('Some error happened -> ' + status)


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=UploadPhoto,
    trigger=IntervalTrigger(hours=Config.INTERVAL_TIME_IN_HOURS),
    id='upload_photo',
    name='upload photo',
    replace_existing=True)

atexit.register(lambda: scheduler.shutdown())

while True:
    sleep(1)
