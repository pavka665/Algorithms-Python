# Validate a subsequence
# You are given two arrays and you have to find if 
# the second one is a subsequence of the first one
# The second array have to appear in the fisrt and
# be in the same order

# We set two pointer in the main array and the subsequence
# array then we move the pointer in the main array until
# we find the pointer of the subsequence

# O(n) time | O(1) time

# Using while loop
def validateSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# Using for loop
def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
