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

def Make_TIPS_1_Plots():

    # import the data needed and call the necessary functions to make the plots for the first TIPS device
    # R. Sheehan 8 - 2 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/TIPS_Characterisation_Feb_2017/"

    os.chdir(DATA_HOME)

    print(os.getcwd())

    #li_data_file = "Measured_DFB_SOA_Voltage.csv"
    #li_data_file = "Measured_DFB_SOA_Voltage_Transparency.csv"
    #ISOA = [0.0, 40.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0] # SOA currents used to take LI measurements
    #ISOA = [0.0, 40.0, 80.0, 100.0, 120.0, 140.0] # SOA currents used to take LI measurements
    #wavelength = 1321 # laser operating wavelength in nm
    #plot_LI_vol_data(li_data_file, ISOA) # plot the measured LI data on volt scale
    #plot_LI_mW_data(li_data_file, ISOA, wavelength, True) # plot the measured LI data on mW scale
        
    #EAM_VI_1 = "EAM_Current_Versus_Voltage.csv"
    #EAM_VI_2 = "EAM_Voltage_Versus_Current.csv"
    #plot_EAM_data(EAM_VI_1, False, True)
    #plot_EAM_data(EAM_VI_2, True, True)

    #SOA_Spctrm = "SOA_Spctrm_T_*_Ilas_000_Isoa_*"
    #SOA_Spctrm = "SOA_Spctrm_T_20_Ilas_000_Isoa_*"
    #wavelength = 1321.0
    #plot_SOA_ASE_data(SOA_Spctrm, True)
    #plot_SOA_LI_mW_data(wavelength, True)

    #Las_Spctrm = "Laser_Spctrm_T_*_Ilas_*_Isoa_*.txt"
    #plot_Laser_data(Las_Spctrm, True)

    # plot the measured wavelength data at different biases
    #plot_WL_data_1(True)
    #plot_WL_data_2(True)

    #plot_resistor_data(True)

    #plot_EAM_data_2(True)

    #plot_throughput_data(True)

    #plot_rewired_char_IV_data(True)

    #plot_rewired_char_VI_data(True)

    #liv_file = "Measured_DFB_Volt_Current_Power.csv"

    #plot_LIV_data(liv_file, True)

    #plot_EAM_transparency(True)

    #compare_measured_power_data(True)

    #plot_spectrum_temperature()

    #fname = "DFB_IV_Temperature.csv"
    #scale = True
    #x_lab = 'Voltage (V)'
    #y_lab = 'Current (mA)'
    #plt_title = ""
    #plt_range = [0.0, 3.0, 0.0, 200.0]
    #fig_name = 'DFB_IV_Char_Temp.png'
    #plot_data_temperature(fname, scale, x_lab, y_lab, plt_title, plt_range, fig_name, True)

    #fname = "DFB_LV_Temperature.csv"
    #scale = True
    #x_lab = 'Voltage (V)'
    #y_lab = 'Power (mW)'
    #plt_title = ""
    #plt_range = [0.0, 3.0, 0.0, 0.5]
    #fig_name = 'DFB_IV_Char_Temp_mW.png'
    #plot_data_temperature(fname, scale, x_lab, y_lab, plt_title, plt_range, fig_name, True)

    #plot_LI_for_variable_Isoa()

    Re_Plot_Measured_Optical_Power()
    
    return 0

