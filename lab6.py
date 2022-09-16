####################################################################################
# Name: Amena Akbary
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#
# Note: Using anything other than recursion will result in a penalty
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

def LLCS(S1, S2):
    if S1 == '':
        return 0
    elif S2 == '':
        return 0
    elif S1[0]==S2[0]:
        return 1 + LLCS(S1[1:],S2[1:])
    a = LLCS(S1[1:],S2)
    b = LLCS(S1,S2[1:])
    if a>b:
        return a
    else: return b

print(LLCS("helllowo_rld","!helloabcworld!"))

'''
Return the length of the longest common subsequence (LLCS) of strings S1 and S2
'''

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    if S1 == '':
        return ''
    elif S2 == '':
        return ''
    elif S1[0]==S2[0]:
        return (S1[0] + LCS(S1[1:],S2[1:]))
    a = LCS(S1[1:],S2)
    b = LCS(S1,S2[1:])
    if len(a)>len(b):
        return a
    else: return b

print(LCS('hello','hello'))
print(LCS("helllowo_rld","!helloabcworld!"))
    
'''return the longest common subsequence (LCS) between strings S1 and S2'''