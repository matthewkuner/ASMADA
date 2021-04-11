# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.optimize as opt
from scipy.stats import linregress
from backend.modified_sigmoid import modified_sigmoid


def find_TRR_tangent_line(temps, strain, min_strain, max_strain, min_temp, max_temp, left_asymp, right_asymp, sigmoid_guess):
    """
    Fits modified sigmoid function to current cycle branch. The
    transformation response region line is determined as the
    tangent line at the point of the maximum slope of the fitted
    function.
    """
    
    # Initial guess for the optimal parameters to fit the modified
    # sigmoid to the data from the current cycle.
    init_point_index = np.argmin(np.abs(strain - (max_strain + min_strain)/2))
    x0 = temps[init_point_index]
    y0 = strain[init_point_index]
    p0 = [left_asymp,
          right_asymp,
          np.mean(sigmoid_guess[:, 0]),
          np.mean(sigmoid_guess[:, 1]),
          x0,
          y0]

    # Determine optimal parameters to fit the data to a modified 
    # sigmoid equation.
    popt, pcov = opt.curve_fit(modified_sigmoid,
                               temps,
                               strain,
                               p0,
                               bounds=((min_strain-5, min_strain-5, 0.001, -0.01, min_temp, min_strain),
                                       (max_strain+5, max_strain+5, 10, 0.01, max_temp, max_strain)))

    # Add current cycle's optimal fit parameters to the
    # sigmoid_guess np array.
    if ~math.isnan(popt[2]) and ~math.isnan(popt[3]):
        sigmoid_guess[:, 0] = np.concatenate((sigmoid_guess[1:,0], [popt[2]]))
        sigmoid_guess[:, 1] = np.concatenate((sigmoid_guess[1:,1], [popt[3]]))

    # Find index of the point with the maximum slope on the fitted
    # smigoid function.
    fit_x = np.linspace(min_temp, max_temp, 500)
    fit_y = modified_sigmoid(fit_x, *popt)
    curve_fit_slope = np.gradient(fit_y)/np.gradient(fit_x)
    sigmoid_fit_max_slope_ind = np.argmax(abs(curve_fit_slope))
    sigmoid_fit_max_slope_ind = sigmoid_fit_max_slope_ind.item(0)

    # Find transformation response region line as the tangent line
    # at steepest point of the fitted sigmoid.
    if sigmoid_fit_max_slope_ind != 0:
        TRR_slope, TRR_intercept, *_ = linregress(fit_x[sigmoid_fit_max_slope_ind-1:sigmoid_fit_max_slope_ind+1],
                                                  fit_y[sigmoid_fit_max_slope_ind-1:sigmoid_fit_max_slope_ind+1])
    else:
        # Account for if the sample undergoes partial cycling.
        # The only difference from the code above is the indexing
        # within fit_x and fit_y (in the below code).
        TRR_slope, TRR_intercept, *_ = linregress(fit_x[sigmoid_fit_max_slope_ind:sigmoid_fit_max_slope_ind+1],
                                                  fit_y[sigmoid_fit_max_slope_ind:sigmoid_fit_max_slope_ind+1])
        
    return [TRR_slope, TRR_intercept, sigmoid_guess, fit_x, fit_y]