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

def Make_TIPS_Pre_Amp():

    # call the functions needed to generate the plots for TIPS Exp 3
    # R. Sheehan 23 - 1 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-3/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())

            run_optical_spectra_plot()

            #directory = "Optical_Spectra/Thorlabs_SOA_Test/"
            #file_name = "TIPS_plus_SOA_D_0km_10dB_Att.txt"
            #att_fac = 10.0
            #Add_XdB_to_OSA_Data(directory, file_name, att_fac)

        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_Pre_Amp_Rx.Make_TIPS_Pre_Amp()")
        print("Error: Could not find",DATA_HOME)
    except Exception:
        print("Error: TIPS_Pre_Amp_Rx.Make_TIPS_Pre_Amp()")

def run_optical_spectra_plot():

    # make the list of file names
    # run the optical spectrum plot

    try:
        #directory = "Optical_Spectra/Kamelian_SOA_Test/"
        
        the_files = []; the_labels = []

        # plot the measured spectrum with no amplification
        
        #plot_title = 'Optical Spectra: No Amplification'
        #figure_name = 'Opt_Spctr_No_Amp'
        #plot_range = [1315, 1330, -72, 10]
        #the_files.append("DUT_D_0_No_Amp.txt"); the_labels.append("D = 0 km")
        #the_files.append("DUT_D_25_No_Amp.txt"); the_labels.append("D = 25 km")
        #the_files.append("DUT_D_50_No_Amp.txt"); the_labels.append("D = 50 km")

        #plot_title = 'Optical Spectra: With Amplification'
        #figure_name = 'Opt_Spctr_With_Amp'
        #plot_range = [1315, 1330, -72, 10]
        #the_files.append("DUT_D_0_With_Amp_I_550.txt"); the_labels.append("D = 0 km")
        #the_files.append("DUT_D_25_With_Amp_I_550.txt"); the_labels.append("D = 25 km")
        #the_files.append("DUT_D_50_With_Amp_I_550.txt"); the_labels.append("D = 50 km")

        #plot_title = 'Optical Spectra: With Amplification'
        #figure_name = 'Opt_Spctr_With_Amp_Coarse'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_0_With_Amp_I_550_Coarse.txt"); the_labels.append("D = 0 km")
        #the_files.append("DUT_D_25_With_Amp_I_550_Coarse.txt"); the_labels.append("D = 25 km")
        ##the_files.append("DUT_D_50_With_Amp_I_550_Coarse.txt"); the_labels.append("D = 50 km")

        #plot_title = 'Optical Spectra: No Amplification'
        #figure_name = 'Opt_Spctr_Coarse'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_0_No_Amp_Coarse.txt"); the_labels.append("D = 0 km")
        #the_files.append("DUT_D_25_No_Amp_Coarse.txt"); the_labels.append("D = 25 km")
        #the_files.append("DUT_D_0_With_Amp_I_550_Coarse.txt"); the_labels.append("D = 0 km with Amp")
        #the_files.append("DUT_D_25_With_Amp_I_550_Coarse.txt"); the_labels.append("D = 25 km with Amp")
        #the_files.append("DUT_D_50_No_Amp_Coarse.txt"); the_labels.append("D = 50 km")

        #plot_title = 'Optical Spectra: D = 0 km'
        #figure_name = 'Opt_Spctr_Coarse_D_0'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_0_No_Amp_Coarse.txt"); the_labels.append("No Amp")
        #the_files.append("DUT_D_0_With_Amp_I_550_Coarse.txt"); the_labels.append("With Amp")

        #plot_title = 'Optical Spectra: D = 25 km'
        #figure_name = 'Opt_Spctr_Coarse_D_25'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_25_No_Amp_Coarse.txt"); the_labels.append("No Amp")
        #the_files.append("DUT_D_25_With_Amp_I_550_Coarse.txt"); the_labels.append("With Amp")

        #plot_title = 'Optical Spectra: With Amplification D = 0 km'
        #figure_name = 'Opt_Spctr_With_Amp_Bias_Compare'
        #plot_range = [1315, 1330, -72, 10]
        #the_files.append("DUT_D_0_No_Amp.txt"); the_labels.append("No Amplification")
        #the_files.append("DUT_D_0_With_Amp_I_250.txt"); the_labels.append("$I_{SOA}$ = 250 mA")
        ##the_files.append("DUT_D_0_With_Amp_I_350.txt"); the_labels.append("$I_{SOA}$ = 350 mA")
        ##the_files.append("DUT_D_0_With_Amp_I_450.txt"); the_labels.append("$I_{SOA}$ = 450 mA")
        #the_files.append("DUT_D_0_With_Amp_I_550.txt"); the_labels.append("$I_{SOA}$ = 550 mA")

        #plot_title = 'Optical Spectra: D = 0 km with Optical Filter'
        #figure_name = 'Opt_Spctr_Coarse_D_0_Filtered'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_0_With_Amp_I_550_Clamped_Filter_Open.txt"); the_labels.append("Filter Open")
        #the_files.append("DUT_D_0_With_Amp_I_550_Clamped_Filter_Closed.txt"); the_labels.append("Filter Closed")

        #plot_title = 'Optical Spectra: D = 25 km with Optical Filter'
        #figure_name = 'Opt_Spctr_Coarse_D_25_Filtered'
        #plot_range = [1250, 1350, -72, 10]
        #the_files.append("DUT_D_25_With_Amp_I_550_Clamped_Filter_Open.txt"); the_labels.append("Filter Open")
        #the_files.append("DUT_D_25_With_Amp_I_550_Clamped_Filter_Closed.txt"); the_labels.append("Filter Closed")

        #plot_title = 'Optical Spectra: TIPS + Kamelian SOA'
        #figure_name = 'Opt_Spctr_TIPS_Kamelian_SOA'
        #plot_range = [1250, 1350, -70, 0]
        #the_files.append("TIPS_only_T_20_IDFB_172_ISOA_170_VEAM_0.txt"); the_labels.append("TIPS Device")
        #the_files.append("KSOA_plus_TIPS_Volt_Source_T_25.txt"); the_labels.append("TIPS + SOA")
        
        #plot_title = 'Optical Spectra: Kamelian SOA ASE'
        #figure_name = 'Opt_Spctr_TIPS_Kamelian_SOA_ASE'
        #plot_range = [1250, 1350, -55, -40]
        #the_files.append("KSOA_only_Output_Side_Volt_Source_T_25.txt"); the_labels.append("Output Side")
        #the_files.append("KSOA_only_Input_Side_Volt_Source_T_25.txt"); the_labels.append("Input Side")

        # Plots of Measured Spectra With Thorlabs SOA
        #directory = "Optical_Spectra/Thorlabs_SOA_Test/"
        directory = "Optical_Spectra/Filt_Test/"

        # plot over distance with / without amplifier
        Ds = [0, 25, 50]
        for distance in Ds:
            #the_files = ["TIPS_D_%(v1)dkm.txt"%{"v1":distance}, "TIPS_plus_SOA_D_%(v1)dkm.txt"%{"v1":distance}, "TIPS_plus_SOA_D_%(v1)dkm_No_Iso.txt"%{"v1":distance}]
            #the_labels = ["Device", "Device + Iso + SOA", "Device + SOA"] # OS_D_0km_No_Filt
            the_files = ["OS_D_%(v1)dkm_No_Filt.txt"%{"v1":distance}, "OS_D_%(v1)dkm_With_Filt.txt"%{"v1":distance}]
            the_labels = ["Amp", "Amp + Filter"]
            plot_range = [1315, 1330, -75, 20]
            plot_title = "Optical Spectrum D = %(v1)d km"%{"v1":distance}
            figure_name = "Opt_Spctrm_D_%(v1)dkm_Filt_Compare"%{"v1":distance}

            SpctrmPlt.multiple_optical_spectrum_plot(directory, the_files, the_labels, plot_range, plot_title, figure_name, True)

    except Exception:
        print("Error: TIPS_Pre_Amp_Rx.run_optical_spectra_plot")

