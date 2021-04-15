import re, sys
from bitstring import BitArray, BitStream
#from collections import Counter
#print(sys.path)

#Custom Compression is a original compression algorithm that borrows heavily from Huffman encoding
#The interfacing with the compression module most likely should be improved, as it makes more sense to accept any generic file and not read it immediately
        
class Custom_Compression(object):
    def __init__(self, file):
        self.path = file
        self.file = open(file, "rb")
        self.efile = open(file, "r")
        #self.code = code

    #get encoded file
    def get_efile(self):
        return self.efile.read()

    #get binary file
    def get_file(self):
        return self.file.read()

    #print encoded file
    def epeek(self):
        print(self.efile.read())
    
    #print binary file
    def peek(self):
        print(self.file.read())

    #get the binary code of the message/file
    def get_bytecode(self):
        bytes = BitArray(self.file.read())
        return bytes.bin

    #return just the unique symbols and count
    def get_unique(self):
        uni = {}
        for keys in self.efile.read():
            uni[keys] = uni.get(keys, 0) + 1
        return uni

    def increment_bin(self, num):
        #return '{:05b}'.format(1 + int(num, 2))
        return str(bin(int(num) + 1))[2:]

    def get_assignment(self):
        #there is most likely a much better way to implement this production of Huffman-style codes
        #pulls unique characters and their count into a dictionary, uses list to sort, and pushes back into a dictionary
        array = []
        uni = {}
        code = 0
        final = {}
        for keys in self.efile.read():
            uni[keys] = uni.get(keys, 0) + 1
        #print(uni)
        #array = sorted(array, key= lambda tup: tup[1], reverse=True)
        for i in uni:
            array.append((i, uni[i]))

        array = sorted(array, key= lambda tup: tup[1], reverse=True)
        #print(array)
        for j in range(len(array)):
            #array[j] = (array[j][0], array[j][1], str(bin(code))[2:])
            array[j] = (array[j][0], str(bin(code))[2:])
            code = code + 1
        array = sorted(array, key= lambda tup: tup[1], reverse=True)
        #self.efile.close()
        final = dict(array)
        return final

    def encode(self):
        print("encoding...")
        text = ""
        lookup = self.get_assignment()
        encode_file = open(self.path, "r")
        for line in encode_file:
            for char in line:
                text = text + lookup[char]
                #print(char)
                #print(lookup[char])
            #char = open(self.path, "r").read(1)
            #text = text + encode_code[2]
        return text

    def decode(self):
        #traditional huffman decoding seems to require the original tree that was used to encode the message
        #under development
        print("decoding...")


    

#driver code
def testBit():
    #test = Shannon_Fano(r'C:/Users/Richard\Documents/VS Code/compression/middle-out/test.txt')
    #test.peek()
    #test_bits = BitArray('0b001')
    #test_bits_2 = BitArray('0b010')
    test = Custom_Compression(r'C:/Users/Richard/Documents/VS Code/compression/middle-out/test.txt')
    print(test.get_bytecode())
    print(test.encode())

testBit()
