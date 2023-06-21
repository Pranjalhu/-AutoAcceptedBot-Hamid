from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21114403"))
    API_HASH = getenv("API_HASH", "192c2b697e9f45650354fd47292ccf78")
    BOT_TOKEN = getenv("BOT_TOKEN", "6066100941:AAFlvX_LdrC_RFlSMJmMd3ZbdWc_7vUBBzE")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001724395212"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hegodal811:yHrW15yCCS5RS2bN@cluster0.br5wbbx.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
