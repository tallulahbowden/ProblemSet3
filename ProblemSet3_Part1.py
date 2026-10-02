#-------------------------------------------------------------
# ProblemSet3_Part1.py
#
# Description: 
#
# Author: Tallulah Bowden (tsb66@duke.edu)
# Date:   October 1, 2026
#--------------------------------------------------------------

#%% Task 1 - Edit code to print as requested
## PS3: Code Block 1

# Values for variables
mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

# Print out statement with values for Denali
print (f"{mountain}, formerly \nknown as {nickname}, \nis {elevation}' above sea level.")


#%% Task 2 - Lists and Iteration
## PS3: Code Block 2

# Assign variable values
data_folder = "W:\\859_data\\triangle"
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"
data_list.append(user_item)

# Loop through each item in data_list and print the full path
for path in data_list:
    print(data_folder + "\\" + path)

# %% Task 3 - 