def Add_XdB_to_OSA_Data(dir_name, file_name, attenuation):
    # To ensure that the SOA did not damage any equipment in the lab a 10 dB attenuator was included in the measurement of certain data
    # The aim of this function is to resave the OSA data with an added 10 dB optical power
    # file_name is the file containing the attenuated data
    # attenuation is the attenuation factor for the data set
    # R. Sheehan 26 - 2 - 2018

    try:
        HOME = os.getcwd() # Get current directory

        if os.path.isdir(dir_name): # check if dir_name is valid directory
            os.chdir(dir_name) # if dir_name is valid location move there

            if glob.glob(file_name):
                delim = '\t'
                data = Common.read_matrix(file_name, delim)
                data = Common.transpose_multi_col(data)

                # Add X dB to measured optical power
                for i in range(0, len(data[1]), 1):
                    data[1][i] = data[1][i] + attenuation

                # Write data to new file
                new_file_name = file_name.replace("_10dB_Att","")
                
                data = Common.transpose_multi_col(data)

                Common.write_matrix(new_file_name, data, delim)

                del data

                os.chdir(HOME)
            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_Pre_Amp_Rx.Add_XdB_to_OSA_Data")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_Pre_Amp_Rx.Add_XdB_to_OSA_Data")
        print("Could not locate: ",file_name)
