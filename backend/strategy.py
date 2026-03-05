import random

def generate_trade(image):

    entry = round(random.uniform(2030,2040),2)
    sl = entry - 5
    tp = entry + 10

    return {
        "pair":"XAUUSD",
        "entry":entry,
        "sl":sl,
        "tp":tp,
        "confidence":"demo"
    }
