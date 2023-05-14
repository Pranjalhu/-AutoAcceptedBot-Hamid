from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "SDBotz")
    CHID = int(getenv("CHID", "-1001876567760"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nejot19048:R3gJAQO3BzgEorUp@cluster0.twqlcdy.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
