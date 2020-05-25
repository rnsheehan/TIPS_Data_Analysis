import os
import glob
import re
import sys # access system routines, including writing console output to file

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt

import Common
import Plotting
import SpctrmPlt
import FR_Analysis

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks' ] # plot labels

def Make_TIPS_WDM_plots():

    # call the functions needed to plot the data for TIPS Exp 4
    # WDM measurement of both TIPS channels
    # R. Sheehan 15 - 2 - 2018

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-4/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())

            #run_optical_spectrum_plots()

            run_FR_plot()

        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_WDM_Exp.Make_TIPS_WDM_Plots()")

def run_optical_spectrum_plots():

    dir_name = 'Optical_Spectra/TIPS_AS_Device/'

    #files = ['Spectrum_T_20_IDFB_100_ISOA_100.txt','Spectrum_T_21_IDFB_100_ISOA_100.txt','Spectrum_T_22_IDFB_100_ISOA_100.txt',
    #         'Spectrum_T_23_IDFB_100_ISOA_100.txt','Spectrum_T_24_IDFB_100_ISOA_100.txt','Spectrum_T_25_IDFB_100_ISOA_100.txt']
    #labels = ['T = 20 C', 'T = 21 C', 'T = 22 C', 'T = 23 C', 'T = 24 C', 'T = 25 C']
    #plot_range = [1318, 1324, -60, 0]
    #plot_title = 'OS Temp. Var. $I_{DFB} = I_{SOA} = 100 mA, V_{EAM} = 0 V$'
    #plot_name = 'OS_var_with_TEMP_IDFB_ISOA_100'

    files = ['Spectrum_T_25_I_100.txt', 'Spectrum_T_25_I_110.txt', 'Spectrum_T_25_I_120.txt', 'Spectrum_T_25_I_130.txt']
    labels = ['I = 100 mA', 'I = 110 mA', 'I = 120 mA', 'I = 130 mA']
    plot_range = [1318, 1324, -60, 0]
    plot_title = 'OS Curr. Var. T = 25 C, $V_{EAM} = 0 V$'
    plot_name = 'OS_var_with_Curr_T_25'

    SpctrmPlt.multiple_optical_spectrum_plot(dir_name, files, labels, plot_range, plot_title, plot_name)

def run_FR_plot():

    # Make a plot of the measured FR data for the TIPS-2 device
    # R. Sheehan 27 - 2 - 2018

    dir_name = 'FR/'

    file_names = ["TIPS2_T_25_IDFB_130_ISOA_130_VEAM_00.s2p", "TIPS2_T_25_IDFB_130_ISOA_130_VEAM_05.s2p", "TIPS2_T_25_IDFB_130_ISOA_130_VEAM_10.s2p"]
    labels = ['$V_{EAM}$ = 0 V', '$V_{EAM}$ = -0.5 V', '$V_{EAM}$ = -1 V']
    s_param = 2
    plot_range = [1, 15, -20, 0]
    plt_title = 'TIPS-2 FR'
    plt_name = 'TIPS_2_FR'

    FR_Analysis.multiple_FR_plot(dir_name, file_names, labels, s_param, plot_range, plt_title, plt_name, loudness = False)