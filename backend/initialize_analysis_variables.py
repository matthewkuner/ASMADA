# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


def initialize_analysis_variables(GUI_inputs):
    # Initialize list to capture transformation temps/strains for each 
    # cycle.
    # First, determine the units that should be associated with each
    # outputted property/parameter.
    if GUI_inputs.temp_unit.values[0] == '[°C]':
        temp_unit = ' ' + '[degC]'
    elif GUI_inputs.temp_unit.values[0] == '[K]':
        temp_unit = ' ' + '[K]'
    elif GUI_inputs.temp_unit.values[0] == '[°F]':
        temp_unit = ' ' + '[degF]'
        
    if GUI_inputs.strain_unit.values[0] == '[%]':
        strain_unit = ' ' + '[%]'
    elif GUI_inputs.strain_unit.values[0] == '[fraction]':
        strain_unit = ''

    CTE_unit = ' [1/' + temp_unit[2:-1] + ']'
    hyst_area_unit = ' [' + temp_unit[2:-1] + ']'

    # Create property/parameter name list.
    mat_param_column_names = ['cycle',
                              'M_s_temp'+temp_unit, 'M_s_strain'+strain_unit,
                              'M_f_temp'+temp_unit, 'M_f_strain'+strain_unit,
                              'A_s_temp'+temp_unit, 'A_s_strain'+strain_unit,
                              'A_f_temp'+temp_unit, 'A_f_strain'+strain_unit,
                              'LCT'+temp_unit, 'LCT_strain'+strain_unit,
                              'UCT'+temp_unit, 'UCT_strain'+strain_unit,
                              'actuation_strain'+strain_unit,
                              'transform_strain'+strain_unit,
                              'TRIP_strain'+strain_unit,
                              'hysteresis_area'+hyst_area_unit,
                              'hysteresis_width'+temp_unit, 'thermal_transform_span'+temp_unit,
                              'aust_coef_thermal_expan'+CTE_unit,
                              'mart_coef_thermal_expan'+CTE_unit,
                              'initial_cycle_strain'+strain_unit,
                              'min_strain'+strain_unit, 'max_strain'+strain_unit]


    # Create variable to store smoothed temp/strain data (for plot of
    # all cycles in the "make_plots" function later in the code)
    df_smoothed_data = pd.DataFrame(columns = ['cycle','temp','strain'])
    

    # Initialize variables to store optimal sigmoid parameters from
    # previous cycles. These values are then used to improve the
    # speed of sigmoid fitting for the next cycle; this is accomplished
    # by using the optimal parameters for these previous cycles as the
    # initial guess for the next cycle's sigmoid parameters.
    cooling_sigmoid_guess = np.zeros([5, 2], dtype=np.float64)
    cooling_sigmoid_guess[:, 0] = 0.1
    cooling_sigmoid_guess[:, 1] = 0
    heating_sigmoid_guess = np.zeros([5, 2], dtype=np.float64)
    heating_sigmoid_guess[:, 0] = 0.1
    heating_sigmoid_guess[:, 1] = 0


    # Initialize variable to capture which cycles, if any, were not
    # able to be analyzed
    cycles_that_failed = []
    
    
    return mat_param_column_names,  df_smoothed_data, cooling_sigmoid_guess, heating_sigmoid_guess, cycles_that_failed