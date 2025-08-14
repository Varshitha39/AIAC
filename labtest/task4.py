def preprocess_text():
    import string

    # Define a simple list of English stop words
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'on', 'in', 'is', 'it', 'this', 'that', 'these', 'those', 'as', 'are', 'was', 'were', 'be', 'been', 'has', 'have', 'had', 'do', 'does', 'did', 'from', 'so', 'not', 'no', 'can', 'will', 'just', 'than', 'then', 'too', 'very', 'you', 'your', 'yours', 'he', 'she', 'they', 'we', 'i', 'me', 'my', 'mine', 'his', 'her', 'their', 'our', 'us', 'them', 'who', 'whom', 'which', 'what', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such'
    }

    text = input("Enter your text: ")

    # Remove punctuation
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))

    # Convert to lowercase
    text_lower = text_no_punct.lower()

    # Remove stop words
    words = text_lower.split()
    filtered_words = [word for word in words if word not in stop_words]

    # Join back to string
    processed_text = ' '.join(filtered_words)

    print("Processed text:", processed_text)

# Call the function
preprocess_text()
