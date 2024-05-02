from transformers import pipeline

classifier = pipeline("text-classification", model="matthewburke/korean_sentiment")


# modelPath = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
# sentiment_task = pipeline("sentiment-analysis", model=modelPath, tokenizer=modelPath)

# 0 ->  "negative" 1 -> Neutral 2 -> Positive
def get_emotion(text: str) -> (str, int):
    pred = classifier(text, return_all_scores=True)
    if pred[0][1]['score'] > 0.5:
        return 'positive', int((pred[0][1]['score'] - 0.5) / 0.16)
    elif pred[0][0]['score'] > 0.5:
        return 'negative', int((pred[0][0]['score'] - 0.5) / 0.16)
    else:
        return 'neutral', 0
