# -*- coding: utf-8 -*-


def make_plot_markers(cycles_to_analyze):
    # Sets marker and linewidth for plot points based on number of
    # points being plotted. ms1 corresponds to smaller markers, whereas
    # ms2 corresponds to larger markers.
    if len(cycles_to_analyze) < 50:
        ms1 = 6
        ms2 = 8
        lw = 1
    elif len(cycles_to_analyze) < 250:
        ms1 = 4.5
        ms2 = 6
        lw = 0.75
    else:
        ms1 = 3
        ms2 = 4
        lw = 0.5
    
    # Marker parameters to use for plots of properties/parameters.
    marker_kwargs = {
                     'Mf': {'marker': 'o', 'markersize': ms1, 'color': '#0072B2', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},    # dark blue
                     'Ms': {'marker': '^', 'markersize': ms1, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},    # green
                     'As': {'marker': 's', 'markersize': ms1, 'color': '#E69F00', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},    # light orange
                     'Af': {'marker': '+', 'markersize': ms2, 'color': '#D55E00', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},    # reddish-orange
                     'Hot': {'marker': 'o', 'markersize': ms1, 'color': '#D55E00', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},   # reddish-orange    # use '#DC267F' for reddish-purple
                     'Cold': {'marker': '^', 'markersize': ms1, 'color': '#56B4E9', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'},  # light blue
                     'Misc1': {'marker': 's', 'markersize': ms1, 'color': '#B94685', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'}, # pink
                     'Misc2': {'marker': '+', 'markersize': ms2, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'}, # green
                     'Misc3': {'marker': '*', 'markersize': ms2, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'}, # green
                     'Misc4': {'marker': 'x', 'markersize': ms1, 'color': '#785EF0', 'fillstyle': 'none', 'markeredgewidth':lw, 'linestyle': 'None'}, # purple-blue
                     } 

    # Marker parameters for the plot *legends*. The only difference
    # from the above is the markersize (this is done manually, as the 
    # 'markerscale' kwarg does not scale 'markeredgewidth' correctly).
    legend_marker_kwargs = {
                            'Mf': {'marker': 'o', 'markersize': 9, 'color': '#0072B2', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},     # dark blue
                            'Ms': {'marker': '^', 'markersize': 9, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},     # green
                            'As': {'marker': 's', 'markersize': 9, 'color': '#E69F00', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},     # light orange
                            'Af': {'marker': '+', 'markersize': 12, 'color': '#D55E00', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},    # reddish-orange
                            'Hot': {'marker': 'o', 'markersize': 9, 'color': '#D55E00', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},    # reddish-orange    # use '#DC267F' for reddish-purple
                            'Cold': {'marker': '^', 'markersize': 9, 'color': '#56B4E9', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},   # light blue
                            'Misc1': {'marker': 's', 'markersize': 9, 'color': '#B94685', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},  # pink
                            'Misc2': {'marker': '+', 'markersize': 12, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'}, # green
                            'Misc3': {'marker': '*', 'markersize': 12, 'color': '#009E73', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'}, # green
                            'Misc4': {'marker': 'x', 'markersize': 9, 'color': '#785EF0', 'fillstyle': 'none', 'markeredgewidth':1.5, 'linestyle': 'None'},  # purple-blue
                            }


    return marker_kwargs, legend_marker_kwargs