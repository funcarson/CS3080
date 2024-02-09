'''
PROGRAMMER: .... Carson King
USERNAME: ...... cking20
PROGRAM: ....... hw02_03.py
DESCRIPTION: Takes the output for question one and outputs only the assembly code
'''
def main():
    #Input the filename from the user
    filename = input("Enter a disassembler output file name (w/o extension): ")

    try:
        #Open the disassembler output file
        with open(filename + ".dis", "rt") as dis_file:
            #Read the contents of the file
            disassembly_code = dis_file.readlines()

        #Process each line to extract the assembly instructions
        assembly_code = ""
        for line in disassembly_code:
            # Splits the line by whitespace and get the assembly instruction part
            parts = line.split()
            if len(parts) > 1:
                assembly_code += parts[1] + "\n"  #Adds the assembly instruction to the code

        #Write the assembly code to a new file
        with open(filename + ".asm", "wt") as asm_file:
            print("ASSEMBLY CODE")
            print(assembly_code)  #Prints to console
            asm_file.write(assembly_code)

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

#runs main
if __name__ == "__main__":
    main()

