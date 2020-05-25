import os
import glob
import re
import sys # access system routines

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt

import Common

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-', 'ro-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-', 'r-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--', 'r--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks', 'ro' ] # plot labels

def Make_TIPS_Transmission():
    # plot the results from the TIPS Transmission experiments
    # R. Sheehan 20 - 3 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/TIPS_Transmission/"

    os.chdir(DATA_HOME)

    print(os.getcwd())

    #Plot_BER_BtB_data_versus_PRx(True)

    #Plot_BER_BtB_data_versus_VDFB(True)

    #ber_files = glob.glob("BER_4.csv")
    #for f in ber_files:
    #    BER_Data = Read_BER_Data(f, 0.1, 0.9, True)
    #    Plot_BER_Data(BER_Data, True)

    dir_name = "BER_Data_ISOA_100/"
    #dir_name = "BER_Data_Two_Currents/"
    #dir_name = "BER_Data_25km/"
    BER_Distance_Comparison(dir_name, True)
    
    #for i in range(0, len(BER_Data[0][2]), 1):
    #    print(BER_Data[0][2][i],",",BER_Data[0][3][i]

##    print(Common.convert_Split_Power_Reading(-16.46, 0.1, 0.9)
##    print(Common.convert_PdBm_PmW( Common.convert_Split_Power_Reading(-16.46, 0.1, 0.9) )

    #plot_Insertion_Loss_data(True)

    #os.chdir("Eye_Diag_27_3_2017/")

    #btb_dir = "BtB_ED/"
    #data_dir = "Data_ED/"
    #trans_dir = "Transmitted_ED/"

    #Rename_BER_Images(data_dir)
    #Rename_BER_Images(btb_dir)
    #Rename_BER_Images(trans_dir)

    #fit_90_10_data()

    #fname = "OSNR_Data.txt"

    #freq = 10.0
    #OSNR_data = read_OSNR_data(fname, freq, True)

    #curve_lab = ""
    #x_lab = '$P_{Rx}$ (dBm)'
    #y_lab = "OSNR (dB)"
    #plt_title = "Measured DFB OSNR for DR = 10 (Gbps)"
    #plt_range = [-25, 0, 30, 50]
    #fig_name = "OSNR_10_Gbps.png"

    ##Common.plot_this(OSNR_data[0], OSNR_data[1], curve_lab, x_lab, y_lab, plt_title, plt_range, fig_name, True)
    #Common.plot_this_with_linear_fit(OSNR_data[0], OSNR_data[1], curve_lab, x_lab, y_lab, plt_title, plt_range, fig_name, True)

    #plot_OSNR_comparison(fname, True)

    return 0

def BER_Data_Comparison():

    ber_files = ["BER_BtB_10.csv", "BER_BtB_12.csv"]
    BER_Data = []
    cnt = 0
    
    for f in ber_files:
        BER_Data.append(read_BER_data(f, 0.1, 0.9, True))
        cnt += 1

    labels = []
    for i in range(0, len(BER_Data), 1):
        labels.append( 'DR = %(v1)s (Gbps)'%{"v1":BER_Data[i][1]['Data Rate (Gbps)']} )
    
    title = 'BtB data $V_{DFB}$ = %(v1)s (V), T = %(v2)s (C)'%{"v1":BER_Data[0][1]['VDFB (V)'],"v2":BER_Data[0][1]['T (C)']}
    plt_range = [-16.5, -10.0, 1.0E-12, 1.0E-2]
    name = "BtB_Data_Comparison.png"

    Combine_Plot_BER_Data(BER_Data, labels, title, plt_range, name, True)

    plt_range = [-16.5, -10.0, -11, -2.9]
    name = "BtB_Data_Comparison_Linear_Fit.png"
    Combine_Plot_Q_factor_Data(BER_Data, labels, title, plt_range, name, True)

    return 0

def BER_Distance_Comparison(dir_name, loud = False):

    # method for plotting BER data in distance comparison mode
    # R. Sheehan 12 - 4 - 2017

    try:

        if os.path.isdir(dir_name):

            os.chdir(dir_name)

            if glob.glob("BER*csv"):

                #ber_files = glob.glob("BER*csv")
                ber_files = ["BER_BtB.csv", "BER_22km.csv"]
                #ber_files_1 = ["BER_BtB_I_62.csv", "BER_6km_I_62.csv", "BER_12km_I_62.csv", "BER_18km_I_62.csv"]
                #ber_files_2 = ["BER_BtB_I_100.csv", "BER_20km_I_100.csv", "BER_22km_I_100.csv", "BER_25km_I_100.csv"]
                #ber_files = ber_files_1 + ber_files_2
                #ber_files = ["BER_BtB_I_62.csv", "BER_BtB_I_100.csv"]
                BER_Data = []
                cnt = 0
    
                for f in ber_files:
                    BER_Data.append(read_BER_data(f, 0.1, 0.9, True))
                    cnt += 1

                labels = []
                for i in range(0, len(BER_Data), 1):
                    labels.append( '%(v1)s, %(v2)s (mA)'%{"v1":BER_Data[i][1]['Distance (km)'] + "(km)" if float(BER_Data[i][1]['Distance (km)']) > 0 else 'BtB', "v2":BER_Data[i][1]['ISOA (mA)']} )

                title = '$V_{DFB}$ = %(v1)s (V), T = %(v2)s (C), DR = %(v3)s (Gbps)'%{"v1":BER_Data[0][1]['VDFB (V)'],
                                                                                               "v2":BER_Data[0][1]['T (C)'], 
                                                                                               "v3":BER_Data[0][1]['Data Rate (Gbps)']}
                plt_range = [-15.5, -7.0, 1.0E-12, 1.0E-2]
                name = "BER_Distance_Comparison_22.png"

                Combine_Plot_BER_Data(BER_Data, labels, title, plt_range, name, loud)

                plt_range = [-15.5, -7.0, -11, -4.0]
                name = "BER_Distance_Comparison_Linear_Fit_22.png"
                Combine_Plot_Q_factor_Data(BER_Data, labels, title, plt_range, name, loud)
            else:
                print("No files of the form BER*.csv found")
                raise Exception

            os.chdir('..')
        else:
            print("Error: No such directory as",dir_name)
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.BER_Distance_Comparison()")

