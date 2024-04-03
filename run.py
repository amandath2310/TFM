import subprocess

#Run each input file generated using orca
for i in range(1,20):
    input_file = f"{i}ccsd.inp"
    output_file = f"{i}ccsd.out"
    command = f"orca {input_file} > {output_file}"
    subprocess.run(command,shell=True)
