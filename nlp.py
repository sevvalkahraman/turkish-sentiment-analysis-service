from textblob import TextBlob
        
def findSentiment(text) :
    result = ""
    blob1 = TextBlob(text)
    blob_eng = blob1.translate(to="en")
    result = blob_eng.sentiment.polarity
    return result