#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: 
#
# Author: Tallulah Bowden (tsb66@duke.edu)
# Date:   October 5, 2026
#--------------------------------------------------------------

#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
with open(file='data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)



# %% Task 4.2

#Split the headerLineString into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index("mmsi")
name_idx = header_items.index("shipname")
fleet_idx = header_items.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

# %%
