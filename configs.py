from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21114403"))
    API_HASH = getenv("API_HASH", "192c2b697e9f45650354fd47292ccf78")
    BOT_TOKEN = getenv("BOT_TOKEN", "5973598173:AAG-WBeBVZuHg9t_HGE9rHfcE84DfsC0Ues")
    FSUB = getenv("FSUB", "SDBotz")
    CHID = int(getenv("CHID", "-1001876567760"))
    SUDO = list(map(int, getenv("5516632396").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nejot19048:R3gJAQO3BzgEorUp@cluster0.twqlcdy.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
