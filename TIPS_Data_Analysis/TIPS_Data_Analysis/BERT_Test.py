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

labs = ['r*-', 'g^-', 'b+-', 'md-', 'cp-', 'yh-', 'ks-', 'ro-' ] # plot labels
labs_lins = ['r-', 'g-', 'b-', 'm-', 'c-', 'y-', 'k-', 'r-' ] # plot labels
labs_dashed = ['r--', 'g--', 'b--', 'm--', 'c--', 'y--', 'k--', 'r--' ] # plot labels
labs_pts = ['r*', 'g^', 'b+', 'md', 'cp', 'yh', 'ks', 'ro' ] # plot labels

def BERT_Plots():
    
    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/BERT_Test/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())

            # run the code you want
            #Measured_Vpp()

            file_rename()

        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: BERT_Test.BERT_plots()")
        print("Error: Cannot find ",DATA_HOME)
    except Exception:
        print("Error: BERT_Test.BERT_plots()")

def Measured_Vpp():
    
    # PPG was set to various Vpp, actual Vpp was measured on DCA
    # Data can be found in Tyn Notebook 2715, pages 139, 140
    # R. Sheehan 31 - 7 - 2017

    try:
        # Define lists to hold the data
        V_PPG = [200, 240, 280, 320, 340, 370] # Vpp setting as stated on PPG

        V_PP_DCA_10 = [229, 282, 333, 379, 399, 424] # Vpp measured on DCA at f = 10 GHz
        V_EA_DCA_10 = [179, 227, 272, 313, 332, 353] # Eye-Amplitude measured on DCA at f = 10 GHz

        V_PP_DCA_15 = [225, 278, 327, 373, 393, 416] # Vpp measured on DCA at f = 15 GHz
        V_EA_DCA_15 = [179, 226, 271, 311, 329, 350] # Eye-Amplitude measured on DCA at f = 15 GHz

        V_PP_DCA_20 = [221, 273, 322, 367, 386, 407] # Vpp measured on DCA at f = 20 GHz
        V_EA_DCA_20 = [177, 223, 266, 305, 323, 344] # Eye-Amplitude measured on DCA at f = 20 GHz

        V_pp_data = []; data_lin = []; labels = []; 
        V_pp_data.append([V_PPG, V_PPG]); data_lin.append(labs_dashed[0]); labels.append('Expected'); 
        V_pp_data.append([V_PPG, V_PP_DCA_10]); data_lin.append(labs[1]); labels.append('f = 10 (GHz)'); 
        V_pp_data.append([V_PPG, V_PP_DCA_15]); data_lin.append(labs[2]); labels.append('f = 15 (GHz)'); 
        V_pp_data.append([V_PPG, V_PP_DCA_20]); data_lin.append(labs[3]); labels.append('f = 20 (GHz)'); 

        # make a plot of the data
        args = Plotting.plot_arguments()

        args.loud = True
        args.x_label = 'PPG Output Amplitude (mV)'
        args.y_label = '$V_{pp}^{DCA}$ (mv)'
        args.plt_range = [195, 375, 195, 430]
        args.crv_lab_list = labels
        args.mrk_list = data_lin
        args.plt_title = 'Peak-Peak Voltage Measured on DCA'
        args.fig_name = 'DCA_Vpp.png'

        Plotting.plot_multiple_curves(V_pp_data, args, False, True)

        # plot the eye-amplitude data
        V_pp_data = []; 
        V_pp_data.append([V_PPG, V_PPG]); 
        V_pp_data.append([V_PPG, V_EA_DCA_10]); 
        V_pp_data.append([V_PPG, V_EA_DCA_15]); 
        V_pp_data.append([V_PPG, V_EA_DCA_20]); 

        # make a plot of the data
        args = Plotting.plot_arguments()

        args.loud = True
        args.x_label = 'PPG Output Amplitude (mV)'
        args.y_label = 'Eye-Amplitude (mv)'
        args.plt_range = [195, 375, 175, 380]
        args.crv_lab_list = labels
        args.mrk_list = data_lin
        args.plt_title = 'Eye Amplitude Measured on DCA'
        args.fig_name = 'DCA_EA.png'

        Plotting.plot_multiple_curves(V_pp_data, args, False, True)
        
    except Exception:
        print("Error: BERT_Test.Measured_Vpp()")

