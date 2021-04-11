# -*- coding: utf-8 -*-


def make_plot_labels(GUI_inputs):
    # Create reusable parameters for axis label and title kwargs. 
    axis_label_kwargs = dict(fontweight = 'semibold', fontsize = 'large')
    plot_title_kwargs = dict(fontsize = 'large')


    # Create axis label strings.
    # Determine appropriate temperature units to use.
    if GUI_inputs.temp_unit.values[0] == '[°C]':
        temp_unit_label = ' ' + '[\u00B0C]'
    elif GUI_inputs.temp_unit.values[0] == '[K]':
        temp_unit_label = ' ' + '[K]'
    elif GUI_inputs.temp_unit.values[0] == '[°F]':
        temp_unit_label = ' ' + '[\u00B0F]'
        
    # Determine appropriate strain units to use.
    if GUI_inputs.strain_unit.values[0] == '[%]':
        strain_unit_label = ' ' + '[%]'
    elif GUI_inputs.strain_unit.values[0] == '[fraction]':
        strain_unit_label = ''
        
    # Combine string with appropriate units.
    temp_axis_label = 'Temperature' + temp_unit_label
    strain_axis_label = 'Strain' + strain_unit_label
    CTE_axis_label = 'Coefficient of Thermal Expansion [1/' + temp_unit_label[2:-1] + ']'
    hyst_area_axis_label = 'Area [' + temp_unit_label[2:-1] + ']'


    return axis_label_kwargs, plot_title_kwargs, temp_axis_label, strain_axis_label, CTE_axis_label, hyst_area_axis_label