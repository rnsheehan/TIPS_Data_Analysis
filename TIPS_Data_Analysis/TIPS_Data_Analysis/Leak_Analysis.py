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

# variables that tell you what data is in each column
CURR_VAL = 0; # column containing current data
DFB_VAL = 1; SOA_VAL = 3; EAM_VAL = 5; PWR_VAL = 7; # columns containing measured data
DFB_ERR = 2; SOA_ERR = 4; EAM_ERR = 6; PWR_ERR = 8; # columns containing errors in measured data

# This module should include methods for reading the leakage analysis data
# and plotting the leakage data for various plots
# R. Sheehan 7 - 11 - 2017

class sweep_params(object):
    # class that contains parameters for a sweep
    # temperature = temperature of device during sweep
    # EAM_bias = voltage across EAM during sweep
    # current = current across section of device during sweep, section may be DFB or SOA
    # sweep_type tells you if sweep is over DFB or SOA section
    # if sweep_device == DFB: current is SOA current
    # if sweep_device == SOA: current is DFB current

    # constructor
    # define default arguments inside
    def __init__(self):
        try: 
            self.temperature = 20.0 # device temperature
            self.EAM_bias = 0.0 # EAM bias
            self.static_device_current = 0.0 # current in other section of device
            self.sweep_device = "" # string that tells you if sweep is over DFB section or SOA section. 
            self.static_device = "" # string that tells you if sweep is over DFB section or SOA section. 
        except TypeError:
            print("Type Error in Leak_Analysis.sweep_params(object) instantiation")

    # return a string the describes the class
    def __str__(self):
        return self.sweep_device + ", " + self.static_device + " Current = " + str(self.static_device_current) + " (mA), EAM bias = " + str(self.EAM_bias) + " (V)"

def read_Leak_data(leak_file, correct_power = True, loud = False):

    # read the measured leakage data from the file
    # Data is stored in columns of the form
    # 0. Current (mA)	
    # 1. V_{DFB} (V)	
    # 2. \DeltaV_{DFB} (V)
    # 3. V_{SOA} (V)	
    # 4. \Delta V_{SOA} (V)	
    # 5. I_{EAM} (mA)
    # 6. \Delta I_{EAM} (mA)
    # 7. P_{out} (dBm)
    # 8. \Delta P_{out} (dBm)
    # correct_power decides whether or not to correct the power being read from the file
    # Due to an oversight the optical power was measured through the 10% arm of the power splitter after it had passed through the VOA
    # While this will not affect the behaviour of the device it will mean that the measured power is less than it should be. 
    # When plotting the measured power remember to convert it to the 90% value and add 1 dB due to the IL of the VOA.
    # R. Sheehan 7 - 11 - 2017

    try:
        if glob.glob(leak_file):

            numbers = Common.extract_values_from_string(leak_file)

            parameters = sweep_params()
            parameters.temperature = float(numbers[1])
            parameters.EAM_bias = float(numbers[3]) 

            if leak_file.find("DFB") > 0:
                parameters.static_device_current = float(numbers[2]) # current across DFB section
                parameters.sweep_device = "SOA"; parameters.static_device = "DFB";               
            elif leak_file.find("SOA") > 0:
                parameters.static_device_current = float(numbers[2]) # current across SOA section
                parameters.sweep_device = "DFB"; parameters.static_device = "SOA";
            else:
                raise Exception         

            delim = '\t'

            data = Common.read_matrix(leak_file, delim)
            data = Common.transpose_multi_col(data)

            if correct_power == True:
                # adjust the power reading to the 90% value
                # add insertion loss due to the VOA
                slope = 1.0038; intercept = 9.4697; # values obtained from fit
                insertion_loss = 0.8 # insertion loss due to VOA in dB
                power_column = 7
                for i in range(0, len(data[power_column]), 1):
                    data[power_column][i] = insertion_loss + intercept + slope*data[power_column][i]
            
            return [parameters, data]
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.read_Leak_data")

