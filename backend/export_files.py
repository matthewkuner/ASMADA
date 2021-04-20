# -*- coding: utf-8 -*-
import os
from pathlib import Path
from configparser import ConfigParser
import numpy as np
import pandas as pd
import matplotlib.animation as animation
from datetime import datetime

# WorkerThread manages all aspects of analysis.
class export_files_class:

    def export_files(self, GUI_inputs, cycles_to_analyze, df_material_parameters, im_animation, fig_all_cycle, fig_temps_separate, fig_temps_all, fig_strains_separate, fig_strains_all, fig_actuation_transform_strain, fig_hysteresis, fig_UCT_LCT, fig_coef_thermal_expan):
        """
        Exports material properties and plots created in previous methods.


        Parameters
        ----------
        GUI_inputs : pandas DataFrame
            Contains all user inputs.
        df_material_parameters : pandas DataFrame
            Contains all material parameters calculated in the
            'analyze_data' method.
        im_animation : matplotlib animation (???)
            --
        fig_all_cycle : matplotlib figure
            --
        fig_temps_separate : matplotlib figure
            --
        fig_temps_all : matplotlib figure
            --
        fig_strains_separate : matplotlib figure
            --
        fig_strains_all : matplotlib figure
            --
        fig_transform_strain : matplotlib figure
            --
        fig_hysteresis : matplotlib figure
            --
        fig_minmax_temps : matplotlib figure
            --
        fig_coef_thermal_expan : matplotlib figure
            --

        Returns
        -------
        None.
        """
        
        config = ConfigParser()
        config.read('ASMADA_config.ini')
        filepath = Path(config['paths']['filepath'])
        path_to_code = config['paths']['path_to_code']
        path_to_parent_dir = Path(config['paths']['path_to_parent_dir'])
        path_to_Exported_Files_folder = Path(config['paths']['path_to_Exported_Files_folder'])
        os.chdir(path_to_Exported_Files_folder)
        

        # Write progress update to GUI.
        self.notifyProgress.emit('exporting files')


        # Create file name prefix for all exported files. 
        # If user inputted a custom file name for exported files, use it.
        if GUI_inputs.export_file_name.values[0]!='':
            export_file_name_prefix = GUI_inputs.export_file_name.values[0]
        # Otherwise, make the file name prefix match the file being 
        # analyzed.
        else:
            export_file_name_prefix = GUI_inputs.export_file_name.values[0]
            export_file_name_prefix = filepath.stem

        
        # Create subfolder within 'Exported_Files' to save the exported
        # files for the current run. This folder has the date/time
        # included for user reference.
        subfolder_name = export_file_name_prefix + datetime.now().strftime('(%Y%b%d-%H%M)')
        path_to_export_subfolder = path_to_Exported_Files_folder / subfolder_name
        
        # If code is ran two times in the same minute, add "_n" to the end
        # of the new folder's name, where n is incremented until a unique
        # folder name is obtained.
        if Path.is_dir(path_to_export_subfolder):
            n = 2
            while Path.is_dir(path_to_export_subfolder):
                # Re-make path for new subfolder.
                path_to_export_subfolder = path_to_Exported_Files_folder / (subfolder_name + '_' + str(n))
                n = n+1
        
        # Create subfolder, then changes directory to this new subfolder.
        Path.mkdir(path_to_export_subfolder)
        os.chdir(path_to_export_subfolder)
        

        # Check file type user desires for exported material 
        # properties/parameters.
        export_as_csv = False
        export_as_excel_workbook = False
        export_as_txt = False
        if GUI_inputs.export_file_type.values[0] == '.csv':
            export_as_csv = True
        elif GUI_inputs.export_file_type.values[0] == '.txt':
            export_as_txt = True
        elif GUI_inputs.export_file_type.values[0] == '.xlsx':
            export_as_excel_workbook = True

        # Create notes to include at the top of all exported files.
        file_analyzed_string = 'Name of file analyzed: ' + filepath.name
        now = datetime.now()
        date_time_string = 'Date and time of analysis: ' + now.strftime('%Y-%b-%d %H:%M:%S')
        comments_to_append = file_analyzed_string + '\n' + date_time_string + '\n\n'


        # Export all material properties/parameters calculated for 
        # all cycles.
        # Export process for .csv files.
        if export_as_csv:
            # First create file, writing only the notes about the 
            # analysis.
            with open(export_file_name_prefix + '_analyzed' + '.csv', 'w') as f:
                f.write(comments_to_append)
            # Then append df_material_parameters to the created file.
            df_material_parameters.to_csv(export_file_name_prefix + '_analyzed' + '.csv', mode = 'a', index = False, encoding = 'utf-8')
        # Export process for .xlsx files.
        elif export_as_excel_workbook:
            # Create writer for excel file.
            writer = pd.ExcelWriter(export_file_name_prefix + '_analyzed' + '.xlsx')
            # Save column names, add them onto file later so that the 
            # file writer does not format the headers incorrectly.
            column_list = df_material_parameters.columns
            # Write header-less dataframe, leaving 5 rows above for 
            # the comments and unformatted column names.
            df_material_parameters.to_excel(writer, sheet_name = 'Sheet1', startcol = 0, startrow = 5, index = False, header = False)
            worksheet = writer.sheets['Sheet1']
            # Write analysis notes to top of excel sheet.
            worksheet.write_string(0, 0, file_analyzed_string)
            worksheet.write_string(1, 0, date_time_string)
            # Write unformatted column names above data.
            for idx, val in enumerate(column_list):
                worksheet.write(4, idx, val)
            # Save file.
            writer.save()
        # Export process for .txt files.
        elif export_as_txt:
            col_names = df_material_parameters.columns
            col_names = ','.join(col_names)
            np.savetxt(export_file_name_prefix + '_analyzed' + '.txt', df_material_parameters.values, fmt = '%f', delimiter = ',', header = col_names, comments = comments_to_append)


        # Export plots.
        figure_save_settings_kwargs = dict(dpi=600, bbox_inches='tight', pad_inches=0.25)
        fig_all_cycle.savefig(export_file_name_prefix + '_analyzed_plot_all_cycles.png', **figure_save_settings_kwargs)
        fig_temps_separate.savefig(export_file_name_prefix + '_analyzed_plot_transform_temps_separate.png', **figure_save_settings_kwargs)
        fig_temps_all.savefig(export_file_name_prefix + '_analyzed_plot_transform_temps_overlaid.png', **figure_save_settings_kwargs)
        fig_strains_separate.savefig(export_file_name_prefix + '_analyzed_plot_transform_strains_separate.png', **figure_save_settings_kwargs)
        fig_strains_all.savefig(export_file_name_prefix + '_analyzed_plot_transform_strains_overlaid.png', **figure_save_settings_kwargs)
        fig_actuation_transform_strain.savefig(export_file_name_prefix + '_analyzed_plot_transform_actuation_strains.png', **figure_save_settings_kwargs)
        fig_coef_thermal_expan.savefig(export_file_name_prefix + '_analyzed_plot_austenite_martensite_CTE.png', **figure_save_settings_kwargs)
        fig_UCT_LCT.savefig(export_file_name_prefix + '_analyzed_plot_cycle_UCT_LCT.png', **figure_save_settings_kwargs)
        fig_hysteresis.savefig(export_file_name_prefix + '_analyzed_plot_hysteresis_area_width.png', **figure_save_settings_kwargs)

        # Export animation of fitted tangent lines.
        # Only export if the below conditions are met, as these are
        # requirements for an animation to be created.
        if cycles_to_analyze != '[custom]' or len(cycles_to_analyze) <= 251:
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=1.5, metadata=dict(artist='Me'), bitrate=-1)
            im_animation.save(export_file_name_prefix + '_analyzed_animation_tangent_line_fitting.mp4',
                              writer=writer,
                              dpi=300)


        # Change the current working directory back to the original folder 
        # containing the Python code.
        os.chdir(path_to_code)