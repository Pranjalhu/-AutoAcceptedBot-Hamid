from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21114403"))
    API_HASH = getenv("API_HASH", "192c2b697e9f45650354fd47292ccf78")
    BOT_TOKEN = getenv("BOT_TOKEN", "6714198586:AAE8G9OuiEyGrRJ2M0OAWtAbqneq4hsyM3U")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1002065379205"))
    SUDO = list(map(int, getenv("SUDO").split(5339716956 5864846606)))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hegodal811:sVOBrVHBgS1pppay@cluster0.uhns1id.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
