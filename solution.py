import pandas as pd
import numpy as np


chat_id = 416934694 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if anderson_ksamp([x, y]).significance_level < 0.07:
        return False
    else:
        return True
