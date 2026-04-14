import pandas as pd

def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # Sidebar selection ready later
    return df