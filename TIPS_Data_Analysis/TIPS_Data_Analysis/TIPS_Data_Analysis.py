
# Import libraries
import sys # access system routines
import os
import glob
import re

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# add path to our file
#sys.path.append('c:/Users/Robert/Dropbox/Python/')

import Common # functions are then called using the command Common.{function_name}
import TIPS_DFB_SOA_Charact # functions that import the measured data and generate plots of the data for the first TIPS device
import TIPS_FR_Analysis # functions that import and plot the measured FR data for the TIPS device
import TIPS_Transmission # functions for plotting the measured BER results
import BERT_Test # make plots of data obtained after post-calibration test of BERT
import TEC_Exam
import TIPS_DFB_EAM_SOA
import Leak_Analysis
import TIPS_Pre_Amp_Rx
import TIPS_WDM_Exp

#import PIL

def sandbox():
    # test out all the python stuff you don't know here

    #str1 = "TIPS_1_EAM_Lk_T_20_IDFB_"

    #print(str1.find("DFB")

    #if str1.find("DFB")  > 0: print(str1," contains DFB"

    #str2 = "TIPS_1_EAM_PC_T_20_ISOA_"

    #print(str2.find("DFB")

    #if str2.find("DFB") > 0: print(str2," contains DFB"

    list_exp = [5, 8, -1, 14, 12, 13]
    #list_exp = [5, 8, 14, 12, 13]

    #print(list_exp
    #print(list_exp[:-1]
    #print(list_exp[2:]

    print(Common.list_has_negative( np.asarray(list_exp) ))

    distance = 67
    the_files = ["TIPS_D_%(v1)dkm.txt"%{"v1":distance}, "TIPS_plus_SOA_D_%(v1)dkm.txt"%{"v1":distance}]

    print(the_files)

def errorbar_plot_test():
    # test the generic error bar plot function in Plotting module
    # R. Sheehan 13 - 11 - 2017

    # example data
    x = np.arange(0.1, 4, 0.25)
    y = np.exp(-x)
    yy = np.cos(x)

    # example variable error bar values
    #yerr = 0.1 + 0.2*np.sqrt(x)
    yerr = np.random.uniform(0.0, 0.5, len(y))
    yyerr = np.random.uniform(0.0, 0.5, len(y))
    xerr = np.random.uniform(0.0, 0.25, len(x))

    # First illustrate basic pyplot interface, using defaults where possible.
    #plt.figure()
    #plt.errorbar(x, y, yerr, xerr)
    #plt.errorbar(x, y, yerr)
    #plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
    #plt.show()

    import Plotting

    #arguments = Plotting.plot_arg_single()
    #arguments.loud = True
    #arguments.log_y = True

    #Plotting.plot_single_curve_with_errors(x, y, yerr, arguments)

    arguments = Plotting.plot_arg_multiple()
    arguments.loud = True
    arguments.crv_lab_list = ['data 1','data 2']
    arguments.mrk_list = [Plotting.labs[2], Plotting.labs[4]]
    arguments.log_y = True

    hv_data = []
    hv_data.append([x, y, yerr]); hv_data.append([x, y, yyerr]); 

    Plotting.plot_multiple_curves_with_errors(hv_data, arguments)

def Image_Format_Convert_Test():
    # use the Python Image library to conver the format of saved figures
    # see https://statbandit.wordpress.com/2011/09/29/converting-images-in-python/ for some details
    # Image Library can be found at http://www.pythonware.com/products/pil/
    # Documentation http://www.pythonware.com/library/pil/handbook/
    # Better documentation? http://effbot.org/imagingbook/image.htm

    DATA_HOME = 'C:/Users/Robert/Research/Publications/SPIE_Europe_2018/Sample_Images/'

    try:
        if os.path.isdir(DATA_HOME):

            from PIL import Image
            from StringIO import StringIO

            os.chdir(DATA_HOME)

            print(os.getcwd())

            img_files = glob.glob("*.png")

            for f in img_files:
                #f_out = f.replace(".png",".EPS") # rename the files
                f_out = f.replace(".png","")
                #print(f,",",f_out
                print(f_out)
                img = Image.open(f)
                print("Image Size:",img.size)
                #img.save(f_out,".jpeg") Seems like you need to do loads of stuff to get this working the way you want, not worth the hassle
                # R. Sheehan 25 - 1 - 2018
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Image_Format_Convert_Test")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("Error: Image_Format_Convert_Test")

def Image_Format_Convert_Test_Matplotlib():

    #DATA_HOME = 'C:/Users/Robert/Research/Publications/SPIE_Europe_2018/Sample_Images/'
    DATA_HOME = 'C:/Users/Robert/Research/Publications/SPIE_Europe_2018/'

    try:
        if os.path.isdir(DATA_HOME):

            os.chdir(DATA_HOME)

            print(os.getcwd())

            img_files = glob.glob("*.png")

            for f in img_files:
                f_out = f.replace(".png",".eps") # rename the files
                print(f_out)
                # read the image from memory
                img = mpimg.imread(f)
                #plt.imshow(img)  
                #plt.show()
                #plt.close()
                mpimg.imsave(f_out, img) # exactly what I was looking for!
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Image_Format_Convert_Test")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("Error: Image_Format_Convert_Test")
    
def main():
    pass

if __name__ == '__main__':
    main()

    #TIPS_DFB_SOA_Charact.Make_TIPS_1_Plots()

    #TIPS_FR_Analysis.Make_TIPS_FR()

    #TIPS_Transmission.Make_TIPS_Transmission()

    #BERT_Test.BERT_Plots()
    
    #TIPS_DFB_EAM_SOA.test_peak_search_analysis()
    #errorbar_plot_test()
    #sandbox()
    Image_Format_Convert_Test_Matplotlib()

    #BERT_Test.file_rename_1()

    #TEC_Exam.Plot_TEC_Exam_Results()

    #TIPS_DFB_EAM_SOA.Make_TIPS_Exp_2_plots()

    #Leak_Analysis.Make_Leak_plots()

    #TIPS_Pre_Amp_Rx.Make_TIPS_Pre_Amp()    

    #TIPS_WDM_Exp.Make_TIPS_WDM_plots()