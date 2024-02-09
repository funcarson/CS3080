'''
PROGRAMMER: .... Carson King
USERNAME: ...... cking20
PROGRAM: ....... hw02_01.py
DESCRIPTION: Dissassemble the assembly code given in the hackman file and output it to the console and another file
(for future problems).
'''
def disassemble_hack_code(filename):
    #Open the file
    with open(filename + ".hack", "r") as file:
        lines = file.readlines()

    #Dictionary for C-type instruction computation
    comp_dict = {
        "0101010": "0",
        "0111111": "1",
        "0111010": "-1",
        "0001100": "D",
        "0110000": "A",
        "0001101": "!D",
        "0110001": "!A",
        "0001111": "-D",
        "0110011": "-A",
        "0011111": "D+1",
        "0110111": "A+1",
        "0001110": "D-1",
        "0110010": "A-1",
        "0000010": "D+A",
        "0010011": "D-A",
        "0000111": "A-D",
        "1000000": "D&A",
        "0010101": "D|A",
        "1110000": "M",
        "1110001": "!M",
        "1110011": "-M",
        "1110111": "M+1",
        "1110010": "M-1",
        "1000010": "D+M",
        "1000111": "D-M",
        "1000001": "M-D",
        "1000011": "D&M",
        "1000110": "D|M"
    }

    #Dictionary for jump instruction mapping
    jump_dict = {
        "000": "",
        "001": "JGT",
        "010": "JEQ",
        "011": "JGE",
        "100": "JLT",
        "101": "JNE",
        "110": "JLE",
        "111": "JMP"
    }

    #List to store disassembled lines
    disassembled_lines = []

    #Iterate through lines and disassemble
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line.startswith('0'):
            #A-type instruction
            disassembled_lines.append(line + " @" + str(int(line[1:], 2)) + "\n")
        elif line.startswith('111'):
            #C-type instruction
            comp = comp_dict.get(line[3:10], "ERROR")
            dest = ''.join('AMD'[int(bit)] for bit in line[10:13])
            jump = jump_dict.get(line[13:], "")
            disassembled_lines.append(line + " " + comp + "=" + dest + ";" + jump + "\n")

    #Print the disassembled code
    for line in disassembled_lines:
        print(line, end="")

    #Write the disassembled code to a file
    with open(filename + ".dis", "w") as output_file:
        output_file.writelines(disassembled_lines)


#Prompt user for the filename
filename = input("Enter the name of a .hack file (without extension): ")
# Call the function to disassemble the code
disassemble_hack_code(filename)
