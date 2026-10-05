#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: 
#
# Author: Tallulah Bowden (tsb66@duke.edu)
# Date:   October 5, 2026
#--------------------------------------------------------------

#%% Task 4.1 Reading in the data and displaying the column headers

#Create a Python file object, i.e., a link to the file's contents
with open(file='data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)



# %% Task 4.2 Splitting the header string into a list of column names and extracting index values

#Split the headerLineString into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index("mmsi")
name_idx = header_items.index("shipname")
fleet_idx = header_items.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)



#%% Task 4.3 Iterating through the data lines and adding values to a dictionary

#Create an empty dictionary
vessel_dict = {}

#Iterate through all lines (except the header) in the data file:
for i in line_list[1:]:
    
    #Split the data into values
    value_list = i.split(',')
    
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = value_list[mmsi_idx]
    
    #Extract the fleet value
    fleet = value_list[fleet_idx]
    
    #Adds info to the vesselDict dictionary
    vessel_dict[mmsi] = fleet


#%% Task 4.4 Using your dictionary

# Create vessel ID variable
vesselID = "312887000"

# Lookup fleet name for this vessel ID
vesselFleet = vessel_dict[vesselID]

# Print statement
print(f'Vessel # {vesselID} flies the flag of {vesselFleet}')


#%% Task 5 Scripting Task

#Create a Python file object to read the loitering file
with open(file='data/raw/loitering_events_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list2 = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line2 = line_list2[0]

#Print the contents of the headerLine
print(header_line2)

#Split the headerLineString into a list of header items
header_items2 = header_line2.split(',')

#List the index of the mmsi, shipname, and fleet_name values
transship_mmsi_idx = header_items2.index("transshippment_mmsi")
start_lat_idx = header_items2.index("starting_latitude")
end_lat_idx = header_items2.index("ending_latitude")
start_long_idx = header_items2.index("starting_longitude")
end_long_idx = header_items2.index("ending_longitude")

#Print the values
print(transship_mmsi_idx, start_lat_idx, end_lat_idx, start_long_idx, end_long_idx)

# Iterate through all lines (except the header) in the loitering data file
for i in line_list2[1:]:
    
    #Split the data into values
    value_list2 = i.split(',')
    
    #Extract the mmsi value
    transship_mmsi = value_list2[transship_mmsi_idx]
    
    #Extract the starting latitude value
    start_lat = value_list2[start_lat_idx]

    #Extract the ending latitude value
    end_lat = value_list2[end_lat_idx]

    #Extract the starting longitude value
    start_long = value_list2[start_long_idx]

    #Extract the ending longitude value
    end_long = value_list2[end_long_idx]

    #Create boolean value for if lat crosses equator

    #Create boolean value for if long ends between 120°E and 135°E

    #If both true, print mmsi and fleet

    #If no vessels meet criteria, print message