def file_rename():
    
    # rename the files inside the ED directory
    # because it's too damn awkward to do it inside CMD
    # R. Sheehan 31 - 7 - 2017

    try:
        DATA_HOME = "Eye_Diag_31_7_2017/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())
        
            #screen_suffices = range(2, 13, 1)
            screen_suffices = range(13, 24, 1)

            freqs = [7.5, 8, 8.5, 9, 10, 11, 12.5, 15, 23, 24.5, 25.0]

            clck_type = "Half"

            if len(screen_suffices) == len(freqs):

                count = 0
                for s in screen_suffices:
                    file_old = "screen%(v1)d.bmp"%{"v1":s}
                    if glob.glob(file_old):
                        file_new = "ED_f_%(v1)0.1f_Clck_%(v2)s.bmp"%{"v1":freqs[count], "v2":clck_type}
                        print(file_old,",",file_new)
                        os.rename(file_old, file_new)
                    count += 1
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: BERT_Test.file_rename")
        print("Error: Cannot find ",DATA_HOME)
    except Exception:
        print("Error: BERT_Test.file_rename")

def file_rename_1():
    
    # rename the files inside the ED directory
    # because it's too damn awkward to do it inside CMD
    # R. Sheehan 19 - 9 - 2017

    try:
        #DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_27_9_2017/A-16dB/"
        #DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_4_10_2017/"
        #DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_10_10_2017/"
        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_30_1_2018/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())

            files = glob.glob("screen*.bmp")

            if files:
                #I_DFB = range(162, 182, 2); 
                

                #DR = [12,10,10,12]
                #Distance = [0, 0, 25, 25]
                #V_EAM = '10'
                #screen_suffices = range(8, 18, 1)
                #screen_suffices.remove(10)

                #screen_suffices = [5, 6, 7, 8, 9]
                #screen_suffices = range(1, 5, 1)
                #Vppg = [200, 240, 280, 320, 340, 370]
                #Vppg = 370
                
                #V_EAM = ['060','065','070','075','080','085']
                #Amp_val = [0, 26, 26, 26, 26, 26]
                #Amp_val = 26
                #Att_val = [0, 0, 3, 6, 9, 12]

                I_DFB = 172;
                I_SOA = 170; 
                V_EAM = '075'
                #DR = 10;
                DR = [12, 10]
                Distance = 27
                Att_val_1 = 13 
                Att_val_2 = [0, 0]
                screen_suffices = range(47, 49, 1)
                #Vppg = [200, 240, 280, 320, 340, 370]                
                Vppg = 370

                count = 0
                for s in screen_suffices: 
                    file_old = "screen%(v1)d.bmp"%{"v1":s}
                    if glob.glob(file_old):
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_DR_%(v3)d.bmp"%{"v1":I_DFB[count],"v2":I_SOA,"v3":DR,"v4":V_EAM}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vpp_20_DR_%(v3)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR,"v4":V_EAM[count]}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR,"v4":V_EAM,"v5":Vppg[count]}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR[count],"v4":V_EAM,"v5":Vppg}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d_D_%(v6)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR[count],"v4":V_EAM,"v5":Vppg, "v6":Distance[count]}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d_Amp_%(v6)d_Att_%(v7)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR, "v4":V_EAM, "v5":Vppg, "v6":Amp_val[count], "v7":Att_val[count]}

                        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d_D_%(v6)d_Att1_%(v7)d_Att2_%(v8)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR[count], "v4":V_EAM, "v5":Vppg, "v6":Distance, "v7":Att_val_1, "v8":Att_val_2[count]}
                        #file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_VEAM_%(v4)s_Vppg_%(v5)d_DR_%(v3)d_D_%(v6)d_Att1_%(v7)d_Att2_%(v8)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR, "v4":V_EAM, "v5":Vppg[count], "v6":Distance, "v7":Att_val_1, "v8":Att_val_2}
                        
                        print(file_old,",",file_new)
                        os.rename(file_old,file_new)
                    count += 1

                #I_DFB = 170; 
                #I_SOA = [161, 164, 167]; 
                #DR = 10;
                #screen_suffices = [15, 16, 17]
                
                #count = 0
                #for s in screen_suffices: 
                #    file_old = "screen%(v1)d.bmp"%{"v1":s}
                #    if glob.glob(file_old):
                #        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_DR_%(v3)d.bmp"%{"v1":I_DFB,"v2":I_SOA[count],"v3":DR}
                #        print(file_old,",",file_new
                #        os.rename(file_old,file_new)
                #    count += 1

                #I_DFB = 170; 
                #I_SOA = [161, 164, 167, 170]; 
                #DR = 10;
                #screen_suffices = [21, 18, 19, 20]
                
                #count = 0
                #for s in screen_suffices: 
                #    file_old = "screen%(v1)d.bmp"%{"v1":s}
                #    if glob.glob(file_old):
                #        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_DR_%(v3)d_Higher_Bias.bmp"%{"v1":I_DFB,"v2":I_SOA[count],"v3":DR}
                #        print(file_old,",",file_new
                #        os.rename(file_old,file_new)
                #    count += 1

                #I_DFB = [174, 176, 172]; 
                #I_SOA = 170; 
                #DR = 10;
                #screen_suffices = [22, 23, 24]
                
                #count = 0
                #for s in screen_suffices: 
                #    file_old = "screen%(v1)d.bmp"%{"v1":s}
                #    if glob.glob(file_old):
                #        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_DR_%(v3)d_Higher_Bias.bmp"%{"v1":I_DFB[count],"v2":I_SOA,"v3":DR}
                #        print(file_old,",",file_new
                #        os.rename(file_old,file_new)
                #    count += 1

                #I_DFB = 172; 
                #I_SOA = 170; 
                #DR = 10;
                #screen_suffices = [26, 27, 28]
                #distances = [25, 20, 0]
                
                #count = 0
                #for s in screen_suffices: 
                #    file_old = "screen%(v1)d.bmp"%{"v1":s}
                #    if glob.glob(file_old):
                #        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_DR_%(v3)d_Higher_Bias_D_%(v4)d.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR,"v4":distances[count]}
                #        print(file_old,",",file_new
                #        os.rename(file_old,file_new)
                #    count += 1

                #I_DFB = 172; 
                #I_SOA = 170; 
                #DR = [15, 12];
                #screen_suffices = [29, 30]
                
                #count = 0
                #for s in screen_suffices: 
                #    file_old = "screen%(v1)d.bmp"%{"v1":s}
                #    if glob.glob(file_old):
                #        file_new = "EAM_ED_I_DFB_%(v1)d_I_SOA_%(v2)d_DR_%(v3)d_Higher_Bias.bmp"%{"v1":I_DFB,"v2":I_SOA,"v3":DR[count]}
                #        print(file_old,",",file_new
                #        #os.rename(file_old,file_new)
                #    count += 1

            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: BERT_Test.file_rename_1")
        print("Error: Cannot find ",DATA_HOME)
    except Exception:
        print("Error: BERT_Test.file_rename_1")

def file_rename_2():
    
    # rename the files inside the ED directory
    # because it's too damn awkward to do it inside CMD
    # R. Sheehan 19 - 9 - 2017

    try:
        DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/EXP-2/ED_19_9_2017/"

        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            print(os.getcwd())

            files = glob.glob("EAM*.bmp")

            if files:
                for f in files:
                    if "Higher" in f:
                        print(f)
                        file_new = f.replace("DR","VEAM_07_DR")
                        file_new = file_new.replace("_Higher_Bias","")
                        print(file_new)
                        os.rename(f,file_new)
            else:
                raise Exception
            os.chdir('..')
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: BERT_Test.file_rename_1")
        print("Error: Cannot find ",DATA_HOME)
    except Exception:
        print("Error: BERT_Test.file_rename_1")