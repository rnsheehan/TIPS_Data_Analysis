import os
import glob
import re
import sys # access system routines

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt

import Common

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks' ] # plot labels

def Make_TIPS_FR(): 
    # call the TIPS FR plotting routines
    # R. Sheehan 1 - 3 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/"
    
    #os.chdir("TIPS_FR_1_3_2017/DFB_Response/")

    os.chdir(DATA_HOME)

    print(os.getcwd())

    #plot_f3dB_current(True)

    #plot_f3dB_current_temp(True)

    #plot_Vpp_variation_with_attenuation(True)

    make_comparison_plot()

    #os.chdir("TIPS_FR_31_3_2017/")
    #dir_name = "T_20/"
    #s_param = 3
    #plot_all_s2p_files(dir_name, s_param, True, True)

    #plot_f3dB_power(True)

    #os.chdir("TIPS_FR_31_3_2017/")
    #os.chdir("T_25/")
    #the_file = "ISOA_62_IEAM_40_VDFB_26_T_25.s2p"
    #s_param = 2
    #curve_label = 'V_{DFB} = 2.6 (V)'
    #plt_title = 'RF Reflection'
    #plt_range = None
    #fig_name = the_file.replace('.s2p','.png')

    #the_data = read_s2p_file(the_file)

    #plot_s2p_data(the_data, s_param, curve_label, plt_title, plt_range, fig_name, True)

    return 0

def make_comparison_plot():

    delimiter = " "

    os.chdir("TIPS_FR_31_3_2017/T_25/")

    filename = "ISOA_62_IEAM_40_VDFB_17_T_25.s2p"
    data_1 = read_s2p_file(filename, delimiter, True)

    filename = "ISOA_62_IEAM_40_VDFB_26_T_25.s2p"
    data_2 = read_s2p_file(filename, delimiter, True)

    s_param = 3

    plot_compare_s2p_data(data_1, data_2, s_param, True)

    os.chdir('..')

