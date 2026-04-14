import warnings
warnings.filterwarnings("ignore")
from statsmodels.tsa.arima.model import ARIMA

def train_model(data):
    model = ARIMA(data, order=(5,1,0))
    model_fit = model.fit()
    return model_fit

def forecast(model, steps=8):
    return model.forecast(steps=steps)
