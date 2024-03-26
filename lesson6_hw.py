# Lesson Six Homework 


def check_reviews(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    keywords =positive_words + negative_words

    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print("Highlighted Review:", highlighted_review)
       
        positive_count = sum(review.lower().count(word) for word in positive_words)
        negative_count = sum(review.lower().count(word) for word in negative_words)
        print("Positive words:", positive_count, "Negative words:", negative_count)

        summary_length = 30
        if len(review) <= summary_length:
            summary = review
        else:
            summary = review[:summary_length]
            last_space_index = summary.rfind(' ') 
            if last_space_index != -1:
                summary = summary[:last_space_index] + "..."
        print("Summary:", summary)
        print()

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

check_reviews(reviews)