def Rename_BER_Images(dir_name):
    # rename the BER images according to frequency and bias values
    # R. Sheehan 30 - 3 - 2017

    try:
        # check if the directory exists
        if os.path.isdir(dir_name):

            # move to the directory
            os.chdir(dir_name)

            print(os.getcwd())

            # Read in the file with the parameter list
            img_file_list = glob.glob("*.bmp")
            
            img_param_file = glob.glob("Image_Params.txt")
            
            if img_file_list and glob.glob("Image_Params.txt"):

                param_data = Common.read_matrix("Image_Params.txt")

                if "Data" in dir_name:
                    # change the names of the data images generated by the BPG
                    
                    freq_vals = list( Common.get_col(param_data,0) ) # numbers for freq values
                    osc_vals = list( Common.get_col(param_data,1) ) # numbers for Osc mode images
                    ed_vals = list( Common.get_col(param_data,2) ) # numbers for ED mode images
                    
                    for f in img_file_list:

                        # you only want to change filenames that have not yet been changed
                        if "screen" in f:
                            # what number is in the file name?
                            num = float( Common.extract_values_from_string(f)[0] )

                            if num in osc_vals:                   
                                fnew = "Osc_f_%(v1)d.bmp"%{"v1":int( freq_vals[osc_vals.index(num)] ) } 
                                #print(fnew                   
                                os.rename(f,fnew)
                            elif num in ed_vals:
                                fnew = "ED_f_%(v1)d.bmp"%{"v1":int( freq_vals[ed_vals.index(num)] ) }   
                                #print(fnew           
                                os.rename(f,fnew)
                            else:
                                print("File ",f," not contained in Image_Params.txt")
                        else:
                            print("f does not contain screen")

                    del osc_vals; del ed_vals; del param_data; del img_file_list;

                elif "BtB" in dir_name:
                    # change the names of the data images generated in BtB configuration

                    freq_vals = list( Common.get_col(param_data,0) ) # numbers for freq values
                    bias_vals = list( Common.get_col(param_data,1) ) # numbers for bias values
                    osc_vals = list( Common.get_col(param_data,2) ) # numbers for Osc mode images
                    ed_vals = list( Common.get_col(param_data,3) ) # numbers for ED mode images

                    for f in img_file_list:

                        # you only want to change filenames that have not yet been changed
                        if "screen" in f:
                            # what number is in the file name?
                            num = float( Common.extract_values_from_string(f)[0] )

                            if num in osc_vals:                        
                                fnew = "Osc_f_%(v1)d_V_%(v2)d.bmp"%{"v1":int( freq_vals[osc_vals.index(num)] ),
                                                                    "v2":int( 1000*bias_vals[osc_vals.index(num)] )}                   
                                os.rename(f,fnew)
                            elif num in ed_vals:
                                fnew = "ED_f_%(v1)d_V_%(v2)d.bmp"%{"v1":int( freq_vals[ed_vals.index(num)] ),
                                                          "v2":int( 1000*bias_vals[ed_vals.index(num)] ) }                  
                                os.rename(f,fnew)
                            else:
                                print("File ",f," not contained in Image_Params.txt")
                        else:
                            print("f does not contain screen")

                    del osc_vals; del ed_vals; del param_data; del img_file_list;

                elif "Transmitted" in dir_name:
                    # change the names of the data images generated after transmission

                    freq_vals = list( Common.get_col(param_data,0) ) # numbers for freq values
                    bias_vals = list( Common.get_col(param_data,1) ) # numbers for bias values
                    dist_vals = list( Common.get_col(param_data,2) ) # numbers for distance values
                    osc_vals = list( Common.get_col(param_data,3) ) # numbers for Osc mode images
                    ed_vals = list( Common.get_col(param_data,4) ) # numbers for ED mode images

                    for f in img_file_list:

                        # you only want to change filenames that have not yet been changed
                        if "screen" in f:
                            # what number is in the file name?
                            num = float( Common.extract_values_from_string(f)[0] )

                            if num in osc_vals:                        
                                fnew = "Osc_f_%(v1)d_V_%(v2)d_D_%(v3)d.bmp"%{"v1":int( freq_vals[osc_vals.index(num)] ),
                                                                             "v2":int( 1000*bias_vals[osc_vals.index(num)] ),
                                                                             "v3":int( dist_vals[osc_vals.index(num)] )}                    
                                print(osc_vals.index(num),",",f,",",fnew)
                                #os.rename(f,fnew)
                            elif num in ed_vals:
                                fnew = "ED_f_%(v1)d_V_%(v2)d_D_%(v3)d.bmp"%{"v1":int( freq_vals[ed_vals.index(num)] ),
                                                          "v2":int( 1000*bias_vals[ed_vals.index(num)] ),
                                                          "v3":int( dist_vals[ed_vals.index(num)] )}                    
                                print(ed_vals.index(num),",",f,",",fnew)
                                #os.rename(f,fnew)
                            else:
                                print("File ",f," not contained in Image_Params.txt")
                        else:
                            print("f does not contain screen")

                    del osc_vals; del ed_vals; del param_data; del img_file_list;
                else:
                    print("If you can read this something has gone terribly wrong!")
                    raise Exception
            else:
                if img_file_list == None: print("Could not find any files of the form *.bmp")
                raise Exception
            
            os.chdir('..')
            print(os.getcwd())
        else:
            print(dir_name," is not a vlid directory")
            raise Exception        
    except Exception:
        print("Error: TIPS_Transmission.Rename_BER_Images()")

