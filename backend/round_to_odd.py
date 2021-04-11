# -*- coding: utf-8 -*-


def round_to_odd(val):
    # Round to nearest odd number, so that the outputted value can
    # be used as a window size
    f = int(round(val))
    return f + 1 if f % 2 == 0 else f


