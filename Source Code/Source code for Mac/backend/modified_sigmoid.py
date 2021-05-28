# -*- coding: utf-8 -*-
import numpy as np


def modified_sigmoid(x, left_asymp, right_asymp, growth_rate, m, x0, y0):
    # Generalized form of the "modified_sigmoid" referenced in
    # other sections of the code.
    y = left_asymp + (right_asymp - left_asymp)/(1 + abs(y0)*np.exp(-growth_rate*(x-x0))) + m*x
    return y