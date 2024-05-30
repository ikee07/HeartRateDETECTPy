# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:09:10 2023

@author: ikbel
"""

import sys, os, os.path
from scipy.io import wavfile
import pandas as pd

# Prompt the user for the input file number (filename)
input_filename = input("Input file number: ")

# Get the current working directory
current_directory = os.getcwd()

# Combine the current directory and input filename to get the full path
full_path = os.path.join(current_directory, input_filename)

if input_filename[-3:] != 'wav':
    print('WARNING!! Input File format should be *.wav')
    sys.exit()

# Read the WAV file from the full path
samrate, data = wavfile.read(full_path)
print('Load is Done!\n')

wavData = pd.DataFrame(data)

if len(wavData.columns) == 2:
    print('Stereo .wav file\n')
    wavData.columns = ['R', 'L']
    stereo_R = pd.DataFrame(wavData['R'] / 1000)  # Normalize data by dividing by 1000
    stereo_L = pd.DataFrame(wavData['L'] / 1000)  # Normalize data by dividing by 1000
    print('Saving...\n')
    stereo_R.to_csv(input_filename[:-4] + "_Output_stereo_R.csv", mode='w')
    stereo_L.to_csv(input_filename[:-4] + "_Output_stereo_L.csv", mode='w')
    print('Save is done ' + input_filename[:-4] + '_Output_stereo_R.csv, ' +
          input_filename[:-4] + '_Output_stereo_L.csv')

elif len(wavData.columns) == 1:
    print('Mono .wav file\n')
    wavData.columns = ['M']
    mono_data = wavData['M'] / 1000  # Normalize data by dividing by 1000
    mono_data.to_csv(input_filename[:-4] + "_Output_mono.csv", mode='w')
    print('Save is done ' + input_filename[:-4] + '_Output_mono.csv')

else:
    print('Multi-channel .wav file\n')
    print('Number of channels: ' + str(len(wavData.columns)) + '\n')
    normalized_data = wavData / 1000  # Normalize data by dividing by 1000
    normalized_data.to_csv(input_filename[:-4] + "Output_multi_channel.csv", mode='w')
    print('Save is done ' + input_filename[:-4] + 'Output_multi_channel.csv')
