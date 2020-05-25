import os
import glob
import re
import sys # access system routines

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt

import Common
import Plotting

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks' ] # plot labels

def Plot_TEC_Exam_Results():
    # Device TIPS-2 exhibits unstable temperature once current across its DFB, SOA sections increases to 120 mA, EAM bis is held at 0 V
    # same behaviour is not oberserved in TIPS-1, suspect that temperature control on TIPS-2 is not as good as it should be
    # However, I had to confirm that the problem did not lie with TEC units
    # I forced a volt-limit error on TIPS-2 using both TEC units
    # Data shows that problem is with device and not TEC unit, TIPS-1 operates with lower power and does not display unstable temperature
    # By unstable temperature I mean that voltage across TEC increases dramatically and temperature is no longer fixed to sdet point
    # For more details see Tyndall Notebook 2715
    # R. Sheehan 15 - 8 - 2017

    try:

        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/TEC_Exam/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            Ivals = [0, 50, 100, 120, 140] # current (mA) across DFB and SOA sections, Veam = 0 V

            # Original Configuration
            Volt_1_T_20_TEC_125 = [0.16, 0.26, 0.5, 0.62, 0.77] # TEC output voltage across TIPS1 using TEC-125 at T = 20
            Curr_1_T_20_TEC_125 = [0.06, 0.11, 0.22, 0.28, 0.34] # TEC output current across TIPS1 using TEC-125 at T = 20
            Power_1_T_20_TEC_125 = compute_power(Volt_1_T_20_TEC_125, Curr_1_T_20_TEC_125) # TEC output power across TIPS1 using TEC-125 at T = 20

            Volt_1_T_25_TEC_125 = [0.06, 0.08, 0.28, 0.39, 0.53] # TEC output voltage across TIPS1 using TEC-125 at T = 25
            Curr_1_T_25_TEC_125 = [0.02, 0.04, 0.13, 0.18, 0.24] # TEC output current across TIPS1 using TEC-125 at T = 25
            Power_1_T_25_TEC_125 = compute_power(Volt_1_T_25_TEC_125, Curr_1_T_25_TEC_125) # TEC output power across TIPS1 using TEC-125 at T = 25

            Volt_1_T_20_TEC_125_Rpt = [0.13, 0.27, 0.51, 0.64, 0.79] # TEC output voltage across TIPS1 using TEC-125 at T = 20 Repeat
            Curr_1_T_20_TEC_125_Rpt = [0.05, 0.11, 0.22, 0.28, 0.35] # TEC output current across TIPS1 using TEC-125 at T = 20 Repeat
            Power_1_T_20_TEC_125_Rpt = compute_power(Volt_1_T_20_TEC_125_Rpt, Curr_1_T_20_TEC_125_Rpt) # TEC output power across TIPS1 using TEC-125 at T = 20 Repeat

            Volt_1_T_25_TEC_125_Rpt = [0.09, 0.04, 0.25, 0.37, 0.49] # TEC output voltage across TIPS1 using TEC-125 at T = 25 Repeat
            Curr_1_T_25_TEC_125_Rpt = [0.04, 0.03, 0.12, 0.17, 0.23] # TEC output current across TIPS1 using TEC-125 at T = 25 Repeat
            Power_1_T_25_TEC_125_Rpt = compute_power(Volt_1_T_25_TEC_125_Rpt, Curr_1_T_25_TEC_125_Rpt) # TEC output power across TIPS1 using TEC-125 at T = 25 Repeat

            Volt_2_T_20_TEC_124 = [0.38, 2.25, 3.49, 7, 7] # TEC output voltage across TIPS2 using TEC-124 at T = 20
            Curr_2_T_20_TEC_124 = [0.05, 0.13, 0.37, 4, 4] # TEC output current across TIPS2 using TEC-124 at T = 20
            Power_2_T_20_TEC_124 = compute_power(Volt_2_T_20_TEC_124, Curr_2_T_20_TEC_124) # TEC output power across TIPS2 using TEC-124 at T = 20

            Volt_2_T_25_TEC_124 = [0.16, 0.2, 0.82, 1.24, 1.92] # TEC output voltage across TIPS2 using TEC-124 at T = 25
            Curr_2_T_25_TEC_124 = [0.02, 0.03, 0.13, 0.2, 0.31] # TEC output current across TIPS2 using TEC-124 at T = 25
            Power_2_T_25_TEC_124 = compute_power(Volt_2_T_25_TEC_124, Curr_2_T_25_TEC_124) # TEC output power across TIPS2 using TEC-124 at T = 25

            Volt_2_T_20_TEC_124_Rpt = [1.02, 1.5, 2.5, 7, 7] # TEC output voltage across TIPS2 using TEC-124 at T = 20 Repeat
            Curr_2_T_20_TEC_124_Rpt = [0.04, 0.12, 0.29, 4, 4] # TEC output current across TIPS2 using TEC-124 at T = 20 Repeat
            Power_2_T_20_TEC_124_Rpt = compute_power(Volt_2_T_20_TEC_124_Rpt, Curr_2_T_20_TEC_124_Rpt) # TEC output power across TIPS2 using TEC-124 at T = 20 Repeat

            Volt_2_T_25_TEC_124_Rpt = [0.31, 0.2, 1.11, 1.6, 2.47] # TEC output voltage across TIPS2 using TEC-124 at T = 25 Repeat
            Curr_2_T_25_TEC_124_Rpt = [0.03, 0.02, 0.13, 0.2, 0.32] # TEC output current across TIPS2 using TEC-124 at T = 25 Repeat
            Power_2_T_25_TEC_124_Rpt = compute_power(Volt_2_T_25_TEC_124_Rpt, Curr_2_T_25_TEC_124_Rpt) # TEC output power across TIPS2 using TEC-124 at T = 25 Repeat

            # Switched Configuration
            Volt_1_T_20_TEC_124 = [0.14, 0.27, 0.5, 0.63, 0.78] # TEC output voltage across TIPS1 using TEC-124 at T = 20
            Curr_1_T_20_TEC_124 = [0.05, 0.11, 0.22, 0.28, 0.35] # TEC output current across TIPS1 using TEC-124 at T = 20
            Power_1_T_20_TEC_124 = compute_power(Volt_1_T_20_TEC_124, Curr_1_T_20_TEC_124) # TEC output power across TIPS1 using TEC-124 at T = 20

            Volt_1_T_25_TEC_124 = [0.08, 0.07, 0.27, 0.38, 0.51] # TEC output voltage across TIPS1 using TEC-124 at T = 25
            Curr_1_T_25_TEC_124 = [0.03, 0.04, 0.13, 0.18, 0.24] # TEC output current across TIPS1 using TEC-124 at T = 25
            Power_1_T_25_TEC_124 = compute_power(Volt_1_T_25_TEC_124, Curr_1_T_25_TEC_124) # TEC output power across TIPS1 using TEC-124 at T = 25

            Volt_2_T_20_TEC_125 = [0.37, 0.91, 1.85, 7, 7] # TEC output voltage across TIPS2 using TEC-125 at T = 20
            Curr_2_T_20_TEC_125 = [0.04, 0.12, 0.28, 4, 4] # TEC output current across TIPS2 using TEC-125 at T = 20
            Power_2_T_20_TEC_125 = compute_power(Volt_2_T_20_TEC_125, Curr_2_T_20_TEC_125) # TEC output power across TIPS2 using TEC-125 at T = 20

            Volt_2_T_25_TEC_125 = [0.18, 0.22, 0.95, 1.41, 2.15] # TEC output voltage across TIPS2 using TEC-125 at T = 25
            Curr_2_T_25_TEC_125 = [0.02, 0.03, 0.14, 0.21, 0.33] # TEC output current across TIPS2 using TEC-125 at T = 25
            Power_2_T_25_TEC_125 = compute_power(Volt_2_T_25_TEC_125, Curr_2_T_25_TEC_125) # TEC output power across TIPS2 using TEC-125 at T = 25

            args = Plotting.plot_arguments()

            # Voltage T = 20
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Volt_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Volt_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Volt_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Volt_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 

            args.loud = False
            args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$V_{TEC}$ (V)'
            args.plt_range = [0.0, 145, 0, 4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Voltage_T_20.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Voltage T = 20 Repeat
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Volt_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Volt_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 
            plt_data.append([Ivals, Volt_1_T_20_TEC_125_Rpt]); labels.append('TIPS-1, TEC = 124 Rpt'); mark_list.append('r^'); 

            plt_data.append([Ivals, Volt_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Volt_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Volt_2_T_20_TEC_124_Rpt]); labels.append('TIPS-2, TEC = 125 Rpt'); mark_list.append('g^'); 

            args.loud = False
            args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$V_{TEC}$ (V)'
            args.plt_range = [0.0, 145, 0, 4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Voltage_T_20_Rpt.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Current T = 20
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Curr_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Curr_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Curr_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Curr_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$I_{TEC}$ (A)'
            args.plt_range = [0.0, 145, 0, 0.4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$I_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Current_T_20.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Current T = 20 Repeat
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Curr_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Curr_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 
            plt_data.append([Ivals, Curr_1_T_20_TEC_125_Rpt]); labels.append('TIPS-1, TEC = 125 Rpt'); mark_list.append('r^'); 

            plt_data.append([Ivals, Curr_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Curr_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Curr_2_T_20_TEC_124_Rpt]); labels.append('TIPS-2, TEC = 124 Rpt'); mark_list.append('g^'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$I_{TEC}$ (A)'
            args.plt_range = [0.0, 145, 0, 0.4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$I_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Current_T_20_Rpt.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Power T = 20
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Power_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Power_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Power_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Power_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$P_{TEC}$ (mW)'
            args.plt_range = [0.0, 145, 0, 1000]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Power_T_20.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Power T = 20 Rpt
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Power_1_T_20_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Power_1_T_20_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 
            plt_data.append([Ivals, Power_1_T_20_TEC_125_Rpt]); labels.append('TIPS-1, TEC = 125 Rpt'); mark_list.append('r^'); 

            plt_data.append([Ivals, Power_2_T_20_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Power_2_T_20_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Power_2_T_20_TEC_124_Rpt]); labels.append('TIPS-2, TEC = 124 Rpt'); mark_list.append('g^'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$P_{TEC}$ (mW)'
            args.plt_range = [0.0, 145, 0, 1000]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
            args.fig_name = 'Power_T_20_Rpt.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Voltage T = 25
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Volt_1_T_25_TEC_125]); labels.append('TIPS-1, T = 25, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Volt_1_T_25_TEC_124]); labels.append('TIPS-1, T = 25, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Volt_2_T_25_TEC_124]); labels.append('TIPS-2, T = 25, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Volt_2_T_25_TEC_125]); labels.append('TIPS-2, T = 25, TEC = 125'); mark_list.append('g--'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$V_{TEC}$ (V)'
            args.plt_range = [0.0, 145, 0, 4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Voltage_T_25.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Voltage T = 25 Repeat
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Volt_1_T_25_TEC_125]); labels.append('TIPS-1, T = 25, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Volt_1_T_25_TEC_124]); labels.append('TIPS-1, T = 25, TEC = 124'); mark_list.append('r--');
            plt_data.append([Ivals, Volt_1_T_25_TEC_125_Rpt]); labels.append('TIPS-1, T = 25, TEC = 125 Rpt'); mark_list.append('r^');  

            plt_data.append([Ivals, Volt_2_T_25_TEC_124]); labels.append('TIPS-2, T = 25, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Volt_2_T_25_TEC_125]); labels.append('TIPS-2, T = 25, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Volt_2_T_25_TEC_124_Rpt]); labels.append('TIPS-2, T = 25, TEC = 124 Rpt'); mark_list.append('g^'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$V_{TEC}$ (V)'
            args.plt_range = [0.0, 145, 0, 4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Voltage_T_25.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Current T = 25
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Curr_1_T_25_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Curr_1_T_25_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Curr_2_T_25_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Curr_2_T_25_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$I_{TEC}$ (A)'
            args.plt_range = [0.0, 145, 0, 0.4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$I_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Current_T_25.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Current T = 25 Repeat
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Curr_1_T_25_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Curr_1_T_25_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 
            plt_data.append([Ivals, Curr_1_T_25_TEC_125_Rpt]); labels.append('TIPS-1, TEC = 125 Rpt'); mark_list.append('r^');

            plt_data.append([Ivals, Curr_2_T_25_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Curr_2_T_25_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Curr_2_T_25_TEC_124_Rpt]); labels.append('TIPS-2, TEC = 124 Rpt'); mark_list.append('g^');

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$I_{TEC}$ (A)'
            args.plt_range = [0.0, 145, 0, 0.4]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$I_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Current_T_25_Rpt.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Power T = 25
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Power_1_T_25_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Power_1_T_25_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 

            plt_data.append([Ivals, Power_2_T_25_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Power_2_T_25_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$P_{TEC}$ (mW)'
            args.plt_range = [0.0, 145, 0, 1000]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Power_T_25.png'

            Plotting.plot_multiple_curves(plt_data, args)

            # Power T = 25 Repeat
            plt_data = []; labels = []; mark_list = []

            plt_data.append([Ivals, Power_1_T_25_TEC_125]); labels.append('TIPS-1, TEC = 125'); mark_list.append('r*-'); 
            plt_data.append([Ivals, Power_1_T_25_TEC_124]); labels.append('TIPS-1, TEC = 124'); mark_list.append('r--'); 
            plt_data.append([Ivals, Power_1_T_25_TEC_125_Rpt]); labels.append('TIPS-1, TEC = 125 Rpt'); mark_list.append('r^'); 

            plt_data.append([Ivals, Power_2_T_25_TEC_124]); labels.append('TIPS-2, TEC = 124'); mark_list.append('g*-'); 
            plt_data.append([Ivals, Power_2_T_25_TEC_125]); labels.append('TIPS-2, TEC = 125'); mark_list.append('g--'); 
            plt_data.append([Ivals, Power_2_T_25_TEC_124_Rpt]); labels.append('TIPS-2, TEC = 124 Rpt'); mark_list.append('g^'); 

            #args.loud = True
            #args.x_label = '$I_{dev}$ (mA)'
            args.y_label = '$P_{TEC}$ (mW)'
            args.plt_range = [0.0, 145, 0, 1000]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{TEC}$ variation with DFB and SOA current at T = 25 (C)'
            args.fig_name = 'Power_T_25.png'

            Plotting.plot_multiple_curves(plt_data, args)
        else:
            raise Exception
    except Exception:
        print("Error: TEC_Exam.Plot_TEC_Exam_Results")

def compute_power(voltage, current):
    # compute the power in mW from input voltage and current values

    try:
        c1 = True if voltage is not None else False
        c2 = True if current is not None else False
        c3 = True if len(voltage) == len(current) else False

        if c1 and c2 and c3:
            power = []
            for i in range(0, len(voltage), 1):
                power.append(1000*voltage[i]*current[i])

            return power
        else:
            raise Exception

    except Exception:
        print("Error: TEC_Exam.compute_power()")