def plot_SOA_LI_mW_data(wavelength, loud = False):
    # plot the measured SOA-LI data on mW scale
    # raw data is given on (V) scale, it must be converted to (mW) scale
    # R. Sheehan 9 - 2 - 2017

    # read in the detector response data
    resp_file = "C:/Users/Robert/Equipment/Equipment_Manuals/Thorlabs/PDA10D_responsivity.csv"

    resp_data = Common.read_two_columns(resp_file)

    if resp_data[0]:
        from scipy import interpolate

        R = interpolate.interp1d(resp_data[1], resp_data[2])

        resp_val = R(wavelength)

        print("Response at L = ",wavelength," is ",R(wavelength))

        # define conversion factors from known values given by Thorlabs
        Sf = 1.7 # scale factor assuming 50 Ohm termination
        Gt = 5e+3 # transimpedance gain of detector
        conversion_factor = ( R(wavelength) * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW

        # correct the measured voltage data for the dark current of the detector
        Vdark = 0.188 # (V)

        SOA_curr = [75, 100, 125, 150, 175]
        SOA_pow = [0.192, 0.196, 0.2, 0.208, 0.216]

        for i in range(0, len(SOA_pow), 1): 
            SOA_pow[i] = Common.convert_PmW_PdBm( ((SOA_pow[i] - Vdark) / conversion_factor) )

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(SOA_curr, SOA_pow, labs[1], lw = 2, label = 'T = 20 ( C )')

        ax.legend(loc='best')
        plt.xlabel('$I_{SOA}$ (mA)', fontsize = 17)
        plt.ylabel('PDA10D (dBm)', fontsize = 17)
        plt.title('TIPS 1 SOA $P_{out}$')
        plt.axis( [70, 180, -25, -15] )

        plt.savefig('TIPS_1_SOA_dBm.png')
        if loud: plt.show()
        plt.clf()
        plt.cla()
        plt.close()

    return 0

def plot_LI_volt_data(filename, SOA_curr_list, loud = False):
    # plot the measured LI data
    # raw data is given on (V) scale, it must be converted to (mW) scale
    # R. Sheehan 8 - 2 - 2017

    try:
        if glob.glob(filename):
            # the file exists
            LI_Data = Common.read_matrix(filename)
            LI_Data = Common.transpose_multi_col(LI_Data)

            # correct the measured voltage data for the dark current of the detector
            Vdark = 0.188 # (V)
            for i in range(1, len(LI_Data), 1): 
                for j in range(0, len(LI_Data[i]), 1):
                    LI_Data[i][j] -= Vdark

            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            for i in range(1, len(SOA_curr_list), 1): 
                ax.plot(LI_Data[0], LI_Data[i+1], labs[cnt], lw = 2, label = '$I_{SOA} = %(v1)0.1f$ (mA)'%{"v1":SOA_curr_list[i]})
                cnt += 1

            ax.legend(loc='best')
            plt.xlabel('$I_{las}$ (mA)', fontsize = 17)
            plt.ylabel('PDA10D (V)', fontsize = 17)
            plt.title('TIPS 1 DFB $P_{out}$')
            plt.axis( [LI_Data[0][0], LI_Data[0][-1], 0.0, LI_Data[-1][-1]] )

            plt.savefig('TIPS_1_DFB.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            del LI_Data

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_LI_data()")
        print("File: ",filename," not found")
        return -1

def plot_LI_mW_data(filename, SOA_curr_list, wavelength, loud = False):
    # plot the measured LI data on mW scale
    # raw data is given on (V) scale, it must be converted to (mW) scale
    # R. Sheehan 9 - 2 - 2017

    try:
        if glob.glob(filename):

            # read in the detector response data
            resp_file = "C:/Users/Robert/Equipment/Equipment_Manuals/Thorlabs/PDA10D_responsivity.csv"

            resp_data = Common.read_two_columns(resp_file)

            if resp_data[0]:
                from scipy import interpolate

                R = interpolate.interp1d(resp_data[1], resp_data[2])

                resp_val = R(wavelength)

                print("Response at L = ",wavelength," is ",R(wavelength))

                # define conversion factors from known values given by Thorlabs
                Sf = 1.7 # scale factor determined by comparison of measured data with data measured on ILX
                Gt = 5e+3 # transimpedance gain of detector
                conversion_factor = ( R(wavelength) * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW

                # the file exists
                LI_Data = Common.read_matrix(filename)
                LI_Data = Common.transpose_multi_col(LI_Data)

                # correct the measured voltage data for the dark current of the detector
                Vdark = 0.188 # (V)
                for i in range(1, len(LI_Data), 1): 
                    for j in range(0, len(LI_Data[i]), 1):
                        LI_Data[i][j] = (LI_Data[i][j] - Vdark) / conversion_factor

                fig = plt.figure()
                ax = fig.add_subplot(111)

                cnt = 0
                for i in range(1, len(SOA_curr_list), 1): 
                    ax.plot(LI_Data[0], LI_Data[i+1], labs[cnt], lw = 2, label = '$I_{SOA} = %(v1)0.1f$ (mA)'%{"v1":SOA_curr_list[i]})
                    cnt += 1

                ax.legend(loc='best')
                plt.xlabel('$I_{las}$ (mA)', fontsize = 17)
                plt.ylabel('$P_{out}$ (mW)', fontsize = 17)
                #plt.title('TIPS 1 DFB $P_{out}$ at EAM Transparency')
                plt.axis( [LI_Data[0][0], LI_Data[0][-1], 0.0, 1.5] )

                #plt.savefig('TIPS_1_DFB_mW.png')
                plt.savefig('TIPS_1_DFB_mW_Trans.png')
                if loud: plt.show()
                plt.clf()
                plt.cla()
                plt.close()

                del LI_Data

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_LI_mW_data()")
        print("File: ",filename," not found")
        return -1

def plot_LIV_data(filename, loud = False):
    # plot the measured LIV data
    # current values measured on Keithley 2400, data is saved in units of (A)
    # power measured on ILX power meter, data is saved in units of (dBm)
    # R. Sheehan 3 - 3 - 2017

    try:
        if glob.glob(filename):
            # the file exists
            LI_Data = Common.read_matrix(filename)
            LI_Data = Common.transpose_multi_col(LI_Data)

            # plot the measured current on (mA) scale
            for i in range(0, len(LI_Data[1]), 1):
                LI_Data[1][i] *= 1000.0
            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(LI_Data[0], LI_Data[1], labs[1], lw = 2, ms = 10, label = '$I_{DFB}$')

            ax.legend(loc='best')
            plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
            plt.ylabel('$I_{DFB}$ (mA)', fontsize = 17)
            plt.title('DFB Characteristic')
            plt.axis( [0.0, 3.0, 0.0, 185.0] )

            plt.savefig('TIPS_DFB_Current_versus_Voltage.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            # plot the measured power on dBm scale
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(LI_Data[0], LI_Data[2], labs[1], lw = 2, ms = 8)

            #ax.legend(loc='best')
            plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
            plt.ylabel('$P_{DFB}$ (dBm)', fontsize = 17)
            plt.title('TIPS DFB Power')
            plt.axis( [0.0, 3.0, -22.0, 2.2] )

            plt.savefig('TIPS_DFB_Power_dBm_versus_Voltage.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            # plot the measured power on (mW) scale
            for i in range(0, len(LI_Data[2]), 1):
                LI_Data[2][i] = Common.convert_PdBm_PmW(LI_Data[2][i])

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(LI_Data[0], LI_Data[2], labs[0], lw = 2, ms = 10)

            #ax.legend(loc='best')
            plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
            plt.ylabel('$P_{DFB}$ (mW)', fontsize = 17)
            plt.title('TIPS DFB Power')
            plt.axis( [0.0, 3.0, 0.0, 1.5] )

            plt.savefig('TIPS_DFB_Power_mW_versus_Voltage.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            del LI_Data

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_LI_data()")
        print("File: ",filename," not found")
        return -1

def plot_EAM_data(filename, switch = False, loud = False):
    # plot the measured IV data taken from the EAM
    # R. Sheehan 8 - 2 - 2017

    try:
        if glob.glob(filename):
            # the file exists
            LI_Data = Common.read_matrix(filename)
            LI_Data = Common.transpose_multi_col(LI_Data)

            params = Common.linear_fit( np.asarray(LI_Data[0]), np.asarray(LI_Data[1]), [0.0, 5.0])

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(LI_Data[0], LI_Data[1], labs_pts[0] if switch else labs_pts[1], lw = 2)
            ax.plot([LI_Data[0][0], LI_Data[0][-1]], 
                    [ params[0] + params[1]*LI_Data[0][0], params[0] + params[1]*LI_Data[0][-1] ], 
                    labs_lins[0] if switch else labs_lins[1], lw = 2, 
                    label = '$V_{EAM} = %(v1)0.5f I_{EAM}$, R = %(v2)0.2f $(\Omega)$'%{"v1":params[1], "v2":1000.0*params[1]} 
                    if switch else '$I_{EAM} = %(v1)0.2f V_{EAM}$, R = %(v2)0.2f $(\Omega)$'%{"v1":params[1], "v2":1000.0/params[1]})

            ax.legend(loc='best')
            if switch: 
                plt.ylabel('$V_{EAM}$ (V)', fontsize = 17)
                plt.xlabel('$I_{EAM}$ (mA)', fontsize = 17)
                plt.title('TIPS 1 EAM IV Curve')
                plt.axis( [LI_Data[0][0], LI_Data[0][-1], LI_Data[1][0], LI_Data[1][-1]] )
                plt.savefig('TIPS_1_EAM_IV.png')
            else:
                plt.xlabel('$V_{EAM}$ (V)', fontsize = 17)
                plt.ylabel('$I_{EAM}$ (mA)', fontsize = 17)
                plt.title('TIPS 1 EAM VI Curve')
                plt.axis( [LI_Data[0][0], LI_Data[0][-1], LI_Data[1][0], LI_Data[1][-1]] )
                plt.savefig('TIPS_1_EAM_VI.png')

            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            del LI_Data
            del params

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_EAM_data()")
        print("File: ",filename," not found")
        return -1

def plot_SOA_ASE_data(filename, loud = False):
    # plot the measured SOA ASE data
    # R. Sheehan 8 - 2 - 2017

    try:
        filelist = glob.glob(filename)
        if filelist:
            # the file exists
            
            for i in range(0, len(filelist), 1): 
                numbers = Common.extract_values_from_string(filelist[i])

                print(numbers)
            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            cnt1 = 0
            for i in range(0, len(filelist), 1): 
                LI_Data = Common.read_matrix(filelist[i])
                LI_Data = Common.transpose_multi_col(LI_Data)

                numbers = Common.extract_values_from_string(filelist[i])
                
                if float(numbers[0]) == 20 and "Rpt" not in filelist[i]:
                    ax.plot(LI_Data[0], LI_Data[1], labs_lins[cnt], lw = 2, label = '$I_{SOA} = %(v1)0.0f (mA)$'%{"v1":float(numbers[2])})
                    cnt+=1

                if float(numbers[0]) == 25:
                    ax.plot(LI_Data[0], LI_Data[1], labs_dashed[cnt1], lw = 2)

                    cnt1+=1

                if "Rpt" in filelist[i]:
                    ax.plot(LI_Data[0], LI_Data[1], labs_dashed[cnt1], lw = 2)

                    cnt1+=1

                del LI_Data
            
            ax.legend(loc='best')
            
            plt.xlabel('Wavelength (nm)', fontsize = 17)
            plt.ylabel('$P_{OSA}$ (dBm)', fontsize = 17)
            plt.title('TIPS 1 SOA Spectrum')
            plt.axis( [1275, 1360, -60, -45] )

            plt.savefig('TIPS_1_SOA_Spctrm_Rpt.png')

            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_SOA_ASE_data()")
        print("File: ",filename," not found")
        return -1

def plot_Laser_data(filename, loud = False):
    # plot the measured laser spectrum data
    # R. Sheehan 8 - 2 - 2017

    try:
        filelist = glob.glob(filename)
        
        if filelist:
            # the file exists
            
            for i in range(0, len(filelist), 1): 
                numbers = Common.extract_values_from_string(filelist[i])

                print(numbers)
            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            cnt1 = 0
            for i in range(0, len(filelist), 1): 
                LI_Data = Common.read_matrix(filelist[i])
                LI_Data = Common.transpose_multi_col(LI_Data)

                numbers = Common.extract_values_from_string(filelist[i])
                
                if float(numbers[0]) == 20:
                    ax.plot(LI_Data[0], LI_Data[1], labs_lins[cnt], lw = 2, label = '$I_{sec} = %(v1)0.0f (mA)$'%{"v1":float(numbers[2])})
                    cnt+=1

                if float(numbers[0]) == 25:
                    ax.plot(LI_Data[0], LI_Data[1], labs_dashed[cnt1], lw = 2)

                    cnt1+=1

                del LI_Data
            
            ax.legend(loc='best')
            
            plt.xlabel('Wavelength (nm)', fontsize = 17)
            plt.ylabel('$P_{OSA}$ (dBm)', fontsize = 17)
            plt.title('TIPS 1 DFB Spectrum')
            #plt.axis( [1316, 1326, -33, 0.0] )

            #plt.savefig('TIPS_1_DFB_Spctrm.png')

            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_Laser_data()")
        print("File: ",filename," not found")
        return -1

def plot_WL_data_1(loud = False):
    # plot the measured laser wavelength data
    # R. Sheehan 9 - 2 - 2017

    I_las = [75.0, 100.0, 150.0]
    T = [20.0, 25.0, 30.0]

    I_las_comb = I_las + I_las + I_las

    wl_1_20 = [1320.246, 1320.708, 1321.628]
    wl_2_20 = [1320.274, 1320.73, 1321.65]
    wl_3_20 = [1320.274, 1320.798, 1321.664]
        
    wl_20_comb = wl_1_20 + wl_2_20 + wl_3_20

    fit_20 = Common.linear_fit( np.asarray(I_las_comb), np.asarray(wl_20_comb), [0.0, 5.0])

    wl_1_25 = [1320.634, 1321.108, 1322.01]
    wl_2_25 = [1320.654, 1321.114, 1322.026]
    wl_3_25 = [1320.728, 1321.164, 1322.082]

    wl_25_comb = wl_1_25 + wl_2_25 + wl_3_25

    fit_25 = Common.linear_fit( np.asarray(I_las_comb), np.asarray(wl_25_comb), [0.0, 5.0])

    wl_1_30 = [1321.09, 1321.514, 1322.434]
    wl_2_30 = [1321.118, 1321.53, 1322.438]
    wl_3_30 = [1321.144, 1321.58, 1322.482]

    wl_30_comb = wl_1_30 + wl_2_30 + wl_3_30

    fit_30 = Common.linear_fit( np.asarray(I_las_comb), np.asarray(wl_30_comb), [0.0, 5.0])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([I_las_comb[0], I_las_comb[-1]], [fit_20[0] + I_las_comb[0]*fit_20[1], fit_20[0] + I_las_comb[-1]*fit_20[1]], 
            labs_lins[0], lw = 2, label = 'T = 20 (C), $\lambda(I) = %(v2)0.2f + %(v1)0.04f I$'%{"v1":fit_20[1], "v2":fit_20[0]})
    ax.plot(I_las_comb, wl_20_comb, labs_pts[0], lw = 2)

    ax.plot([I_las_comb[0], I_las_comb[-1]], [fit_25[0] + I_las_comb[0]*fit_25[1], fit_25[0] + I_las_comb[-1]*fit_25[1]], 
            labs_lins[1], lw = 2, label = 'T = 25 (C), $\lambda(I) = %(v2)0.2f + %(v1)0.04f I$'%{"v1":fit_20[1], "v2":fit_25[0]})
    ax.plot(I_las_comb, wl_25_comb, labs_pts[1], lw = 2)

    ax.plot([I_las_comb[0], I_las_comb[-1]], [fit_30[0] + I_las_comb[0]*fit_30[1], fit_30[0] + I_las_comb[-1]*fit_30[1]], 
            labs_lins[2], lw = 2, label = 'T = 30 (C), $\lambda(I) = %(v2)0.2f + %(v1)0.04f I$'%{"v1":fit_20[1], "v2":fit_30[0]})
    ax.plot(I_las_comb, wl_30_comb, labs_pts[2], lw = 2)

    ax.legend(loc='upper left')
            
    plt.xlabel('$I_{las}$ (mA)', fontsize = 17)
    plt.ylabel('Wavelength (nm)', fontsize = 17)
    plt.title('TIPS 1 DFB Spectrum')
    plt.axis( [70, 155, 1315, 1325] )

    plt.savefig('TIPS_1_DFB_WL_Curr.png')

    if loud: plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return 0

def plot_WL_data_2(loud = False):
    # plot the measured laser wavelength data
    # R. Sheehan 9 - 2 - 2017

    I_las = [75.0, 100.0, 150.0]
    T = [20.0, 25.0, 30.0]

    T = [20.0 for i in range(9)] + [25.0 for i in range(9)] + [30.0 for i in range(9)]

    wl_20_75 = [1320.246, 1320.274, 1320.274]
    wl_20_100 = [1320.708, 1320.73, 1320.798]
    wl_20_150 = [1321.628, 1321.65, 1321.664]

    wl_20 = wl_20_75 + wl_20_100 + wl_20_150

    wl_25_75 = [1320.634, 1320.654, 1320.728]
    wl_25_100 = [1321.108, 1321.114, 1321.164]
    wl_25_150 = [1322.01, 1322.026, 1322.082]

    wl_25 = wl_25_75 + wl_25_100 + wl_25_150

    wl_30_75 = [1321.09, 1321.118, 1321.144]
    wl_30_100 = [1321.514, 1321.53, 1321.58]
    wl_30_150 = [1322.434, 1322.438, 1322.482]

    wl_30 = wl_30_75 + wl_30_100 + wl_30_150

    wl = wl_20 + wl_25 + wl_30

    fit = Common.linear_fit( np.asarray(T), np.asarray(wl), [0.0, 5.0])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([T[0], T[-1]], [fit[0] + T[0]*fit[1], fit[0] + T[-1]*fit[1]], 
            labs_lins[1], lw = 2, label = '$\lambda(T) = %(v2)0.2f + %(v1)0.04f T$'%{"v1":fit[1], "v2":fit[0]})
    ax.plot(T, wl, labs_pts[1], lw = 2)

    ax.legend(loc='upper left')
            
    plt.xlabel('Temperature (C)', fontsize = 17)
    plt.ylabel('Wavelength (nm)', fontsize = 17)
    plt.title('TIPS 1 DFB Spectrum')
    plt.axis( [18, 32, 1315, 1325] )

    plt.savefig('TIPS_1_DFB_WL_Temp.png')

    if loud: plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return 0

def plot_resistor_data(loud = False):
    # plot the measured IV characteristic of a known diode
    # this is to check that the wiring for the LDD units is correct
    # R. Sheehan 31 - 1 - 2017

    I_las = [1.0, 10.0, 20.0, 50.0]
    V1 = [0.02, 0.21, 0.42, 1.05] # NWPRT S/N 1038
    V2 = [0.02, 0.22, 0.44, 1.09] # NWPRT S/N 10070
    V3 = [0.02, 0.22, 0.44, 1.10] # NWPRT S/N 10072
    V4 = [0.019, 0.219, 0.438, 1.096] # THOR S/N M00223157
    V5 = [0.021, 0.218, 0.436, 1.095] # Keithley? 

    II = I_las + I_las + I_las + I_las + I_las
    VV = V1 + V2 + V3 + V4 + V5

    fit = Common.linear_fit( np.asarray(II), np.asarray(VV), [0.0, 0.2])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([II[0], II[-1]], [fit[0] + II[0]*fit[1], fit[0] + II[-1]*fit[1]], 
            labs_lins[0], lw = 2, label = '$V(I) = %(v2)0.5f + %(v1)0.05f I$'%{"v1":fit[1], "v2":fit[0]})
    ax.plot(II, VV, labs_pts[0], lw = 2)

    ax.legend(loc='upper left')
            
    plt.xlabel('Current (mA)', fontsize = 17)
    plt.ylabel('Voltage (V)', fontsize = 17)
    plt.title('Measured Voltage across Test Resistor')
    plt.axis( [-0.1, 51, -0.1, 1.2] )

    plt.savefig('Test_Resistor.png')

    if loud: plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return 0

def plot_EAM_data_2(loud = False):
    # plot the measured throughput data
    # R. Sheehan 14 - 2 - 2017

    resp_val = 0.451 # at lambda = 1320 nm
    vdark = 0.188 # dark current reading
    Sf = 1.7 # scale factor assuming 50 Ohm termination
    Gt = 5e+3 # transimpedance gain of detector
    conversion_factor = ( resp_val * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW

    Vvals = [0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5]
    Ieam132 = [93.46, 56.29, 18.76, -0.04, -18.81, -56.22, -93.38]
    Ieam146 = [93.45, 56.21, 18.74, -0.04, -18.83, -56.31, -93.45]

    Vvals2 = [-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
    Ieam2 = [-96.04, -76.87, -57.74, -38.54, -19.305, -3.30E-02, 19.261, 38.564, 57.82, 76.99, 96.1]

    Veam = Vvals + Vvals + Vvals2[::-1] # the syntax L[::-1] represents the list in reverse order
    Ieam = Ieam132 + Ieam146 + Ieam2[::-1]

    fit = Common.linear_fit( np.asarray(Veam), np.asarray(Ieam), [0.0, 0.2])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([Veam[0], Veam[-1]], [fit[0] + Veam[0]*fit[1], fit[0] + Veam[-1]*fit[1]], 
            labs_lins[1], lw = 2, label = '$I_{EAM}(V) = %(v1)0.2f V_{EAM}, R = %(v2)0.2f (\Omega)$'%{"v1":fit[1], "v2":1000.0/fit[1]})
    ax.plot(Veam, Ieam, labs_pts[1], lw = 2)

    ax.legend(loc='upper left')
            
    plt.ylabel('Current (mA)', fontsize = 17)
    plt.xlabel('Voltage (V)', fontsize = 17)
    
    plt.title('TIPS 1 EAM VI Curve')
    #plt.axis( [Veam[0]-0.1, Veam[-1]+0.1, Ieam[0]-1, Ieam[-1]+1 ] )
    plt.savefig('TIPS_1_EAM_VI.png')

    if loud: plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return 0

def plot_throughput_data(loud = False):
    # plot the measured throughput data
    # R. Sheehan 14 - 2 - 2017

    resp_val = 0.451 # at lambda = 1320 nm
    vdark = 0.188 # dark current reading
    Sf = 1.7 # scale factor assuming 50 Ohm termination
    Gt = 5e+3 # transimpedance gain of detector
    conversion_factor = ( resp_val * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW

    # EAM Data
    Vvals = [0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5]
    
    P132 = [2.64, 2.64, 2.64, 2.64, 2.64, 2.64, 2.64]
    P146 = [2.88, 2.88, 2.88, 2.88, 2.88, 2.88, 2.88]

    for i in range(0, len(P132), 1):
        P132[i] = (P132[i]-vdark) / conversion_factor
        P146[i] = (P146[i]-vdark) / conversion_factor

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(Vvals, P132, labs[0], lw = 2, label = '$I_{DFB} = 132 (mA)$')
    ax.plot(Vvals, P146, labs[2], lw = 2, label = '$I_{DFB} = 146 (mA)$')

    ax.legend(loc='center right')
            
    plt.ylabel('$P_{out}$ (mW)', fontsize = 17)
    plt.xlabel('$V_{EAM}$ (V)', fontsize = 17)
    
    plt.title('TIPS 1 EAM $P_{out}$')
    #plt.axis( [Veam[0]-0.1, Veam[-1]+0.1, Ieam[0]-1, Ieam[-1]+1 ] )
    plt.savefig('TIPS_1_EAM_Pout.png')

    if loud: plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return 0

def plot_rewired_char_IV_data(loud = False):
    # plot the diode characteristic data that was measured after the device was re-wired
    # R. Sheehan 22 - 2 - 2017

    try:

        ivfiles = glob.glob("DFB_IV_Curve_After_Fix.txt")

        if ivfiles is not None:

            # read the IV data
            current = []
            voltage = []
            for i in range(0, len(ivfiles), 1):
                data = Common.read_matrix(ivfiles[i], '\t')
                data = Common.transpose_multi_col(data)
                for j in range(0, len(data[0]), 1):
                    current.append(data[0][j]) # store current data
                    voltage.append(data[1][j]) # store voltage data
                del data

            # fit a line to the data
            #fit = Common.linear_fit( np.asarray(current), np.asarray(voltage), [0.0, 0.2])

            # plot the data
            fig = plt.figure()
            ax = fig.add_subplot(111)

            #ax.plot([current[0], current[-1]], [fit[0] + current[0]*fit[1], fit[0] + current[-1]*fit[1]], 
            #        labs_lins[0], lw = 2, label = '$V_{DFB}(V)$')
            ax.plot(current, voltage, labs[0], lw = 2, label = '$V_{DFB}(V)$')

            ax.legend(loc='upper left')
            
            plt.xlabel('Current (mA)', fontsize = 17)
            plt.ylabel('Voltage (V)', fontsize = 17)
    
            plt.title('Characteristic Through RF Connector')
            plt.axis( [0.0, 51, 0.0, 1.6 ] )
            plt.savefig('DFB_IV_Through_RF_After_Connection_Fixed.png')

            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            # Fit the diode equation to the data
            # write the results of the Fitting process to a txt file instead of the console
            name = 'DFB_Diode_Fit_Results.txt'
            sys.stdout = open(name, 'w')

            diode_fit(current[1:], voltage[1:], T = 20)

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_rewired_char_data()")
        print("No data available to be read")
        return -1

def diode_voltage(x, eta, rs, eye0, T):
    # ideal diode equation inverted for voltage with Ohm's law contribution
    # across diode included, see Tyndall Notebook 2353, page 100
    # (k_{B} / q) = 8.61733e-5 [J / C K]
    # series resistance needs to have negative sign for some reason
    # what does eye0 represent? Bias saturation current

    # For this function to work you need to use np.log, not math.log!!!

    # need to define temperature as a global variable so that it gets assigned when function is called
    T_term = 8.61733e-5*Common.convert_C_K(T) # at T = 25 C T_term = 0.0256926 [J/C]
    
    return ( eta*T_term*np.log( 1.0 + x*eye0 ) - rs*x )

def diode_fit(hor_data, vert_data, T):
    # fit the diode voltage equation to the data
    # Temperature T is input in units of deg C
    # T is converted to units of K inside function diode_voltage

    from scipy.optimize import curve_fit

    params = ['eta', 'R_{s}', 'I_{0}']

    # lambda function needed to include temperature dependence in fit calculations
    # https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions

    popt, pcov = curve_fit( lambda x, eta, rs, eye0: diode_voltage(x, eta, rs, eye0, T), hor_data, vert_data )

    #print("Fit parameters =",popt
    #print("Fit covariance =",pcov
    #print("eta, rs, I_{0} =", popt[0], -1000*popt[1], 1.0/popt[2]
    #print("eta, rs, I_{0} =", popt[0], popt[1], 1.0/popt[2]

    for i in range(0, len(params), 1):
        if i == 1:
            print(params[i]," =",-1000.0*popt[i]," +/-",1000.0*math.sqrt(abs(pcov[i][i])))
        else:
            print(params[i]," =",popt[i]," +/-",math.sqrt(abs(pcov[i][i])))
    print(" ")

    return popt

def plot_rewired_char_VI_data(loud = False):
    # plot the diode characteristic data that was measured after the device was re-wired
    # R. Sheehan 22 - 2 - 2017

    try:

        vifiles = glob.glob("DFB_VI_Curve_After_Fix_Reverse.txt")

        if vifiles is not None:

            # read the IV data
            current = []
            voltage = []
            for i in range(0, len(vifiles), 1):
                data = Common.read_matrix(vifiles[i], '\t')
                data = Common.transpose_multi_col(data)
                for j in range(0, len(data[0]), 1):
                    voltage.append(data[0][j]) # store current data
                    current.append(data[1][j]*1E+6) # store voltage data
                del data

            #Vvals = [0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5]
            #Ieam132 = [93.46, 56.29, 18.76, -0.04, -18.81, -56.22, -93.38]
            #Ieam146 = [93.45, 56.21, 18.74, -0.04, -18.83, -56.31, -93.45]

            #Vvals2 = [-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
            #Ieam2 = [-96.04, -76.87, -57.74, -38.54, -19.305, -3.30E-02, 19.261, 38.564, 57.82, 76.99, 96.1]

            #Veam = Vvals + Vvals + Vvals2[::-1] # the syntax L[::-1] represents the list in reverse order
            #Ieam = Ieam132 + Ieam146 + Ieam2[::-1]

            # fit a line to the data
            #fit = Common.linear_fit( np.asarray(voltage), np.asarray(current), [0.0, 0.2])

            # plot the data
            fig = plt.figure()
            ax = fig.add_subplot(111)

            #.plot([voltage[0], voltage[-1]], [fit[0] + voltage[0]*fit[1], fit[0] + voltage[-1]*fit[1]], 
            #        labs_lins[1], lw = 2, label = '$I_{DFB}(mA) = %(v1)0.1f V_{DFB}, R = %(v2)0.1f (\Omega)$'%{"v1":fit[1], "v2":1000.0/fit[1]})
            ax.plot(voltage, current, labs[1], lw = 2, label = '$I_{DFB}$')
            #ax.plot(Veam, Ieam, labs_pts[5], lw = 2, label = 'Data Measured Across EAM')

            ax.legend(loc='upper left')
            
            plt.ylabel('Current (nA)', fontsize = 17)
            plt.xlabel('Voltage (V)', fontsize = 17)
    
            plt.title('Characteristic Through RF Connector')
            plt.axis( [-1.0, 0.1, -70, 15.0 ] )
            plt.savefig('DFB_VI_Through_RF_After_Connection_Fixed_Reverse.png')

            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise IOError
            return -1
    except IOError:
        print("Error: TIPS_DFB_SOA_Charact.plot_rewired_char_data()")
        print("No data available to be read")
        return -1

def plot_EAM_transparency(loud = False):

    # plot the measured optical output while the EAM bias is varied
    # DFB and SOA bias are fixed
    # R. Sheehan 5 - 3 - 2017

    try:

        EAM_Curr_mA = [0, 5, 10, 15, 20, 25, 30, 35, 38, 40, 43, 45, 50, 55, 60, 65, 70, 75, 80]
        Pout_V = [0.360, 0.384, 0.496, 0.584, 0.648, 0.704, 0.760, 0.780, 0.840, 0.860, 0.860, 0.860, 0.840, 
              0.820, 0.680, 0.640, 0.520, 0.440, 0.360]

        # read in the detector response data
        resp_file = "C:/Users/Robert/Equipment/Equipment_Manuals/Thorlabs/PDA10D_responsivity.csv"

        resp_data = Common.read_two_columns(resp_file)

        c1 = True if len(EAM_Curr_mA) == len(Pout_V) else False
        c2 = True if resp_data[0] else False
        
        if c1 and c2:

            from scipy import interpolate

            wavelength = 1321.0

            R = interpolate.interp1d(resp_data[1], resp_data[2])

            resp_val = R(wavelength)

            if loud: print("Response at L = ",wavelength," is ",R(wavelength))

            # define conversion factors from known values given by Thorlabs
            Sf = 1.7 # scale factor assuming 50 Ohm termination
            Gt = 5e+3 # transimpedance gain of detector
            conversion_factor = ( R(wavelength) * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW

            # correct the measured voltage data for the dark current of the detector
            Vdark = 0.188 # (V)
            for j in range(0, len(Pout_V), 1):
                Pout_V[j] = (Pout_V[j] - Vdark) / conversion_factor

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(EAM_Curr_mA, Pout_V, labs[0], ms = 10, label = '$I_{SOA} = I_{DFB} = 80 (mA)$')
                        
            ax.legend(loc='best')
            plt.xlabel('$I_{EAM}$ (mA)', fontsize = 17)
            plt.ylabel('$P_{out}$ (mW)', fontsize = 17)
            plt.title('EAM Transparency Bias')
            #plt.axis( [-0.5, 80.5, 0, 0.61] )

            plt.savefig('EAM_Transparency.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise Exception
            return -1
    except Exception:
        print("Error: TIPS_DFB_SOA_Charact.plot_EAM_transparency()")
        if c1 == False: print("Measured data not input correctly")
        if c2 == False: print("Response data not available")
        return -1
    
def plot_LI_for_variable_Isoa():
    # plot the measured LI data as a function of bias while the current across the SOA section is varied
    # R. Sheehan 

    try:

        I_SOA = [0, 60, 120, 180]

        V_DFB = [0.5, 1.0, 1.5, 2.0, 2.5, 2.9]

        P_0 = [-42.213, -42.145, -40.903, -22.348, -18.32, -16.67]
        P_1 = [-30.266, -30.246, -29.562, -7.248, -4.438, -3.573]; ER_1 = [];  
        P_2 = [-22.722, -22.699, -21.883, -1.296, 0.544, 1.197]; ER_2 = []; 
        P_3 = [-19.584, -19.564, -18.747, -0.245, 1.669, 2.261]; ER_3 = []; 

        ER_1 = Common.list_diff(P_1, P_0)
        ER_2 = Common.list_diff(P_2, P_0)
        ER_3 = Common.list_diff(P_3, P_0)

        hv_data = []; labels = []; mark_list = []; 
        hv_data.append([V_DFB, P_0]); labels.append('$I_{SOA}$ = 0 (mA)'); mark_list.append('r*-'); 
        hv_data.append([V_DFB, P_1]); labels.append('$I_{SOA}$ = 60 (mA)'); mark_list.append('g^-'); 
        hv_data.append([V_DFB, P_2]); labels.append('$I_{SOA}$ = 120 (mA)'); mark_list.append('bo-'); 
        hv_data.append([V_DFB, P_3]); labels.append('$I_{SOA}$ = 180 (mA)'); mark_list.append('md-'); 
    
        args = Plotting.plot_arguments()

        args.loud = True
        args.x_label = '$V_{DFB}$ (V)'
        args.y_label = '$P_{DFB}$ (dBm)'
        args.plt_range = [0.4, 3, -45, 3]
        args.crv_lab_list = labels
        args.mrk_list = mark_list
        args.plt_title = '$P_{out}$ variation with SOA current at T = 20 (C)'
        args.fig_name = 'Pout_vs_ISOA.png'

        Plotting.plot_multiple_curves(hv_data, args, False, True)

        hv_data = []; labels = []; mark_list = []; 
        hv_data.append([V_DFB, ER_1]); labels.append('$I_{SOA}$ = 60 (mA)'); mark_list.append('g^-'); 
        hv_data.append([V_DFB, ER_2]); labels.append('$I_{SOA}$ = 120 (mA)'); mark_list.append('bo-'); 
        hv_data.append([V_DFB, ER_3]); labels.append('$I_{SOA}$ = 180 (mA)'); mark_list.append('md-'); 
    
        args = Plotting.plot_arguments()

        args.loud = True
        args.x_label = '$V_{DFB}$ (V)'
        args.y_label = 'ER (dB)'
        args.plt_range = [0.4, 3, 10, 24]
        args.crv_lab_list = labels
        args.mrk_list = mark_list
        args.plt_title = 'ER variation with SOA current at T = 20 (C)'
        args.fig_name = 'ER_vs_ISOA.png'

        Plotting.plot_multiple_curves(hv_data, args, False, True)
    except Exception:
        print("Error: plot_LI_for_variable_Isoa()")

def compare_measured_power_data(loud = False):
    # compare power data from TIPS DFB-EAM-SOA as recorded on two power meters
    # trying to determine the scale factor that makes the measured powers equal
    # R. Sheehan 8 - 3 - 2017

    try:        
        # responsivity data
        wavelength = 1321.0

        # read in the detector response data
        resp_file = "C:/Users/Robert/Equipment/Equipment_Manuals/Thorlabs/PDA10D_responsivity.csv"

        resp_data = Common.read_two_columns(resp_file)

        # Measured Power data
        V = [0.5, 1.0, 1.5, 2.0, 2.5, 2.9]
        P_ILX_60 = [-30.266, -30.246, -29.562, -7.248, -4.438, -3.573]
        P_PDA_60 = [0.204, 0.204, 0.204, 0.94, 1.62, 1.92]

        P_ILX_120 = [-22.722, -22.699, -21.883, -1.296, 0.544, 1.197]
        P_PDA_120 = [0.224, 0.22, 0.228, 3.12, 4.64, 5.2]

        P_ILX_180 = [-19.584, -19.564, -18.747, -0.245, 1.669, 2.261]
        P_PDA_180 = [0.244, 0.244, 0.252, 3.84, 5.68, 6.48]

        c1 = True if len(V) == len(P_ILX_180) else False
        c3 = True if len(V) == len(P_PDA_180) else False
        c2 = True if resp_data[0] else False

        if c1 and c2 and c3:
            from scipy import interpolate

            wavelength = 1321.0

            R = interpolate.interp1d(resp_data[1], resp_data[2])

            resp_val = float( R(wavelength) )

            if loud: print("Response at L = ",wavelength," is ",resp_val)

            # correct the measured voltage data for the dark current of the detector
            Vdark = 0.196 # (V)
            
            # convert P_dBm -> P_mW
            for i in range(0, len(P_ILX_120), 1):
                P_ILX_120[i] = Common.convert_PdBm_PmW(P_ILX_120[i])

            determine_scale_factor(P_ILX_120, P_PDA_120, resp_val, Vdark, True)

        else:
            raise Exception
    except:
        print("Error: TIPS_DFB_SOA_Charact.compare_measured_power_data()")
        return -1

def determine_scale_factor(P_ILX_mW, P_PDA_V, resp_val, Vdark, loud = True):
    # search for the scale factor that ensures that conversion of P_PDA_V into mW scale 
    # matches data provided by P_ILX_mW
    # R. Sheehan 8 - 3 - 2017

    try:

        if len(P_ILX_mW) == len(P_PDA_V) and resp_val > 0.0:
            # define conversion factors from known values given by Thorlabs
            
            Gt = 5e+3 # transimpedance gain of detector

            Sf_min = 0.5 # scale factor
            Sf_max = 3.0
            delta_Sf = 0.05

            Sf_vals = []
            Err_vals = []

            Sf = Sf_min
            while Sf < Sf_max:                
                # convert V -> mW
                conversion_factor = ( resp_val * Sf * Gt ) / 1000.0 # divide by 1000 to convert to mW
               
                P_PDA_mW = []
                for j in range(0, len(P_PDA_V), 1):
                    P_PDA_mW.append( (P_PDA_V[j] - Vdark) / conversion_factor )

                # compute difference between P_PDA_V(mW) and P_ILX_mW
                diff = []
                for j in range(0, len(P_ILX_mW), 1):
                    diff.append(math.fabs(P_ILX_mW[j] - P_PDA_mW[j]))

                #print("Sf =",Sf,"Err =",max(diff)

                Sf_vals.append(Sf)
                Err_vals.append(max(diff))

                Sf = Sf + delta_Sf

            # Find index of minimum error value
            min_err = min(Err_vals)
            min_err_indx = Err_vals.index(min_err)
            Sf_true = Sf_vals[min_err_indx]

            print("True Sf =",Sf_true)

            # plot Err versus Sf to determine location of minimum error
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(Sf_vals, Err_vals, labs[0], ms = 10, label = "Min(Err) => Sf = %(v1)0.2f"%{"v1":Sf_true})
                        
            ax.legend(loc='best')
            plt.xlabel('Scale Factor', fontsize = 17)
            plt.ylabel('Error', fontsize = 17)
            plt.title('Min Error => Correct Scale Factor')
            #plt.axis( [-0.5, 80.5, 0, 0.61] )

            plt.savefig('Scale_Factor.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise Exception
    except:
        print("Error: TIPS_DFB_SOA_Charact.determine_scale_factor()")
        return -1

def plot_spectrum_temperature():
    # plot the measured optical spectrum at different temperatures
    # make sure to show the noise floor also. 
    # R. Sheehan 10 - 4 - 2017

    try:
        if os.path.isdir("Spectra_Temperature_High_Res/"):
            os.chdir("Spectra_Temperature_High_Res/")

            print(os.getcwd())

            files = glob.glob("LDAT_T_*_V_260.txt")

            if files is not None:

                plt_title = ""
                plt_range = [1315, 1330, -63, -0.0]
                fig_name = "Optical_Spectrum.png"
                loud = True
                #delim = '\t'
                delim = ','

                fig = plt.figure()
                ax = fig.add_subplot(111)

                cnt = 0
                for f in files:
                    if '25' not in f and '35' not in f and '45' not in f:
                        numbers = Common.extract_values_from_string(f)

                        spectrum = Common.read_matrix(f, delim)
                        spectrum = Common.transpose_multi_col(spectrum)

                        ax.plot(spectrum[0], spectrum[1], labs_lins[cnt], lw = 2, label = 'T = %(v1)s (C)'%{"v1":numbers[0]})

                        del spectrum
                        cnt += 1

                ax.legend(loc='upper right')            
                plt.xlabel('Wavelength (nm)', fontsize = 17)
                plt.ylabel('Spectral Power (dBm/0.05 nm)', fontsize = 17)

                if plt_title is not "": plt.title(plt_title)
                if plt_range is not None: plt.axis( plt_range )

                # See http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow for arrow properties
                # also http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate
                #ax.arrow(1320.5, -50, 0, 37, head_width=0.2, head_length=0.5, fc='k', ec='k')
                plt.annotate(s='', xy=(1321.0, -49), xytext=(1321.0,-0.7), arrowprops=dict(arrowstyle='<->'))
                plt.text(1320.25, -20, r'SMSR > 45 (dB)', fontsize=14, color = 'black', rotation = 90)

                if fig_name is not "": plt.savefig(fig_name)
                if loud: plt.show()
                plt.clf()
                plt.cla()
                plt.close()

            else:
                print("Error: No files found")
                raise Exception

            os.chdir('..')
            print(os.getcwd())
        else:
            print("Error: directory Spectra_Temperature/ does not exist")
            raise Exception
    except Exception:
        print("Error: TIPS_DFB_SOA_Charact.plot_spectrum_temperature()")

def plot_data_temperature(fname, scale = False, x_lab = "", y_lab = "", plt_title = "", plt_range = None, fig_name = "", loud = False):
    # plot the measured current voltage data as a function of temperature
    # R. Sheehan 11 - 4 - 2017

    try:
        if glob.glob(fname):
            
            delim = ','
            numbers = ['20', '25', '30', '35', '40']
            data = Common.read_matrix(fname, delim)
            data = Common.transpose_multi_col(data)

            if scale and "IV" in fname:
                # scale current data to (mA)
                for i in range(1, len(data), 1):
                    for j in range(0, len(data[i]), 1):
                        data[i][j] *= 1000.0

            if scale and "LV" in fname:
                # scale current data to (mA)
                for i in range(1, len(data), 1):
                    for j in range(0, len(data[i]), 1):
                        data[i][j] = Common.convert_PdBm_PmW(data[i][j])

                # write the converted data to a txt file
                Common.write_matrix("LV_Data_Temperature.txt", data)

            fig = plt.figure()
            ax = fig.add_subplot(111)

            for i in range(1, len(data), 1):
                ax.plot(data[0], data[i], labs[i-1], lw = 2, label = 'T = %(v1)s (C)'%{"v1":numbers[i-1]})

            ax.legend(loc='upper left')            
            if x_lab is not "": plt.xlabel(x_lab, fontsize = 17)
            if x_lab is not "": plt.ylabel(y_lab, fontsize = 17)

            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )

            # See http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow for arrow properties
            # also http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate
            #ax.arrow(1320.5, -50, 0, 37, head_width=0.2, head_length=0.5, fc='k', ec='k')
            #plt.annotate(s='', xy=(1320.7, -50), xytext=(1320.7,-12.2), arrowprops=dict(arrowstyle='<->'))
            #plt.text(1320.25, -25, r'SMSR > 38 (dB)', fontsize=14, color = 'black', rotation = 90)

            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            print("Could not find file",fname)
            raise Exception
    except Exception:
        print("Error: TIPS_DFB_SOA_Charact.plot_data_temperature()")

def Re_Plot_Measured_Optical_Power():
    # plot the newly measured output power versus DFB bias for different temperatures and SOA biases
    # R. Sheehan 19 - 7 - 2017

    THE_DATA = "TIPS_DFB_SOA_LI_Curves_July_2017/"

    try:
        if os.path.isdir(THE_DATA):
            os.chdir(THE_DATA)

            print(os.getcwd())

            # for this set of measurements I_EAM = 40.1

            # originial data set
            V_DFB = [0.5, 1.0, 1.5, 2.0, 2.5, 2.9]

            P_0 = [-42.213, -42.145, -40.903, -22.348, -18.32, -16.67]
            P_1 = [-30.266, -30.246, -29.562, -7.248, -4.438, -3.573]; 
            P_2 = [-22.722, -22.699, -21.883, -1.296, 0.544, 1.197]; 
            P_3 = [-19.584, -19.564, -18.747, -0.245, 1.669, 2.261]; 

            orig_data = []; labels = []; mark_list = []; 
            orig_data.append([V_DFB, P_0]); labels.append('$I_{SOA}$ = 0 (mA)'); mark_list.append('r*-'); 
            orig_data.append([V_DFB, P_1]); labels.append('$I_{SOA}$ = 60 (mA)'); mark_list.append('g^-'); 
            orig_data.append([V_DFB, P_2]); labels.append('$I_{SOA}$ = 120 (mA)'); mark_list.append('bo-');
            orig_data.append([V_DFB, P_3]); labels.append('$I_{SOA}$ = 180 (mA)'); mark_list.append('md-'); 

            # plot the power variation with I_SOA for the newly measured data
            I_SOA_Vals = [0, 60, 120]

            T = 20

            delim = '\t'

            mark_list = labs; 

            current_data = []; power_data = []; power_data_lin = []; labels = []; 
            for i in range(0, len(I_SOA_Vals), 1):
                file = "Volt_Pow_T_%(v1)d_ISOA_%(v2)d.txt"%{"v1":T, "v2":I_SOA_Vals[i]}
                if glob.glob(file):
                    data = Common.read_matrix(file, delim)
                    data = Common.transpose_multi_col(data)

                    current_data.append([data[0], data[1]])
                    power_data.append([data[0], data[2]])
                    power_data_lin.append([data[0], Common.list_convert_dBm_mW(data[2])])

                    labels.append('$I_{SOA}$ = %(v2)d (mA)'%{"v2":I_SOA_Vals[i]})

            args = Plotting.plot_arguments()

            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (dBm)'
            args.plt_range = [0.0, 3.2, -43, 3]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{out}$ variation with SOA current at T = 20 (C)'
            args.fig_name = 'Pout_vs_ISOA_dBm.png'

            Plotting.plot_multiple_curves(power_data, args, False, True)

            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (mW)'
            args.plt_range = [0.0, 3.2, 0, 1.5]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{out}$ variation with SOA current at T = 20 (C)'
            args.fig_name = 'Pout_vs_ISOA_mW.png'

            Plotting.plot_multiple_curves(power_data_lin, args, False, True)

            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$I_{DFB}$ (mA)'
            args.plt_range = [0.0, 3.5, 0.0, 200]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$I_{DFB}$ variation with SOA current at T = 20 (C)'
            args.fig_name = 'IDFB_vs_ISOA.png'

            Plotting.plot_multiple_curves(current_data, args, False, True)

            # plot a comparison of the original data with the new data
            hv_data = []; mark_list = []; labels = [];  
            for i in range(0, len(I_SOA_Vals), 1):
                hv_data.append(orig_data[i]); mark_list.append(labs_lins[i]); labels.append('$I_{SOA}$ = %(v2)d (mA) Old'%{"v2":I_SOA_Vals[i]})
                hv_data.append(power_data[i]); mark_list.append(labs_dashed[i]); labels.append('$I_{SOA}$ = %(v2)d (mA) New'%{"v2":I_SOA_Vals[i]})

            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (dBm)'
            args.plt_range = [0.0, 3.2, -43, 3]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{out}$ variation with SOA current at T = 20 (C)'
            args.fig_name = 'Pout_vs_ISOA_dBm_Compare.png'

            Plotting.plot_multiple_curves(hv_data, args, False, True)

            # Compute the difference between each data set

            from scipy import interpolate

            #R = interpolate.interp1d(resp_data[1], resp_data[2])

            #resp_val = R(wavelength)

            diff_data = []; labels = []; mark_list = labs
            for i in range(0, len(I_SOA_Vals), 1):
                
                #R = interpolate.interp1d(power_data[i][0], power_data[i][1])

                new_mW = Common.list_convert_dBm_mW(power_data[i][1]) # convert dBm data to mW
                R = interpolate.interp1d(power_data[i][0], new_mW)

                diff = []
                for j in range(0, len(orig_data[i][0]), 1):
                    
                    #new_val = R(orig_data[i][0][j])
                    #print(orig_data[i][1][j],",",new_val,",",orig_data[i][1][j] - new_val
                    #diff.append(orig_data[i][1][j] - new_val)

                    old_mW = Common.list_convert_dBm_mW(orig_data[i][1])
                    new_val = R(orig_data[i][0][j])
                    #print(old_mW[j],",",new_val,",",old_mW[j] - new_val
                    diff.append(old_mW[j] - new_val)

                diff_data.append([orig_data[i][0], diff]); labels.append('$I_{SOA}$ = %(v2)d (mA)'%{"v2":I_SOA_Vals[i]})

            args.loud = True
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$\Delta P_{DFB}$ (mW)'
            args.plt_range = [1.7, 3.2, 0, 0.16]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{out}$ variation with SOA current at T = 20 (C)'
            args.fig_name = 'Pout_vs_ISOA_mW_Difference.png'

            Plotting.plot_multiple_curves(diff_data, args, False, True)

            # plot the power variation with temperature
            T_vals = [20, 25, 30, 35]

            #import and store the original data set
            delim = ','
            fname = "DFB_LV_Temperature.csv"
            orig_data_temp = []; 
            
            data = Common.read_matrix(fname, delim)
            data = Common.transpose_multi_col(data)  
            for i in range(0, len(T_vals), 1):
                orig_data_temp.append([data[0], data[i+1]])

            I_SOA = 62

            delim = '\t'
            power_data_temp = []; labels = [];
            for i in range(0, len(T_vals), 1):
                file = "Volt_Pow_T_%(v1)d_ISOA_%(v2)d.txt"%{"v1":T_vals[i], "v2":I_SOA}
                if glob.glob(file):
                    data = Common.read_matrix(file, delim)
                    data = Common.transpose_multi_col(data)
                    
                    power_data_temp.append([data[0], data[2]])
                    labels.append("T = %(v1)d (C)"%{"v1":T_vals[i]})

            # plot variation of power with temperature
            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (dBm)'
            args.plt_range = [0.0, 3.2, -33, -3]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{DFB}$ variation with Temperature at $I_{SOA}$ = 62 (mA)'
            args.fig_name = 'PDFB_vs_Temperature.png'

            Plotting.plot_multiple_curves(power_data_temp, args, False, True)

            # plot a comparison of the original data with the new data
            hv_data = []; mark_list = []; labels = []
            for i in range(0, len(T_vals), 1):
                hv_data.append(orig_data_temp[i]); mark_list.append(labs_lins[i]); labels.append("T = %(v1)d (C) Old"%{"v1":T_vals[i]})
                hv_data.append(power_data_temp[i]); mark_list.append(labs_dashed[i]); labels.append("T = %(v1)d (C) New"%{"v1":T_vals[i]})
                
            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (dBm)'
            args.plt_range = [1.7, 3.2, -33, -2.8]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{DFB}$ variation with Temperature at $I_{SOA}$ = 62 (mA)'
            args.fig_name = 'PDFB_vs_Temperature_Compare.png'

            Plotting.plot_multiple_curves(hv_data, args, False, True)

            # What is the actual difference in power?
            diff_data = []; labels = []; mark_list = labs
            for i in range(0, len(T_vals), 1):

                #R = interpolate.interp1d(power_data_temp[i][0], power_data_temp[i][1])

                new_mW = Common.list_convert_dBm_mW(power_data_temp[i][1])                
                R = interpolate.interp1d(power_data_temp[i][0], new_mW)

                diff = []
                for j in range(0, len(orig_data_temp[i][0]), 1):                    
                    
                    #new_val = R(orig_data_temp[i][0][j])                    
                    #print(orig_data_temp[i][1][j],",",new_val,",",orig_data_temp[i][1][j] - new_val
                    #diff.append(orig_data_temp[i][1][j] - new_val)
                    
                    old_mW = Common.list_convert_dBm_mW(orig_data_temp[i][1])
                    new_val = R(orig_data_temp[i][0][j]) 
                    #print(old_mW[j],",",new_val,",",old_mW[j] - new_val
                    diff.append(old_mW[j] - new_val)

                diff_data.append([orig_data_temp[i][0], diff]); labels.append("T = %(v1)d (C)"%{"v1":T_vals[i]})

            args.loud = True
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$\Delta P_{DFB}$ (mW)'
            args.plt_range = [2.0, 3.0, 0, 0.06]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{DFB}$ variation with Temperature at $I_{SOA}$ = 62 (mA)'
            args.fig_name = 'PDFB_vs_Temperature_mW_Difference.png'

            Plotting.plot_multiple_curves(diff_data, args, False, True) 

            # plot P_DFB versus Temperature on linear scale
            for i in range(0, len(power_data_temp), 1):
                power_data_temp[i][1] = Common.list_convert_dBm_mW(power_data_temp[i][1])

            args.loud = False
            args.x_label = '$V_{DFB}$ (V)'
            args.y_label = '$P_{DFB}$ (mW)'
            args.plt_range = [0.0, 3.2, 0, 0.5]
            args.crv_lab_list = labels
            args.mrk_list = mark_list
            args.plt_title = '$P_{DFB}$ variation with Temperature at $I_{SOA}$ = 62 (mA)'
            args.fig_name = 'PDFB_vs_Temperature_mW.png'

            Plotting.plot_multiple_curves(power_data_temp, args, False, True)

            os.chdir('..')
            print(os.getcwd())
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Re_Plot_Measured_Optical_Power()")
        print("Error: Directory",THE_DATA,"does not exist")
    except Exception:
        print("Error: Re_Plot_Measured_Optical_Power()")
