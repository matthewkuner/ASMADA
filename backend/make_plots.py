# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from backend.make_plot_labels import make_plot_labels
from backend.make_plot_markers import make_plot_markers

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




# WorkerThread manages all aspects of analysis.
class make_plots_class:

    def make_plots(self, GUI_inputs, df_material_parameters, df_smoothed_data, cycles_to_analyze, tot_num_cyc):
        """
        Creates plot of all cycles together, alongside many plots for most 
        of the material properties calculated.


        Parameters
        ----------
        GUI_inputs : pandas DataFrame
            Contains all user inputs.
        df_material_parameters : pandas DataFrame
            Contains all material parameters calculated in the
            'analyze_data' method.
        df_smooth_data : pandas DataFrame
            Array containing temperature and strain data after being
            smoothed (alongside identified cycle numbers).
        cycles_to_analyze : list
            Used to only plot cycles specified by the user for analysis.

        Returns
        ----------
        fig_all_cycle : matplotlib figure
            Figure of all cycles for export.
        fig_temps_separate : matplotlib figure
            Figure of transformation temperatures (plotted separately).
        fig_temps_all : matplotlib figure
            Figure of transformation temperatures (plotted together).
        fig_strains_separate : matplotlib figure
            Figure of transformation strains (plotted separately).
        fig_strains_all : matplotlib figure
            Figure of transformation strains (plotted together).
        fig_transform_strain : matplotlib figure
            Figure of transformation strain and actuation strain.
        fig_hysteresis : matplotlib figure
            Figure of HWIDTH and HAREA.
        fig_minmax_temps : matplotlib figure
            Figure of minimum and maximimum cycle temperatures.
        fig_coef_thermal_expan : matplotlib figure
            Figure of Austenite and Martensite CTE's.
        """

        # Write progress update to GUI.
        self.notifyProgress.emit('making plots')


        axis_label_kwargs, plot_title_kwargs, temp_axis_label, strain_axis_label, CTE_axis_label, hyst_area_axis_label = make_plot_labels(GUI_inputs)


        marker_kwargs, legend_marker_kwargs = make_plot_markers(cycles_to_analyze)


        


        # Plot all cycles specified for analysis on the temperature
        # and strain axes.
        # Initializes plot size, labels, etc.
        fig_all_cycle, ax_all_cycle = plt.subplots(figsize = (10,6))
        ax_all_cycle.set_title('All Thermal Cycles', **plot_title_kwargs)
        ax_all_cycle.set_xlabel(temp_axis_label, **axis_label_kwargs)
        ax_all_cycle.set_ylabel(strain_axis_label, **axis_label_kwargs)
        # Plot the first cycle in green, all intermediate cycles in
        # light gray, and the final cycle in purple.
        for i in range(3):
            # Plot first cycle in green.
            if i == 0:
                # Ensure that the first cycle plotted excludes the
                # initialization procedure. This does not apply to isobaric
                # thermal cycling tests with a small number of cycles.
                if tot_num_cyc > 10 and cycles_to_analyze[0] == 0 and cycles_to_analyze[1]:
                    first_cycle = 1
                else:
                    first_cycle = 0
                    
                df = df_smoothed_data.loc[df_smoothed_data['cycle'] == cycles_to_analyze[first_cycle]]
                temps = df['temp'].to_numpy()
                strain = df['strain'].to_numpy()

                ax_all_cycle.plot(temps,
                                  strain,
                                  color='#117733',
                                  linewidth=2,
                                  zorder=2,
                                  label='First Cycle')
            # Plot all intermediate cycles in light gray.
            elif i == 1:
                df = df_smoothed_data.loc[df_smoothed_data['cycle'].isin(cycles_to_analyze[1:-1])]
                temps = df['temp'].to_numpy()
                strain = df['strain'].to_numpy()

                ax_all_cycle.plot(temps,
                                  strain,
                                  color='#CCCCCC',
                                  linewidth=1,
                                  zorder=1,
                                  label='All Intermediate Cycles')
            # Plot final cycle in purple.
            else:
                # Ensure that the last cycle plotted excludes the cycle at
                # failure. This does not apply to isobaric thermal cycling
                # tests with a small number of cycles.
                if tot_num_cyc > 10 and cycles_to_analyze[-1] == tot_num_cyc:
                    last_cycle = -2
                else:
                    last_cycle = -1

                df = df_smoothed_data.loc[df_smoothed_data['cycle']==cycles_to_analyze[last_cycle]]
                temps = df['temp'].to_numpy()
                strain = df['strain'].to_numpy()

                ax_all_cycle.plot(temps,
                                  strain,
                                  color='#A926A8',
                                  linewidth=2,
                                  zorder=2,
                                  label='Final Completed Cycle')

        ax_all_cycle.legend(loc='best')




        ##### Plotting of Properties/Parameters determined in the
        ##### 'analyze_data' function.
        

        # Prepare units to use to index columns from 
        # df_material_parameters (this is slightly different from 
        # determining units for plot axis labels).
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

        # Extract cycle numbers and properties/parameters for plotting
        # from df_material_parameters.
        cycle = df_material_parameters['cycle']
        M_s_temp = df_material_parameters['M_s_temp'+temp_unit]
        M_f_temp = df_material_parameters['M_f_temp'+temp_unit]
        A_s_temp = df_material_parameters['A_s_temp'+temp_unit]
        A_f_temp = df_material_parameters['A_f_temp'+temp_unit]
        M_s_strain = df_material_parameters['M_s_strain'+strain_unit]
        M_f_strain = df_material_parameters['M_f_strain'+strain_unit]
        A_s_strain = df_material_parameters['A_s_strain'+strain_unit]
        A_f_strain = df_material_parameters['A_f_strain'+strain_unit]
        LCT = df_material_parameters['LCT'+temp_unit]
        UCT = df_material_parameters['UCT'+temp_unit]
        LCT_strain = df_material_parameters['LCT_strain'+strain_unit]
        UCT_strain = df_material_parameters['UCT_strain'+strain_unit]
        actuation_strain = df_material_parameters['actuation_strain'+strain_unit]
        transform_strain = df_material_parameters['transform_strain'+strain_unit]
        TRIP_strain = df_material_parameters['TRIP_strain'+strain_unit]
        hysteresis_area = df_material_parameters['hysteresis_area'+hyst_area_unit]
        hysteresis_width = df_material_parameters['hysteresis_width'+temp_unit]
        thermal_transform_span = df_material_parameters['thermal_transform_span'+temp_unit]
        aust_coef_thermal_expan = df_material_parameters['aust_coef_thermal_expan'+CTE_unit]
        mart_coef_thermal_expan = df_material_parameters['mart_coef_thermal_expan'+CTE_unit]
        min_strain = df_material_parameters['min_strain'+strain_unit]
        max_strain = df_material_parameters['max_strain'+strain_unit]


        def make_single_plot(ylabel):
            fig, ax = plt.subplots(figsize = (10,6))
            plt.subplots_adjust(wspace = 0.3, hspace = 0.5)
            ax.set_xlabel('Cycle Number', **axis_label_kwargs)
            ax.set_ylabel(ylabel, **axis_label_kwargs)
            return fig, ax

        
        def make_multi_plot(ylabel, nrows, ncols):
            fig, ax = plt.subplots(nrows, ncols, figsize = (10,7.5))
            plt.subplots_adjust(wspace = 0.3, hspace = 0.5)
            for x in range(nrows):
                for y in range(ncols):
                    ax[x,y].set_xlabel('Cycle Number', **axis_label_kwargs)
                    ax[x,y].set_ylabel(ylabel, **axis_label_kwargs)
            return fig, ax


        def resize_axes(ax, width_fraction):
            # Shrink current axis by 20%.
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            return ax
        



        # Plot evolution of all four transformation temperatures over all
        # cycles on separate plots.
        fig_temps_separate, ax_temps_separate = make_multi_plot(temp_axis_label,2,2)
        ax_temps_separate[0, 0].plot(cycle, M_f_temp, **marker_kwargs['Mf'])
        ax_temps_separate[1, 0].plot(cycle, M_s_temp, **marker_kwargs['Ms'])
        ax_temps_separate[0, 1].plot(cycle, A_s_temp, **marker_kwargs['As'])
        ax_temps_separate[1, 1].plot(cycle, A_f_temp, **marker_kwargs['Af'])
        ax_temps_separate[1, 0].set_title('$\mathregular{M_s}$', **plot_title_kwargs)
        ax_temps_separate[0, 0].set_title('$\mathregular{M_f}$', **plot_title_kwargs)
        ax_temps_separate[0, 1].set_title('$\mathregular{A_s}$', **plot_title_kwargs)
        ax_temps_separate[1, 1].set_title('$\mathregular{A_f}$', **plot_title_kwargs)


        # Plot evolution of all four transformation temperatures over all
        # cycles on the same plot.
        fig_temps_all, ax_temps_all = make_single_plot(temp_axis_label)
        ax_temps_all.plot(cycle, M_f_temp, **marker_kwargs['Mf'])
        ax_temps_all.plot(cycle, M_s_temp, **marker_kwargs['Ms'])
        ax_temps_all.plot(cycle, A_s_temp, **marker_kwargs['As'])
        ax_temps_all.plot(cycle, A_f_temp, **marker_kwargs['Af'])
        ax_temps_all.set_title('All Transformation Temperatures', **plot_title_kwargs)
        ax_temps_all = resize_axes(ax_temps_all, 0.8)
        legend_elements = [Line2D([0],[0], label='$\mathregular{M_f}$', **legend_marker_kwargs['Mf']),
                           Line2D([0],[0], label='$\mathregular{M_s}$', **legend_marker_kwargs['Ms']),
                           Line2D([0],[0], label='$\mathregular{A_s}$', **legend_marker_kwargs['As']),
                           Line2D([0],[0], label='$\mathregular{A_f}$', **legend_marker_kwargs['Af'])]
        ax_temps_all.legend(handles=legend_elements,
                            loc='center left', 
                            bbox_to_anchor=(1, 0.5))


        # Plotbranch using Savitzky-Golay filter. evolution of all four transformation strains over all
        # cycles on separate plots.
        fig_strains_separate, ax_strains_separate = make_multi_plot(strain_axis_label,2,2)
        ax_strains_separate[0, 0].plot(cycle, M_f_strain, **marker_kwargs['Mf'])
        ax_strains_separate[1, 0].plot(cycle, M_s_strain, **marker_kwargs['Ms'])
        ax_strains_separate[0, 1].plot(cycle, A_s_strain, **marker_kwargs['As'])
        ax_strains_separate[1, 1].plot(cycle, A_f_strain, **marker_kwargs['Af'])
        ax_strains_separate[1, 0].set_title('$\mathregular{M_s}$', **plot_title_kwargs)
        ax_strains_separate[0, 0].set_title('$\mathregular{M_f}$', **plot_title_kwargs)
        ax_strains_separate[0, 1].set_title('$\mathregular{A_s}$', **plot_title_kwargs)
        ax_strains_separate[1, 1].set_title('$\mathregular{A_f}$', **plot_title_kwargs)
                

        # Plot evolution of all four transformation strains over all
        # cycles on the same plot.
        fig_strains_all, ax_strains_all = make_single_plot(strain_axis_label)
        ax_strains_all.plot(cycle, M_f_strain, **marker_kwargs['Mf'])
        ax_strains_all.plot(cycle, M_s_strain, **marker_kwargs['Ms'])
        ax_strains_all.plot(cycle, A_s_strain, **marker_kwargs['As'])
        ax_strains_all.plot(cycle, A_f_strain, **marker_kwargs['Af'])
        ax_strains_all.set_title('All Transformation Strains', **plot_title_kwargs)
        ax_strains_all = resize_axes(ax_strains_all, 0.8)
        legend_elements = [Line2D([0],[0], label='$\mathregular{M_f}$', **legend_marker_kwargs['Mf']),
                           Line2D([0],[0], label='$\mathregular{M_s}$', **legend_marker_kwargs['Ms']),
                           Line2D([0],[0], label='$\mathregular{A_s}$', **legend_marker_kwargs['As']),
                           Line2D([0],[0], label='$\mathregular{A_f}$', **legend_marker_kwargs['Af'])]
        ax_strains_all.legend(handles=legend_elements,
                              loc='center left',
                              bbox_to_anchor=(1, 0.5))


        # plots evolution of austenite, martensite, and total transformation strains over all cycles
        fig_actuation_transform_strain, (ax_act_transform1, ax_act_transform2) = plt.subplots(1, 2, figsize = (18,6), sharey = True)
        plt.subplots_adjust(wspace = 0.05)
        ax_act_transform1.plot(cycle, A_s_strain, **marker_kwargs['As'])
        ax_act_transform1.plot(cycle, A_f_strain, **marker_kwargs['Af'])
        ax_act_transform1.plot(cycle, transform_strain, **marker_kwargs['Misc3'])
        ax_act_transform1.set_title('$\epsilon_{A_s}$, $\epsilon_{A_f}$, and Total Transformation Strains', **plot_title_kwargs)
        # Shrink current axis by 20%
        box = ax_act_transform1.get_position()
        ax_act_transform1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        legend_elements = [Line2D([0],[0], label='$\epsilon_{t}$', **legend_marker_kwargs['Misc3']),
                           Line2D([0],[0], label='$\epsilon_{A_s}$', **legend_marker_kwargs['As']),
                           Line2D([0],[0], label='$\epsilon_{A_f}$', **legend_marker_kwargs['Af'])]
        ax_act_transform1.legend(handles=legend_elements,
                                 loc='best')
        ax_act_transform1.set_xlabel('Cycle Number', **axis_label_kwargs)
        ax_act_transform1.set_ylabel('Strain [%]', **axis_label_kwargs)

        # plots evolution of UCT, LCT, and Actuation strains over all cycles
        #fig_presentation2, ax_presentation2 = plt.subplots(figsize = (10,6))
        #plt.subplots_adjust(wspace = 0.3, hspace = 0.5)
        ax_act_transform2.plot(cycle, UCT_strain, **marker_kwargs['Hot'])
        ax_act_transform2.plot(cycle, LCT_strain, **marker_kwargs['Cold'])
        ax_act_transform2.plot(cycle, actuation_strain, **marker_kwargs['Misc4'])
        ax_act_transform2.set_title('$\mathregular{UCT}$, $\mathregular{LCT}$, and Actuation Strains', **plot_title_kwargs)
        # Shrink current axis by 20%
        box = ax_act_transform2.get_position()
        ax_act_transform2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        legend_elements = [Line2D([0],[0], label='$\epsilon_{act}$', **legend_marker_kwargs['Misc4']),
                           Line2D([0],[0], label='$\epsilon_{LCT}$', **legend_marker_kwargs['Cold']),
                           Line2D([0],[0], label='$\epsilon_{UCT}$', **legend_marker_kwargs['Hot'])]
        ax_act_transform2.legend(handles=legend_elements,
                                 loc='best')
        ax_act_transform2.set_xlabel('Cycle Number', **axis_label_kwargs)
        ax_act_transform2.set_ylabel('Strain [%]', **axis_label_kwargs)
        ax_act_transform2.yaxis.set_tick_params(labelleft=True)


        # Function specifically made to make the plot of the hysteresis
        # area/width plot have aesthetically pleasing y-axes (this plot
        # has two y-axes). Secondary axes act strangely in matplotlib; this
        # ensure that both of the y-axes have the same number of ticks 
        # (simple) while also having ticks with 'round' numbers (more 
        # tricky).
        def correct_yaxis(ax, num_ticks_needed, tick_spacing):
            num_ticks_to_add = num_ticks_needed - len(ax.get_yticks())
            ymin, ymax = ax.get_ylim()
            new_ymin = ymin - tick_spacing*math.floor(num_ticks_to_add/2)
            new_ymax = ymax + tick_spacing*math.ceil(num_ticks_to_add/2)
            ax.set_yticks(np.linspace(new_ymin, 
                                      new_ymax, 
                                      num_ticks_needed))
            return ax

        # Plot evolution of hysteresis area and hysteresis width over all 
        # cycles.
        fig_hysteresis, ax_hysteresis = make_single_plot(temp_axis_label)
        ax_hysteresis.plot(cycle, hysteresis_width, **marker_kwargs['Misc1'])
        ax_hysteresis.set_ylabel(temp_axis_label, **axis_label_kwargs)
        ax_hysteresis.yaxis.label.set_color('#B94685')
        ax_hysteresis2 = ax_hysteresis.twinx()
        ax_hysteresis2.plot(cycle, hysteresis_area, **marker_kwargs['Misc2'])
        ax_hysteresis2.set_ylabel(hyst_area_axis_label, labelpad=10, **axis_label_kwargs)
        ax_hysteresis2.yaxis.label.set_color('#009E73')
        # Color y-axes separately.
        ax_hysteresis.tick_params(axis='y', colors = '#B94685')
        ax_hysteresis2.tick_params(axis='y', colors = '#009E73')
        ax_hysteresis2.spines['left'].set_color('#B94685')
        ax_hysteresis2.spines['right'].set_color('#009E73')
        # Use above-made function to make both y-axes more aesthetically 
        # pleasing.
        if len(ax_hysteresis.get_yticks()) > len(ax_hysteresis2.get_yticks()):
            ax_hysteresis2 = correct_yaxis(ax_hysteresis2, 
                                           len(ax_hysteresis.get_yticks()),
                                           abs(ax_hysteresis2.get_yticks()[1] - ax_hysteresis2.get_yticks()[0]))
        elif len(ax_hysteresis2.get_yticks()) > len(ax_hysteresis.get_yticks()):
            ax_hysteresis = correct_yaxis(ax_hysteresis, 
                                          len(ax_hysteresis2.get_yticks()),
                                          abs(ax_hysteresis.get_yticks()[1] - ax_hysteresis.get_yticks()[0]))
        ax_hysteresis.set_title('Hysteresis Width and Hysteresis Area', **plot_title_kwargs)
        legend_elements = [Line2D([0],[0], label='HWIDTH', **legend_marker_kwargs['Misc1']),
                           Line2D([0],[0], label='HAREA', **legend_marker_kwargs['Misc2'])]
        ax_hysteresis.legend(handles=legend_elements,
                             loc='best')


        # Plot UCT and LCT over all cycles.
        fig_UCT_LCT, (ax_UCT, ax_LCT) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
        plt.subplots_adjust(hspace = 0.2)
        ax_UCT.plot(cycle, UCT, **marker_kwargs['Hot'])
        ax_LCT.plot(cycle, LCT, **marker_kwargs['Cold'])
        # Set the temperature range on both of the y-axis to be equal.
        # This allows better comparison of the apparatus' control over the
        # LCT and UCT with respect to each other.
        LCT_temp_range = LCT.max()-LCT.min()
        UCT_temp_range = UCT.max()-UCT.min()
        temp_range_diff = abs(LCT_temp_range - UCT_temp_range)
        if LCT_temp_range > UCT_temp_range:
            ax_UCT.plot((cycle[0],cycle[0]), 
                        (UCT.min()-temp_range_diff/2, UCT.max()+temp_range_diff/2),
                        linestyle = 'None',
                        alpha = 0)
        elif LCT_temp_range < UCT_temp_range:
            ax_LCT.plot((cycle[0],cycle[0]), 
                        (LCT.min()-temp_range_diff/2, LCT.max()+temp_range_diff/2),
                        linestyle = 'None',
                        alpha = 0)
        fig_UCT_LCT.suptitle('Upper and Lower Cycle Temperatures', **plot_title_kwargs, y = 0.92)
        legend_elements = [Line2D([0],[0], label='UCT', **legend_marker_kwargs['Hot']),
                           Line2D([0],[0], label='LCT', **legend_marker_kwargs['Cold'])]
        fig_UCT_LCT.legend(handles=legend_elements, 
                           loc = 'center left',
                           bbox_to_anchor=(.9, 0.50))
        fig_UCT_LCT.text(0.5, 0.05, 'Cycle Number', ha='center', **axis_label_kwargs)
        fig_UCT_LCT.text(0.03, 0.5, temp_axis_label, va='center', rotation='vertical', **axis_label_kwargs)


        # Plot evolution of the two coefficients of thermal expansion over
        # all cycles.
        fig_coef_thermal_expan, ax_coef_thermal_expan = make_single_plot(CTE_axis_label)
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText = True)
        ax_coef_thermal_expan.plot(cycle, aust_coef_thermal_expan, **marker_kwargs['Hot'])
        ax_coef_thermal_expan.plot(cycle, mart_coef_thermal_expan, **marker_kwargs['Cold'])
        ax_coef_thermal_expan.set_title('Single-Phase Coefficients of Thermal Expansion', **plot_title_kwargs)
        ax_coef_thermal_expan = resize_axes(ax_coef_thermal_expan, 0.8)
        legend_elements = [Line2D([0],[0], label='Austenite CTE', **legend_marker_kwargs['Hot']),
                           Line2D([0],[0], label='Martensite CTE', **legend_marker_kwargs['Cold'])]
        ax_coef_thermal_expan.legend(handles=legend_elements,
                                     loc='center left',
                                     bbox_to_anchor=(1, 0.5))





        return fig_all_cycle, fig_temps_separate, fig_temps_all, fig_strains_separate, fig_strains_all, fig_actuation_transform_strain, fig_hysteresis, fig_UCT_LCT, fig_coef_thermal_expan