def read_BER_data(ber_file, sr_low = 0.1, sr_high = 0.9, loud = False):

    # method for reading the data associated with a BER measurement
    # R. Sheehan 23 -3 - 2017

    try:
        if glob.glob(ber_file):
            
            thefile = file(ber_file,"r") # open file for reading

            # file is available for reading
            thedata = thefile.readlines() # read the data from the file

            nrows = Common.count_lines(thedata, ber_file) # count the number of rows

            if loud: 
                print("%(path)s is open"%{"path":ber_file})
                print("Nrows = ",nrows)

            # declare a dictionary to save the paramaters associated with a particular BER test
            ber_dict = {}

            # declare lists to store Rx power data and Measured BER values
            PRx_dBm = [] # stored received power value is 10% of true value
            BER_vals = []
            param_titles = []
            param_values = []

            for line in thedata:
                parameter = line.split(',')
                if Common.isfloat(parameter[0]):
                    # you've reached the data   
                    p_val = float( parameter[0] )                 
                    #PRx_dBm.append( Common.convert_Split_Power_Reading( p_val, sr_low, sr_high)  )
                    #PRx_dBm.append( -1.0*(abs(p_val/2.4575062) )  ) # x_{90} = x_{10} / 2.4575062
                    PRx_dBm.append(9.575235+1.006838*p_val) # x_{90} = 9.575235 + 1.006838 x_{10}, see notebook 2715, page 79

                    BER_vals.append( float(parameter[1].replace("\n","") ) )
                else:
                    param_titles.append( parameter[0] )
                    param_values.append( parameter[1].replace("\n","") )
               
            # use the in-built zip function to create the dictionary
            ber_dict = dict( zip(param_titles, param_values) )

            ber_dict.update({'Title':ber_file.replace(".csv","")})

            del ber_dict['Experiment Parameters']
            del ber_dict['Pout (dBm) @ 10%']
            del param_titles
            del param_values

            if not PRx_dBm and not BER_vals:
                raise Exception
            else:
                print("Data acquired from",ber_file)
                return [True, ber_dict, PRx_dBm, BER_vals]
        else:
            # file cannot be found
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.Read_BER_Data")
        if thefile.closed:print("Error: Cannot Open File",ber_file)
        return None

def Plot_BER_Data(BER_Data, curve_label = "", plt_title = "", plt_range = None, fig_name = "", loud = False):
    # make a plot of measured BER data
    # BER_data is a list that contains the following elements
    # 0: True / False depending on whether was read correctly or not
    # 1: Dictionary that contains experimental parameters used in measurement of BER data
    # 2: List of Receieved Power data at 90% value
    # 3: List that contains measured BER data
    # R. Sheehan 23 - 3 - 2017

    try:
        if BER_Data[0]:

            #plt_title = '$I_{SOA}$ = %(v1)s (mA), $I_{EAM}$ = %(v2)s (mA), DR = %(v3)s (Gbps), $L_{PRBS}$ = %(v4)s'%{"v1":BER_Data[1]['ISOA (mA)'], 
            #                                                                                                                             "v2":BER_Data[1]['IEAM (mA)'], 
            #                                                                                                                             "v3":BER_Data[1]['Data Rate (Gbps)'], 
            #                                                                                                                             "v4":BER_Data[1]['LPRBS']}
            ##end_pts = [BER_Data[2][-1], BER_Data[2][0], BER_Data[3][0], BER_Data[3][-1]]
            #end_pts = [-15, -7.5, 1.0E-12, 1.0E-2]
            #curve_label = '$V_{DFB}$ = %(v1)s (V)'%{"v1":BER_Data[1]['VDFB (V)']}
            #fig_name = BER_Data[1]['Title'] + '_Plot.png'

            fig = plt.figure()
            ax = fig.add_subplot(111)

            if curve_label is not "":
                ax.plot(BER_Data[2], BER_Data[3], labs_pts[0], markersize = 10, label = curve_label)
                ax.legend(loc='best')
            else:
                ax.plot(BER_Data[2], BER_Data[3], labs_pts[0], markersize = 10)

            ax.set_yscale('log')            
            
            plt.xlabel('$P_{Rx}$ (dBm)', fontsize = 17)
            plt.ylabel('BER', fontsize = 17)

            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( end_pts )
            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()

            plt.clf()
            plt.cla()
            plt.close()
        else:
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.Plot_BER_Data")
        return -1