def get_Leak_label(quantity):
    # return a string to serve as a label on a plot based on the value of quantity
    # R. Sheehan 8 - 11 - 2017

    try:
        c2 = True if quantity > 0 and quantity < 9 else False

        if c2:
            if quantity == 1:
                return 'DFB Voltage $V_{DFB}$ (V)'
            elif quantity == 2:
                return 'DFB Voltage Variation $\Delta V_{DFB}$ (V)'
            elif quantity == 3:
                return 'SOA Voltage $V_{SOA}$ (V)'
            elif quantity == 4:
                return 'SOA Voltage Variation $\Delta V_{SOA}$ (V)'
            elif quantity == 5:
                return 'EAM Current $I_{EAM}$ (mA)'
            elif quantity == 6:
                return 'EAM Current Variation $\Delta I_{EAM}$ (mA)'
            elif quantity == 7:
                return 'Optical Power $P_{out}$ (dBm)'
            elif quantity == 8:
                return 'Optical Power Variation $\Delta P_{out}$ (dBm)'
            else:
                raise Exception
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.get_Leak_label()")

def get_Leak_name(quantity):
    # return a string to serve as a name for a file containing a plot based on the value of quantity
    # R. Sheehan 9 - 11 - 2017

    try:
        c2 = True if quantity > 0 and quantity < 9 else False

        if c2:
            if quantity == 1:
                return 'DFB_Voltage'
            elif quantity == 2:
                return 'Delta_DFB_Voltage'
            elif quantity == 3:
                return 'SOA_Voltage'
            elif quantity == 4:
                return 'Delta_SOA_Voltage'
            elif quantity == 5:
                return 'EAM_Current'
            elif quantity == 6:
                return 'Delta_EAM_Current'
            elif quantity == 7:
                return 'Optical_Power'
            elif quantity == 8:
                return 'Delta_Optical_Power'
            else:
                raise Exception
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.get_Leak_label()")

def get_Leak_plot_range(quantity):
    # return a list to serve as a plot range for a plot based on the value of quantity
    # R. Sheehan 9 - 11 - 2017

    try:
        c2 = True if quantity > 0 and quantity < 9 else False

        if c2:
            if quantity == 1:
                return [0, 180, 0, 2.1]
            elif quantity == 2:
                return [0, 180, 1.0e-4, 1.0]
            elif quantity == 3:
                return [0, 180, 0, 2.6]
            elif quantity == 4:
                return [0, 180, 1.0e-4, 1.0]
            elif quantity == 5:
                return [0, 180, -4, 0.0]
            elif quantity == 6:
                return [0, 180, 1.0e-6, 1.0]
            elif quantity == 7:
                return [0, 180, -90, 0.0]
            elif quantity == 8:
                return [0, 180, 0, 0.01]
            else:
                raise Exception
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.get_Leak_label()")

def plot_Leak_quantity(leak_data_1, leak_data_2, quantity, loud = False):

    # plot a measured quantity from the leakage analysis
    # sweep_type of each data set has to be the same
    # R. Sheehan 8 - 11 - 2017

    try:
        c1 = True if leak_data_1[0].sweep_device == leak_data_1[0].sweep_device else False
        c2 = True if quantity > 0 and quantity < 9 else False
        c3 = True if leak_data_1[0].static_device_current == leak_data_1[0].static_device_current else False

        if c1 and c2 and c3:
            hv_data = []; labels = []; marks = []; 

            hv_data.append([ leak_data_1[1][CURR_VAL], leak_data_1[1][quantity] ] ); 
            marks.append(Plotting.labs_lins[0]); 
            labels.append('$V_{EAM}$ = %(v1)0.2f V'%{ "v1":leak_data_1[0].EAM_bias } )

            hv_data.append([leak_data_2[1][CURR_VAL], leak_data_2[1][quantity] ]); 
            marks.append(Plotting.labs_lins[1]); 
            labels.append('$V_{EAM}$ = %(v1)0.2f V'%{"v1":leak_data_2[0].EAM_bias})

            arguments = Plotting.plot_arg_multiple()

            arguments.loud = loud
            arguments.crv_lab_list = labels
            arguments.mrk_list = marks
            arguments.x_label = leak_data_1[0].sweep_device + ' Current (mA)'
            arguments.y_label = get_Leak_label(quantity)
            arguments.plt_range = get_Leak_plot_range(quantity)
            arguments.plt_title = leak_data_1[0].static_device + ' Current = ' + str(leak_data_1[0].static_device_current) + ' (mA)'
            arguments.fig_name = get_Leak_name(quantity) + '_I' + leak_data_1[0].static_device + '_' + str(leak_data_1[0].static_device_current).replace('.0','')
            if quantity%2 == 0 and quantity < PWR_ERR: arguments.log_y = True

            Plotting.plot_multiple_curves(hv_data, arguments)

            # error in this case is very small, best to do separate analysis on error data
            #Plotting.plot_multiple_curves_with_errors(hv_data, arguments) 

            del hv_data; del labels; del marks; del arguments; 
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.plot_Leak_quantity")

