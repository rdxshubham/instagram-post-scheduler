import os


class Config:

    USERNAME = 'USERNAME'
    PASSWORD = 'PASSWORD'
    IMAGE_FOLDER_PATH = os.getcwd() + '/images/'
    CAPTION_LIST = ['Hello', 'Its fun loving']
    INTERVAL_TIME_IN_HOURS = 1