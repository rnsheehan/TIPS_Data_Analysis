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
import BER_Analysis
import FR_Analysis

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks' ] # plot labels

def Make_TIPS_Exp_2_plots():

    # call the functions needed to generate the plots for TIPS Exp 2
    # R. Sheehan 30 - 8 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            #temperature = 20
            
            #run_IV_plots(temperature)

            #run_LI_plots(temperature)

            #IDFB = 160
            #run_ER_1(IDFB, temperature)

            #IDFB = 170
            #run_ER_1(IDFB, temperature, True)

            #IDFB = 180
            #run_ER_1(IDFB, temperature)

            #ISOA = 160
            #run_ER_5(ISOA, temperature, True)

            #ISOA = 170
            #run_ER_5(ISOA, temperature, True)

            #ISOA = 180
            #run_ER_5(ISOA, temperature, True)

            #run_ER_data(temperature, True)

            #run_BER_plots()

            #compare_BER_BtB_plots()

            compare_BER_DR_plots()

            #compare_BER_VEAM_plots()

            #BER_min_EAM_bias_2()

            #BER_compare_Vpp()

            #run_FR_plots_2(True)

            #BERT_ED_Amplitude_Plot_2(True)

            #run_FR_plots()

            #run_FR_plots_3()

            #run_f3dB_analysis(True)

            #VEAM = '10'

            #get_S21_data_matrix(1, VEAM, False)

            #plot_S21_data_2D_errors(1, 20, VEAM, True)

            #plot_S21_data_2D(1, 20, VEAM, True)            

            #OSNR_Spectrum_Plots()

            print(os.getcwd())
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.Make_TIPS_Exp_2_plots()")
        print("Error: Could not find",DATA_HOME)

def optical_spectrum_plot(dir_name, file_name):
    # make a plot of a measured optical spectrum
    # R. Sheehan 30 - 8 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if glob.glob(file_name):

                data = Common.read_matrix(file_name)
                data = Common.transpose_multi_col(data)

                arguments = Plotting.plot_arg_single()

                arguments.loud = True
                arguments.x_label = '$\lambda$ (nm)'
                arguments.y_label = 'Spectral Power (dBm/0.01 nm)'
                arguments.plt_range = [1320, 1325, -65, -5]
                arguments.marker = 'r-'
                #arguments.crv_lab_list = labels
                #arguments.mrk_list = mark_list
                #arguments.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
                #arguments.fig_name = 'Voltage_T_20.png'

                Plotting.plot_single_curve(data[0], data[1], arguments)

                os.chdir('..')
            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.optical_spectrum_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.optical_spectrum_plot()")
        print("Error: Could not find",file_name)

def multiple_optical_spectrum_plot(dir_name, file_names, labels, plt_name = ''):
    # make a plot of a measured optical spectrum
    # R. Sheehan 30 - 8 - 2017

    try:

        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if file_names is not None:

                delim = '\t'
                hv_data = []; mark_list = []

                for i in range(0, len(file_names), 1):
                    data = Common.read_matrix(file_names[i], delim)
                    data = Common.transpose_multi_col(data)
                    hv_data.append(data); 
                    mark_list.append(Plotting.labs_lins[i%len(Plotting.labs_lins)]); 

                arguments = Plotting.plot_arg_multiple()

                arguments.loud = True
                arguments.x_label = 'Wavelength (nm)'
                arguments.y_label = 'Spectral Power (dBm/0.05 nm)'
                arguments.plt_range = [1315, 1325, -60, 0]
                arguments.crv_lab_list = labels
                arguments.mrk_list = mark_list
                #arguments.plt_title = '$V_{TEC}$ variation with DFB and SOA current at T = 20 (C)'
                arguments.fig_name = plt_name

                Plotting.plot_multiple_curves(hv_data, arguments)

                os.chdir('..')
            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.multiple_optical_spectrum_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.multiple_optical_spectrum_plot()")

def run_optical_spectrum_plots():
    # small script to run functions to generate optical spectrum plots

    dir_name = "Optical_Spectra/"
    #file_name = "Ch1_075_Ch2_075.txt"
    #file_name = "Ch1_100_Ch2_100.txt"
    #file_name = "Ch1_120_Ch2_120.txt"
            
    #file_name = "Ch1_140_Ch2_120.txt"
    #file_name = "Ch1_140.txt"
    #file_name = "Ch2_120.txt"
            
    #optical_spectrum_plot(dir_name, file_name)

    #file_names = ["Ch1_140_Ch2_120.txt", "Ch1_140.txt", "Ch2_120.txt"]
    #plt_name = 'Channel_Sum.png'
    #multiple_optical_spectrum_plot(dir_name, file_names, plt_name)

    #plt_name = 'Channel_Shift.png'
    #file_names = ["Ch1_075_Ch2_075.txt", "Ch1_100_Ch2_100.txt", "Ch1_120_Ch2_120.txt"]
    #multiple_optical_spectrum_plot(dir_name, file_names, plt_name)

    dir_name = "Optical_Spectra/Variation_With_IDFB"
    file_names = ["TIPS_1_OS_T_20_IDFB_100_ISOA_170_VEAM_00.txt", 
                    "TIPS_1_OS_T_20_IDFB_120_ISOA_170_VEAM_00.txt",
                    "TIPS_1_OS_T_20_IDFB_140_ISOA_170_VEAM_00.txt",
                    "TIPS_1_OS_T_20_IDFB_160_ISOA_170_VEAM_00.txt",
                    "TIPS_1_OS_T_20_IDFB_180_ISOA_170_VEAM_00.txt"]
    labels = ["$I_{DFB}$ = 100 (mA)", "$I_{DFB}$ = 120 (mA)", "$I_{DFB}$ = 140 (mA)", "$I_{DFB}$ = 160 (mA)", "$I_{DFB}$ = 180 (mA)"]
    plt_name = "TIPS_1_OS_vs_IDFB"
    multiple_optical_spectrum_plot(dir_name, file_names, labels, plt_name)

