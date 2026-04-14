import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def prepare_data(series, window_size):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(series.values.reshape(-1, 1))

    X, y = [], []
    for i in range(window_size, len(scaled)):
        X.append(scaled[i-window_size:i])
        y.append(scaled[i])

    return np.array(X), np.array(y), scaler

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm(series, epochs, window_size):
    X, y, scaler = prepare_data(series, window_size)
    model = build_model((X.shape[1], 1))

    history = model.fit(X, y, epochs=epochs, batch_size=16, verbose=0)

    return model, scaler, history

def forecast_lstm(model, scaler, series, steps, window_size):
    data = scaler.transform(series.values.reshape(-1, 1))
    input_seq = data[-window_size:]

    preds = []
    for _ in range(steps):
        pred = model.predict(input_seq.reshape(1, window_size, 1), verbose=0)
        preds.append(pred[0][0])
        input_seq = np.append(input_seq[1:], pred, axis=0)

    preds = scaler.inverse_transform(np.array(preds).reshape(-1,1))
    return preds.flatten()
