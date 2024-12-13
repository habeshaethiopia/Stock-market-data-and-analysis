import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')  # Ensure VADER is ready

def analyze_sentiment_textblob(text):
    """Analyze sentiment using TextBlob."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_sentiment_vader(text):
    """Analyze sentiment using VADER."""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']

def process_dataframe(df, method='textblob'):
    """
    Analyze sentiment in a pandas DataFrame.

    Parameters:
    - df: Input DataFrame.
    - method: Sentiment analysis method ('textblob' or 'vader').

    Returns:
    - DataFrame with sentiment scores and labels added.
    """
    if method == 'textblob':
        df['sentiment_score'] = df['headline'].apply(analyze_sentiment_textblob)
    elif method == 'vader':
        df['sentiment_score'] = df['headline'].apply(analyze_sentiment_vader)
    else:
        raise ValueError("Invalid method. Choose 'textblob' or 'vader'.")

    # Classify sentiment
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda score: 'positive' if score > 0 else ('negative' if score < 0 else 'neutral')
    )
    return df
