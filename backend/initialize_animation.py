# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


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


def initialize_animation(cycles_to_analyze, GUI_inputs):
    # Initialize figure (fig_anim) and frame stack 
    # (animation_frame_stack) used for the animation of tangent
    # line fitting.
    fig_anim, ax_anim = plt.subplots(figsize = (10,6))
    fig_anim.subplots_adjust(left=0.1, bottom=0.1, right=0.97, top=0.93, wspace=None, hspace=None)
    ax_anim.cla()
    
    temp_axis_label = 'Temperature'
    if GUI_inputs.temp_unit.values[0] == '[°C]':
        temp_axis_label = temp_axis_label + ' ' + '[\u00B0C]'
    elif GUI_inputs.temp_unit.values[0] == '[K]':
        temp_axis_label = temp_axis_label + ' ' + '[K]'
    elif GUI_inputs.temp_unit.values[0] == '[°F]':
        temp_axis_label = temp_axis_label + ' ' + '[\u00B0F]'
        
    strain_axis_label = 'Strain'
    if GUI_inputs.strain_unit.values[0] == '[%]':
        strain_axis_label = strain_axis_label + ' ' + '[%]'
    elif GUI_inputs.strain_unit.values[0] == '[fraction]':
        pass
        
    # Label axes of figure
    ax_anim.set_xlabel(temp_axis_label, fontweight = 'semibold', fontsize = 'large')
    ax_anim.set_ylabel(strain_axis_label, fontweight = 'semibold', fontsize = 'large')


    # Initialize frame capture variable for animation
    animation_frame_stack = []

    # Set frame capture frequency for the animation.
    # If the user inputted a custom range of cycles, it will either
    # add all cycles as frames to the animation or none of the
    # cycles, depending on the number of cycles being analyzed;
    # this is to prevent outputted animations from being 
    # unreasonably large.
    if GUI_inputs.cycles_to_analyze.values[0] == '[custom]':
        if len(cycles_to_analyze) <= 251:
            frame_capture_freq = 1
        else:
            frame_capture_freq = 100000
    # If the user specified for all cycles to be analyzed, frames
    # will be captured at a regular interval that is chosen
    # based on the total number of cycles being analyzed.
    elif GUI_inputs.cycles_to_analyze.values[0] == 'all cycles':
        if len(cycles_to_analyze) < 200:
            frame_capture_freq = 10
        elif len(cycles_to_analyze) < 1000:
            frame_capture_freq = 20
        elif len(cycles_to_analyze) < 2500:
            frame_capture_freq = 50
        elif len(cycles_to_analyze) < 5000:
            frame_capture_freq = 100
        elif len(cycles_to_analyze) < 10000:
            frame_capture_freq = 200
        else:
            frame_capture_freq = 250


    return fig_anim, ax_anim, animation_frame_stack, frame_capture_freq