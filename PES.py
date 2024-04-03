import os
import csv

def extract_energy(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "Total MDCI Energy" in line:
                energy = float(line.split(':')[1].strip())
                return energy

#Creating the csv file
with open('CCSD_PES.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distance', 'CCSD-energy'])

    #Iteration in the mwfn files
    for i in range(1,20):
        file_path = f"{i}ccsd_property.txt"
        distance = (i+1) * 0.2

        #Extracting energy values
        energy = extract_energy(file_path)

        #Write the values in the csv file
        writer.writerow([distance, energy])
