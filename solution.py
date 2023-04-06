import pandas as pd
import numpy as np


chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x -= 567
    log_x = np.log(x)
    log_mean = np.mean(log_x)
    a = np.exp(log_mean)
    return a
