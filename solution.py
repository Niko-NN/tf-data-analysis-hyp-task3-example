import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(npv_control, npv_test, alpha=0.05) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    t_stat, p_val = stats.ttest_ind(npv_control, npv_test)
    return p_val < alpha
