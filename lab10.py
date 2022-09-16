# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Amena Akbary
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r11 r1 r2 
03 sub r12 r2 r1
04 jltzn r11 06
05 jltzn r12 07
06 write r2
07 write r1
08 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """ 
00 read r1
01 read r2
02 setn r3 01
03 jeqzn r2 08
04 setn r3 01 
05 mul r3 r3 r1
06 addn r2 -1
07 jgtzn r2 05
08 write r3
09 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 jeqzn r1 08
02 setn r13 00
03 setn r14 01	
04 addn r1 -1	
05 add r4 r13 r14
06 copy r13 r14
07 copy r14 r4
08 addn r1 -1
09 jnezn r1 05
10 write r4
11 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Max  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


    