import os
import csv

def extract_occupancy(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if "Natural Orbital Occupation Numbers:" in line:
                occupancies = []
                for j in range(28):
                    occupancy_line = next(f).strip().split('=')[1]
                    occupancies.append(float(occupancy_line))
                return occupancies

#Creating the csv file
with open('all_CCSD.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distance'] + [f'Occ{i+1}' for i in range(28)])

    #Iteration in the mwfn files
    for i in range(1,20):
        file_path = f"{i}ccsd.out"
        distance = (i+1) * 0.2

        #Extracting occupancy values
        occupancies = extract_occupancy(file_path)

        #Write the values in the csv file
        writer.writerow([distance] + occupancies)
