# -*- coding: utf-8 -*-


def line_intersection(m1, b1, m2, b2):
    x_val = (b2 - b1)/(m1 - m2)
    y_val = m1*x_val + b1
    return x_val, y_val
