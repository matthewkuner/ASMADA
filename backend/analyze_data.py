# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import linregress
from scipy.signal import savgol_filter
from backend.line_intersection import line_intersection
from backend.round_to_odd import round_to_odd
from backend.find_TRR_tangent_line import find_TRR_tangent_line
from backend.find_SPR_tangent_lines import find_SPR_tangent_lines
from backend.initialize_animation import initialize_animation
from backend.initialize_analysis_variables import initialize_analysis_variables


# Set paramaeters for matplotlib plotting
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = '#cccccc'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['agg.path.chunksize'] = 10000




class analyze_data_class:

    def analyze_data(self, GUI_inputs, df_raw_data, tot_num_cyc, cycles_to_analyze):
        
        """
        Determines material properties for all cycles specified by the user.

        !!!!!
        Important terminology:
            SPR = single-phase region (flatter)
            TRR = transformation response region (steeper)
        !!!!!
        

        This method has the following sections:
            1)  Initialization of variables for:
                    i)   storing calculated material properties;
                    ii)  creating an animation showing fitted tangent
                         lines for a small number of cycles, chosen
                         periodically throughout the file;
                    iii) keeping track of cycles that failed to be
                         analyzed;
                    iv)  improving analysis speed by using parameters from
                         previous cycles as an initial guess for the next
                         cycle; and
                    v)   storing smoothed temp/strain data; this data is
                         used to plot all cycles together in the 
                         "make_plots" function later in the code.
            2)  iterates through all cycles specified by the user. Material
                properties are determined according to ASTM 3097-17. This
                has several parts:
                    i)   performs smoothing using a Savitzky-Golay filter.
                         This smoothing is applied to the heating and
                         cooling branches of a cycle *separately*, wherein
                         the window size used is proportional to the number
                         of data points in a cycle branch.
                    ii)  fitting a sigmoid function to the data; this
                         function is used to find the transformation
                         response region tangent line.
                    iii) fitting of tangent lines to the single-phase
                         regions. This is done by finding the intersection
                         of the horizontal line at the maximum/minimum
                         branch strain value & the transformation response
                         tangent line. The points that correspond to the
                         lower 50% of temperatures between the LCT/UCT and
                         the above-described intersection point are used to
                         fit the single-phase region tangent line.
                    iv)  creation of an animation showing these tangent
                         lines for a small number of cycles, chosen
                         periodically throughout the file.


        Note: UCT, LCT, and their associated strains are calculated at the 
        UCT/LCT of an individual cycle. This is because many of these tests 
        have the UCT/LCT change over the course of the test.


        Parameters
        ----------
        GUI_inputs : pandas DataFrame
            Contains all user inputs.
        df_raw_data : pandas DataFrame
            contains raw temperature and strain data, alongside identified
            cycles numbers.
        tot_num_cyc : int
            Total number of cycles in the file. Used to accurately update 
            status bar on GUI with 'analyzing cycle x / tot_num_cyc' 
            message. This is necessary as the length of 'cycles_to_analyze'
            may be less than the total number of cycles in the file, were 
            the user to input a custom cycle range.
        cycles_to_analyze : list
            List of cycles to analyze, per the user's inputs.

        Returns
        -------
        df_material_parameters : pandas DataFrame
            Array containing all material parameters calculated.
        df_smooth_data : pandas DataFrame
            Array containing temperature and strain data after being
            smoothed using a Savitzky-Golay filter (alongside identified
            cycle numbers)
        im_animation : ???
            Animation showing the tangent lines fitted for a small
            number of cycles.
        """

        # Write progress update to GUI.
        self.notifyProgress.emit('analyzing cycle ' + str(0) + ' / ' + str(tot_num_cyc))

        # Initialize variables to create animation of tangent line fitting.
        fig_anim, ax_anim, animation_frame_stack, frame_capture_freq = initialize_animation(cycles_to_analyze, 
                                                                                            GUI_inputs)

        mat_param_column_names,  df_smoothed_data, cooling_sigmoid_guess, heating_sigmoid_guess, cycles_that_failed = initialize_analysis_variables(GUI_inputs)
        
        mat_param_dict_list = [] #used in place of repeatedly calling df.append for efficiency.

        for i in cycles_to_analyze:
            try:
                # Write progress update to GUI.
                self.notifyProgress.emit('analyzing cycle ' + str(i) + ' / ' + str(tot_num_cyc))

                # Extract data for current cycle (cycle "i")
                df = df_raw_data.loc[df_raw_data['cycle']==i]
                temps = df['temp'].to_numpy()
                strain = df['strain'].to_numpy()
                

                # Separate cooling and heating branches of the cycle.
                # Cycles always start with COOLing, and have HEATing
                # at the latter half of the cycle (this is assured based
                # on the procedure used to identify cycles in the
                # "pre_processing" function).
                cool_heat_cutoff = np.argmin(temps)
                cooling_temps = temps[0:cool_heat_cutoff]
                cooling_strain = strain[0:cool_heat_cutoff]
                heating_temps = temps[cool_heat_cutoff:]
                heating_strain = strain[cool_heat_cutoff:]


                # Find the LCT and UCT(according to ASTM E3097-17).
                LCT = min(heating_temps)
                UCT = max(heating_temps)

                # Find the strains at the LCT and UCT (according to 
                # ASTM E3097-17).
                LCT_strain = heating_strain[0]
                UCT_strain = heating_strain[-1]

                # Find the initial cycle strain (according to ASTM 
                # E3097-17).
                initial_cycle_strain = strain[0]


                # Smooth the cooling and heating branches separately, as
                # they typically have a different number of points. This
                # ensures that one branch is not oversmoothed while the
                # other is undersmoothed.
                
                # Smooth cooling branch using Savitzky-Golay filter.                 
                cool_data_length = len(cooling_temps)
                cooling_smooth_wsz = round_to_odd(math.sqrt(cool_data_length))
                if cooling_smooth_wsz >= 3:
                    cooling_temps = savgol_filter(cooling_temps, cooling_smooth_wsz, 3, mode='nearest')
                    cooling_strain = savgol_filter(cooling_strain, cooling_smooth_wsz, 3, mode='nearest')
                

                # Smooth heating branch using Savitzky-Golay filter.
                heat_data_length = len(heating_temps)
                heating_smooth_wsz = round_to_odd(math.sqrt(heat_data_length))
                if heating_smooth_wsz >= 3:
                    heating_temps = savgol_filter(heating_temps, heating_smooth_wsz, 3, mode='nearest')
                    heating_strain = savgol_filter(heating_strain, heating_smooth_wsz, 3, mode='nearest')




                # Concatenate smoothed data from current cycle to the
                # df_smoothed_data
                df_cur_cyc_smoothed_data = pd.DataFrame({'temp': np.concatenate((cooling_temps, heating_temps), axis = None), 
                                                         'strain': np.concatenate((cooling_strain, heating_strain), axis = None)})
                df_cur_cyc_smoothed_data.insert(0,'cycle', i)
                df_smoothed_data = pd.concat([df_smoothed_data, df_cur_cyc_smoothed_data], ignore_index=True)
                del df_cur_cyc_smoothed_data


                # Invert ordering of cooling data so that it goes from
                # lowest to highest temperature (thus being similar to
                # the heating branch data in that respect).
                cooling_temps = cooling_temps[::-1]
                cooling_strain = cooling_strain[::-1]




                # Determine if this cycle is inverted (e.g. the test was 
                # performed under compression rather than tension. This is
                # not performed for all cycles simultaneously, in case the
                # experimentalist decides to alternate between positive and
                # negative strain for some strange reason.
                if np.mean(strain) > 0:
                    is_inverted = False
                else:
                    is_inverted = True




    ##########  Processing for COOLING portion of cycle  ##########
                max_cool_strain = max(cooling_strain)
                min_cool_strain = min(cooling_strain)
                max_cool_temp = max(cooling_temps)
                min_cool_temp = min(cooling_temps)


                # The left and right "asymptotes" are parameters used
                # as initial guesses for the sigmoid fitting parameters.
                # These are determined as the 5th and 95th percentiles to 
                # prevent outliers from disrupting the analysis.
                left_asymp = np.percentile(cooling_strain, 95)
                right_asymp = np.percentile(cooling_strain, 5)
                if is_inverted:
                    temp = left_asymp
                    left_asymp = right_asymp
                    right_asymp = temp

                # Determine the transformation response region line for
                # the cooling branch. Several parameters are included
                # to use as initial sigmoid parameter guesses.
                cool_TRR_tangent_vars = find_TRR_tangent_line(cooling_temps, 
                                                              cooling_strain, 
                                                              min_cool_strain, 
                                                              max_cool_strain, 
                                                              LCT, 
                                                              UCT, 
                                                              left_asymp, 
                                                              right_asymp, 
                                                              cooling_sigmoid_guess)
                
                cool_TRR_slope = cool_TRR_tangent_vars[0]
                cool_TRR_intercept = cool_TRR_tangent_vars[1]
                cooling_sigmoid_guess = cool_TRR_tangent_vars[2]
                cool_fit_x = cool_TRR_tangent_vars[3]
                cool_fit_y = cool_TRR_tangent_vars[4]


                # The left/right extrema strain values serve as important
                # parameters in determining the single-phase region lines; 
                # hence they are determined here.
                left_extrema = max(cooling_strain)
                right_extrema = min(cooling_strain)
                if is_inverted:
                    temp = left_extrema
                    left_extrema = right_extrema
                    right_extrema = temp

                # Determine single-phase region lines for cooling branch.
                cool_SPR_tangent_vars = find_SPR_tangent_lines(cooling_temps, 
                                                               cooling_strain, 
                                                               left_extrema, 
                                                               right_extrema, 
                                                               cool_TRR_slope, 
                                                               cool_TRR_intercept, 
                                                               min_cool_temp, 
                                                               max_cool_temp)

                cool_left_SPR_slope = cool_SPR_tangent_vars[0]
                cool_left_SPR_intercept = cool_SPR_tangent_vars[1]
                cool_right_SPR_slope = cool_SPR_tangent_vars[2]
                cool_right_SPR_intercept = cool_SPR_tangent_vars[3]




    ##########  Processing for HEATING portion of cycle  ##########
                max_heat_strain = max(heating_strain)
                min_heat_strain = min(heating_strain)
                max_heat_temp = max(heating_temps)
                min_heat_temp = min(heating_temps)
                
                
                # The left and right "asymptotes" are parameters used
                # as initial guesses for the sigmoid fitting parameters.
                # These are determined as the 5th and 95th percentiles to 
                # prevent outliers from disrupting the analysis.
                left_asymp = np.percentile(heating_strain, 95)
                right_asymp = np.percentile(heating_strain, 5)
                if is_inverted:
                    temp = left_asymp
                    left_asymp = right_asymp
                    right_asymp = temp

                # Determine the transformation response region line for
                # the heating branch. Several parameters are included
                # to use as initial sigmoid parameter guesses.
                heat_TRR_tangent_vars = find_TRR_tangent_line(heating_temps, 
                                                              heating_strain, 
                                                              min_heat_strain, 
                                                              max_heat_strain, 
                                                              LCT, 
                                                              UCT, 
                                                              left_asymp, 
                                                              right_asymp, 
                                                              heating_sigmoid_guess)
                
                heat_TRR_slope = heat_TRR_tangent_vars[0]
                heat_TRR_intercept = heat_TRR_tangent_vars[1]
                heating_sigmoid_guess = heat_TRR_tangent_vars[2]
                heat_fit_x = heat_TRR_tangent_vars[3]
                heat_fit_y = heat_TRR_tangent_vars[4]


                # The left/right extrema strain values serve as important
                # parameters in determining the single-phase region lines; 
                # hence they are determined here.
                left_extrema = max(heating_strain)
                right_extrema = min(heating_strain)
                if is_inverted:
                    temp = left_extrema
                    left_extrema = right_extrema
                    right_extrema = temp

                # Determine single-phase region lines for heating branch.
                heat_SPR_tangent_vars = find_SPR_tangent_lines(heating_temps, 
                                                               heating_strain, 
                                                               left_extrema, 
                                                               right_extrema, 
                                                               heat_TRR_slope, 
                                                               heat_TRR_intercept, 
                                                               min_heat_temp, 
                                                               max_heat_temp)
                
                heat_left_SPR_slope = heat_SPR_tangent_vars[0]
                heat_left_SPR_intercept = heat_SPR_tangent_vars[1]
                heat_right_SPR_slope = heat_SPR_tangent_vars[2]
                heat_right_SPR_intercept = heat_SPR_tangent_vars[3]




                ##### Processing for remaining properties #####
                    # (many of which are determined using
                    # values obtained during the above analysis
                    # of cooling/heating cycle branches)


                # Calculate transformation temperatures & strains as the 
                # intersection between the appropriate tangent lines.
                M_s_temp, M_s_strain = line_intersection(cool_TRR_slope, cool_TRR_intercept, cool_right_SPR_slope, cool_right_SPR_intercept)
                M_f_temp, M_f_strain = line_intersection(cool_TRR_slope, cool_TRR_intercept, cool_left_SPR_slope, cool_left_SPR_intercept)
