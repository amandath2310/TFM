import os
import csv

def extract_occupancy(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "Natural Orbital Occupation Numbers:" in line:
                occupancy1_line = lines[i+1] # The line in which I have the first occupation number
                occupancy2_line = lines[i+2]
                occupancy1 = float(occupancy1_line.strip().split('=')[1])
                occupancy2 = float(occupancy2_line.strip().split('=')[1])
                return occupancy1, occupancy2

#Creating the csv file
with open('CCSD.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distance', 'CCSD-1', 'CCSD-2'])

    #Iteration in the mwfn files
    for i in range(1,20):
        file_path = f"{i}ccsd.out"
        distance = (i+1) * 0.2

        #Extracting occupancy values
        occupancy1, occupancy2 = extract_occupancy(file_path)

        #Write the values in the csv file
        writer.writerow([distance, occupancy1, occupancy2])
