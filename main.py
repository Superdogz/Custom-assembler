def convert(i):
    binary = []
    i = i.split(" ")
    print(i)
    if i[0] == "setreg":
        binary.append(format(int(i[1]), '016b'))

    elif i[0] == "ramstore":
        binary.append("1")
        binary.append(format(int(i[1]), '04b'))
        if i[2] == "A":
            binary.append("10011110000")
        elif i[2] == "B":
            binary.append("10010110000")
        elif i[2] == "C":
            binary.append("10010110100")

    elif i[0] == "ramload":
        binary.append("1")
        binary.append(format(int(i[2]), '04b'))
        if i[1] == "A":
            binary.append("10010001100")
        elif i[1] == "B":
            binary.append("10010011100")
        elif i[1] == "C":
            binary.append("10010101100")

    elif i[0] == "jump":
        binary.append("1111110011000001")

    elif i[0] == "jz":
        if i[1] == "A":
            binary.append("1111110011000010")
        elif i[1] == "B":
            binary.append("1111110010010010")
        elif i[1] == "C":
            binary.append("1111110010100110")

    elif i[0] == "A=B":
        binary.append("1000010010000000")
    elif i[0] == "A=C":
        binary.append("1000010010000100")
    elif i[0] == "B=A":
        binary.append("1000010011010000")
    elif i[0] == "B=C":
        binary.append("1000010010010100")
    elif i[0] == "C=A":
        binary.append("1000010011100000")
    elif i[0] == "C=B":
        binary.append("1000010010100000")
    elif i[0] == "A=A":
        binary.append("1000010011000000")


    elif i[0] == "and" or i[0] == "or" or i[0] == "xor" or i[0] == "add" or i[0] == "sub":
        if i[0] == "and":
            binary.append("10000000")
        elif i[0] == "or":
            binary.append("10000001")
        elif i[0] == "xor":
            binary.append("10000010")
        elif i[0] == "add":
            binary.append("10000100")
        elif i[0] == "sub":
            binary.append("10000101")
        if (i[2] == "A" and i[3] == "B") or (i[2] == "A" and i[3] == "C") or (i[2] == "B" and i[3] == "C"):
            binary.append("00")
        else:
            binary.append("01")
        if i[1] == "A":
            binary.append("00")
        elif i[1] == "B":
            binary.append("01")
        elif i[1] == "C":
            binary.append("10")
        if (i[2] == "A" and i[3] == "B") or (i[2] == "B" and i[3] == "A"):
            binary.append("00")
        elif (i[2] == "A" and i[3] == "C") or (i[2] == "C" and i[3] == "A"):
            binary.append("01")
        elif (i[2] == "B" and i[3] == "C") or (i[2] == "C" and i[3] == "B"):
            binary.append("10")
        binary.append("00")

    elif i[0] == "inv" or i[0] == "inc" or i[0] == "dec":
        if i[0] == "inv":
            binary.append("10000011")
        elif i[0] == "inc":
            binary.append("100000110")
        elif i[0] == "dec":
            binary.append("10000111")
        if i[2] == "A":
            binary.append("00")
        elif i[2] == "B":
            binary.append("01")
        elif i[2] == "C":
            binary.append("01")
        if i[1] == "A":
            binary.append("00")
        elif i[1] == "B":
            binary.append("01")
        elif i[1] == "C":
            binary.append("10")
        if i[2] == "A":
            binary.append("00")
        elif i[2] == "B":
            binary.append("00")
        elif i[2] == "C":
            binary.append("01")
        binary.append("00")
    
    binary = int("".join(binary), 2)
    print(binary)
    return(binary)



f = open("test_files/factorial.txt") #change the file you want to assemble here




instruction = f.read()
instruction = instruction.splitlines()
list = []
for inst in instruction:
    list.append(hex(convert(inst))[2:].zfill(4))

content = " ".join(list)
print("\n")
print(content)
filename = "ouput_file.txt"
content_to_write = "v2.0 raw\n"+content

with open(filename, 'w') as file_object:
    file_object.write(content_to_write)