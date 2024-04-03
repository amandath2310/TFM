def generate_input_file(file_name, offset):
    with open(file_name, 'w') as f:
        f.write("! CCSD cc-pVDZ VeryTightSCF AIM\n")
        f.write("\n%maxcore 2000\n")
        f.write("\n%mdci\n")
        f.write(" citype CCSD\n")
        f.write(" Denmat orbopt\n")
        f.write(" doNatOrbs true\n")
        f.write("end\n")
        f.write("\n*xyz 0 1\n")
        f.write("H 0.0 0.0 0.0\n")
        f.write(f"H {offset} 0.0 0.0\n")
        f.write("*\n")

#Generating 19 input files
for i in range(1,20):
    offset = (i+1) * 0.2
    file_name = f"{i}ccsd.inp"
    generate_input_file(file_name, offset)
