"""
SpaceX is testing flight software subroutines (i.e., programs that consist of sequences of instructions) for a custom rocket CPU. To ensure that the software runs correctly before it's loaded into the rocket, you need to create a CPU simulator.

The CPU has 43 32-bit unsigned integer registers, which are named R00..R42. At the start of the program, all the registers contain 0. The CPU supports the following instructions:

MOV Rxx,Ryy - copies the value from register Rxx to register Ryy;
MOV d,Rxx - copies the numeric constant d (specified as a decimal) to register Rxx;
ADD Rxx,Ryy - calculates (Rxx + Ryy) MOD 232 and stores the result in Rxx;
DEC Rxx - decrements Rxx by one. Decrementing 0 causes an overflow and results in 232-1;
INC Rxx - increments Rxx by one. Incrementing 232-1 causes an overflow and results in 0;
INV Rxx - performs a bitwise inversion of register Rxx;
JMP d - unconditionally jumps to instruction number d (1-based). d is guaranteed to be a valid instruction number;
JZ d - jumps to instruction d (1-based) only if R00 contains 0;
NOP - does nothing.
After the last instruction has been executed, the contents of R42 are considered to be the result of the subroutine.

Write a software emulator for this CPU that executes the subroutines and returns the resulting value from R42.

All the commands in the subroutine are guaranteed to be syntactically correct and have valid register numbers, numeric constants, and jump addresses. The maximum program length is 1024 instructions. The maximum total number of instructions that will be executed until the value is returned is 5 · 104. (Keep in mind that the same instruction will be counted as many times as it will be executed.)

Example

For

subroutine = [
  "MOV 5,R00",
  "MOV 10,R01",
  "JZ 7",
  "ADD R02,R01",
  "DEC R00",
  "JMP 3",
  "MOV R02,R42"
]
the output should be
solution(subroutine) = "50".

Here is the information about the CPU state after certain steps:

Step	Last executed
command	Non-zero registers	Comment
1	1. MOV 5,R00	R00 = 5	Put 5 into R00
2	2. MOV 10,R01	R00 = 5, R01 = 10	Put 10 into R01
3	3. JZ 7	R00 = 5, R01 = 10	Move to the next instruction
because R00 ≠ 0
4	4. ADD R02,R01	R00 = 5, R01 = 10,
R02 = 10	R02 += R01
5	5. DEC R00	R00 = 4, R01 = 10,
R02 = 10	R00 -= 1
6	6. JMP 3	R00 = 4, R01 = 10,
R02 = 10	Jump to instruction number 3,
i.e. JZ 7
7	3. JZ 7	R00 = 4, R01 = 10,
RO2 = 10	Move to the next instruction
because R00 ≠ 0
Information about 11 steps is skipped
19	3. JZ 7	R00 = 1, R01 = 10,
RO2 = 40	Move to the next instruction
because R00 ≠ 0
20	4. ADD R02,R01	R00 = 1, R01 = 10,
R02 = 50	R02 += R01
21	5. DEC R00	R00 = 0, R01 = 10,
R02 = 50	R00 -= 1
22	6. JMP 3	R00 = 0, R01 = 10,
R02 = 50	Jump to instruction number 3,
i.e. JZ 7
23	3. JZ 7	R00 = 0, R01 = 10,
R02 = 50	Jump to instruction number 7
because R00 = 0
24	7. MOV R02,R42	R00 = 0, R01 = 10,
R02 = 50, R42 = 50	R42 += R02
The subroutine is exited
Input/Output

[execution time limit] 0.5 seconds (cpp)

[memory limit] 1 GB

[input] array.string subroutine

Guaranteed constraints:
1 ≤ subroutine.length ≤ 1024.

[output] string

Return the resulting 32-bit unsigned integer, converted into a string.


Solution: Cainan Black
"""

auto split_string(const string& input, const char delimiter) 
{
    stringstream ss {input.data()};
    vector<string> result;
    
    for (string buffer; 
         getline(ss, buffer, delimiter);) 
            {result.push_back(move(buffer));}
    
    return result;
}

string solution(vector<string> subroutine) {
    vector<unsigned> REG (43, 0);
    
    for (int i=0; i<subroutine.size(); ++i) {
        auto inst = subroutine[i];
        auto s = split_string(inst, ' ');
        
        if (s[0] == "NOP") {continue;}
        else if (s[0] == "JMP") {
            i = stol(s[1]) - 2;
        }
        else if (s[0] == "JZ") {
            if (REG[0] == 0) {
                i = stol(s[1]) - 2;
            }
        }
        else if (s[0] == "INV") {
            int num = stoul(string(begin(s[1])+1, end(s[1])));
            REG[num] = ~ REG[num];
        }
        else if (s[0] == "INC") {
            int num = stoul(string(begin(s[1])+1, end(s[1])));
            if (REG[num] == 4294967295) {
                REG[num] = 0;
            }
            else {
                ++REG[num];
            }
        }
        else if (s[0] == "DEC") {
            int num = stoul(string(begin(s[1])+1, end(s[1])));
            if (REG[num] == 0) {
                REG[num] = 4294967295;
            }
            else {
                --REG[num];
            }
        }
        else if (s[0] == "ADD") {
            auto c = split_string(s[1], ',');
            auto n1 = stoul(string(begin(c[0])+1, end(c[0])));
            auto n2 = stoul(string(begin(c[1])+1, end(c[1])));

            REG[n1] = ((REG[n1] % 4294967296) + (REG[n2] % 4294967296)) % 4294967296;
        }
        else if (s[0] == "MOV") {
            auto c = split_string(s[1], ',');
            
            if (c[0][0] == 'R') {
                auto n1 = stoul(string(begin(c[0])+1, end(c[0])));
                auto n2 = stoul(string(begin(c[1])+1, end(c[1])));
                
                REG[n2] = REG[n1];
            }
            else {
                auto n1 = stoul(c[0]);
                auto n2 = stoul(string(begin(c[1])+1, end(c[1])));
                
                REG[n2] = n1;
            }
        }
    }
    return to_string(REG[42]);
}