def SOA_Sweep_Plots(DFB_Current, plot_errors = False, loud = False):
    # make plots of the data for the SOA Sweep
    # R. Sheehan 8 - 11 - 2017

    try:
        files = glob.glob("TIPS_1_EAM_Lk_T_20_IDFB_%(v)d_VEAM*"%{"v":DFB_Current})
        if files:
            the_data = []
            for f in files:
                the_data.append( read_Leak_data(f) )

            if plot_errors:
                plot_Leak_quantity(the_data[1], the_data[0], DFB_ERR, loud)
                plot_Leak_quantity(the_data[1], the_data[0], EAM_ERR, loud)
                plot_Leak_quantity(the_data[1], the_data[0], PWR_ERR, loud)
            else:
                plot_Leak_quantity(the_data[1], the_data[0], DFB_VAL, loud)
                plot_Leak_quantity(the_data[1], the_data[0], EAM_VAL, loud)
                plot_Leak_quantity(the_data[1], the_data[0], PWR_VAL, loud)
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.SOA_Sweep_Plots")

def DFB_Sweep_Plots(SOA_Current, plot_errors = False, loud = False):
    # make plots of the data for the DFB Sweep
    # R. Sheehan 8 - 11 - 2017

    try:
        files = glob.glob("TIPS_1_EAM_PC_T_20_ISOA_%(v)d_VEAM*"%{"v":SOA_Current})
        if files:
            the_data = []
            for f in files:
                the_data.append( read_Leak_data(f) )

            if plot_errors:
                plot_Leak_quantity(the_data[1], the_data[0], SOA_ERR, loud)
                plot_Leak_quantity(the_data[1], the_data[0], EAM_ERR, loud)
                plot_Leak_quantity(the_data[1], the_data[0], PWR_ERR, loud)
            else:
                plot_Leak_quantity(the_data[1], the_data[0], SOA_VAL, loud)
                plot_Leak_quantity(the_data[1], the_data[0], EAM_VAL, loud)
                plot_Leak_quantity(the_data[1], the_data[0], PWR_VAL, loud)
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.DFB_Sweep_Plots")

def Error_Statistics(error_data, drop_terms = 1, neglect_zeroes = False, scale = True, scale_factor = 1000.0):
    # compute the average value and standard deviation of a set of measured error values
    # error_data should be input as numpy array
    # use np.asarray(input)
    # R. Sheehan 9 - 11 - 2017

    # if you want to drop the first element use error_data[1:]

    # In certain situtations error data may be dominated by zero values, too many zeroes will give an incorrect estimate of mean and std. dev
    # if neglect_zeroes == True compute mean and std. dev of non-zero error_data only

    try:
        if error_data is not None:
            if neglect_zeroes == False:
                # compute mean and std. dev using all data in the array
                average = np.mean(error_data[drop_terms:])
                std_dev = np.std(error_data[drop_terms:], ddof = 1)
                #std_dev = np.max(error_data[drop_terms:]) - np.min(error_data[drop_terms:])
            else:
                # compute mean and std. dev neglecting zero values
                # use the corrected two-pass formula given in NRinC, sect. 14.1

                #first step is to ensure that there are more than one non-zero terms
                count = 0
                for j in range(0, len(error_data), 1):
                    if math.fabs(error_data[j]) > 0.0:
                        count += 1
                if count > 1:
                    count1 = count2 = 0
                    average = std_dev = ep = 0.0; 
                    # first pass compute the average
                    for j in range(0, len(error_data), 1): 
                        if math.fabs(error_data[j]) > 0.0:
                            average += error_data[j]
                            count1 += 1
                    average = average/count1
                    # second pass compute the variance
                    for j in range(0, len(error_data), 1): 
                        if math.fabs(error_data[j]) > 0.0:
                            s = error_data[j] - average
                            ep += s
                            std_dev += s**2 # variance is stored in std_dev for now
                            count2 += 1
                    std_dev = (std_dev - (ep**2/count2))/(count2-1)
                    std_dev = math.sqrt(std_dev)
                else:
                    # revert to whatever numpy wants to do if there's not enough data points
                    # in fact numpy will just return zero values under the same circumstances so may as well not bother with the numpy call
                    #print("Not enough data points to use corrected two-pass formula\nreverting to numpy"
                    #average = np.mean(error_data[drop_terms:])
                    #std_dev = np.std(error_data[drop_terms:], ddof = 1)
                    average = std_dev = 0.0
            if scale == True:
                average = scale_factor*average;
                std_dev = scale_factor*std_dev;
            return [ average, std_dev ]
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.Error_Statistics()")

