# Custom-assembler
## About This Project:
In this project, I created my own version of the assembly language for a 16x16 RAM CPU that I designed in Logisim Evolution. The main.py file is the assembler that translates the assembly code into hex machine code that can then be executed in the CPU.circ Logisim file.
## How to Use:
    1. Running the main.py file will output the assembly code 
    in the terminal and save it into ouput_file.txt file which 
    you can then load image to logisim (you can also copy and paste
    the hex from the terminal into ROM)
    
    2. You can change the file to assemble on line 117 of main.py:
        a. "test_files/loadstore.txt"
        b. "test_files/fibonacci.txt"
        c. "test_files/multiplier.txt"
        d. "test_files/factorial.txt"

## Expected Outputs:
    1. "test_files/loadstore.txt"
    0043 b4f0 b49c 8460 8764
            Sets register A to 67 = 0x0043
            loads that into RAM index 6 (7th register)
            Sets the B register to RAM index 6 (7th register)
            Sets the C register to the sum of A and B
            Decrements C

    2. "test_files/fibonacci.txt"
    0005 fcf0 0001 84f0 8cf0 848c 8c9c 8420 8c8c 84f0 8cb4 fcc1
            Sets the jump value to line 5 (line 6 in vscode)
            initializes A and B to 1
            Adds A and B and sets the last two values of the new fibonacci sequence to reg 0 and 1 of RAM
            repeat last step

    3. "test_files/multiplier.txt"
    0007 fcf0 0006 84d0 0007 84e0 0000 8404 8750 fc92 84f0
            Multiplies two numbers by adding repeatedly
            Stores the output in first register in RAM
            You can multiply different numbers by changing the numbers in lines 3 and 5
            Currently multiplying 6 and 7; result should be 0x002a = 42 stored in first register in RAM

    4. "test_files/factorial.txt"
    0005 8710 84e0 84b0 0007 fcf0 0000 8404 8750 fc92 8cf0 848c 8710 0002 fcf0 8c8c fc92 8c8c
            Calculates 5 factorial by multiplying 5 times 4, times 3, etc. all the way to 1
            Works up to 7! because the limit is 2^16
            You can change the factorial value by changing the first line (ex.0006 means 6 factorial)
            Stores the final value in the SECOND register of RAM
            Currently does 5 factorial; result should be 0x0078 = 120

## Assembly Code Documentation:
<img width="745" height="98" alt="Machine Code info chart" src="https://github.com/user-attachments/assets/370630e4-f2b7-405d-83dc-2a71bb155aa1" />
### General:

**Format: 1-bit control input, 4-bit RAM address, 5-bit ALU operations, 2-bit target, 2-bit operands, 2-bit jump**

<img width="408" height="392" alt="ALUops" src="https://github.com/user-attachments/assets/08343702-e9f5-47a3-84b9-1616d977d80f" />


**RAM Store Operation (ramstore)**  
    Assembly: ramstore 3 A  
    Machine Code: 0b 1 0011 10011 11 00 00  
    Effect: The contents of register A are stored in RAM location 3  

**RAM Load Operation (ramload)**  
    Assembly: ramload A 8  
    Machine Code: 0b 1 1000 10010 00 11 00  
    Effect: The contents of RAM location 8 are loaded into register A  

**Register Set Operation (regset)**  
    Note: Can only set the A register  
    Assembly: regset 27  
    Machine Code: 0b 0 0000 00000 01 10 11  
    Effect: The number 27 is stored in register A  

**Unconditional Jump (jump)**  
	    Assembly: jump  
	    Machine Code: 0b 1 0000 10011 00 0 111  
	    Effect: Jumps to whatever is set in register A  

**Jump zero(jz)**  
    Jumps if the value is not zero (used in for loops) 
    Assembly: jz B  
    Machine Code: 0b 1 1111 10010 01 00 10  
    Effect: If register B is not 0, jumps to whatever is set in register 16  

### Keywords:

<img width="488" height="624" alt="Keywords" src="https://github.com/user-attachments/assets/3728cfcf-18d6-411b-bf94-931f759166e5" />








        


