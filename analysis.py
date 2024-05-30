# Import the required packages
# Make sure to install the 'heartpy' library if not already installed
import heartpy as hp
import matplotlib.pyplot as plt
%matplotlib inline  # Ensure Matplotlib is in inline mode

# Clear any existing figures
plt.close('all')

# Set the sample rate for the heart rate data
sample_rate = 250

# Load heart rate data from a CSV file named '1_Output_mono.csv'
data = hp.get_data('1_Output_mono.csv')
# Alternatively, you can load data from another source using the 'get_data' function.

# Plot the loaded heart rate data
plt.figure(figsize=(12, 4))
plt.plot(data)
plt.show()

# Perform an analysis on the heart rate data using HeartPy's 'process' function
wd, m = hp.process(data, sample_rate)

# Visualize the analysis results using HeartPy's 'plotter' function
plt.figure(figsize=(12, 4))
hp.plotter(wd, m)

# Display computed measures from the analysis
for measure in m.keys():
    print('%s: %f' % (measure, m[measure]))