def Print_Error_Analysis(static_device_name, static_device_current):
    # go through the measured errors for each data set and determine the average measured error
    # along with std. deviation.
    # Make a plot of the results 
    # R. Sheehan 9 - 11 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            files = glob.glob("TIPS_1_EAM_*_T_20_I%(v1)s_%(v2)d_VEAM*"%{"v1":static_device_name, "v2":static_device_current})
            if files:
                drop_vals = 1
                scale_data = False
                neglect_zeroes = False
                scale_factor = 1.0
                volt_units = " (uV)" if scale_factor == 1.0e+6 else " (V)"
                current_units = " (nA)" if scale_factor == 1.0e+6 else " (mA)"
                for f in files:
                    data = read_Leak_data(f)

                    print(data[0])
                    print("DFB voltage error: ",Error_Statistics( np.asarray(data[1][2]), drop_vals, neglect_zeroes, scale_data, scale_factor )[0],volt_units)
                    print("SOA voltage error: ",Error_Statistics( np.asarray(data[1][4]), drop_vals, neglect_zeroes, scale_data, scale_factor )[0],volt_units)
                    print("EAM current error: ",Error_Statistics( np.asarray(data[1][6]), drop_vals, neglect_zeroes, scale_data, scale_factor )[0],current_units)
                    print("Optical power error: ",Error_Statistics( np.asarray(data[1][8]), drop_vals, neglect_zeroes, False )[0]," (dBm)\n")

                    del data; 
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.Print_Error_Analysis()")

def Get_Error_Analysis_Data(static_device_name, static_device_current, eam_bias, quantity, remove_zeroes = False, loud = False):
    # go through the measured errors for each data set and determine the average measured error 
    # along with std. deviation versus the applied current
    # Make a plot of the results 
    # R. Sheehan 9 - 11 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            c1 = True if quantity > 1 and quantity < 9 else False
            files = glob.glob("TIPS_1_EAM_*_T_20_I%(v1)s_%(v2)d_VEAM_%(v3)0.2f.txt"%{"v1":static_device_name, "v2":static_device_current, "v3":eam_bias})
            if files and c1:
                drop_vals = 0                
                ret_data = []
                for f in files:
                    data = read_Leak_data(f)

                    dfb_err = Error_Statistics( np.asarray(data[1][quantity]), drop_vals, remove_zeroes, False) # no scaling is being applied when error statistics are computed

                    ret_data.append(data[0].static_device_current); 
                    ret_data.append(data[0].temperature);
                    ret_data.append( math.fabs(dfb_err[0]) ); 
                    ret_data.append( math.fabs(dfb_err[1]) );                   

                    if loud:
                        scale_factor = 1.0e+3
                        volt_units = " (uV)" if scale_factor == 1.0e+6 else " (mV)"
                        current_units = " (nA)" if scale_factor == 1.0e+6 else " (uA)"
                        print(data[0])
                        print("DFB voltage error: ",Error_Statistics( np.asarray(data[1][2]), drop_vals, remove_zeroes, True, scale_factor),volt_units)
                        print("SOA voltage error: ",Error_Statistics( np.asarray(data[1][4]), drop_vals, remove_zeroes, True, scale_factor),volt_units)
                        print("EAM current error: ",Error_Statistics( np.asarray(data[1][6]), drop_vals, remove_zeroes, True, scale_factor),current_units)
                        print("Optical power error: ",Error_Statistics( np.asarray(data[1][8]), drop_vals, remove_zeroes, False)," (dBm)\n")

                    del data;

                return ret_data
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.Get_Error_Analysis_Data()")

