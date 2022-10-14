import  os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'dsfhgaedshgqejoigtuwioht;4ewhg3uil4ngtgheq'
