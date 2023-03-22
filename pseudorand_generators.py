import numpy as np
import random
#multiplicatove congruential method
def linear_generator(a,c,m,nums,seed):
    randomNumbers = [seed]
    for i in range(1, nums):
        randomNum = (a * randomNumbers[i-1] + c) % m
        randomNumbers.append(randomNum)
    return randomNumbers

#linear feedback shift registers
def generator_lfsr(seedBit):
    for i in range(1,15):
        print("{:04b}".format(seedBit))
        newBit = (seedBit ^ (seedBit >> 1)) & 1
        #xor'ing seedBit with seedBit,that was shifted and bitwise and'ing it with 1
        seedBit = (seedBit >> 1) | (newBit << 3)
        #creating a new seedBit by puting in place newBit
    return seedBit

#generator for <0,1> numbers
def generator_lfsr_01(seedBit):
    num = '0.'
    for i in range(1,5):
        print("{:04b}".format(seedBit))
        newBit = (seedBit ^ (seedBit >> 1)) & 1
        #xor'ing seedBit with seedBit,that was shifted and bitwise and'ing it with 1
        seedBit = (seedBit >> 1) | (newBit << 3)
        #creating a new seedBit by puting in place newBit
        num= num + str(seedBit)
        #concatenation of the seedBit values after the decimal point
    return num

#linear feedback shift registers, that replaces p and q bits
def generator_lfsr(seedBit, p, q, n):
    randomNums = []
    mask = (1 << 31) - 1
    for _ in range(n):
        for _ in range(31):
            newBitP = (seedBit >> (p - 1)) & 1
            newBitQ = (seedBit >> (q - 1)) & 1
            newBit = newBitP ^ newBitQ
            seedBit = ((seedBit << 1) | newBit) & mask
        randomNums.append(seedBit)
        seedBit = ((seedBit >> (p-1)) | (random.getrandbits(31 - p) << p)) & mask
    return randomNums