def Gather_Error_Analysis_Data(static_dev_name, eam_bias, quantity, remove_zeroes = False):
    # gather together all the error analysis data in a format suitable for plotting
    # this function returns the average error for each static device current
    # value being computed is the average error over the swept current
    # R. Sheehan 9 - 11 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            dev_current = [0, 50, 100, 140, 150, 160, 170, 180]
            error_data = []
            for ii in dev_current:
                data = Get_Error_Analysis_Data(static_dev_name, ii, eam_bias, quantity, remove_zeroes)
                error_data.append(data); del data; 
            
            del dev_current; 

            error_data = Common.transpose_multi_col(error_data)

            return error_data
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.Gather_Error_Analysis_Data()")

def plot_Error_Analysis_data(swept_device_name, static_device_name, quantity, remove_zeroes = False, loud = False):
    # make plots of the gathered error analysis data
    # the error is averaged over all static_device_current values

    # what is the scaling being applied when the plot is being made? 

    try:
        VEAM = 0.0
        ds1 = Gather_Error_Analysis_Data(static_device_name, VEAM, quantity, remove_zeroes)
        
        VEAM = -0.5
        ds2 = Gather_Error_Analysis_Data(static_device_name, VEAM, quantity, remove_zeroes)

        if ds1 is not None and ds2 is not None:
            hv_data = []; labels = []; marks = []; 

            hv_data.append([ds1[0], ds1[2]]); labels.append('$V_{EAM}$ = 0 (V)'); marks.append(Plotting.labs_pts[0])
            hv_data.append([ds2[0], ds2[2]]); labels.append('$V_{EAM}$ = -0.5 (V)'); marks.append(Plotting.labs_pts[1])

            arguments = Plotting.plot_arg_multiple()

            arguments.loud = loud
            arguments.crv_lab_list = labels; arguments.mrk_list = marks;
            arguments.x_label = static_device_name + ' Current (mA)'
            arguments.y_label = get_Leak_label(quantity)
            #arguments.plt_range = get_Leak_plot_range(quantity) if quantity < PWR_ERR else None
            arguments.plt_range = get_Leak_plot_range(quantity)
            arguments.plt_title = 'Average Error while current sweeps across ' + swept_device_name
            if quantity < PWR_ERR: arguments.log_y = True 
            arguments.fig_name = get_Leak_name(quantity-1) + '_' + swept_device_name + '_Sweep_Error'

            Plotting.plot_multiple_curves(hv_data, arguments)

            del ds1; del ds2; del hv_data; del marks; del labels;
        else:
            raise Exception
    except Exception:
        print("Error: Leak_Analysis.plot_Error_Analysis_data()")

def SOA_Sweep_Error_Plots(remove_zeroes = False, loud = False):
    # Make a plot of the averaged measured error for each measurement
    # R. Sheehan 15 - 11 - 2017

    try:
        swept_device_name = 'SOA'; static_device_name = 'DFB'; 

        plot_Error_Analysis_data(swept_device_name, static_device_name, DFB_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name, static_device_name, SOA_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name, static_device_name, EAM_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name, static_device_name, PWR_ERR, remove_zeroes, loud)
    except Exception:
        print("Error: Leak_Analysis.SOA_Sweep_Error_Plots()")

def DFB_Sweep_Error_Plots(remove_zeroes = False, loud = False):
    # Make a plot of the averaged measured error for each measurement
    # R. Sheehan 15 - 11 - 2017

    try:
        swept_device_name = 'DFB'; static_device_name = 'SOA'; 

        plot_Error_Analysis_data(swept_device_name,static_device_name, DFB_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name,static_device_name, SOA_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name,static_device_name, EAM_ERR, remove_zeroes, loud)
        
        plot_Error_Analysis_data(swept_device_name,static_device_name, PWR_ERR, remove_zeroes, loud)
    except Exception:
        print("Error: Leak_Analysis.SOA_Sweep_Error_Plots()")

def run_Leak_sweep_plots_all(error_plots = False):

    # short script for plotting all measured data
    Ival = [0, 50, 100, 140, 150, 160, 170, 180]
    for ii in Ival:
        SOA_Sweep_Plots(ii,error_plots)
        DFB_Sweep_Plots(ii,error_plots)

def Compare_Higher_Bias(static_device, quantity, loud = False):
    # compare data measured at higher bias

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/Higher_Bias/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            files = glob.glob("TIPS_1_EAM*T_20_I%(v1)s*VEAM*"%{"v1":static_device})
            if files:
                for f in files: print(f)
            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Leak_Analysis.Compare_Higher_Bias()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("Error: Leak_Analysis.Compare_Higher_Bias()")