#                M_f_temp, M_f_strain = line_intersection(cool_TRR_slope, cool_TRR_intercept, heat_left_SPR_slope, heat_left_SPR_intercept)   # such a line would be used for constitutive modeling (not performed here)
                A_s_temp, A_s_strain = line_intersection(heat_TRR_slope, heat_TRR_intercept, heat_left_SPR_slope, heat_left_SPR_intercept)
                A_f_temp, A_f_strain = line_intersection(heat_TRR_slope, heat_TRR_intercept, heat_right_SPR_slope, heat_right_SPR_intercept)
#                A_f_temp, A_f_strain = line_intersection(heat_TRR_slope, heat_TRR_intercept, cool_right_SPR_slope, cool_right_SPR_intercept)   # such a line would be used for constitutive modeling (not performed here)


                # Calculate min and max cycle strain (NOT specified by an
                # ASTM standard).
                min_strain = min([min_heat_strain, min_cool_strain])
                max_strain = max([max_heat_strain, max_cool_strain])


                # Calculate coefficients of thermal expansion (CTE) for 
                # the austenite and martensite phases.
                aust_coef_thermal_expan = cool_right_SPR_slope
                mart_coef_thermal_expan = heat_left_SPR_slope
                # Divide by 100 if strain data is in [%] (as CTE is 
                # universally reported with no associated strain unit).
                if GUI_inputs.strain_unit.values[0] == '[%]':
                    aust_coef_thermal_expan /= 100
                    mart_coef_thermal_expan /= 100


                # Filter out outliers from the data--
                    # Outliers for temperature are values outside the range of temperatures found within the cycle (i.e. not between LCT and UCT)
                    # Outliers for strain are values more than 2% strain outside the range of strains found within the cycle
                    # Outliers for coefficient of thermal expansion are values above 5x10^-4 (no metal is expected to have a coef. above 5x10^-4 degC^-1; if units are in degF, then this is a lenient cutoff)
                    # Also checks transformation start/finish strain values relative to each other--
                        # e.g. M_s and A_f strains should never be greater than M_f and A_s strains (and vice versa)
                valid_max_strain = max_strain + 2   # don't use LCT_strain, as that is not always the maximum (absolute) strain
                valid_min_strain = min_strain - 2   # don't use UCT_strain, as that is not always the minimum (absolute) strain
                valid_CTE = 5*10**-4
                # Adjust valid CTE ranges depending on user-inputted
                # temperature unit. If '[°F]' is selected, the valid CTE
                # is multiplied by 1.8, as 1 Celsius unit is equal to
                # 1.8 Fahrenheit units (note this is distinct from a direct 
                # direct converion from °C to °F).
                if GUI_inputs.temp_unit.values[0] == '[°F]':
                    valid_CTE = 1.8 * valid_CTE

                if ~(LCT < M_s_temp < UCT) or ~(valid_min_strain < M_s_strain < valid_max_strain) or (abs(M_s_strain) > abs(M_f_strain) and abs(M_s_strain) > abs(A_s_strain)):
                    M_s_temp = M_s_strain = np.nan
                if ~(LCT < M_f_temp < UCT) or ~(valid_min_strain < M_f_strain < valid_max_strain) or (abs(M_f_strain) < abs(M_s_strain) and abs(M_f_strain) < abs(A_f_strain)):
                    M_f_temp = M_f_strain = np.nan
                if ~(LCT < A_s_temp < UCT) or ~(valid_min_strain < A_s_strain < valid_max_strain) or (abs(A_s_strain) < abs(M_s_strain) and abs(A_s_strain) < abs(A_f_strain)):
                    A_s_temp = A_s_strain = np.nan
                if ~(LCT < A_f_temp < UCT) or ~(valid_min_strain < A_f_strain < valid_max_strain) or (abs(A_f_strain) > abs(M_f_strain) and abs(A_f_strain) > abs(A_s_strain)):
                    A_f_temp = A_f_strain = np.nan
                if ~(abs(aust_coef_thermal_expan) < valid_CTE):
                    aust_coef_thermal_expan = np.nan
                if ~(abs(mart_coef_thermal_expan) < valid_CTE):
                    mart_coef_thermal_expan = np.nan

                # Determine if any of the transformation start/finish 
                # points were not able to be determined/were invalid 
                # outliers.
                if [np.isnan(A_s_temp), np.isnan(A_f_temp), np.isnan(M_s_temp), np.isnan(M_f_temp)].count(True) >= 1:
                    cycles_that_failed.append(i)


                # Calculate actuation, transformation, and TRIP strains
                # (according to ASTM E3097-17).
                actuation_strain = LCT_strain - UCT_strain
                transform_strain = A_s_strain - A_f_strain
                TRIP_strain = UCT_strain - strain[0]

                # Calculate hysteresis width and thermal transformation
                # span (according to ASTM E3097-17).
                hysteresis_width = abs((A_s_temp + A_f_temp)/2 - (M_s_temp + M_f_temp)/2)
                thermal_transform_span = A_f_temp - M_f_temp




                # Calculate hysteresis *area* (NOT specified by an
                # ASTM standard). This is calculated as the difference in
                # area underneath the heating and cooling branches.

                # Make separate set of temp/strain vectors. The "_area" 
                # string is added to the variable names simply to signify
                # that these values are used for calculated hysteresis area.
                heating_temps_area = heating_temps
                heating_strain_area = heating_strain
                cooling_temps_area = cooling_temps
                cooling_strain_area = cooling_strain
                
                # These vectors are then slightly modified to improve
                # accuracy of the area calculations.

                # First, ensure that the two branches go to the exact
                # same maximum temperature.
                # Each branch (coolign and heating) has a maximum 
                # temperature. One branch has a lower maximum temperature.
                # The other branch may have several points above this
                # temperature. These points are removed, and subsequently
                # replaced with an interpolated point--this ensures that
                # both branches go to *exactly* the same maximum
                # temperature.
                max_temp_cutoff_for_area = min(max_cool_temp, max_heat_temp)
                if max_cool_temp > max_heat_temp:
                    temp_cutoff_ind = np.where(cooling_temps > max_temp_cutoff_for_area)[0]
                    cooling_temps_area = cooling_temps_area[:temp_cutoff_ind[0]+1]
                    cooling_strain_area = cooling_strain_area[:temp_cutoff_ind[0]+1]
                    m, b, *_ = linregress(cooling_temps_area[-2:],
                                          cooling_strain_area[-2:])
                    cooling_temps_area[-1] = max_temp_cutoff_for_area
                    cooling_strain_area[-1] = b + m*max_temp_cutoff_for_area
                elif max_heat_temp > max_cool_temp:
                    temp_cutoff_ind = np.where(heating_temps > max_temp_cutoff_for_area)[0]
                    heating_temps_area = heating_temps_area[:temp_cutoff_ind[0]+1]
                    heating_strain_area = heating_strain_area[:temp_cutoff_ind[0]+1]
                    m, b, *_ = linregress(heating_temps_area[-2:],
                                          heating_strain_area[-2:])
                    heating_temps_area[-1] = max_temp_cutoff_for_area
                    heating_strain_area[-1] = b + m*max_temp_cutoff_for_area

                # Second, ensure that the two branches go to the exact
                # same minimum temperature.
                # Each branch (coolign and heating) has a minimum 
                # temperature. One branch has a higher minimum temperature.
                # The other branch may have several points below this
                # temperature. These points are removed, and subsequently
                # replaced with an interpolated point--this ensures that
                # both branches go to *exactly* the same minimum
                # temperature.
                min_temp_cutoff_for_area = max(min_cool_temp, min_heat_temp)
                if min_cool_temp < min_heat_temp:
                    temp_cutoff_ind = np.where(cooling_temps < min_temp_cutoff_for_area)[0]
                    cooling_temps_area = cooling_temps_area[temp_cutoff_ind[-1]:]
                    cooling_strain_area = cooling_strain_area[temp_cutoff_ind[-1]:]
                    m, b, *_ = linregress(cooling_temps_area[:2],
                                          cooling_strain_area[:2])
                    cooling_temps_area[0] = min_temp_cutoff_for_area
                    cooling_strain_area[0] = b + m*min_temp_cutoff_for_area
                elif min_heat_temp < min_cool_temp:
                    temp_cutoff_ind = np.where(heating_temps < min_temp_cutoff_for_area)[0]
                    heating_temps_area = heating_temps_area[temp_cutoff_ind[-1]:]
                    heating_strain_area = heating_strain_area[temp_cutoff_ind[-1]:]
                    m, b, *_ = linregress(heating_temps_area[:2],
                                          heating_strain_area[:2])
                    heating_temps_area[0] = min_temp_cutoff_for_area
                    heating_strain_area[0] = b + m*min_temp_cutoff_for_area                    

                # Find area under each branch using the composite trapezoid 
                # rule. 
                cooling_area = np.trapz(cooling_strain_area, cooling_temps_area)
                heating_area = np.trapz(heating_strain_area, heating_temps_area)  
                # The hysteresis area is defined as (the absolute value of)
                # the difference between the areas under the cooling and
                # heating branches.
                hysteresis_area = abs(heating_area - cooling_area)
                # Divide by 100 if strain data is in % (hysteresis area is
                # reported with no associated strain unit to facilitate 
                # conversion to Joules/g, which would be accomplished by
                # multiplying the hysteresis area by the specific heat 
                # capacity of the material).
                if GUI_inputs.strain_unit.values[0] == '[%]':
                    hysteresis_area /= 100
               



                cur_cycle_mat_params=[i,
                                      M_s_temp, M_s_strain,
                                      M_f_temp, M_f_strain,
                                      A_s_temp, A_s_strain,
                                      A_f_temp, A_f_strain,
                                      LCT, LCT_strain,
                                      UCT, UCT_strain,
                                      actuation_strain,
                                      transform_strain,
                                      TRIP_strain,
                                      hysteresis_area,
                                      hysteresis_width, thermal_transform_span,
                                      aust_coef_thermal_expan, mart_coef_thermal_expan,
                                      initial_cycle_strain,
                                      min_strain, max_strain]


                # Add transformation temps/strains from this cycle to the 
                # 'df_material_parameters' DataFrame.
                cur_cycle_mat_param_dict = dict(zip(mat_param_column_names,cur_cycle_mat_params))

                mat_param_dict_list.append(cur_cycle_mat_param_dict)




                # Add selected frames of tangent line fitting to 
                # animation. The first 10 frames are always added, 
                # alongside a frame every (frame_capture_freq) number
                # of cycles.
                if i in range(1,11) or i%frame_capture_freq == 0:

                    ##### Creates points for COOLING plots
                    # Points for plotting the transformation response
                    # region line of the cooling branch.
                    cool_TRR_y = np.linspace(M_s_strain, M_f_strain, 10)
                    cool_TRR_x = (cool_TRR_y - cool_TRR_intercept)/cool_TRR_slope
                    # Points for plotting the left single-phase region line 
                    # of the cooling branch.
                    cool_left_SPR_x = np.linspace(cooling_temps[0], M_f_temp, 10)
                    cool_left_SPR_y = cool_left_SPR_intercept + cool_left_SPR_slope*cool_left_SPR_x
                    # Points for plotting the right single-phase region 
                    # line of the cooling branch.
                    cool_right_SPR_x = np.linspace(M_s_temp, cooling_temps[-1], 10)
                    cool_right_SPR_y = cool_right_SPR_intercept + cool_right_SPR_slope*cool_right_SPR_x

                    ##### Creates points for HEATING plots
                    # Points for plotting the transformation response
                    # region line of the heating branch.
                    heat_TRR_y = np.linspace(A_f_strain, A_s_strain, 10)
                    heat_TRR_x = (heat_TRR_y - heat_TRR_intercept)/heat_TRR_slope
                    # Points for plotting the left single-phase region line  
                    # of the heating branch.
                    heat_left_SPR_x = np.linspace(heating_temps[0], A_s_temp, 10)
                    heat_left_SPR_y = heat_left_SPR_intercept + heat_left_SPR_slope*heat_left_SPR_x
                    # Points for plotting the right single-phase region 
                    # line of the heating branch.
                    heat_right_SPR_x = np.linspace(A_f_temp, heating_temps[-1], 10)
                    heat_right_SPR_y = heat_right_SPR_intercept + heat_right_SPR_slope*heat_right_SPR_x


                    # Plot current cycle
                    cur_plot1 = ax_anim.plot(cooling_temps, cooling_strain, '.', color='#56B4E9')
                    cur_plot2 = ax_anim.plot(heating_temps, heating_strain, '.', color='#DC3220')
                    # Plot hysteresis area (shaded lightly)
                    cur_plot3 = ax_anim.fill(np.concatenate((cooling_temps_area[::-1], heating_temps_area), axis = None),
                                                 np.concatenate((cooling_strain_area[::-1], heating_strain_area), axis = None),
                                                 color = '#009E73',
                                                 linewidth = 0,
                                                 alpha = 0.15)
