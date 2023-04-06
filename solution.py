import pandas as pd
import numpy as np


chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    log_x = np.log(x - 567)

    a = log_x.mean()

    return a