def plot_f3dB_current(loud = False):
    # plot the measured f3dB as a function of current
    # R. Sheehan 1 - 3 - 2017

    try:

        Isoa = 160 # (mA)
        T = 20 # (C)

        Idfb = [70, 80, 100, 110, 120, 130, 140, 150, 160, 180]
        f3dB1 = [1.836, 3.445, 5.075, 7.376, 6.883, 7.575, 7.677, 7.894, 7.406, 7.376]

        if len(Idfb) == len(f3dB1):

            params_20 = Common.linear_fit( np.asarray(Idfb), np.asarray(f3dB1), [0.0, 5.0])

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(Idfb, f3dB1, labs_pts[0], markersize = 10, label = '$I_{SOA}$ = %(v1)0.0f (mA), T = %(v2)0.0f (C)'%{"v1":Isoa, "v2":T})

            ax.legend(loc='lower right')
            plt.xlabel('$I_{DFB}$ (mA)', fontsize = 17)
            plt.ylabel('$f_{3dB}$ (GHz)', fontsize = 17)
            plt.title('TIPS DFB Frequency Response')
            plt.axis( [65, 185, 1, 8] )

            plt.savefig('TIPS_DFB_FR.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise RuntimeError
            return -1
    except RuntimeError:
        print("Error: TIPS_FR_Analysis.plot_f3dB_current()")
        print("Arrays being plotted are not the same length")
        return -1

    return 0

def plot_f3dB_current_temp(loud = False):
    # plot the measured f3dB as a function of current
    # R. Sheehan 1 - 3 - 2017

    try:

        Isoa_20 = [140, 150, 160, 170, 180]
        f3dB_20 = [6.938, 6.865, 6.883, 6.92, 6.783]

        Isoa_25 = [160, 170, 180]
        f3dB_25 = [7.308, 7.366, 7.202]

        if len(Isoa_20) == len(f3dB_20) and len(Isoa_25) == len(f3dB_25):

            params_20 = Common.linear_fit( np.asarray(Isoa_20), np.asarray(f3dB_20), [0.0, 5.0])

            params_25 = Common.linear_fit( np.asarray(Isoa_25), np.asarray(f3dB_25), [0.0, 5.0])

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot([140, 180], [params_20[0] + params_20[1]*140, params_20[0] + params_20[1]*180], labs_lins[0], lw = 2, label = 'T = 20 (C)')
            ax.plot(Isoa_20, f3dB_20, labs_pts[0], markersize = 10)
            ax.plot([160, 180], [params_25[0] + params_25[1]*160, params_25[0] + params_25[1]*180], labs_lins[1], lw = 2, label = 'T = 25 (C)')
            ax.plot(Isoa_25, f3dB_25, labs_pts[1], markersize = 8)

            ax.legend(loc='lower left')
            plt.xlabel('$I_{SOA}$ (mA)', fontsize = 17)
            plt.ylabel('$f_{3dB}$ (GHz)', fontsize = 17)
            plt.title('TIPS DFB Frequency Response $I_{DFB}$ = 120 (mA)')
            plt.axis( [135, 185, 6.6, 7.6] )

            plt.savefig('TIPS_DFB_FR_Temperature.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise RuntimeError
            return -1
    except RuntimeError:
        print("Error: TIPS_FR_Analysis.plot_f3dB_current_temp()")
        print("Arrays being plotted are not the same length")
        return -1

    return 0

def plot_Vpp_variation_with_attenuation(loud = False):
    # plot the measured Vpp variation with varying amounts of attenuation
    # experiment configuration described in notebook 2715, pages 40 - 45
    # there is, by default, a 20 dB attenuator placed on the detector
    # the extra attenuation is added after the amplifier
    # R. Sheehan 5 - 3 - 2017

    BPG_RF_Amp = [200, 230, 260, 290, 320, 350, 370] # RF Vpp output from SHF-BPG
    Vpp_0dB = [5.417, 5.907, 6.204, 6.392, 6.5, 6.572, 6.6] # RF Vpp as measured after amplification on DCA
    Vpp_10dB = [1.7497, 1.9116, 2.0101, 2.034, 2.1045, 2.125, 2.133]
    Vpp_13dB = [1.2509, 1.366, 1.438, 1.478, 1.505, 1.5201, 1.527]
    Vpp_16dB = [0.8983, 0.9808, 1.030, 1.06, 1.0794, 1.0907, 1.096]

    try:
        c1 = True if len(BPG_RF_Amp) == len(Vpp_0dB) else False
        c2 = True if len(BPG_RF_Amp) == len(Vpp_10dB) else False
        c3 = True if len(BPG_RF_Amp) == len(Vpp_13dB) else False
        c4 = True if len(BPG_RF_Amp) == len(Vpp_16dB) else False

        if c1 and c2 and c3 and c4:
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(BPG_RF_Amp, Vpp_0dB, labs[0], ms = 10, label = '20 (dB)')
            ax.plot(BPG_RF_Amp, Vpp_10dB, labs[1], ms = 8, label = '30 (dB)')
            ax.plot(BPG_RF_Amp, Vpp_13dB, labs[2], ms = 10, label = '33 (dB)')
            ax.plot(BPG_RF_Amp, Vpp_16dB, labs[3], ms = 8, label = '36 (dB)')
            
            ax.legend(loc='best')
            plt.xlabel('SHF BPG $V_{pp}$ (mV)', fontsize = 17)
            plt.ylabel('DCA Measured $V_{pp}$ (V)', fontsize = 17)
            #plt.title('TIPS DFB Frequency Response $I_{DFB}$ = 120 (mA)')
            plt.axis( [195, 375, 0, 7] )

            plt.savefig('DCA_Measured_Vpp.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise Exception
            return -1
    except Exception:
        print("Error: TIPS_FR_Analysis.plot_Vpp_variation_with_attenuation()")
        return -1

def read_s2p_file(s2pfile, delimiter = " ", loud = False):
    # method for reading the data in an s2p file
    # for more info see 
    # http://na.support.keysight.com/plts/help/WebHelp/FilePrint/SnP_File_Format.htm 
    # http://na.support.keysight.com/pna/help/WebHelp7_5/S1_Settings/Data_Format_and_Scale

    # Lines that contain symbol ! are comment lines
    # Lines that contain symbol # are option lines

    # R. Sheehan 2 - 4 - 2017

    try:
        if glob.glob(s2pfile):

            thefile = file(s2pfile,"r") # open file for reading

            # file is available for reading
            thedata = thefile.readlines() # read the data from the file

            nrows = Common.count_lines(thedata, s2pfile) # count the number of rows

            if loud: 
                print("%(path)s is open"%{"path":s2pfile})
                print("Nrows = ",nrows)

            # s2p file consists of header data followed by complex S_{ij} frequency response data in the form
            # frequency S_{11}^{real} S_{11}^{imag} S_{12}^{real} S_{12}^{imag} S_{21}^{real} S_{21}^{imag} S_{22}^{real} S_{22}^{imag}
            # or it could be exported in dB scale with phase data
            # frequency log mag. S_{11} (dB) S_{11}^{phase} log mag. S_{12} (dB) S_{12}^{phase} log mag. S_{21} (dB) S_{21}^{phase} log mag. S_{22} (dB) S_{22}^{phase}

            # lists to store the retrieved data
            # to be honest I'm only interested in the log mag data
            Frequency = []; options = ""
            S11 = []; S21 = [];
            S12 = []; S22 = [];

            f_3dB = 0.0; S12_3dB = 0.0;

            cnt = 0; fcnt = 0;
            Rmax = -200.0; tmp = 0.0; indx = 0
            for line in thedata:
                parameters = line.split(delimiter)

                if "#" in line: options = line

                if Common.isfloat(parameters[0]):
                    # store the data
                    Frequency.append( float( parameters[0] )/1.0e+9 )
                    S11.append( float( parameters[1] ) )
                    S12.append( float( parameters[3] ) )
                    S21.append( float( parameters[5] ) )
                    S22.append( float( parameters[7] ) )

                    # find the max S_{11} value, max RF reflection from DUT
                    tmp = float( parameters[1] )
                    if tmp > Rmax: Rmax = tmp; indx_Rmax = indx

                    # set the 3_dB limit value
                    if fcnt == 0: 
                        S12_3dB = float( parameters[3] ) - 3.0
                        fcnt = 1

                    # check if the 3dB limit is reached
                    #if fcnt == 1 and abs(float( parameters[3] ) - S12_3dB) < 1.0e-6:
                    #    f_3dB = float( parameters[0] )/1.0e+9
                    #    print("f3dB =",f_3dB,"(GHz)"
                    #    fcnt = 2

                    # check if the 3dB limit is reached
                    if fcnt == 1 and float( parameters[3] ) < S12_3dB:
                        f_3dB = float( parameters[0] )/1.0e+9
                        if loud: print("f3dB =",f_3dB,"(GHz)")
                        fcnt = 2

                    indx += 1
                    
            # f_3dB > 50 (GHz), will you ever see the day?
            if fcnt == 1: f_3dB = 50.0
            
            s2p_dict = {'Options':options, 'f_3dB':f_3dB, 'S_3dB':S12_3dB, 'f_Rmax':Frequency[indx_Rmax], 'Rmax':Rmax}

            return [s2p_dict, Frequency, S11, S12, S21, S22]
        else:
            print("Error: Cannot find ",filename)
            raise Exception
    except Exception:
        print("Error: TIPS_FR_Analysis.read_s2p_file")
        return None

def plot_s2p_data(s2p_data, s_param = 3, curve_label = "", plt_title = "", plt_range = None, fig_name = "", loud = False):
    # plot some measured S_{ij} that has been read from an s2p file
    # assumes DUT is connected to port 1 and Rx is connected to port 2
    # s2p_data comprises a list with elements of the form
    # s2p_data[0] = dictonary that contains information on the data set
    # s2p_data[1] = Frequency (GHz)
    # s2p_data[2] = S_{11} (dB), use this to plot RF reflection from DUT
    # s2p_data[3] = S_{12} (dB), use this to plot FR of DUT
    # s2p_data[4] = S_{21} (dB), use this to plot X-Talk between DUT and Rx
    # s2p_data[5] = S_{22} (dB), use this to plot RF reflection from Rx

    # s_param is an integer equal to 2,3,4,5 that specifies what data should be plotted
    # curve_label is a string applied to the curve being plotted
    # plt_title is a string in the figure, this can be empty
    # plt_range is a list that specifies the boundary of the plot region
    # fig_name is a string that specifies the name of the file where the plot will be saved

    # R. Sheehan 3 - 4 - 2017

    try:
        if s2p_data is not None:

            # re-set s_param value if it has been entered incorrectly
            # default plot will be the S_{12} data
            if s_param < 2 or s_param > 5: s_param = 3

            # set the y-label accoring to what's being plotted
            if s_param == 2: y_label = '$S_{11}$ (dB)'
            elif s_param == 3: y_label = '$S_{12}$ (dB)'
            elif s_param == 4: y_label = '$S_{21}$ (dB)'
            elif s_param == 5: y_label = '$S_{22}$ (dB)'
            else: y_label = '$S_{12}$ (dB)'

            # make the plot
            fig = plt.figure()
            ax = fig.add_subplot(111)

            if curve_label is not "":
                ax.plot(s2p_data[1], s2p_data[s_param], labs_lins[0], lw = 2, label = curve_label)
                ax.legend(loc='upper left')
            else:
                ax.plot(s2p_data[1], s2p_data[s_param], labs_lins[0], lw = 2)
            
            plt.xlabel('Freq. (GHz)', fontsize = 17)
            plt.ylabel(y_label, fontsize = 17)
            
            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )

            # f_3dB embellishment
            if plt_range is not None:
                x1 = 0.01; x2 = s2p_data[0]['f_3dB']; val = s2p_data[0]['S_3dB'];
                plt.hlines(val, x1, x2, 'k', 'dashed', lw = 2)     
                        
                y1 = plt_range[2]; y2 = val
                plt.vlines(x2, y1, y2, 'k', 'dashed', lw = 2)

                plt.text(1, s2p_data[0]['S_3dB']-3, r'$f_{3dB}$ = %(v1)0.2f (GHz)'%{"v1":s2p_data[0]['f_3dB']}, 
                         fontsize=14, color = 'black')

            # plot endmatter
            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            print("Cannot plot data that is not there")
            raise Exception
    except Exception:
        print("Error: TIPS_FR_Analysis.plot_s2p_data()")

def plot_compare_s2p_data(s2p_data_1, s2p_data_2, s_param, loud = False):
    # plot some measured S_{ij} that has been read from an s2p file
    # assumes DUT is connected to port 1 and Rx is connected to port 2
    # s2p_data comprises a list with elements of the form
    # s2p_data[0] = dictonary that contains information on the data set
    # s2p_data[1] = Frequency (GHz)
    # s2p_data[2] = S_{11} (dB), use this to plot RF reflection from DUT
    # s2p_data[3] = S_{12} (dB), use this to plot FR of DUT
    # s2p_data[4] = S_{21} (dB), use this to plot X-Talk between DUT and Rx
    # s2p_data[5] = S_{22} (dB), use this to plot RF reflection from Rx
    # R. Sheehan 3 - 4 - 2017

    try:
        if s2p_data_1 is not None and s2p_data_2 is not None:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(s2p_data_1[1], s2p_data_1[3], labs_lins[0], lw = 2, 
                    label = 'Noise Floor')
            ax.plot(s2p_data_2[1], s2p_data_2[3], labs_lins[1], lw = 2, 
                    label = 'V = 2.6 (V)')
            ax.legend(loc='upper right')
            plt.xlabel('Freq. (GHz)', fontsize = 17)
            plt.ylabel('$S_{21}$ (dB)', fontsize = 17)
            plt.title('DFB Frequency Response')
            plt.axis( [0.01, 20, -80, 0] )

            #x1 = 0.01; x2 = s2p_data_1[0]['f_3dB']; val = s2p_data_1[0]['S_3dB'];
            #plt.hlines(val, x1, x2, 'k', 'dashed', lw = 2) 
            
            #y1 = -40; y2 = val
            #plt.vlines(x2, y1, y2, 'k', 'dashed', lw = 2)

            #plt.text(1, s2p_data_1[0]['S_3dB']-2, r'$f_{3dB}$ = %(v1)0.2f (GHz)'%{"v1":s2p_data_1[0]['f_3dB']}, fontsize=14, color = 'black')

            x1 = 0.01; x2 = s2p_data_2[0]['f_3dB']; val = s2p_data_2[0]['S_3dB'];
            plt.hlines(val, x1, x2, 'k', 'dashed', lw = 2) 
            
            y1 = -80; y2 = val
            plt.vlines(x2, y1, y2, 'k', 'dashed', lw = 2)
            plt.text(1, s2p_data_2[0]['S_3dB']-5, r'$f_{3dB}$ = %(v1)0.2f (GHz)'%{"v1":s2p_data_2[0]['f_3dB']}, fontsize=14, color = 'black')

            plt.savefig('TIPS_DFB_FR_Noise.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            print("Cannot plot data that is not there")
            raise Exception
    except Exception:
        print("Error: TIPS_FR_Analysis.plot_s2p_data()")

def plot_all_s2p_files(dir_name, s_param = 3, gather_f3dB = True, loud = False):
    # plot all the s21 data in a given directory
    # dir_name is a string that holds the name of a given directory
    # s_param is the integer that specifies what is to be plotted
    # gather_f3dB is a Boolean that specified whether or not the 3dB data from each file should be stored
    # R. Sheehan 3 - 4 - 2017

    try:
        if os.path.isdir(dir_name):
            # move to directory that contains s2p files
            os.chdir(dir_name)

            print(os.getcwd())

            # find names of all s2p files
            s2p_files = glob.glob("*.s2p")

            plt_tit = "Frequency Response"

            if s2p_files is not None:

                if gather_f3dB:
                    V = [] # list to hold all the bias data
                    f = [] # list to hold all the 3dB frequency data

                for file in s2p_files:

                    file_nums = Common.extract_values_from_string(file)
                    bias = float(file_nums[2])/10.0
                    crv_lbl = "$V_{DFB}$ = %(v1)0.1f (V)"%{"v1":bias}                    
                    fig_name = file.replace(".s2p",".png")

                    s2p_data = read_s2p_file(file)

                    if gather_f3dB:
                        V.append(bias)
                        f.append(s2p_data[0]['f_3dB'])

                    plot_s2p_data(s2p_data, s_param, crv_lbl, plt_tit, [0.01, 15, -80.0, 0.0], fig_name)

                    del s2p_data; del file_nums; 

                if gather_f3dB and V is not None and f is not None:
                    # export the BW versus Bias data
                    Common.write_data("V_DFB.txt",V)
                    Common.write_data("f_3dB.txt",f)

                    # plot the f3dB data versus bias
                    Common.plot_this(V, f, "", "$V_{DFB}$ (V)", "$f_{3dB}$ (GHz)", "BW versus Bias", None, "BW_Bias.png", True)

                    del V; del f; 
            else:
                print(dir_name," contains no s2p files")
                raise Exception

            del s2p_files

            os.chdir('..') # return to previous directory

            print(os.getcwd())
        else:
            print(dir_name," is not a valid directory")
            raise Exception
    except Exception:
        print("Error: TIPS_FR_Analysis.plot_all_s2p_files")

def plot_f3dB_power(loud = False):
    # plot the 3dB BW versus square root optical power
    # all things going well it should be a straight line relationship
    # R. Sheehan 11 - 4 - 2017

    try:
        from scipy import interpolate

        power_name = "C:/Users/Robert/Research/EU_TIPS/Data/TIPS_Characterisation_Feb_2017/DFB_LV_Temperature.csv"

        fname = "f_3dB.txt"
        vname = "V_DFB.txt"

        #temperatures = [20, 25, 30]
        temperatures = [25]

        if glob.glob(power_name):

            # read the power data
            power_data = Common.read_matrix(power_name)
            power_data = Common.transpose_multi_col(power_data)

            os.chdir("TIPS_FR_31_3_2017/")

            print(os.getcwd())

            # read the bandwidth data
            f_data = []
            v_data = []

            for T in temperatures:

                dir_name = "T_%(v1)d/"%{"v1":T}

                if os.path.isdir(dir_name):
                    os.chdir(dir_name)

                    print(os.getcwd())
                    
                    fdata = Common.read_data(fname) # read frequency data in (GHz)
                    vdata = Common.read_data(vname) # read voltage data in (V)

                    f_data.append(fdata)
                    v_data.append(vdata)

                    os.chdir("..")

            # make a plot of the frequency versus square root of power
            fig_name = "f3db_power.png"
            plt_title = ""
            plt_range = [0.0, 0.7, 0.0, 12]

            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            for i in range(0, len(f_data), 1):
                #ax.plot(v_data[i], f_data[i], labs_pts[cnt], markersize = 10, label = curve_labels[cnt])
                R = interpolate.interp1d(power_data[0], power_data[i+1]) # make an interpolation over the power-voltage data

                sqrt_power = []
                for j in range(0, len(v_data[i])-1, 1):
                    val = math.sqrt( Common.convert_PdBm_PmW( float( R( v_data[i][j] ) ) ) )
                    sqrt_power.append( val )

                lin_fit = Common.linear_fit(np.asarray(sqrt_power), np.asarray(f_data[i][:-1]), [0.2, 0.5])

                ax.plot(sqrt_power, f_data[i][:-1], labs_pts[cnt], ms = 8, label = "T = %(v1)d (C)"%{"v1":temperatures[cnt]})
                ax.plot([sqrt_power[0], sqrt_power[-1]],
                        [lin_fit[0]+lin_fit[1]*sqrt_power[0], lin_fit[0]+lin_fit[1]*sqrt_power[-1]], labs_lins[cnt], lw = 2)
                
                cnt += 1
                del sqrt_power

            ax.legend(loc='upper left')
            
            plt.xlabel('$\sqrt{P}$ $(mW)^{1/2}$', fontsize = 15)
            plt.ylabel('$f_{3dB}$ (GHz)', fontsize = 17)

            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )
            
            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
            
            del v_data
            del f_data
            del power_data
        else:
            print("Error: File",power_name," not found")
            raise Exception
    except Exception: 
        print("Error: TIPS_FR_Analysis.plot_f3dB_power()")

        
