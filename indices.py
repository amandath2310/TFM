import pandas as pd
import numpy as np
import csv

#Open the files with the NOOs
file_path = 'all_CCSD.csv' # Change the route in each case
df_NOO = pd.read_csv(file_path)

Ind_value = []
Id_value = []
It_value = []

#write the number of electrons
nelec = 2

#For CASSCF
for i in range(len(df_NOO)):
    # Selecting the NOOs
    NOO_val = df_NOO.iloc[i,1:].values
    # Calculation of the correlation indices
    Ind = (1/(nelec*2)) * (np.sum(NOO_val * (2 - NOO_val)))
    Id = ((1/4)* np.sum((NOO_val * (2 - NOO_val))**(1/2))) - Ind
    It = Ind + Id
    # Appending the calculated values
    It_value.append(It)
    Id_value.append(Id)
    Ind_value.append(Ind)
  
# Escribir los resultados en un nuevo archivo CSV
with open('Indices_CCSD.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distance', 'Ind', 'Id', 'It'])
    
    for i in range(len(df_NOO)):
        distance = round((i+2) * 0.2, 2)
        writer.writerow([distance, Ind_value[i], Id_value[i], It_value[i]])