def IV_curve_plot(dir_name, file_name, plt_args, scale = False, loud = False):
    # plot the measured IV characteristic data for each section of the device
    # R. Sheehan 4 - 9 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())
            if loud: print(glob.glob("*.txt")

            if glob.glob(file_name):
                delim = '\t'
                data = Common.read_matrix(file_name, delim)
                data = Common.transpose_multi_col(data)

                if scale: 
                    # scale data to uA
                    for i in range(0, len(data[1]), 1):
                        data[1][i] *= 1000

                Plotting.plot_single_curve(data[0], data[1], plt_args)
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.IV_curve_plots()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.IV_curve_plots()")
        print("Error: Could not find",file_name)

def run_IV_plots(temp = 20):
    # script to run the functions needed to generate the IV curve plots

    arguments = Plotting.plot_arg_single()

    dir_name = "IV_SWP/"

    file_name = "TIPS_1_DFB_IV_T_%(v1)d_ISOA_0_VEAM_0.txt"%{"v1":temp}
    arguments.loud = False
    arguments.x_label = 'Current (mA)'
    arguments.y_label = 'Voltage (V)'
    arguments.plt_range = [0, 100, 0, 1.7]
    arguments.marker = 'r-'
    arguments.plt_title = "DFB IV Curve, T = %(v1)d C, $I_{SOA}$ = 0 mA, $V_{EAM}$ = 0 V"%{"v1":temp}
    arguments.fig_name = file_name.replace('.txt','.png')

    IV_curve_plot(dir_name, file_name, arguments)

    file_name = "TIPS_1_SOA_IV_T_%(v1)d_IDFB_0_VEAM_0.txt"%{"v1":temp}
    arguments.loud = False
    arguments.x_label = 'Current (mA)'
    arguments.y_label = 'Voltage (V)'
    arguments.plt_range = [0, 100, 0, 2.0]
    arguments.marker = 'r-'
    arguments.plt_title = "SOA IV Curve, T = %(v1)d C, $I_{DFB}$ = 0 mA, $V_{EAM}$ = 0 V"%{"v1":temp}
    arguments.fig_name = file_name.replace('.txt','.png')

    IV_curve_plot(dir_name, file_name, arguments)

    file_name = "TIPS_1_EAM_VI_T_%(v1)d_IDFB_0_ISOA_0.txt"%{"v1":temp}
    arguments.loud = False
    arguments.y_label = 'Current (mA)'
    arguments.x_label = 'Voltage (V)'
    arguments.plt_range = [0, 2, 0, 35]
    arguments.marker = 'r-'
    arguments.plt_title = "EAM VI Curve, T = %(v1)d C, $I_{DFB}$ = 0 mA, $I_{SOA}$ = 0 mA"%{"v1":temp}
    arguments.fig_name = file_name.replace('.txt','.png')

    IV_curve_plot(dir_name, file_name, arguments)

    file_name = "TIPS_1_EAM_Idark_T_%(v1)d_IDFB_0_ISOA_0.txt"%{"v1":temp}
    arguments.loud = True
    arguments.y_label = 'Current ($\mu$A)'
    arguments.x_label = 'Voltage (V)'
    arguments.plt_range = [-3, 0, -0.3, 0.1]
    arguments.marker = 'r-'
    arguments.plt_title = "EAM Dark Current, T = %(v1)d C, $I_{DFB}$ = 0 mA, $I_{SOA}$ = 0 mA"%{"v1":temp}
    #arguments.fig_name = file_name.replace('.txt','.png')   
    scale = True

    IV_curve_plot(dir_name, file_name, arguments, scale)

def LI_curve_plot(dir_name, file_str, temp, scale = False, sort_for_ISOA = True, loud = False):
    # plot the measured LI data for different currents across the SOA section
    # you can also plot the data for different temperatures by setting sort_for_ISOA = False
    # R. Sheehan 4 - 9 - 2017

    try:
        HOME = os.getcwd()
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{SOA} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        if sort_for_ISOA: the_files.append([values[2],f]) # sort according to ISOA
                        else: the_files.append([values[1],f]) # sort according to Temperature
                    del values

                # sort the file names according to I_{SOA}
                Common.sort_multi_col(the_files)               

                # import and store the data
                delim = '\t'; count = 0; 
                hv_data = []; mrk_list = []; labels = []; 
                start_val = 1 if sort_for_ISOA else 0
                for f in range(start_val, len(the_files), 1):
                    data = Common.read_matrix(the_files[f][1], delim)
                    data = Common.transpose_multi_col(data)
                    if scale: data[1] = Common.list_convert_dBm_mW(data[1])# convert dBm data to mW
                    hv_data.append(data); mrk_list.append(Plotting.labs_lins[count]); 
                    if sort_for_ISOA: labels.append( '$I_{SOA}$ = %(v1)s mA'%{ "v1":the_files[f][0] } ); # sweeping over ISOA
                    else: labels.append( 'T = %(v1)s C'%{ "v1":the_files[f][0] } ); # sweeping over temperature
                    del data
                    count += 1

                # define the arguments for the plot
                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = 'DFB Current (mA)'
                args.y_label = 'Power (mW)' if scale else 'Power (dBm)'
                args.plt_range = [0.0, 171, 0.0, 0.7] if scale else [0.0, 171, -40, 0.0]
                args.crv_lab_list = labels
                args.mrk_list = mrk_list
                #args.plt_title = 'TIPS-1 Optical Power T = %(v1)d C, $V_{EAM} = 0 V$'%{"v1":temp}
                #args.plt_title = 'TIPS-1 Optical Power $I_{SOA}$ = %(v1)d mA, $V_{EAM} = 0 V$'%{"v1":temp}                
                if sort_for_ISOA: args.fig_name = 'DFB_EAM_SOA_Optical_Power_mW_T_%(v1)d.png'%{"v1":temp} if scale else 'DFB_EAM_SOA_Optical_Power_dBm_T_%(v1)d.png'%{"v1":temp}
                else: args.fig_name = 'DFB_EAM_SOA_Optical_Power_mW_ISOA_%(v1)d.png'%{"v1":temp} if scale else 'DFB_EAM_SOA_Optical_Power_dBm_ISOA_%(v1)d.png'%{"v1":temp}

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data; del args; del the_files; 
            else:
                raise Exception
            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.LI_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.LI_curve_plot()")

def run_LI_plots(temp = 20):

    # script for plotting the LI data

    dir_name = "LI_SWP/"
    
    file_str = "TIPS*LIV*T_%(v1)d*.txt"%{"v1":temp} # sweeping over ISOA
    sort_for_ISOA = True

    #file_str = "TIPS*LIV*ISOA_%(v1)d*.txt"%{"v1":temp} # sweeping over temperature
    sort_for_ISOA = False

    #LI_curve_plot(dir_name, file_str, temp, False) # dBm scale

    LI_curve_plot(dir_name, file_str, temp, True) # mW scale

def ER_curve_plot_1(dir_name, file_str, temp, IDFB, scale = False, loud = False):
    # plot the measured optical power for different currents across the SOA section while the bias across the EAM is varied
    # and current across DFB is fixed
    # R. Sheehan 4 - 9 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{SOA} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        the_files.append([values[3],f])
                    del values

                # sort the file names according to I_{SOA}
                if len(the_files)>1:
                    Common.sort_multi_col(the_files)  
                
                count = 0
                #for f in the_files: print(count,f; count += 1          

                # import and store the data
                delim = '\t'; count = 0; 

                hv_data = []; mrk_list = []; labels = []; 
                
                for f in range(0, len(the_files), 2):                    
                    if float(the_files[f][0]) > 130:
                        data = Common.read_matrix(the_files[f][1], delim)                    
                        data = Common.transpose_multi_col(data)                 
                        if scale: data[1] = Common.list_convert_dBm_mW(data[1]) # convert dBm data to mW                    
                        hv_data.append( data ); mrk_list.append( labs[count] ); 
                        labels.append( '$I_{SOA}$ = %(v1)s mA'%{ "v1":the_files[f][0] } );
                        del data
                        count = (count + 1)%len(Plotting.labs)

                # define the arguments for the plot
                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = 'EAM Bias (V)'
                args.y_label = 'Transmitted Power (mW)' if scale else 'Transmitted Power (dBm)'
                args.plt_range = [-2.5, 0, 0.0, 0.7] if scale else [-2.5, 0, -25, 0.0]
                args.crv_lab_list = labels
                args.mrk_list = mrk_list
                args.plt_title = 'TIPS-1 Optical Power T = %(v2)d C, $I_{DFB}$ = %(v1)d mA'%{"v2":temp, "v1":IDFB}
                args.fig_name = 'DFB_EAM_SOA_Opt_Pow_IDFB_%(v1)d_mW_T_%(v2)d.png'%{"v1":IDFB, "v2":temp} if scale else 'DFB_EAM_SOA_Opt_Pow_IDFB_%(v1)d_dBm_T_%(v2)d.png'%{"v1":IDFB, "v2":temp}

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data; 
                del args; 
                del the_files; 
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")

def ER_curve_plot_2(dir_name, file_str, scale = False, loud = False):
    # plot the measured optical power difference between the I-SOA = 0 mA case and I-SOA > 0 mA as a function of EAM bias
    # R. Sheehan 4 - 9 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{SOA} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        the_files.append([values[3],f])
                    del values

                # sort the file names according to I_{SOA}
                Common.sort_multi_col(the_files)      

                # import and store the data
                delim = '\t'; count = 1; 

                data_zero = Common.read_matrix(the_files[0][1], delim)
                data_zero = Common.transpose_multi_col(data_zero)
                data_zero[1] = Common.list_convert_dBm_mW(data_zero[1]) # convert dBm data to mW

                hv_data = []; mrk_list = []; labels = []; 
                for f in range(1, len(the_files)-1, 1): 
                    data = Common.read_matrix(the_files[f][1], delim)
                    data = Common.transpose_multi_col(data)
                    data[1] = Common.list_convert_dBm_mW(data[1]) # convert dBm data to mW
                    # compute difference between power for I-SOA = 0 mA case and I-SOA > 0 mA 
                    data[1] = Common.list_diff(data[1], data_zero[1])
                    if scale:data[1] = Common.list_convert_mW_dBm(data[1]) # convert dBm data to mW
                    hv_data.append(data); mrk_list.append(labs[count]); 
                    labels.append( '$I_{SOA}$ = %(v1)s mA'%{ "v1":the_files[f][0] } );
                    del data
                    count += 1

                # define the arguments for the plot
                args = Plotting.plot_arg_multiple()

                args.loud = True
                args.x_label = 'EAM Bias (V)'
                args.y_label = 'ER (dB)' if scale else 'ER (mW)'
                args.plt_range = [-2, 0, -40, 0] if scale else [-2, 0, 0.0, 0.61]
                args.crv_lab_list = labels
                args.mrk_list = mrk_list
                args.plt_title = 'TIPS-1 ER rel. $I_{SOA}$ = 0 mA, T = 20 C, $I_{DFB}$ = 170 mA'
                args.fig_name = 'DFB_EAM_SOA_ER_dBm.png' if scale else 'DFB_EAM_SOA_ER_mW.png'

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data; 
                del args; 
                del the_files; 
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot_2()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot_2()")

def ER_curve_data(dir_name, file_str, temp, I_DFB, Veam, Vpp, er_data = True, loud = False):
    # if er_data == True
        # use this function to extract the extinction ratio data
        # assuming EAM will operate at V = -0.5 V with Vpp = +1 V
        # what is the optical power difference as a function of I_SOA? 
        # how does this vary with I_DFB?
    # else
        # use this function to return the optical power at a given value of Veam
        # want to see if there is a local maximum associated with value of ISOA
        # how does this vary with I_DFB?
    
    # R. Sheehan 4 - 9 - 2017
    # updated 17 - 10 - 2017

    try:
        HOME = os.getcwd()
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{SOA} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        the_files.append([values[3],f])
                    del values

                # sort the file names according to I_{SOA}
                Common.sort_multi_col(the_files)  
                
                # import the necessary interpolation object 
                from scipy.interpolate import interp1d          

                # import and store the data
                delim = '\t';
                V_high = Veam+0.5*Vpp; V_low = Veam-0.5*Vpp;
                Isoa = []; computed_data = []
                for f in range(0, len(the_files), 1): 
                    data = Common.read_matrix(the_files[f][1], delim)
                    data = Common.transpose_multi_col(data)
                    #if scale: data[1] = Common.list_convert_dBm_mW(data[1]) # convert dBm data to mW, don't need this option
                    
                    # make an interpolating object over the data set
                    fobj = interp1d(data[0], data[1], 'quadratic')

                    if er_data:
                        # compute the extinction ratio data                                            
                        P_high = float( fobj(V_high) ); P_low = float( fobj(V_low) );                     
                        #delta_P = Common.convert_PmW_PdBm( (P_high - P_low) ) if scale else (P_high - P_low)
                        delta_P = (P_high - P_low)
                    
                        # Save the data
                        if loud: print("I_{SOA} =",the_files[f][0],", ER =",delta_P
                        computed_data.append(delta_P)
                    else:
                        # save the response data at the value of Veam
                        resp_val = float( fobj(Veam) )

                        # Save the data
                        if loud: print("I_{SOA} =",the_files[f][0],", Response =",resp_val

                        computed_data.append(resp_val)

                    # Save ISOA values for file
                    Isoa.append( float( the_files[f][0] ) ); 
                    
                    del data; del fobj; 

                # write the ER data to a file
                if er_data:
                    wr_file = "ER_Data_I_DFB_%(v1)d_T_%(v2)d.txt"%{"v1":I_DFB, "v2":temp}
                    header = "ISOA (mA), ER (dB)"
                else:
                    wr_file = "ER_Val_Data_I_DFB_%(v1)d_T_%(v2)d.txt"%{"v1":I_DFB, "v2":temp}
                    header = "ISOA (mA), ER Value (dBm)"

                Common.write_two_columns(wr_file, header, Isoa, computed_data, "w")

                del the_files; 
            else:
                raise Exception
            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")

def ER_curve_plot_3(dir_name, file_str, I_DFB, Veam, Vpp, scale = False, loud = False):
    # assuming EAM will operate at V = -0.5 V with Vpp = +1 V
    # what is the optical power difference as a function of I_SOA? 
    # R. Sheehan 4 - 9 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{SOA} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        the_files.append([values[3],f])
                    del values

                # sort the file names according to I_{SOA}
                Common.sort_multi_col(the_files)  
                
                # import the necessary interpolation object 
                from scipy.interpolate import interp1d          

                # import and store the data
                delim = '\t'; count = 0; 
                V_high = Veam+0.5*Vpp; V_low = Veam-0.5*Vpp;
                Isoa = []; ER = []
                for f in range(0, len(the_files), 1): 
                    data = Common.read_matrix(the_files[f][1], delim)
                    data = Common.transpose_multi_col(data)
                    data[1] = Common.list_convert_dBm_mW(data[1])# convert dBm data to mW
                    
                    # make an interpolating object over the data set
                    fobj = interp1d(data[0], data[1], 'quadratic')                    
                    P_high = float(fobj(V_high)); P_low = float(fobj(V_low));                     
                    delta_P = Common.convert_PmW_PdBm( (P_high - P_low) ) if scale else (P_high - P_low)
                    
                    print("I_{SOA} =",the_files[f][0],", ER =",delta_P
                    Isoa.append(float(the_files[f][0])); ER.append(delta_P)
                    
                    del data
                    count += 1

                # define the arguments for the plot
                args = Plotting.plot_arg_single()

                args.loud = True
                args.x_label = '$I_{SOA}$ mA'
                args.y_label = 'ER (dBm)' if scale else 'ER (mW)'
                args.plt_range = [0, 171, -25, 0.61] if scale else [0, 171, 0, 0.6]
                args.curve_label = '$I_{DFB}$ = %(v1)d mA'%{"v1":I_DFB}
                args.plt_title = 'TIPS-1 ER T = 20 C, $V_{EAM}$ = %(v1)0.1f V, $V_{pp}$ = %(v2)0.2f'%{"v1":Veam, "v2":Vpp}
                args.fig_name = 'DFB_EAM_SOA_ER_dBm.png' if scale else 'DFB_EAM_SOA_ER_mW.png'

                Plotting.plot_single_curve(Isoa, ER, args)

                del the_files; 
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")

def ER_curve_plot_4(dir_name, file_str, temp, Veam, Vpp, er_data = True, loud = False):
    # if er_data == True
        # use this function to extract the extinction ratio data
        # assuming EAM will operate at V = -0.5 V with Vpp = +1 V
        # what is the optical power difference as a function of I_SOA? 
        # how does this vary with I_DFB?
    # else
        # use this function to return the optical power at a given value of Veam
        # want to see if there is a local maximum associated with value of ISOA
        # how does this vary with I_DFB?

    # R. Sheehan 4 - 9 - 2017
    # updated 17 - 10 - 2017

    try:
        HOME = os.getcwd()
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # read and store the ER data for the difference DFB biases
                hv_data = []; marks = []; labels = []; 
                delim = ','
                count = 0
                for f in files:
                    values = Common.extract_values_from_string(f)
                    data = Common.read_matrix(f, delim, True)
                    data = Common.transpose_multi_col(data)
                    hv_data.append(data); marks.append(labs[count]); labels.append('$I_{DFB}$ = %(v1)s mA'%{"v1":values[0]})
                    count += 1

                # define the arguments for the plot
                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = '$I_{SOA}$ (mA)'
                
                #args.plt_range = [119, 181, 0, 0.71]
                #args.plt_range = [119, 181, 0.0, 22.5]
                #
                args.crv_lab_list = labels
                args.mrk_list = marks
                if er_data:
                    args.plt_title = 'TIPS-1 ER T = %(v3)d C, $V_{EAM}$ = %(v1)0.2f V, $V_{pp}$ = %(v2)0.2f V'%{"v1":Veam, "v2":Vpp, "v3":temp}
                    args.fig_name = 'DFB_EAM_SOA_ER_VEAM_%(v1)0.1f_Vpp_%(v2)0.1f_dBm_T_%(v3)d.png'%{"v1":Veam, "v2":Vpp, "v3":temp}
                    args.plt_range = [119, 181, 0.0, 23]
                    args.y_label = 'ER (dB)'
                else:
                    args.plt_title = 'TIPS-1 Response T = %(v3)d C, $V_{EAM}$ = %(v1)0.2f V'%{"v1":Veam, "v2":Vpp, "v3":temp}
                    args.fig_name = 'DFB_EAM_SOA_Response_VEAM_%(v1)0.2f_dBm_T_%(v3)d.png'%{"v1":Veam, "v2":Vpp, "v3":temp}
                    args.plt_range = [119, 181, -8, -1]
                    args.y_label = 'Response (dBm)'

                Plotting.plot_multiple_curves(hv_data, args)
            else:
                raise Exception
            #os.chdir('..')
            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")

def ER_curve_plot_5(dir_name, file_str, temp, ISOA, scale = False, loud = False):
    # plot the measured optical power for different currents across the DFB section while the bias across the EAM is varied
    # and current across SOA is fixed
    # R. Sheehan 4 - 9 - 2017

    try:
        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            if loud: print(os.getcwd())

            files = glob.glob(file_str)

            if files:
                # store the file-names with sorted I_{DFB} values
                the_files = []
                for f in files:
                    values = Common.extract_values_from_string(f)
                    if values:
                        the_files.append([values[2],f])
                    del values

                # sort the file names according to I_{DFB}
                if len(the_files)>1:
                    Common.sort_multi_col(the_files)  
                
                count = 0
                #for f in the_files: print(count,f; count += 1          

                # import and store the data
                delim = '\t'; count = 0; 

                hv_data = []; mrk_list = []; labels = []; 
                
                for f in range(0, len(the_files), 2):                    
                    if float(the_files[f][0]) > 130:
                        data = Common.read_matrix(the_files[f][1], delim)                    
                        data = Common.transpose_multi_col(data)                 
                        if scale: data[1] = Common.list_convert_dBm_mW(data[1]) # convert dBm data to mW                    
                        hv_data.append( data ); mrk_list.append( labs[count] ); 
                        labels.append( '$I_{DFB}$ = %(v1)s mA'%{ "v1":the_files[f][0] } );
                        del data
                        count = (count + 1)%len(Plotting.labs)

                # define the arguments for the plot
                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = 'EAM Bias (V)'
                args.y_label = 'Transmitted Power (mW)' if scale else 'Transmitted Power (dBm)'
                args.plt_range = [-2.5, 0, 0.0, 0.7] if scale else [-2.5, 0, -25, 0.0]
                args.crv_lab_list = labels
                args.mrk_list = mrk_list
                #args.plt_title = 'TIPS-1 Optical Power T = %(v2)d C, $I_{SOA}$ = %(v1)d mA'%{"v2":temp, "v1":ISOA}
                args.fig_name = 'DFB_EAM_SOA_Opt_Pow_ISOA_%(v1)d_mW_T_%(v2)d.png'%{"v1":ISOA, "v2":temp} if scale else 'DFB_EAM_SOA_Opt_Pow_ISOA_%(v1)d_dBm_T_%(v2)d.png'%{"v1":ISOA, "v2":temp}

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data; 
                del args; 
                del the_files; 
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")
        print("Error: Could not find",dir_name)
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.ER_curve_plot()")

def run_ER_1(IDFB = 180, temp = 20, loud = False):
    # plot the optical power data as a function of EAM bias for a given DFB bias
    # no need to plot the ER-2 curve as it adds nothing to the understanding
    dir_name = "ER_SWP/"
    
    file_str = "TIPS*ER*T_%(v2)d*IDFB_%(v1)d*.txt"%{"v2":temp, "v1":IDFB}    

    scale = True; 
    #ER_curve_plot_1(dir_name, file_str, temp, IDFB, scale, loud) # mW scale

    scale = False;
    ER_curve_plot_1(dir_name, file_str, temp, IDFB, scale, loud) # dBm scale

def run_ER_5(ISOA = 170, temp = 20, loud = False):
    # plot the optical power data as a function of EAM bias for a given SOA bias
    # no need to plot the ER-2 curve as it adds nothing to the understanding
    # There seems to be no change in ER with varying SOA bias so what does ER look like
    # as IDFB changes? 
    dir_name = "ER_SWP/"
    
    file_str = "TIPS*ER*T_%(v2)d*ISOA_%(v1)d*.txt"%{"v2":temp, "v1":ISOA}    

    #scale = True; 
    #ER_curve_plot_1(dir_name, file_str, temp, IDFB, scale, loud) # mW scale

    scale = False;
    ER_curve_plot_5(dir_name, file_str, temp, ISOA, scale, loud) # dBm scale

def run_ER_data(temp = 20, loud = False):
    # generate the data needed to get ER plot

    dir_name = "ER_SWP/"

    Vpp = 1.0
    
    Veam = -0.75
    
    I_DFB = [160, 165, 170, 175, 180]    
    
    er_data = False
    for ii in I_DFB:
        print(os.getcwd())

        file_str = "TIPS*ER*T_%(v2)d*IDFB_%(v1)d*.txt"%{"v2":temp,"v1":ii}

        ER_curve_data(dir_name, file_str, temp, ii, Veam, Vpp, er_data, loud)

        if loud: print(os.getcwd())

    if er_data:
        file_str = "ER_Data_I_DFB_*_T_%(v1)d.txt"%{"v1":temp}
    else:
        file_str = "ER_Val_Data_I_DFB_*_T_%(v1)d.txt"%{"v1":temp}

    ER_curve_plot_4(dir_name, file_str, temp, Veam, Vpp, er_data, loud)

def run_BER_plots():
    # make plots of the BER data

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            #file = 'BtB_BER_1_22_9_2017.csv'
            #file = 'BtB_BER_1_5_10_2017.csv'
            #file = 'BtB_BER_1_10_10_2017.csv'
            #file = 'BtB_BER_1_11_10_2017.csv'
            #file = 'BtB_BER_2_11_10_2017.csv'
            #file = 'BtB_BER_3_11_10_2017.csv'

            # Compare file = 'BtB_BER_1_5_10_2017.csv' and file = 'BtB_BER_1_10_10_2017.csv'
            # Compare file = 'BtB_BER_1_10_10_2017.csv' and file = 'BtB_BER_2_11_10_2017.csv' and file = 'BtB_BER_2_11_10_2017.csv'

            # Data Feb 2018
            #file = 'BER_D_0_DR_10_wrfps.csv'
            #file = 'BER_D_0_DR_12_wrfps.csv'
            #file = 'BER_D_20_DR_10_wrfps.csv'
            #file = 'BER_D_20_DR_12_wrfps.csv'
            #file = 'BER_D_25_DR_10_wrfps.csv'
            file = 'BER_D_25_DR_12_wrfps.csv'

            #files = ['BER_D_0_DR_10_wrfps.csv', 'BER_D_0_DR_12_wrfps.csv', 'BER_D_20_DR_10_wrfps.csv'
            #         'BER_D_20_DR_12_wrfps.csv', 'BER_D_25_DR_10_wrfps.csv', 'BER_D_25_DR_12_wrfps.csv']

            ber_data = BER_Analysis.read_BER_data(file)

            #BER_Analysis.plot_raw_BER_data(ber_data, True)

            BER_Analysis.plot_formatted_BER_data(ber_data, True)

            #BER_Analysis.compute_Rx_sensitivity(ber_data, 1.0e-9, True)

            #BER_Analysis.compute_Rx_sensitivity(ber_data, 1.0e-3, True)

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.run_BER_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.run_BER_plots()")
        print("Investigate error\n")

def compare_BER_BtB_plots():
    # make plots of the BER data
    # compare BER data for different parameters

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            # Compare post-detection amplification
            #file_1 = 'BtB_BER_1_5_10_2017.csv' # BER Data No Amplification after detection
            #file_2 = 'BtB_BER_1_10_10_2017.csv' # BER Data With Amplification after detection
            #labels = ['No Amp.', 'With Amp.']
            #ber_data_1 = BER_Analysis.read_BER_data(file_1)
            #ber_data_2 = BER_Analysis.read_BER_data(file_2)
            #ber_list = [ber_data_1, ber_data_2]
            
            # Compare data rates
            file_1 = 'BtB_BER_1_10_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps
            file_2 = 'BtB_BER_1_11_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps
            file_3 = 'BtB_BER_2_11_10_2017.csv' # BER Data With Amplification after detection DR = 15 Gbps
            
            labels = ['10 (Gbps)', '12.5 (Gbps)', '15 (Gbps)']          
            
            ber_data_1 = BER_Analysis.read_BER_data(file_1)
            ber_data_2 = BER_Analysis.read_BER_data(file_2)
            ber_data_3 = BER_Analysis.read_BER_data(file_3)
            ber_list = [ber_data_1, ber_data_2, ber_data_3]

            fig_name = 'BER_BtB_DR_Comparison'
            plot_title = 'BER BtB format'            

            BER_Analysis.plot_multiple_raw_BER_data(ber_list, labels, fig_name, plot_title, False)

            fig_name = 'BER_BtB_DR_fmtd_Comparison'
            plot_title = 'BER BtB format'

            BER_Analysis.plot_multiple_formatted_BER_data(ber_list, labels, fig_name, plot_title, True)
            
            del ber_list; del labels; 
            del ber_data_1; del ber_data_2; del ber_data_3; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_BtB_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_BtB_plots()")
        print("Investigate error\n")

def compare_BER_DR_plots():
    # make plots of the BER data
    # compare BER data for different parameters

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            # Compare data rates
            #file_1 = 'BtB_BER_1_10_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 0 km
            #file_2 = 'BER_1_D_20_DR_10_12_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 20 km
            #file_3 = 'BER_1_D_25_DR_10_12_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 25 km

            #file_1 = 'BtB_BER_1_11_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 0 km
            #file_2 = 'BER_1_D_20_DR_12_12_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 20 km
            #file_3 = 'BER_1_D_25_DR_12_12_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 25 km
            
            labels = ['BtB', '20 (km)', '25 (km)']            

            # New Measured Data with RF Phase Shifter Included
            # Compare Distances for given data rate
            #file_1 = 'BER_D_0_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 0 km
            
            #file_1 = 'BtB_BER_1_10_10_2017_sub.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 0 km
            #file_2 = 'BER_D_20_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 20 km
            #file_3 = 'BER_D_25_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 25 km

            #file_1 = 'BER_D_0_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 0 km
            
            file_1 = 'BtB_BER_1_11_10_2017_sub.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 0 km
            file_2 = 'BER_D_20_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 20 km
            file_3 = 'BER_D_25_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 25 km

            # Compare Old data with New

            # BtB DR = 10 Gbps
            #file_1 = 'BtB_BER_1_10_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 0 km
            #file_2 = 'BER_D_0_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 0 km

            # D = 20 km, DR = 10 Gbps
            #file_1 = 'BER_1_D_20_DR_10_12_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 20 km
            #file_2 = 'BER_D_20_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 20 km

            # D = 25 km, DR = 10 Gbps
            #file_1 = 'BER_1_D_25_DR_10_12_10_2017.csv' # BER Data With Amplification after detection DR = 10 Gbps, Distance = 25 km
            #file_2 = 'BER_D_25_DR_10_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 10 Gbps, Distance = 25 km

            # BtB, DR = 12.5 Gbps
            #file_1 = 'BtB_BER_1_11_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 0 km
            #file_2 = 'BER_D_0_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 0 km

            # D = 20 km, DR = 12.5 Gbps
            #file_1 = 'BER_1_D_20_DR_12_12_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 20 km
            #file_2 = 'BER_D_20_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 20 km

            # D = 25 km, DR = 12.5 Gbps
            #file_1 = 'BER_1_D_25_DR_12_12_10_2017.csv' # BER Data With Amplification after detection DR = 12.5 Gbps, Distance = 25 km
            #file_2 = 'BER_D_25_DR_12_wrfps.csv' # BER Data With Amp. after detection and RF phase-shifter DR = 12.5 Gbps, Distance = 25 km

            #labels = ['BtB Old', 'BtB New']            
            
            ber_data_1 = BER_Analysis.read_BER_data(file_1)
            ber_data_2 = BER_Analysis.read_BER_data(file_2)
            ber_data_3 = BER_Analysis.read_BER_data(file_3)
            ber_list = [ber_data_1, ber_data_2, ber_data_3]  
            #ber_list = [ber_data_1, ber_data_2]  
            
            fig_name = 'BER_DR_12_Comparison_wrfps_comb'

            #plot_title = 'BER Over Optical Fibre DR = 10 Gbps'
            plot_title = ''
            #BER_Analysis.plot_multiple_raw_BER_data(ber_list, labels, fig_name, plot_title, True)

            fig_name = 'BER_DR_12_Comparison_fmtd_wrfps_comb_sub'
            BER_Analysis.plot_multiple_formatted_BER_data(ber_list, labels, fig_name, plot_title, True)
            
            del ber_list; del labels; 
            del ber_data_1; del ber_data_2; del ber_data_3; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_DR_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_DR_plots()")
        print("Investigate error\n")

def compare_BER_VEAM_plots():
    # make plots of the BER data
    # compare BER data for different parameters

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            # Compare data rates
            
            file_1 = 'BER_1_D_25_DR_10_12_10_2017.csv' # BER Data With Amp. after det. DR = 10 Gbps, D. = 25 km, ISOA = 170, IDFB = 172, VEAM = -0.75
            file_2 = 'BER_2_D_25_DR_10_12_10_2017.csv' # BER Data With Amp. after det. DR = 10 Gbps, D. = 25 km, ISOA = 170, IDFB = 180, VEAM = -0.75
            file_3 = 'BER_3_D_25_DR_10_12_10_2017.csv' # BER Data With Amp. after det. DR = 10 Gbps, D. = 25 km, ISOA = 170, IDFB = 180, VEAM = -0.7
            file_4 = 'BER_4_D_25_DR_10_12_10_2017.csv' # BER Data With Amp. after det. DR = 10 Gbps, D. = 25 km, ISOA = 170, IDFB = 180, VEAM = -0.5
            
            labels = ['$I_{DFB}$ = 172 mA, $V_{EAM}$ = -0.75 V', 
                      '$I_{DFB}$ = 180 mA, $V_{EAM}$ = -0.75 V', 
                      '$I_{DFB}$ = 180 mA, $V_{EAM}$ = -0.7 V', 
                      '$I_{DFB}$ = 180 mA, $V_{EAM}$ = -0.5 V']
            ber_data_1 = BER_Analysis.read_BER_data(file_1)
            ber_data_2 = BER_Analysis.read_BER_data(file_2)
            ber_data_3 = BER_Analysis.read_BER_data(file_3)
            ber_data_4 = BER_Analysis.read_BER_data(file_4)
            ber_list = [ber_data_1, ber_data_2, ber_data_3, ber_data_4]
            
            fig_name = 'BER_DR_10_Dist_Compar_VEAM'

            plot_title = 'BER Over 25 km SMF DR = 10 Gbps, $I_{SOA}$ = 170 mA'
            BER_Analysis.plot_multiple_raw_BER_data(ber_list, labels, fig_name, plot_title, True)

            fig_name = 'BER_DR_10_Dist_Compar_VEAM_fmtd'
            BER_Analysis.plot_multiple_formatted_BER_data(ber_list, labels, fig_name, plot_title, True)
            
            del ber_list; del labels; 
            del ber_data_1; del ber_data_2; del ber_data_3; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_DR_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.compare_BER_DR_plots()")
        print("Investigate error\n")

def BER_min_EAM_bias():

    # make a plot of the measured BER versus EAM bias
    # optical power into detector was a constant
    # parameters for the measurement were fixed
    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            VEAM = [-0.6, -0.65, -0.7, -0.75, -0.8, -0.85]

            PRx = [-12.709, -12.638, -12.418] # received power for each measurement

            BER1 = [2.998E-05, 9.007E-06, 2.837E-06, 1.556E-06, 3.215E-06, 1.07E-05]

            BER2 = [2.419E-05, 6.702E-06, 1.887E-06, 1.293E-06, 2.955E-06, 8.832E-06]

            BER3 = [1.900E-05, 4.712E-06, 1.082E-06, 6.133E-07, 1.491E-06, 5.576E-06]

            oldstdout = sys.stdout

            filename = "BER_vs_VEAM_Quad_Fit_Results.txt"
            sys.stdout = open(filename, "w")

            print("Quadratic Fit Results to BER versus VEAM data"

            for i in range(0, len(BER1), 1): BER1[i] = BER1[i]*1.0E+6
            Common.quadratic_fit( np.asarray(VEAM), np.asarray(BER1), [1.0, 1.0, 1.0])

            for i in range(0, len(BER2), 1): BER2[i] = BER2[i]*1.0E+6
            Common.quadratic_fit( np.asarray(VEAM), np.asarray(BER2), [1.0, 1.0, 1.0])

            for i in range(0, len(BER3), 1): BER3[i] = BER3[i]*1.0E+6
            Common.quadratic_fit( np.asarray(VEAM), np.asarray(BER3), [1.0, 1.0, 1.0])

            sys.stdout = oldstdout

            hv_data = []; marks = []; labels = [];
            indx = 0
            hv_data.append([VEAM, BER1]); marks.append(Plotting.labs[indx]); labels.append('$P_{Rx}$ = %(v1)0.2f (dBm)'%{"v1":PRx[indx]})

            indx = 1
            hv_data.append([VEAM, BER2]); marks.append(Plotting.labs[indx]); labels.append('$P_{Rx}$ = %(v1)0.2f (dBm)'%{"v1":PRx[indx]})

            indx = 2
            hv_data.append([VEAM, BER3]); marks.append(Plotting.labs[indx]); labels.append('$P_{Rx}$ = %(v1)0.2f (dBm)'%{"v1":PRx[indx]})

            args = Plotting.plot_arg_multiple()

            args.crv_lab_list = labels
            args.mrk_list = marks
            args.loud = True
            args.y_label = 'BER * $10^{-6}$'
            args.x_label = '$V_{EAM}$ (V)'
            args.plt_range = [-0.86, -0.59, 0, 31]
            args.plt_title = 'BER is minimal for $V_{EAM}$ = -0.75 V'
            args.fig_name = 'BER_versus_VEAM'

            Plotting.plot_multiple_curves(hv_data, args)

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Investigate error\n")

def BER_min_EAM_bias_2():

    # make a plot of the measured BER versus EAM bias
    # optical power into detector was a constant
    # parameters for the measurement were fixed
    # R. Sheehan 5 - 10 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            VEAM = [-0.6, -0.65, -0.7, -0.75, -0.8, -0.85]

            PRx = [-12.698, -12.257] # received power for each measurement

            BER1 = [5.828E-04, 2.419E-04, 7.397E-05, 3.135E-05, 2.868E-05, 7.647E-05]

            BER2 = [3.211E-04, 1.116E-04, 3.323E-05, 1.266E-05, 1.527E-05, 4.266E-05]

            oldstdout = sys.stdout

            filename = "BER_vs_VEAM_Quad_Fit_Results_2.txt"
            sys.stdout = open(filename, "w")

            print("Quadratic Fit Results to BER versus VEAM data"

            for i in range(0, len(BER1), 1): BER1[i] = BER1[i]*1.0E+4
            Common.quadratic_fit( np.asarray(VEAM), np.asarray(BER1), [1.0, 1.0, 1.0])

            for i in range(0, len(BER2), 1): BER2[i] = BER2[i]*1.0E+4
            Common.quadratic_fit( np.asarray(VEAM), np.asarray(BER2), [1.0, 1.0, 1.0])

            sys.stdout = oldstdout

            hv_data = []; marks = []; labels = [];
            indx = 0
            hv_data.append([VEAM, BER1]); marks.append(Plotting.labs[indx]); labels.append('$P_{Rx}$ = %(v1)0.2f (dBm)'%{"v1":PRx[indx]})

            indx = 1
            hv_data.append([VEAM, BER2]); marks.append(Plotting.labs[indx]); labels.append('$P_{Rx}$ = %(v1)0.2f (dBm)'%{"v1":PRx[indx]})

            args = Plotting.plot_arg_multiple()

            args.crv_lab_list = labels
            args.mrk_list = marks
            args.loud = True
            args.y_label = 'BER * $10^{-4}$'
            args.x_label = '$V_{EAM}$ (V)'
            args.plt_range = [-0.86, -0.59, 0, 6]
            args.plt_title = 'BER is minimal for $V_{EAM}$ = -0.75 V'
            args.fig_name = 'BER_versus_VEAM_2'

            Plotting.plot_multiple_curves(hv_data, args)

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Investigate error\n")

def BER_compare_Vpp():

    # plot data comparing the operation of the device at different Vpp
    # it turns out that you minimise BER when operating with A = 16 dB and Vppg = 370 mV
    # compared to A = 13 dB and Vppg = 200 mV, even though the Vpp are quite similar in each case
    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "BER_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            # A = 13 dB, Vppg = 200 mV, Vpp = 0.97 V, Veam = -0.7
            Prx1 = [-6.382, -6.625, -7.124]
            BER1 = [8.000E-11, 1.183E-10, 2.700E-10]

            # A = 13 dB, Vppg = 200 mV, Vpp = 0.97 V, Veam = -0.75
            Prx11 = [-6.622, -6.904, -7.201, -7.527, -7.851, -8.102, -8.428, -8.732, -9.015, -9.325]
            BER11 = [1.100E-10, 1.250E-10, 3.233E-10, 5.850E-10, 1.115E-09, 1.945E-09, 3.815E-09, 7.577E-09, 1.360E-08, 2.612E-08]

            # A = 13 dB, Vppg = 200 mV, Vpp = 0.97 V, Veam = -0.7
            Prx111 = [-6.339, -6.605, -6.900, -7.194, -7.528, -7.805, -8.127, -8.426, -8.786, -9.015, -9.344]
            BER111 = [4.000E-11, 6.000E-11, 8.500E-11, 1.517E-10, 3.767E-10, 8.583E-10, 1.298E-09, 2.498E-09, 5.993E-09, 1.089E-08, 3.153E-08]

            # A = 16dB, Vppg = 370 mV, Vpp = 0.95 V, Veam = -0.7
            Prx2 = [-9.345, -9.770, -10.515]
            BER2 = [1.500E-11, 5.500E-11, 1.055E-09]

            # A = 16dB, Vppg = 370 mV, Vpp = 0.95 V, Veam = -0.75
            Prx22 = [-9.641, -9.924, -10.239, -10.569, -10.836, -11.131, -11.447]
            BER22 = [6.333E-11, 1.800E-10, 4.417E-10, 1.383E-09, 3.417E-09, 1.001E-08, 2.926E-08]

            # make a plot of the data
            hv_data = []; marks = []; labels = []; 

            #hv_data.append([Prx111, BER111]); marks.append(Plotting.labs_dashed[1]);
            hv_data.append([Prx1, BER1]); marks.append(Plotting.labs_dashed[1]);
            hv_data.append([Prx11, BER11]); marks.append(Plotting.labs[1]); 
            #labels.append('A = 13 dB, Vppg = 200 mV, Vpp = 0.97 V')
            #labels.append('$V_{EAM}$ = -0.7 V, $V_{pp}$ = 0.97 V')
            #labels.append('')
            labels.append('')
            labels.append('$V_{pp}$ = 0.97 V')

            hv_data.append([Prx2, BER2]); marks.append(Plotting.labs_dashed[3]);
            hv_data.append([Prx22, BER22]); marks.append(Plotting.labs[3]); 
            #labels.append('A = 16 dB, Vppg = 370 mV, Vpp = 0.95 V')
            #labels.append('$V_{EAM}$ = -0.7 V, $V_{pp}$ = 0.95 V')
            labels.append('')
            labels.append('$V_{pp}$ = 0.95 V')

            args = Plotting.plot_arg_multiple()

            args.loud = True
            args.crv_lab_list = labels
            args.mrk_list = marks
            args.x_label = '$P_{Rx}$ (dBm)'
            args.y_label = 'BER'
            args.plt_range = [-12, -6, 1e-11, 5e-8]
            args.log_y = True  
            args.plt_title = 'BER comparison for different $V_{pp}$, $V_{EAM}$ = -0.75 V'
            args.fig_name = 'BER_Vpp_comparison'          

            Plotting.plot_multiple_curves(hv_data, args)


            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.BER_min_EAM_bias()")
        print("Investigate error\n")

def run_FR_plots():

    # plot the FR data in a single file only

    try:
        HOME = os.getcwd()

        #DATA_HOME = "FR/Reg_Scan_T_20/"
        #DATA_HOME = "FR/Reg_Scan_T_25/"
        #DATA_HOME = "FR/Reg_Scan_T_30/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_25/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_25/"
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            #files = glob.glob("*.s2p")
            files  = glob.glob("TIPS_1_EAM_FR_T_20_IDFB_160_ISOA_167_VEAM_05.s2p")

            for f in files:
                print(f
                data = FR_Analysis.read_s2p_file(f)

                s_param = 2
                #FR_Analysis.plot_s2p_data(data, s_param, True)

                s_param = 3
                FR_Analysis.plot_s2p_data(data, s_param, False)

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.run_FR_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.run_FR_plots()")
        print("Investigate error\n")

def run_FR_plots_2(loud = False):

    # plot the measured S21 data at multiple biases

    try:
        HOME = os.getcwd()

        #DATA_HOME = "FR/Reg_Scan_T_20/"
        #DATA_HOME = "FR/Reg_Scan_T_25/"
        DATA_HOME = "FR/Reg_Scan_T_30/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_20/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_25/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            files = glob.glob("*IDFB_170*ISOA_170*.s2p")

            if files:
                T = 0.0; IDFB = 0.0; ISOA = 0.0; VEAM = 0.0; name = ""
                hv_data = []; markers = []; labels = []; 
                s_param = 3

                count = 0
                for f in files:
                    print(f

                    vals = Common.extract_values_from_string(f)

                    VEAM = float(vals[4].replace(".",""))/10.0;
                
                    if count == 0:
                        T = vals[1]; IDFB = vals[2]; ISOA = vals[3]; 
                        name = f.replace("_VEAM_%(v1)ss2p"%{"v1":vals[4]},"")
                        print(name)

                    if VEAM < 1.5:
                        labels.append('$V_{EAM}$ = -%(v1)0.1f'%{ "v1":VEAM }) 
               
                        markers.append( Plotting.labs_lins[count] )               

                        s2pdata = FR_Analysis.read_s2p_file(f)

                        hv_data.append([ s2pdata[1], s2pdata[s_param] ]);
                
                        del s2pdata 

                    count = (count + 1)%len(Plotting.labs)

                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.crv_lab_list = labels
                args.mrk_list = markers
                args.x_label = 'Frequency (GHz)'
            
                if s_param == 2:args.y_label = '$S_{11}$ (dB)'
                elif s_param == 3: args.y_label = '$S_{21}$ (dB)'
                elif s_param == 4: args.y_label = '$S_{12}$ (dB)'
                elif s_param == 5: args.y_label = '$S_{22}$ (dB)'
                else: args.y_label = '$S_{12}$ (dB)'
            
                args.plt_range = [1, 15, -40, -10]
                args.plt_title = "T = %(v1)s C, $I_{DFB}$ = %(v2)s mA, $I_{SOA}$ = %(v3)s mA"%{"v1":T, "v2":IDFB, "v3":ISOA}
            
                args.fig_name = name
                if s_param == 2:args.fig_name += "_S11"
                elif s_param == 3: args.fig_name += "_S21"
                elif s_param == 4: args.fig_name += "_S12"
                elif s_param == 5: args.fig_name += "_S22"
                else: args.fig_name += "_S21"

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data
                del labels
                del markers

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.run_FR_plots_2()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.run_FR_plots_2()")
        print("Investigate error\n")

def FR_plot(dir_name, IDFB, ISOA, s_param, loud = False):

    # plot the measured S21 data at multiple biases

    try:
        HOME = os.getcwd()

        if os.path.isdir(dir_name):
            os.chdir(dir_name)

            files = glob.glob("*IDFB_%(v1)d*ISOA_%(v2)d*.s2p"%{"v1":IDFB,"v2":ISOA})

            if files:
                T = 0.0; VEAM = 0.0; name = ""
                hv_data = []; markers = []; labels = []; 

                count = 0
                #for f in files:
                for i in range(0, len(files), 1):
                    #print(f

                    vals = Common.extract_values_from_string(files[i])

                    VEAM = float(vals[4].replace(".",""))/10.0;
                
                    if count == 0:
                        T = vals[1];
                        name = files[i].replace("_VEAM_%(v1)ss2p"%{"v1":vals[4]},"")
                        print(name)

                    if VEAM < 1.5:
                        labels.append('$V_{EAM}$ = -%(v1)0.1f'%{ "v1":VEAM }) 
               
                        markers.append( Plotting.labs_lins[count] )               

                        s2pdata = FR_Analysis.read_s2p_file(files[i])

                        hv_data.append([ s2pdata[1], s2pdata[s_param] ]);
                
                        del s2pdata 

                    count = (count + 1)%len(Plotting.labs)

                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.crv_lab_list = labels
                args.mrk_list = markers
                args.x_label = 'Frequency (GHz)'
            
                if s_param == 2:args.y_label = '$S_{11}$ (dB)'
                elif s_param == 3: args.y_label = '$S_{21}$ (dB)'
                elif s_param == 4: args.y_label = '$S_{12}$ (dB)'
                elif s_param == 5: args.y_label = '$S_{22}$ (dB)'
                else: args.y_label = '$S_{12}$ (dB)'
            
                if s_param == 3: args.plt_range = [1, 20, -45, 0]
                if s_param == 2: args.plt_range = [1, 15, -30, 0]
                args.plt_title = "T = %(v1)s C, $I_{DFB}$ = %(v2)s mA, $I_{SOA}$ = %(v3)s mA"%{"v1":T, "v2":IDFB, "v3":ISOA}
            
                args.fig_name = name
                if s_param == 2:args.fig_name += "_S11"
                elif s_param == 3: args.fig_name += "_S21"
                elif s_param == 4: args.fig_name += "_S12"
                elif s_param == 5: args.fig_name += "_S22"
                else: args.fig_name += "_S21"

                Plotting.plot_multiple_curves(hv_data, args)

                del hv_data
                del labels
                del markers

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.FR_plot()")
        print("Cannot find",dir_name)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.FR_plot()")
        print("Investigate error\n")

def run_FR_plots_3(loud = False):

    # loop over the generation of multiple S21 plots

    #DATA_HOME = "FR/Sml_Stp_Scn_T_20/"
    #DATA_HOME = "FR/Sml_Stp_Scn_T_25/"
    #DATA_HOME = "FR/Sml_Stp_Scn_T_30/"
    #IDFB = [180]; ISOA = [176]
    
    #DATA_HOME = "FR/Res_Peak_Scan_T_20/"
    #IDFB = [160, 162, 164, 166, 168, 172, 174, 176, 178, 180]
    #ISOA = [170, 170, 170, 170, 170, 170, 170, 170, 170, 170]
    #IDFB = [170, 170, 170]
    #ISOA = [161, 164, 167]
    
    #DATA_HOME = "FR/Res_Peak_Scan_T_25/"
    #IDFB = [164, 177]
    #ISOA = [170, 170]

    DATA_HOME = "FR/Full_Scan_T_20/"
    #IDFB = [160, 180]
    #ISOA = [160, 176]
    IDFB_vals = [160]
    ISOA_vals = [167]

    #for i in range(0, len(IDFB), 1):
    #    s_param = 3
    #    FR_plot(DATA_HOME, IDFB[i], ISOA[i], s_param, loud = True)

    #IDFB_vals = [160, 163, 167, 170, 172, 176, 180]
    #ISOA_vals = [160, 163, 167, 170, 172, 176]
    #IDFB_vals = [125, 130, 133, 137, 140, 143, 147, 150, 153, 157]
    #ISOA_vals = [160, 170]

    s_param = 3
    #for v in IDFB_vals:
    #    IDFB = []
    #    for ii in range(0, len(ISOA_vals), 1): IDFB.append(v)
    #    for i in range(0, len(IDFB), 1):
    #        FR_plot(DATA_HOME, IDFB[i], ISOA_vals[i], s_param, loud = True)

    for v in ISOA_vals:
        for vv in IDFB_vals:
            FR_plot(DATA_HOME, vv, v, s_param, loud); 

def run_f3dB_analysis(loud = False):

    # determine the 3dB BW from a set of measured FR data
    # R. Sheehan 3 - 10 - 2017

    try:
        HOME = os.getcwd()

        #DATA_HOME = "FR/Reg_Scan_T_20/"
        #DATA_HOME = "FR/Reg_Scan_T_25/"
        #DATA_HOME = "FR/Reg_Scan_T_30/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_20/"
        #DATA_HOME = "FR/Res_Peak_Scan_T_25/"
        #DATA_HOME = "FR/Sml_Stp_Scn_T_20/"
        #DATA_HOME = "FR/Sml_Stp_Scn_T_25/"
        #DATA_HOME = "FR/Sml_Stp_Scn_T_30/"
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            #files = glob.glob("*IDFB_%(v1)d*ISOA_%(v2)d*.s2p"%{"v1":IDFB,"v2":ISOA})
            files = glob.glob("*VEAM_00.s2p")

            if files:                

                filename = "Data_3dB_BW.txt"

                oldstdout = sys.stdout

                sys.stdout = open(filename, 'w')

                fmax = ""; tmax = 0.0; 

                for f in files:
                    #if loud: print(f
                    data = FR_Analysis.read_s2p_file(f)

                    f_3dB = FR_Analysis.estimate_f3dB(data, False)

                    if f_3dB > tmax: 
                        tmax = f_3dB; fmax = f; 

                    print(f,", f_{3dB} =",f_3dB,"(GHz)"

                sys.stdout = oldstdout

                print("Max 3dB BW measured =",tmax,"GHz")
                print("Data in file",fmax)

            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nTIPS_DFB_EAM_SOA.run_f3dB_analysis()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nTIPS_DFB_EAM_SOA.run_f3dB_analysis()")

def get_S21_data_matrix(data_choice, VEAM, loud = False):
    # extract the f3dB values from the Full scan data and store it in an array for plotting
    # extract the S21 resonance values from the full scan data and store it in an array for plotting
    # extract the S21 resonance frequencies from the full scan data and store it in an array for plotting
    # each column will represent f3dB data for fixed ISOA
    # each row will represent f3dB data for fixed IDFB
    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()
        
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            if loud:print(os.getcwd())

            # DFB and SOA sections current values
            IDFB_vals = [160, 163, 167, 170, 172, 176, 180] # len(IDFB_vals) = no. of rows of storage array
            ISOA_vals = [160, 163, 167, 170, 172, 176] # len(ISOA_vals) = no. of columns of storage array

            # create the array to be used for storing the data
            storage = Common.list_2D_array( len(IDFB_vals), len(ISOA_vals) )

            # S21 data stored in array with index
            sparam = 3; 

            for v in range(0, len(IDFB_vals), 1):
                for u in range(0, len(ISOA_vals), 1):
                    files = glob.glob("*IDFB_%(v1)d*ISOA_%(v2)d*VEAM_%(v3)s.s2p"%{"v1":IDFB_vals[v], "v2":ISOA_vals[u], "v3":VEAM})
                    if files:
                        if loud: print(files
                        s2pdata = FR_Analysis.read_s2p_file(files[0])
                        storage[v][u] = FR_Analysis.estimate_f3dB(s2pdata)
                        del s2pdata
                    del files

            filename = "f3dB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            Common.write_matrix(filename, storage)
            
            filename = "IDFB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            Common.write_data(filename, IDFB_vals)
            
            filename = "ISOA_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            Common.write_data(filename, ISOA_vals)

            del storage; del IDFB_vals; del ISOA_vals; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nError: TIPS_DFB_EAM_SOA.get_f3dB_matrix()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nError: TIPS_DFB_EAM_SOA.get_f3dB_matrix()")

def plot_S21_data_2D(data_choice, temperature, VEAM, loud = False):
    # make 2D plots of the data extracted from the S21 files

    # plot the f3dB values from the Full scan data
    # plot the S21 resonance values from the full scan dat
    # plto the S21 resonance frequencies from the full scan data
    # each column will represent f3dB data for fixed ISOA
    # each row will represent f3dB data for fixed IDFB

    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()
        
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            if loud:print(os.getcwd())

            # read the data into memory
            filename = "f3dB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            stored_data = Common.read_matrix(filename)
            
            filename = "IDFB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            IDFB_vals = Common.read_data(filename)
            
            filename = "ISOA_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            ISOA_vals = Common.read_data(filename)

            filename = "f3dB_avg_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            avg_vals = Common.read_data(filename)

            # make a plot of the f3dB data versus IDFB for different ISOA
            hv_data = []; marks = []; labels = [];

            avg = np.mean(np.asarray(avg_vals))

            hv_data.append( [IDFB_vals, avg_vals ] )
            marks.append('r-'); 
            labels.append('Avg = %(v1)0.2f (GHz)'%{"v1":avg});

            count = 0
            for j in range(0, len(ISOA_vals), 1):
                hv_data.append( [IDFB_vals, Common.get_col(stored_data, j) ] )
                marks.append(Plotting.labs_pts[count]); 
                labels.append('$I_{SOA}$ = %(v1)d (mA)'%{"v1":ISOA_vals[j]}); 
                count = (count + 1)%len(Plotting.labs_pts)

            args = Plotting.plot_arg_multiple()

            args.loud = loud
            args.crv_lab_list = labels
            args.mrk_list = marks
            args.x_label = '$I_{DFB}$ (mA)'
            args.y_label = '$f_{3dB}$ (GHz)'
            args.plt_range = [159, 181, 0, 10]
            args.plt_title = 'TIPS-1 3dB BW T = %(v1)d C, $V_{EAM}$ = %(v2)s'%{"v1":temperature, "v2":VEAM}
            args.fig_name = 'TIPS1_3dB_BW_T_%(v1)d_VEAM_%(v2)s'%{"v1":temperature, "v2":VEAM}

            Plotting.plot_multiple_curves(hv_data, args)

            del hv_data; del marks; del labels; 
            del stored_data; del ISOA_vals; del IDFB_vals; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_2D()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_2D()")

def plot_S21_data_2D_errors(data_choice, temperature, VEAM, loud = False):
    # make 2D plots of the data extracted from the S21 files

    # plot the f3dB values from the Full scan data
    # plot the S21 resonance values from the full scan dat
    # plto the S21 resonance frequencies from the full scan data
    # each column will represent f3dB data for fixed ISOA
    # each row will represent f3dB data for fixed IDFB

    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()
        
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            if loud:print(os.getcwd())

            # read the data into memory
            filename = "f3dB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            stored_data = Common.read_matrix(filename)
            
            filename = "IDFB_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            IDFB_vals = Common.read_data(filename)
            
            filename = "ISOA_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            ISOA_vals = Common.read_data(filename)

            # make a plot of the f3dB data versus IDFB averaged over the different ISOA
            avg_data = []; 
            count = 0
            for j in range(0, len(IDFB_vals), 1):
                data = Common.get_row(stored_data, j)
                avg_data.append( np.mean( np.asarray( data ) ) )

            filename = "f3dB_avg_data_VEAM_%(v1)s.txt"%{"v1":VEAM}
            Common.write_data(filename, avg_data)

            args = Plotting.plot_arg_single()

            args.loud = loud
            args.x_label = '$I_{DFB}$ (mA)'
            args.y_label = '$f_{3dB}$ (GHz)'
            args.plt_range = [159, 181, 0, 10]
            args.plt_title = 'TIPS-1 3dB BW T = %(v1)d C, $V_{EAM}$ = %(v2)s'%{"v1":temperature, "v2":VEAM}
            args.fig_name = 'TIPS1_3dB_Avg_BW_T_%(v1)d_VEAM_%(v2)s'%{"v1":temperature, "v2":VEAM}

            Plotting.plot_single_curve(IDFB_vals, avg_data, args)
 
            del stored_data; del ISOA_vals; del IDFB_vals; 

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_2D()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_2D()")

def plot_S21_data_3D():
    # make 3D plots of the data extracted from the S21 files

    # plot the f3dB values from the Full scan data
    # plot the S21 resonance values from the full scan dat
    # plto the S21 resonance frequencies from the full scan data
    # each column will represent f3dB data for fixed ISOA
    # each row will represent f3dB data for fixed IDFB

    # R. Sheehan 4 - 10 - 2017

    try:
        HOME = os.getcwd()
        
        DATA_HOME = "FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            if loud:print(os.getcwd())

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_3D()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nError: TIPS_DFB_EAM_SOA.plot_S21_data_3D()")

def test_peak_search_analysis(loud = False):
    # locate the peaks that occur in the S_21 data
    
    try:
        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/FR/Full_Scan_T_20/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            from scipy import signal

            #IDFB = '160'; ISOA = '160'; VEAM = '00';# one peaks
            IDFB = '160'; ISOA = '163'; VEAM = '00';# two peaks
            #IDFB = '160'; ISOA = '167'; VEAM = '00';# can't find peak, peak is below signal at f = 0 GHz
            #IDFB = '160'; ISOA = '172'; VEAM = '05';# two peaks
            #IDFB = '160'; ISOA = '172'; VEAM = '00';# two peaks
            IDFB = '160'; ISOA = '172'; VEAM = '00';# two peaks
            #IDFB = '167'; ISOA = '172'; VEAM = '00';# can't find peak, peak is below signal at f = 0 GHz


            filename = "TIPS_1_EAM_FR_T_20_IDFB_%(v1)s_ISOA_%(v2)s_VEAM_%(v3)s.s2p"%{"v1":IDFB, "v2":ISOA, "v3":VEAM} 

            s2pdata = FR_Analysis.read_s2p_file(filename); 
            frindx = 1
            sparam = 3
            frvals = np.asarray(s2pdata[frindx])
            data = np.asarray(s2pdata[sparam])           

            # apply a Savitzky-Golay filter to the data 
            # window_length must be odd integer
            # https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.signal.savgol_filter.html
            #y = signal.savgol_filter(data, window_length = 7, polyorder = 5)            

            # You can think of the widths argument as a list of the possible widths between peaks. 
            # The algorithm smooths over these widths and then look for a peak. if it consistently finds a peak in 
            # each "width", it declares that the peak exists.
            # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.find_peaks_cwt.html

            #peakind = signal.find_peaks_cwt(data, widths, min_snr = 1, noise_perc = 10)
            peakind = signal.find_peaks_cwt(data, widths = np.arange(20,21), min_snr = 2, noise_perc = 10)

            print("peak index:",peakind
            print("peak location:",frvals[peakind]
            print("peak value:",data[peakind]

            # make a quick plot of the data
            plt.plot(frvals, data, 'b-', frvals[peakind], data[peakind], 'r*', ms = 12)
            #plt.plot(frvals, data, 'b-', frvals, y, 'm--', frvals[peakind], data[peakind], 'r*', ms = 12)
            plt.show()
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: test_peak_search_analysis")
    except Exception:
        print("Error: run_peak_search_analysis")

def BERT_ED_Amplitude_Plot(loud = False):

    # plot the Data Eye Amplitude versus PPG output voltage
    # for different amplifier + attenuator combinations
    # Amplifier SHF810MT, Gain +30dB, Psat = 20 dBm
    # Attenuator variable 6-16 dB
    # R. Sheehan 29 - 9 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_27_9_2017/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            V_PPG = [200, 240, 280, 320, 340, 370] # Voltage outputs from PPG / mV

            EA_A6 = [2160, 2510, 2740, 2900, 2950, 3010] # Measured Eye Amplitudes for Att = 6 dB

            EA_A9 = [1530, 1770, 1950, 2060, 2090, 2140] # Measured Eye Amplitudes for Att = 9 dB

            EA_A10 = [1360, 1580, 1740, 1840, 1870, 1910] # Measured Eye Amplitudes for Att = 10 dB

            EA_A13 = [970, 1120, 1230, 1300, 1320, 1350] # Measured Eye Amplitudes for Att = 13 dB

            EA_A16 = [690, 790, 870, 920, 940, 960] # Measured Eye Amplitudes for Att = 16 dB

            Att_vals = [6, 9, 10, 13, 16] # List of attenuation values

            c1 = True if len(V_PPG) == len(EA_A6) else False
            c2 = True if len(V_PPG) == len(EA_A9) else False
            c3 = True if len(V_PPG) == len(EA_A10) else False
            c4 = True if len(V_PPG) == len(EA_A13) else False
            c5 = True if len(V_PPG) == len(EA_A16) else False
            c6 = True if (c1 and c2 and c3 and c4 and c5) else False

            if c6:

                hv_data = []; marks = []; labels = []; 
                #hv_data.append( [V_PPG, EA_A6] )
                #hv_data.append( [V_PPG, EA_A9] )
                #hv_data.append( [V_PPG, EA_A10] )
                hv_data.append( [V_PPG, EA_A13] )
                hv_data.append( [V_PPG, EA_A16] )

                for i in range(3, len(Att_vals), 1):
                    marks.append(Plotting.labs[i])
                    labels.append('Att. %(v1)d dB'%{"v1":Att_vals[i]})

                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = "PPG Voltage Out (mV)"
                args.y_label = "NRZ Data Eye Amplitude (mV)"
                args.mrk_list = marks
                args.crv_lab_list = labels
                args.plt_range = [195, 375, 600, 1400]
                args.plt_title = "NRZ Data Eye Amplitude DR = 10 Gbps"
                args.fig_name = "NRZ_Eye_Amp_DR_10_Zm"

                Plotting.plot_multiple_curves(hv_data, args)

            else:
                raise Exception

            os.chdir(HOME)
        else:
            print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
            print("Cannot find",DATA_HOME)
            raise EnvironmentError
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
        print("Go and investigate")

def BERT_ED_Amplitude_Plot_2(loud = False):

    # plot the Data Eye Amplitude versus PPG output voltage
    # for different amplifier + attenuator combinations
    # Amplifier SHF810MT, Gain +30dB, Psat = 20 dBm
    # Attenuator variable 6-16 dB
    # R. Sheehan 29 - 9 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_27_9_2017/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            V_PPG = [0.69, 0.81, 0.9, 0.95, 0.97, 1.15, 1.26, 1.33, 1.53, 1.81, 2, 2.11] # Data peak-peak voltage

            V_PPG_A16 = [0.69, 0.81, 0.9, 0.95]
            V_PPG_A13 = [0.97, 1.15, 1.26, 1.33]
            V_PPG_A9 = [1.53, 1.81, 2, 2.11]

            EA_Data = [128, 146, 156, 161, 162, 180, 189, 194, 199, 206, 209, 208] # Measured Eye Amplitudes for different Vpp

            EA_A16 = [128, 146, 156, 161]
            EA_A13 = [162, 180, 189, 194]
            EA_A9 = [199, 206, 209, 208]

            Att_vals = [16, 13, 9] # List of attenuation values

            # break the data up into its subsets

            c1 = True if len(V_PPG) == len(EA_Data) else False
            
            if c1:

                hv_data = []; marks = []; labels = []; 
                hv_data.append( [V_PPG_A16, EA_A16] )
                hv_data.append( [V_PPG_A13, EA_A13] )
                hv_data.append( [V_PPG_A9, EA_A9] )
                
                for i in range(0, len(Att_vals), 1):
                    marks.append(Plotting.labs[i])
                    labels.append('Att. %(v1)d dB'%{"v1":Att_vals[i]})

                args = Plotting.plot_arg_multiple()

                args.loud = loud
                args.x_label = "NRZ Data Eye Amplitude (V)"
                args.y_label = "BtB Eye Amplitude (mV)"
                args.mrk_list = marks
                args.crv_lab_list = labels
                #args.plt_range = [195, 375, 600, 1400]
                args.plt_title = "BtB Eye Amplitude DR = 10 Gbps"
                args.fig_name = "BtB_Eye_Amp_DR_10"

                Plotting.plot_multiple_curves(hv_data, args)

            else:
                raise Exception

            os.chdir(HOME)
        else:
            print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
            print("Cannot find",DATA_HOME)
            raise EnvironmentError
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
        print("Go and investigate")

def BERT_ED_Amplitude(loud = False):

    # output Data Eye Amplitude versus PPG output voltage
    # for different amplifier + attenuator combinations
    # Amplifier SHF810MT, Gain +30dB, Psat = 20 dBm
    # Attenuator variable 6-16 dB
    # R. Sheehan 29 - 9 - 2017

    try:
        HOME = os.getcwd()

        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_27_9_2017/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            V_PPG = [200, 240, 280, 320, 340, 370] # Voltage outputs from PPG / mV

            EA_A6 = [2160, 2510, 2740, 2900, 2950, 3010] # Measured Eye Amplitudes for Att = 6 dB

            EA_A9 = [1530, 1770, 1950, 2060, 2090, 2140] # Measured Eye Amplitudes for Att = 9 dB

            EA_A10 = [1360, 1580, 1740, 1840, 1870, 1910] # Measured Eye Amplitudes for Att = 10 dB

            EA_A13 = [970, 1120, 1230, 1300, 1320, 1350] # Measured Eye Amplitudes for Att = 13 dB

            EA_A16 = [690, 790, 870, 920, 940, 960] # Measured Eye Amplitudes for Att = 16 dB

            EA_data = [EA_A6, EA_A9, EA_A10, EA_A13, EA_A16]

            Att_vals = [6, 9, 10, 13, 16] # List of attenuation values

            c1 = True if len(V_PPG) == len(EA_A6) else False
            c2 = True if len(V_PPG) == len(EA_A9) else False
            c3 = True if len(V_PPG) == len(EA_A10) else False
            c4 = True if len(V_PPG) == len(EA_A13) else False
            c5 = True if len(V_PPG) == len(EA_A16) else False
            c7 = True if len(EA_data) == len(Att_vals) else False
            c6 = True if (c1 and c2 and c3 and c4 and c5 and c7) else False

            if c6:

                # load 1D interpolation module from scipy
                from scipy.interpolate import interp1d

                # create interpolating object over the data set
                #f_data = interp1d(wl_data, pow_data, kind='quadratic')

                filename = "Data_Eye_Amplitudes.txt"

                oldstdout = sys.stdout

                sys.stdout = open(filename, 'w')

                print("NRZ Data\nData Rate : 10 Gbps\nAmplifier : SHF810 MT\n"

                ppg_volt_vals = [200, 250, 300, 350]

                for i in range(0, len(Att_vals), 1):
                    print("\nAttenuation =",Att_vals[i],"dB"

                    # create interpolating object over the data set
                    f_data = interp1d(np.asarray(V_PPG), np.asarray(EA_data[i]), kind='linear')

                    print("PPG Voltage (mV), NRZ Data Eye Amplitude (V)"
                    for v in ppg_volt_vals:
                        #print(v,",",f_data(v)
                        print("%(v1)d, %(v2)0.2f"%{"v1":v, "v2":f_data(v)/1000.0}
                    #print("\n"

                sys.stdout = oldstdout

            else:
                raise Exception

            os.chdir(HOME)
        else:
            print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
            print("Cannot find",DATA_HOME)
            raise EnvironmentError
    except Exception:
        print("Error: TIPS_DFB_EAM_SOA.BERT_ED_Amplitude")
        print("Go and investigate")

def OSNR_Spectrum_Plots(loud = False):

    # plot the measured optical spectra obtained during OSNR measurements
    # should be able to observe spectral broadening due to modulation
    # R. Sheehan 1 - 11 - 2017

    try:
        HOME = os.getcwd()
        
        DATA_HOME = "SNR_Data/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            if loud:print(os.getcwd())

            plot = 3 # decide which plot is going to be made

            if plot == 2:
                files = glob.glob("Trace*DR_10*D*.txt")
            elif plot == 3:
                files = glob.glob("Trace*DR_12*D*.txt")
            else:
                files = glob.glob("Trace*DR*D*00*.txt")

            hv_data = []; labels = []; marks = []
            count = 0
            delim = '\t'
            for x in files:
                data = Common.read_matrix(x, delim)
                data = Common.transpose_multi_col(data)

                hv_data.append(data)
                marks.append(Plotting.labs_lins[count])

                nums = Common.extract_values_from_string(x)
                print(nums

                if plot == 2 or plot == 3:
                    labels.append("D = %(v1)s km"%{"v1":nums[1]})
                else:
                    if nums[0] == '00':
                        labels.append("No Modulation")
                    elif nums[0] == '12':
                        labels.append("DR = 12.5 Gbps")
                    elif nums[0] == '17':
                        labels.append("DR = 17.5 Gbps")
                    else:
                        labels.append("DR = %(v1)s Gbps"%{"v1":nums[0]})

                count = (count+1)%len(Plotting.labs_lins)
                del data
            
            del files

            args = Plotting.plot_arg_multiple()
            args.crv_lab_list = labels
            args.mrk_list = marks
            args.loud = loud
            args.x_label = 'Wavelength (nm)'
            args.y_label = 'Spectral Power (dBm/0.05 nm)'
            args.plt_range = [1320, 1325, -65, -10]

            if plot == 2:
                args.plt_title = 'Optical Spectrum DR = 10 Gbps, $<P_{Rx}> = -13.51 \pm 0.97$ dBm'
                args.fig_name = 'Optical_Spectrum_DR_10'
            elif plot == 3:
                args.plt_title = 'Optical Spectrum DR = 12.5 Gbps, $<P_{Rx}> = -13.63 \pm 1.07$ dBm'
                args.fig_name = 'Optical_Spectrum_DR_12'
            else:
                args.plt_title = 'Optical Spectrum D = 0 km, $<P_{Rx}> = -12.65 \pm 0.04$ dBm'
                args.fig_name = 'Optical_Spectrum_D_0'

            Plotting.plot_multiple_curves(hv_data, args)

            del hv_data; del labels; del marks;

            os.chdir(HOME)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("\nError: TIPS_DFB_EAM_SOA.OSNR_Spectrum_Plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("\nError: TIPS_DFB_EAM_SOA.OSNR_Spectrum_Plots()")
