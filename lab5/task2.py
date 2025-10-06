import re

# Simple sentiment analysis using a predefined lexicon
positive_words = {"good", "happy", "excellent", "great", "fantastic", "love", "wonderful", "amazing", "positive", "enjoy"}
negative_words = {"bad", "sad", "terrible", "awful", "hate", "horrible", "poor", "negative", "angry", "dislike"}

def preprocess_text(text):
    # Lowercase and remove non-alphabetic characters
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def detect_bias(text):
    # Example: Check for gender or racial bias keywords (very basic demo)
    bias_keywords = {"he", "she", "him", "her", "black", "white", "asian", "latino"}
    found = [word for word in bias_keywords if word in text.split()]
    if found:
        print("Warning: Potential bias detected in input data (keywords: {})".format(", ".join(found)))

def sentiment_analysis(text):
    text = preprocess_text(text)
    detect_bias(text)
    words = set(text.split())
    pos_count = len(words & positive_words)
    neg_count = len(words & negative_words)
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    user_input = input("Enter a sentence for sentiment analysis: ")
    sentiment = sentiment_analysis(user_input)
    print("Sentiment:", sentiment)