#                    cur_plot4 = ax_anim.plot(cool_fit_x, cool_fit_y, 'k-')    # Formerly used to examine the accuracy of the fitted sigmoid functions
#                    cur_plot5 = ax_anim.plot(heat_fit_x, heat_fit_y, 'k-')    # Formerly used to examine the accuracy of the fitted sigmoid functions
                    # Plot transformation response region lines and
                    # single-phase region lines for cooling and heating
                    # cycle branches.
                    cur_plot6 = ax_anim.plot(cool_TRR_x, cool_TRR_y, 'k--')
                    cur_plot7 = ax_anim.plot(cool_right_SPR_x, cool_right_SPR_y,'k--')
                    cur_plot8 = ax_anim.plot(cool_left_SPR_x, cool_left_SPR_y,'k--')
                    cur_plot9 = ax_anim.plot(heat_TRR_x, heat_TRR_y, 'k--')
                    cur_plot10 = ax_anim.plot(heat_left_SPR_x, heat_left_SPR_y,'k--')
                    cur_plot11 = ax_anim.plot(heat_right_SPR_x, heat_right_SPR_y,'k--')
                    # Plot the four transformation start/finish points.
                    cur_plot12 = ax_anim.plot(M_s_temp, M_s_strain, 'ko', markersize=5)
                    cur_plot13 = ax_anim.plot(M_f_temp, M_f_strain, 'ko', markersize=5)
                    cur_plot14 = ax_anim.plot(A_s_temp, A_s_strain, 'ko', markersize=5)
                    cur_plot15 = ax_anim.plot(A_f_temp, A_f_strain, 'ko', markersize=5)

                    # Animate figure title text to correspond to current 
                    # cycle; do NOT do this by using ax.set_title, as it 
                    # does not correctly interface with the ArtistAnimation 
                    # function used to animate these plots.
                    title = ax_anim.text(0.5,
                                         1.01,
                                         'cycle ' + str(i),
                                         ha="center",
                                         va="bottom",
                                         color='k',
                                         transform=ax_anim.transAxes,
                                         fontsize="xx-large")

                    # Append plots for current cycle onto 
                    # animation_frame_stack.
                    animation_frame_stack.append([
                                                  cur_plot1[0],
                                                  cur_plot2[0],
                                                  cur_plot3[0],
#                                                      cur_plot4[0],
#                                                      cur_plot5[0],
                                                  cur_plot6[0],
                                                  cur_plot7[0],
                                                  cur_plot8[0],
                                                  cur_plot9[0],
                                                  cur_plot10[0],
                                                  cur_plot11[0],
                                                  cur_plot12[0],
                                                  cur_plot13[0],
                                                  cur_plot14[0],
                                                  cur_plot15[0],
                                                  title
                                                  ])
                
                ##### END OF ANALYSIS FOR CYCLE
                

            # Capture cycles that were not able to be analyzed/errored.
            except Exception as e:
                # Append current cycle number to list of cycles that 
                # failed.
                cycles_that_failed.append(i)

                cur_cycle = np.empty((1, len(mat_param_column_names)))
                cur_cycle[0, 1:] = np.nan
                cur_cycle[0, 0] = i

                # Add blank row to material_parameters_dict_list. This ensures
                # that there is some indication that a cycle completely 
                # failed (which would not be accomplished by simply
                # excluding failed cycles from exported files).
                cur_cycle_mat_params = [None] * 24


                # Add transformation temps/strains from this cycle to the 
                # 'df_material_parameters' DataFrame.
                cur_cycle_mat_param_dict = dict(zip(mat_param_column_names,cur_cycle_mat_params))

                mat_param_dict_list.append(cur_cycle_mat_param_dict)
                
                
                
                exception_type, exception_object, exception_traceback = sys.exc_info()
                error_on_line_number = exception_traceback.tb_lineno
                print(e)    # Helpful for those who wish to edit the code
                print(error_on_line_number)     # Helpful for those who wish to edit the code

        # Convert "ims" figure frame stack variable into an animation.
        im_animation = animation.ArtistAnimation(fig_anim,
                                                  animation_frame_stack,
                                                  interval=1000,
                                                  repeat_delay=0,
                                                  blit=True)
        
        # Helpful for those who wish to edit the code
        if str(cycles_that_failed) != '[]':
            print('One or more material parameters was not able to be calculated for the following cycles: ' + str(cycles_that_failed))
        
        df_material_parameters = pd.DataFrame.from_dict(mat_param_dict_list)


        return df_material_parameters, df_smoothed_data, im_animation