def Compare_Higher_Temperature(static_device, eam_bias, loud = False):
    # compare data measured over higher temperatures
    # read in data
    # loop over quantity to make all the necessary plots
    # power data at T = 25, 30 was collected without the need for correction
    # R. Sheehan 16 - 11 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/Higher_Temperature/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)
            files = glob.glob("TIPS_1_EAM*T*I%(v1)s*VEAM_%(v2)0.2f.txt"%{"v1":static_device, "v2":eam_bias})
            if files:
                # read in all data
                the_data = []
                for i in range(0, len(files), 1):
                    numbers = Common.extract_values_from_string(files[i])
                    if int(numbers[1]) == 20:
                        correct_power = True
                    else:
                        correct_power = False
                    the_data.append( read_Leak_data(files[i], correct_power) )
                    del numbers
                
                # loop over quantity to make the necessary plots
                quantity = [DFB_VAL, SOA_VAL, EAM_VAL, PWR_VAL]                

                #eam_str = "%(v2)0.2f"%{"v2":eam_bias}
                
                for q in quantity:
                    hv_data = []; labels = []; marks = [];
                    
                    for i in range(0, len(the_data), 1):
                        hv_data.append( [ the_data[i][1][CURR_VAL], the_data[i][1][q] ] ); 
                        marks.append(Plotting.labs_lins[i])
                        labels.append('T = %(v1)0.0f C'%{"v1":the_data[i][0].temperature})

                    arguments = Plotting.plot_arg_multiple()

                    arguments.loud = loud
                    arguments.crv_lab_list = labels
                    arguments.mrk_list = marks
                    arguments.x_label = the_data[0][0].sweep_device + ' Current (mA)'
                    arguments.y_label = get_Leak_label(q)
                    #arguments.plt_range = get_Leak_plot_range(q)
                    arguments.plt_title = the_data[0][0].static_device + ' Current = ' + str(the_data[0][0].static_device_current) + ' (mA)'
                    arguments.fig_name = get_Leak_name(q) + '_I' + the_data[0][0].static_device + '_' + str(the_data[0][0].static_device_current).replace('.0','') + '_VEAM_' + '%(v2)0.2f'%{"v2":eam_bias} + '.png'
                    #if q%2 == 0 and q < PWR_ERR: arguments.log_y = True

                    Plotting.plot_multiple_curves(hv_data, arguments)

                    del hv_data; del labels; del marks; 

                del the_data; del files;                 
            else:
                raise Exception
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Leak_Analysis.Compare_Higher_Temperature()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("Error: Leak_Analysis.Compare_Higher_Temperature()")

def Make_Leak_plots():

    # call the functions needed to generate the plots for TIPS Exp 2
    # R. Sheehan 30 - 8 - 2017

    DATA_HOME = "C:/Users/Robert/Research/EU_TIPS/Data/Exp-2/Leak_SWP/"

    try:
        if os.path.isdir(DATA_HOME):
            os.chdir(DATA_HOME)

            #ii = 170
            #SOA_Sweep_Plots(ii, True, True)

            #run_Leak_sweep_plots_all(error_plots = False)                

            #static_device_name = 'DFB'
            #static_device_current = 180
            #eam_bias = 0
            #quantity = DFB_ERR            
            #loud = True

            #remove_zeroes = False
            #Get_Error_Analysis_Data(static_device_name, static_device_current, eam_bias, quantity, remove_zeroes, loud)  
            
            #remove_zeroes = True
            #Get_Error_Analysis_Data(static_device_name, static_device_current, eam_bias, quantity, remove_zeroes, loud)

            #remove_zeroes = True; loud = False
            #SOA_Sweep_Error_Plots(remove_zeroes, loud)
            #DFB_Sweep_Error_Plots(remove_zeroes, loud) 

            static_device = 'DFB'
            quantity = DFB_VAL
            loud = False
            #Compare_Higher_Bias(static_device, DFB_VAL, loud)

            eam_bias = -0.5
            Compare_Higher_Temperature(static_device, eam_bias, loud)
        else:
            raise EnvironmentError
    except EnvironmentError:
        print("Error: Leak_Analysis.Make_Leak_plots()")
        print("Cannot find",DATA_HOME)
    except Exception:
        print("Error: Leak_Analysis.Make_Leak_plots()")