def Combine_Plot_BER_Data(ber_data_sets, curve_labels = None, plt_title = "", plt_range = None, fig_name = "", loud = False):
    # plot multiple BER on same plot
    # BER_data is a list that contains the following elements
    # 0: True / False depending on whether was read correctly or not
    # 1: Dictionary that contains experimental parameters used in measurement of BER data
    # 2: List of Receieved Power data at 90% value
    # 3: List that contains measured BER data
    # R. Sheehan 23 - 3 - 2017
    
    try:

        if all(item[0] == True for item in ber_data_sets):

            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            for item in ber_data_sets:
                ax.plot(item[2], item[3], labs_pts[cnt], ms = 8 if cnt == 1 or cnt == 3 or cnt == 6 or cnt == 7 else 10, label = curve_labels[cnt])
                cnt += 1

            ax.set_yscale('log')

            ax.legend(loc='upper right')
            
            plt.xlabel('$P_{Rx}$ (dBm)', fontsize = 17)
            plt.ylabel('BER', fontsize = 17)

            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )
            
            x1 = -17; x2 = 7.5; val = 1.0e-3
            plt.hlines(val, x1, x2, 'k', 'dashed', lw = 2)
            #plt.text(-14.5, 1.0e-3 - 2e-3, r'BER = 1.0E-3', fontsize=14, color = 'black')

            x1 = -17; x2 = 7.5; val = 1.0e-9
            plt.hlines(val, x1, x2, 'k', 'dashed', lw = 2)
            #plt.text(-11, 1.0e-9 - 2e-9, r'BER = 1.0E-9', fontsize=14, color = 'black')

            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.Combine_Plot_BER_Data")
        return -1

def Combine_Plot_Q_factor_Data(ber_data_sets, curve_labels = None, plt_title = "", plt_range = None, fig_name = "", loud = False):
    # plot multiple BER on same plot as Q-factors
    # BER_data is a list that contains the following elements
    # 0: True / False depending on whether was read correctly or not
    # 1: Dictionary that contains experimental parameters used in measurement of BER data
    # 2: List of Receieved Power data at 90% value
    # 3: List that contains measured BER data
    # R. Sheehan 4 - 4 - 2017
    
    try:

        if all(item[0] == True for item in ber_data_sets):

            # need ticks for the Q-scale
            #vals = [1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5,1.0e-6, 1.0e-9, 1.0e-12]
            #tck_vals = []
            #for x in vals: tck_vals.append( -10.0*math.log10( -1.0*math.log10(vals) ) )
            
            #tck_vals = [-3.0103,   -4.7712,   -6.0206,   -6.9897,   -7.7815,   -9.5424,   -10.7918]
            #tck_labs = [r'1.0E-2', r'1.0E-3', r'1.0E-4', r'1.0E-5', r'1.0E-6', r'1.0E-9', r'1.0E-12']

            tck_vals = [-4.7712,   -6.0206,   -6.9897,   -7.7815,   -9.5424,   -10.7918]
            tck_labs = [r'1.0E-3', r'1.0E-4', r'1.0E-5', r'1.0E-6', r'1.0E-9', r'1.0E-12']

            fig = plt.figure()
            ax = fig.add_subplot(111)

            cnt = 0
            for item in ber_data_sets:
                
                # convert the data to Q-factor 
                Q_item = []
                for i in range(0, len(item[3])):
                    Q_item.append( -10.0*math.log10( -1.0*math.log10(item[3][i]) ) )

                # make a linear fit to the Q data
                lin_pars = Common.linear_fit( np.asarray(item[2]), np.asarray(Q_item), [1.0, -1.0])

                lin_fit = lambda p, x: p[0] + p[1]*x # target function

                sens_val = 1.0E-9
                Q_sens = -10.0*math.log10( -1.0*math.log10(sens_val) )
                print(curve_labels[cnt],", Sensitivity =",(Q_sens-lin_pars[0])/lin_pars[1])

                ax.plot(item[2], Q_item, labs_pts[cnt], ms = 8 if cnt == 1 or cnt == 3 or cnt == 6 or cnt == 7 else 10, label = curve_labels[cnt])

                # linear approximation
                ax.plot([item[2][0], item[2][-1]], 
                        [ lin_pars[1]*item[2][0]+lin_pars[0], lin_pars[1]*item[2][-1]+lin_pars[0] ], 
                        labs_lins[cnt], lw = 2)
                
                cnt += 1

                del Q_item

            ax.legend(loc='upper right')
            
            plt.xlabel('$P_{Rx}$ (dBm)', fontsize = 17)
            plt.ylabel('-log(BER)', fontsize = 17)

            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )

            # change out the ticks on the y-axis
            plt.yticks( tck_vals, tck_labs)
            
            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.Combine_Plot_BER_Data")
        return -1

