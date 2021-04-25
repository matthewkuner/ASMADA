# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import linregress
from backend.line_intersection import line_intersection
from backend.find_nearest import find_nearest


def find_SPR_tangent_lines(temps, strain, left_extrema, right_extrema, TRR_slope, TRR_intercept, min_temp, max_temp):
    """
    Finds the left and right tangent lines for the single-phase regions of
    a cycle branch.
    """                
    
    def find_left_SPR_tangent(temps, strain, TRR_slope, TRR_intercept, left_extrema, min_temp):
        """
        Finds tangent line for the left single-phase region of the
        cycle branch.
        
        Uses the intersection of the transformation response region
        tangent line with the left asymptote strain value as the 
        total number of points that could possibly fall within the 
        left single-phase region. Uses the points corresponding to 
        the lowest 50% of temperatures between the LCT and the 
        above-described intersection points.
        """
        
        # Trim out the first and last 1% of points.
        temps = temps[round(.01*len(temps)):round(0.99*len(temps))]
        strain = strain[round(.01*len(strain)):round(0.99*len(strain))]
        
        maximum_left_single_phase_region_temp, *_ = line_intersection(TRR_slope, TRR_intercept, 0, left_extrema)
        left_SPR_max_ind = find_nearest(temps, maximum_left_single_phase_region_temp)
        # Finds index of halway point between the min_temp and the
        # maximum_left_single_phase_region_temp point.
        left_SPR_cutoff = find_nearest(temps, (maximum_left_single_phase_region_temp + min_temp)/2)
        
        # Ensure at least 3 points (or 5% of the points in the branch) are used
        # to determine the single-phase region tangent line. 
        if left_SPR_cutoff >= left_SPR_max_ind or any(val < 3 for val in [left_SPR_cutoff, left_SPR_max_ind]):
            left_SPR_cutoff = max(round(0.05*len(temps)), 3)
            left_SPR_max_ind = max(round(0.2*len(temps)), 4)
        
        # Apply linear fit to the selected points. The determined line is the
        # single-phase region line for this side of the cycle branch.
        left_SPR_slope, left_SPR_intercept, r_value, *_ = linregress(temps[:left_SPR_cutoff],
                                                                   strain[:left_SPR_cutoff])
        
        return left_SPR_slope, left_SPR_intercept, left_SPR_max_ind
    
    
    def find_right_SPR_tangent(temps, strain, TRR_slope, TRR_intercept, right_extrema, max_temp):
        """
        Finds tangent line for the right single-phase region of the
        cycle branch.
        
        Uses the intersection of the transformation response region
        line with the right asymptote strain value as the total 
        number of points that could possibly fall within the right 
        single-phase region. Uses the points corresponding to the 
        highest 50% of  temperatures between the UCT and the 
        above-described intersection points.
        """
        
        # Trim out the first and last 1% of points.
        temps = temps[round(.01*len(temps)):round(0.99*len(temps))]
        strain = strain[round(.01*len(strain)):round(0.99*len(strain))]
        
        minimum_right_single_phase_region_temp, *_ = line_intersection(TRR_slope, TRR_intercept, 0, right_extrema)                  
        right_SPR_min_ind = find_nearest(temps, minimum_right_single_phase_region_temp)
        # Finds index of halfway point between the max_temp and the
        # minimum_right_single_phase_region_temp point.
        right_SPR_cutoff = find_nearest(temps, (minimum_right_single_phase_region_temp + max_temp)/2)
        
        # Ensure at least 3 points (or 5% of the points in the branch) are used
        # to determine the single-phase region tangent line. 
        if right_SPR_cutoff <= right_SPR_min_ind or any(val > len(temps)-3 for val in [right_SPR_cutoff, right_SPR_min_ind]):
            right_SPR_cutoff = min(round(0.95*len(temps)), len(temps)-3)
            right_SPR_min_ind = min(round(0.8*len(temps)), len(temps)-4)
        
        # Apply linear fit to the selected points. The determined line is the
        # single-phase region line for this side of the cycle branch.
        right_SPR_slope, right_SPR_intercept, r_value, *_ = linregress(temps[right_SPR_cutoff:],
                                                                         strain[right_SPR_cutoff:])
            
        return right_SPR_slope, right_SPR_intercept, right_SPR_min_ind
    
    


    left_SPR_slope, left_SPR_intercept, left_SPR_max_ind = find_left_SPR_tangent(temps, 
                                                                                 strain, 
                                                                                 TRR_slope, 
                                                                                 TRR_intercept, 
                                                                                 left_extrema, 
                                                                                 min_temp)
    
    # If the slope is above that which is possible (i.e. it
    # corresponds to a CTE that no SMA could possess), the
    # determination of the left single-phase region line is re-ran.
    # Before it is re-ran, some points which have significant
    # variation from their neighbors (i.e. have a large slope 
    # between them and local points) are removed.
    # This is meant to prevent outliers at the ends of a cycle
    # branch from adversely affecting results.
    if abs(left_SPR_slope) > 10**-2:
        left_temps = temps[:left_SPR_max_ind]
        left_strain = strain[:left_SPR_max_ind]
        slope_between_points = np.gradient(left_strain)/np.gradient(left_temps)
        bad_slope_cutoff = np.percentile(abs(slope_between_points), 67)
        filtered_left_temps = left_temps[(abs(slope_between_points) < bad_slope_cutoff)]
        filtered_left_strain = left_strain[(abs(slope_between_points) < bad_slope_cutoff)]
        if len(filtered_left_temps) >= 5:
            left_SPR_slope, left_SPR_intercept, *_ = find_left_SPR_tangent(filtered_left_temps, 
                                                                           filtered_left_strain, 
                                                                           TRR_slope, 
                                                                           TRR_intercept, 
                                                                           left_extrema, 
                                                                           min_temp)



    right_SPR_slope, right_SPR_intercept, right_SPR_min_ind = find_right_SPR_tangent(temps, 
                                                                                     strain, 
                                                                                     TRR_slope, 
                                                                                     TRR_intercept, 
                                                                                     right_extrema, 
                                                                                     max_temp)
    # If the slope is above that which is possible (i.e. it
    # corresponds to a CTE that no SMA could possess), the
    # determination of the left single-phase region line is re-ran.
    # Before it is re-ran, some points which have significant
    # variation from their neighbors (i.e. have a large slope 
    # between them and local points) are removed.
    # This is meant to prevent outliers at the ends of a cycle
    # branch from adversely affecting results.
    if abs(right_SPR_slope) > 10**-2:
        right_temps = temps[right_SPR_min_ind:]
        right_strain = strain[right_SPR_min_ind:]
        slope_between_points = np.gradient(right_strain)/np.gradient(right_temps)
        bad_slope_cutoff = np.percentile(abs(slope_between_points), 67)
        filtered_right_temps = right_temps[(abs(slope_between_points) < bad_slope_cutoff)]
        filtered_right_strain = right_strain[(abs(slope_between_points) < bad_slope_cutoff)]
        if len(filtered_right_temps) >= 5:
            right_SPR_slope, right_SPR_intercept, *_ = find_right_SPR_tangent(filtered_right_temps, 
                                                                              filtered_right_strain, 
                                                                              TRR_slope, 
                                                                              TRR_intercept, 
                                                                              right_extrema, 
                                                                              max_temp)
    
    
    return [left_SPR_slope, left_SPR_intercept, right_SPR_slope, right_SPR_intercept]