def Plot_BER_BtB_data_versus_PRx(loud = False):
    # plot the measured TIPS DFB-SOA BtB BER data
    # R. Sheehan 20 - 3 - 2017

    try:

        P_Rx_10_v1_f1 = [-21.255, -21.314, -21.486, -21.685, -21.837, -22.011, -22.293, -22.415, -22.648, -22.729, -22.997, 
            -23.271, -23.288, -23.637, -23.861, -23.941, -24.244] # Received 10% power at v = 2.3030 (V) and f = 7 (GHz)
        BER_v1_f1 = [1.18E-11, 1.60E-11, 1.24E-10, 9.70E-10, 4.57E-09, 1.88E-08, 2.00E-07, 5.17E-07, 2.47E-06, 4.30E-06, 1.93E-05,
            7.71E-05, 8.34E-05, 3.68E-04, 8.48E-04, 1.09E-03, 2.96E-03] # BER at v = 2.3030 (V) and f = 7 (GHz)

        c1 = True if len(P_Rx_10_v1_f1) == len(BER_v1_f1) else False

        P_Rx_10_v1_f2 = [-20.741, -21.064, -21.266, -21.619, -22.000, -22.285, -22.447, -22.551, -22.667, -23.036, 
            -23.302, -23.600, -24.055, -24.236] # Received 10% power at v = 2.3030 (V) and f = 7.5 (GHz)
        BER_v1_f2 = [1.80E-10, 7.23E-10, 4.15E-09, 6.45E-08, 9.19E-07, 4.45E-06, 7.94E-06, 1.37E-05, 2.82E-05, 1.18E-04, 
            3.04E-04, 7.05E-04, 2.38E-03, 3.65E-03] # BER at v = 2.3030 (V) and f = 7.5 (GHz)
        
        c2 = True if len(P_Rx_10_v1_f2) == len(BER_v1_f2) else False

        P_Rx_10_v2_f2 = [-17.635, -17.800, -18.019, -18.224, -18.400, -18.610, -18.800, -19.040, -19.200, -19.400, -19.610, -19.814, -20.004, 
            -20.210, -20.400, -20.610, -20.793, -21.028, -21.212, -21.394, -21.606, -21.806, -21.989, -22.206, -22.419, -22.599, -22.793, 
            -22.948, -23.205] # Received 10% power at v = 2.3090 (V) and f = 7.5 (GHz)
        BER_v2_f2 = [1.000E-10, 2.178E-10, 5.467E-10, 1.136E-09, 1.469E-09, 2.840E-09, 4.509E-09, 1.080E-08, 1.696E-08, 3.877E-08, 7.814E-08, 
            1.298E-07, 2.132E-07, 3.835E-07, 7.237E-07, 1.438E-06, 2.225E-06, 3.827E-06, 6.41E-06, 9.71E-06, 1.95E-05, 3.71E-05, 7.42E-05, 
            1.76E-04, 3.77E-04, 7.56E-04, 1.46E-03, 1.70E-03, 4.14E-03] # BER at v = 2.3090 (V) and f = 7.5 (GHz)
        
        c3 = True if len(P_Rx_10_v2_f2) == len(BER_v2_f2) else False

        if c1 and c2 and c3:

            # Convert measured 10% power readings into their 90% values
            P_Rx_90_v1_f1 = Common.convert_Split_Power_Readings(P_Rx_10_v1_f1, 0.1, 0.9)
            P_Rx_90_v1_f2 = Common.convert_Split_Power_Readings(P_Rx_10_v1_f2, 0.1, 0.9)
            P_Rx_90_v2_f2 = Common.convert_Split_Power_Readings(P_Rx_10_v2_f2, 0.1, 0.9)
            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(P_Rx_90_v1_f1, BER_v1_f1, labs_pts[0], markersize = 10, label = "$V_{DFB}$ = 2.303 (V) and f = 7 (GHz)")
            ax.plot(P_Rx_90_v1_f2, BER_v1_f2, labs_pts[1], markersize = 10, label = "$V_{DFB}$ = 2.303 (V) and f = 7.5 (GHz)")
            ax.plot(P_Rx_90_v2_f2, BER_v2_f2, labs_pts[2], markersize = 10, label = "$V_{DFB}$ = 2.309 (V) and f = 7.5 (GHz)")
            ax.set_yscale('log')

            ax.legend(loc='upper right')
            
            plt.xlabel('$P_{Rx}$ (dBm)', fontsize = 17)
            plt.ylabel('BER', fontsize = 17)
            plt.title('$L_{PRBS} = 2^{7}-1$, DR = 7.5 (Gbps), ')
            plt.axis( [-15, -7.5, 1.0E-12, 1.0E-2] )

            plt.savefig('TIPS_DFB_BER_First.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise Exception
            return -1
    except Exception:
        print("Error: TIPS_Transmission.Plot_BER_BtB_data()")
        if c1 == False: print("Error in c1")
        if c2 == False: print("Error in c2")
        if c3 == False: print("Error in c3")
        return -1

def Plot_BER_BtB_data_versus_VDFB(loud = False):
    # plot the measured TIPS DFB-SOA BtB BER data
    # R. Sheehan 20 - 3 - 2017

    try:

        V_DFB = [2.3, 2.3030, 2.306, 2.307, 2.308, 2.309, 2.312, 2.315]
        
        BER_var_P_Rx = [2.84E-05, 1.37E-05, 7.80E-06, 6.36E-06, 6.48E-06, 8.59E-06, 1.54E-05, 3.57E-05]
        Var_P_Rx = [-22.557, -22.551, -22.537, -22.531, -22.526, -22.523, -22.504, -22.488]
        True_Var_P_Rx = Common.convert_Split_Power_Readings(Var_P_Rx, 0.1, 0.9)
        
        BER_const_P_Rx = [2.68E-05, 1.24E-05, 7.37E-06, 7.29E-06, 7.00E-06, 8.59E-06, 1.55E-05, 4.62E-05]
        Const_P_Rx = [-22.55, -22.55, -22.55, -22.55, -22.55, -22.55, -22.55, -22.55]
        True_Const_P_Rx = Common.convert_Split_Power_Readings(Const_P_Rx, 0.1, 0.9)

        volts = V_DFB + V_DFB
        BER = BER_const_P_Rx + BER_var_P_Rx

        c1 = True if len(V_DFB) == len(BER_var_P_Rx) else False

        c2 = True if len(V_DFB) == len(BER_const_P_Rx) else False

        p_var = sum(True_Var_P_Rx) / len(True_Var_P_Rx)
        p_dev = 0.5*( max(True_Var_P_Rx) - min(True_Var_P_Rx) )
        p_const = sum(True_Const_P_Rx) / len(True_Const_P_Rx)

        # make a quadratic fit to the measured data and find the location of minimum BER
        params = Common.quadratic_fit(np.asarray(volts), np.asarray(BER), [0.75, 0.5, -0.25])

        min_loc = (-1.0*params[1]) / (2.0*params[2])
        min_val = ( params[0] - (params[1]**2)/(4.0*params[2]) )

        print("Min Value occurs at x =",min_loc)
        print("Min Value is fmin =",min_val)

        if c1 and c2:

            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.plot(V_DFB, BER_var_P_Rx, labs_pts[0], markersize = 10, 
                    label = '$P_{Rx}$ = %(v1)0.4f $\pm$ %(v2)0.4f (dBm)'%{"v1":p_var, "v2":p_dev})
            ax.plot(V_DFB, BER_const_P_Rx, labs_pts[1], markersize = 10, 
                    label = '$P_{Rx}$ = %(v1)0.4f (dBm)'%{"v1":p_const})
            ax.set_yscale('log')

            ax.legend(loc='upper center')
            
            plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
            plt.ylabel('BER', fontsize = 17)
            plt.title('TIPS DFB BER f = 7.5 (GHz), $L_{PRBS} = 2^{7}-1$')
            #plt.axis( [65, 185, 1, 8] )

            x1 = V_DFB[0]; x2 = min_loc
            plt.hlines(min_val, x1, x2, 'k', 'dashed', lw = 2) # line to indicate pi rad on plot
            
            y1 = 1.0E-6; y2 = min_val
            plt.vlines(min_loc, y1, y2, 'k', 'dashed', lw = 2)

            plt.text(min_loc + 1.0E-4, 2.5E-6, r'$V_{min}$ = %(v1)0.3f (V)'%{"v1":min_loc}, fontsize=12, color = 'black')
            plt.text(min_loc + 1.0E-4, 2.0E-6, r'$BER_{min}$ = %(v2)0.4E'%{"v2":min_val}, fontsize=12, color = 'black')

            plt.savefig('TIPS_DFB_BER_Voltage.png')
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()

            return 0
        else:
            raise Exception
            return -1
    except Exception:
        print("Error: TIPS_Transmission.Plot_BER_BtB_data()")
        if c1 == False: print("Error in c1")
        if c2 == False: print("Error in c2")
        return -1

def plot_Insertion_Loss_data(loud = False):
    # plot the measured insertion loss data for the BER set up
    # see Tyndall Notebook 2715, page 73

    try:

        T = 25.0
        V_DFB = [2.3, 2.6, 2.9]

        # power from device
        P_DUT_1 = [-6.192, -5.164, -4.446]
        P_DUT_2 = [-6.194, -5.147, -4.441]
        P_DUT = []
        for i in range(0, len(P_DUT_1), 1): 
            P_DUT.append( 0.5*(P_DUT_1[i] + P_DUT_2[i]) )

        # power from device after passing through 90-10 splitter
        P_DS_90 = [-7.492, -6.448, -5.738]
        P_DS_10 = [-16.891, -15.846, -15.136]

        # power from device after passing through variable attenuator
        P_DV = [-6.992, -5.930, -5.230]

        # power from device after passing though variable attenuator and 90-10 splitter, P_{out} in BtB config. 
        P_DVS_BtB_1 = [-9.406, -8.359, -7.649] # 90% arm
        P_DVS_BtB_2 = [-9.425, -8.362, -7.644] # 90% arm
        P_DVS_BtB = []
        for i in range(0, len(P_DVS_BtB_1), 1): 
            P_DVS_BtB.append( (P_DVS_BtB_1[i] + P_DVS_BtB_2[i])/2.0 )

        # power from device after passing though variable attenuator and 90-10 splitter, power from 10% arm
        P_DVS_10_1 = [-18.829, -17.807, -17.079]
        P_DVS_10_2 = [-18.857, -17.792, -17.066]
        P_DVS_10_3 = [-18.842, -17.782, -17.062]
        P_DVS = []
        for i in range(0, len(P_DVS_10_1), 1): 
            P_DVS.append( (P_DVS_10_1[i] + P_DVS_10_2[i] + P_DVS_10_3[i])/3.0 )

        # power from device after passing though variable attenuator and 90-10 splitter and 2km of optical fibre
        P_DVSF_2 = [-10.150, -9.096, -8.396]

        # power from device after passing though variable attenuator and 90-10 splitter and 5.463km of optical fibre
        P_DVSF_5 = [-11.776, -10.708, -9.973]

        # power from device after passing though variable attenuator and 90-10 splitter and 6km of optical fibre
        P_DVSF_6 = [-11.497, -10.442, -9.720]

        # power from device after passing though variable attenuator and 90-10 splitter and 12km of optical fibre
        P_DVSF_12 = [-13.302, -12.245, -11.532]

        # power from device after passing though variable attenuator and 90-10 splitter and 14.037km of optical fibre
        P_DVSF_14 = [-14.774, -13.710, -12.979]

        # power from device after passing though variable attenuator and 90-10 splitter and 18km of optical fibre
        P_DVSF_18 = [-15.323, -14.260, -13.527]

        # power from device after passing though variable attenuator and 90-10 splitter and 20.037km of optical fibre
        P_DVSF_20 = [-16.556, -15.481, -14.746]
        
        # Power in the System
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(V_DFB, P_DUT, labs[0], markersize = 10, lw = 2, label = 'DUT')        
        ax.plot(V_DFB, P_DVS_BtB, labs[1], markersize = 10, lw = 2, label = 'BtB')
        ax.plot(V_DFB, P_DVSF_2, labs[2], markersize = 10, lw = 2, label = '2.037 (km)')
        #ax.plot(V_DFB, P_DVSF_5, labs[3], markersize = 10, lw = 2, label = '5.463 (km)')
        ax.plot(V_DFB, P_DVSF_6, labs[3], markersize = 10, lw = 2, label = '6.0 (km)')
        ax.plot(V_DFB, P_DVSF_12, labs[4], markersize = 10, lw = 2, label = '12 (km)')
        ax.plot(V_DFB, P_DVSF_14, labs[5], markersize = 10, lw = 2, label = '14.037 (km)')
        ax.plot(V_DFB, P_DVSF_18, labs[6], markersize = 10, lw = 2, label = '18 (km)')
        ax.plot(V_DFB, P_DVSF_20, labs[1], markersize = 10, lw = 2, label = '20.037 (km)')
        ax.legend(loc='upper left')            
        plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
        plt.ylabel('P (dBm)', fontsize = 17)
        plt.title('TIPS DFB BER Power T = 25 (C)')
        plt.axis( [2.2, 3.0, -17, 0.0] )

        plt.savefig('TIPS_DFB_BER_Power.png')
        if loud: plt.show()
        plt.clf()
        plt.cla()
        plt.close()

        # Insertion Loss is measured relative to measured BtB power
        IL_BtB = []; IL_2 = []; IL_5 = []; IL_6 = []; 
        IL_12 = []; IL_14 = []; IL_18 = []; IL_20 = []; 
        for i in range(0, len(P_DVS_BtB), 1): 
            #IL_BtB.append( -1.0*abs(P_DUT[i] - P_DVS_BtB[i]) )
            IL_2.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_2[i]))
            IL_5.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_5[i]))
            IL_6.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_6[i]))
            IL_12.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_12[i]))
            IL_14.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_14[i]))
            IL_18.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_18[i]))
            IL_20.append( -1.0*abs(P_DVS_BtB[i] - P_DVSF_20[i]))

        # Insertion Loss due to optical fibre against voltage
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #ax.plot(V_DFB, IL_BtB, labs[1], markersize = 10, lw = 2, label = 'BtB')
        ax.plot(V_DFB, IL_2, labs[2], markersize = 10, lw = 2, label = '2.037 (km)')
        ax.plot(V_DFB, IL_5, labs[3], markersize = 10, lw = 2, label = '5.463 (km)')
        ax.plot(V_DFB, IL_12, labs[4], markersize = 10, lw = 2, label = '12 (km)')
        ax.plot(V_DFB, IL_14, labs[5], markersize = 10, lw = 2, label = '14.037 (km)')
        ax.plot(V_DFB, IL_18, labs[6], markersize = 10, lw = 2, label = '18.0 (km)')
        ax.plot(V_DFB, IL_20, labs[1], markersize = 10, lw = 2, label = '20.037 (km)')
        ax.legend(loc='upper left')            
        plt.xlabel('$V_{DFB}$ (V)', fontsize = 17)
        plt.ylabel('Insertion Loss (dB)', fontsize = 17)
        plt.title('TIPS DFB BER IL T = 25 (C)')
        plt.axis( [2.2, 3.0, -8.0, 0.0] )

        plt.savefig('TIPS_DFB_BER_IL.png')
        if loud: plt.show()
        plt.clf()
        plt.cla()
        plt.close()

        # Insertion Loss versus distance at V = 2.55 (V)
        dist = [0.0, 2.037, 5.463, 6.0, 12.0, 14.037, 18.0, 20.037]
        IL_dist = [0.0, IL_2[1], IL_5[1], IL_6[1], IL_12[1], IL_14[1], IL_18[1], IL_20[1]]
        
        # make a linear fit to the data
        lin_fit = Common.linear_fit(np.asarray(dist), np.asarray(IL_dist), [0.0, -1.0])

        print("\n")
        for i in range(0, len(dist),1):
            lin_val = lin_fit[0]+lin_fit[1]*dist[i]
            val_str = "%(v1)0.3ff, %(v2)0.3f, %(v3)0.3f"%{"v1":dist[i], "v2":IL_dist[i], "v3":lin_val}
            print(val_str)
        print("\n")

        # Insertion Loss due to optical fibre against distance at V = 2.6 (V)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([dist[0], dist[-1]], [lin_fit[0]+lin_fit[1]*dist[0], lin_fit[0]+lin_fit[1]*dist[-1]], labs_lins[5], 
                markersize = 10, lw = 2, label = '$V_{DFB} = 2.6 (V)$, IL = %(v1)0.3f D %(v2)0.3f'%{"v1":lin_fit[1], "v2":lin_fit[0]})
        ax.plot(dist, IL_dist, labs_pts[5], markersize = 10, lw = 2)
        ax.legend(loc='upper right')            
        plt.xlabel('Distance (km)', fontsize = 17)
        plt.ylabel('Insertion Loss (dB)', fontsize = 17)
        plt.title('TIPS DFB BER IL T = 25 (C)')
        plt.axis( [0.0, 22.0, -8.0, 0.0] )

        plt.savefig('TIPS_DFB_BER_IL_Dist.png')
        if loud: plt.show()
        plt.clf()
        plt.cla()
        plt.close()
        
    except:
        print("Error: TIPS_Transmission.plot_Insertion_Loss_Data()")

def fit_90_10_data():
    # make a linear fit to power data, in dBm, that has been measured through a 90-10 splitter
    # given a 10% power reading what is the 90% equivalent? 
    # R. Sheehan 

    try:

        P_10 = [-18.004, -18.501, -19.002, -19.505, -20.052, -20.475, -21.008, -21.474, -22.006]
        P_90 = [-8.552, -9.047, -9.54, -10.08, -10.621, -11.049, -11.577, -12.041, -12.574]

        if len(P_10) == len(P_90):
            lin_fit = Common.linear_fit(np.asarray(P_10), np.asarray(P_90), [-1.0, -2.0])

            print("Fit polynomial is ",lin_fit[0],"+",lin_fit[1],"x")
            for i in range(0, len(P_10), 1):
                fit_val = lin_fit[0]+lin_fit[1]*P_10[i]
                residual = abs(P_90[i]-fit_val)
                print(P_10[i],",",fit_val,",",P_90[i],",",residual)

        else:
            print("lists are not of the same length")
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.fit_90_10_data")

def read_OSNR_data(fname, mod_freq, loud = False):

    # OSNR data is stored in columns with headings
    # f(GHz) [0], V_{DFB}(V) [1], Power 10% (dBm) [2], T (C) [3], SMSR (dB) [4], 
    # WL Peak (nm) [5], Power Peak (dBm) [6], OSNR (dB) [7], Power Noise (dB) [8]
    # there may be some readings for which the noise level is too low, in this case the OSNR is suspect
    # R. Sheehan 11 - 4 - 2017

    # x_{90} = 9.575235 + 1.006838 x_{10}, see notebook 2715, page 79

    try:
        if glob.glob(fname):
            # file exists and can be opened

            thefile = file(fname,"r") # open file for reading

            # file is available for reading
            thedata = thefile.readlines() # read the data from the file

            nrows = Common.count_lines(thedata, fname) # count the number of rows

            if loud: 
                print("%(path)s is open"%{"path":fname})
                print("Nrows = ",nrows)

            PRx_dBm = []
            OSNR = []

            has_data = False
            for line in thedata:
                parameter = line.split(',')
                if Common.isfloat(parameter[0]):
                    # you've reached the data   
                    if float( parameter[0] ) == mod_freq and float( parameter[8] ) > -70.0:
                        has_data = True
                        # does frequency match input value?
                        p_val = float( parameter[2] ) # read 10% power
                        PRx_dBm.append(9.575235+1.006838*p_val) # x_{90} = 9.575235 + 1.006838 x_{10}, see notebook 2715, page 79

                        OSNR.append( float(parameter[7]) ) # store OSNR value

            if has_data:
                return [PRx_dBm, OSNR]
            else:
                return None
        else:
            print("Error: Cannot locate file",fname)
            raise Exception
    except Exception:
        print("Error: TIPS_Transmission.plot_OSNR_data()")

def plot_OSNR_comparison(fname, loud = False):
    # compare the measured OSNR data
    # R. Sheehan 11 - 4 - 2017

    try:
        freq_vals = [7.0, 9.0, 10.0, 12.0]
        P_arrs = []
        OSNR_arrs = []
        valid_f_vals = []

        for f in freq_vals:
            data = read_OSNR_data(fname, f)
            if data is not None:
                P_arrs.append(data[0])
                OSNR_arrs.append(data[1])
                valid_f_vals.append(f)
                del data

        if len(P_arrs) > 0:
            # make a plot of the measured data at the different frequencies
            x_label = '$P_{Rx} (dBm)$'
            y_label = 'OSNR (dB)'
            plt_title = ""
            plt_range = [-65, -5, 0, 55]
            fig_name = "All_OSNR.png"

            # make the plot
            fig = plt.figure()
            ax = fig.add_subplot(111)

            for i in range(0, len(P_arrs), 1):
                # make a linear fit to the data
                ax.plot(P_arrs[i], OSNR_arrs[i], labs_pts[i], ms = 10, label = 'DR = %(v1)0.1f (Gbps)'%{"v1":valid_f_vals[i]})
                lin_fit = Common.linear_fit(np.asarray(P_arrs[i]), np.asarray(OSNR_arrs[i]), [0.0, 1.0])
                ax.plot([ P_arrs[i][0], P_arrs[i][-1] ], 
                    [ lin_fit[0] + lin_fit[1]*P_arrs[i][0], lin_fit[0] + lin_fit[1]*P_arrs[i][-1] ], 
                    labs_lins[i], lw = 2)
            
            ax.legend(loc = 'best')
            plt.xlabel(x_label, fontsize = 17)
            plt.ylabel(y_label, fontsize = 17)
            
            if plt_title is not "": plt.title(plt_title)
            if plt_range is not None: plt.axis( plt_range )

            # plot endmatter
            if fig_name is not "": plt.savefig(fig_name)
            if loud: plt.show()
            plt.clf()
            plt.cla()
            plt.close()
        else:
            print("Error: No data found to match input frequencies")
            raise Exception

    except Exception:
        print("Error: TIPS_Transmission.plot_OSNR_comparison()")

    

