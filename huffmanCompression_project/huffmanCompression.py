import heapq
import os
class BinaryTree:
    def __init__(self,value,frequ):
        self.value = value
        self.frequ = frequ
        self.left = None
        self.right = None
    def __lt__(self,other):
        return self.frequ < other.frequ
    def __eq__(self,other):
        return self.frequ == other.frequ        
class Huffmancode:
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__code = {}
        self.__reversecode = {}
        
    def __frequency_from_text(self,text):
        frequ_dict = {}
        for char in text:
            if char not in frequ_dict:
                frequ_dict[char] = 0
            frequ_dict[char] +=1
        return frequ_dict    
    
    def __Build_heap(self,frequency_dict):
        for key in frequency_dict:
            frequency = frequency_dict[key]
            binary_tree_node = BinaryTree(key,frequency)
            heapq.heappush(self.__heap , binary_tree_node)
    
    def __Build_Binary_Tree(self):
        while len(self.__heap) > 1:
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            sum_of_freq = binary_tree_node_1.frequ + binary_tree_node_2.frequ
            newnode = BinaryTree(None,sum_of_freq)
            newnode.left = binary_tree_node_1
            newnode.right = binary_tree_node_2
            heapq.heappush(self.__heap,newnode)
        return
    def __Build_Tree_Code_Helper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.__code[root.value] = curr_bits
            self.__reversecode[curr_bits] = root.value
            return
        self.__Build_Tree_Code_Helper(root.left,curr_bits+'0')
        self.__Build_Tree_Code_Helper(root.right,curr_bits+'1')
    
    def __Build_Tree_Code(self):
        root = heapq.heappop(self.__heap)
        self.__Build_Tree_Code_Helper(root,'')
        

    def __Build_Encoded_Text(self,text):
        encoded_text = ''
        for char in text:
            encoded_text += self.__code[char]
        return encoded_text  
    
    def __Build_Padded_Text(self,encoded_text):
        padding_value = 8 - (len(encoded_text) % 8)
        for i in range(padding_value):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padding_value)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text
    
    def __Build_Byte_Array(self, padded_text):
        array = []
        for i in range(0,len(padded_text) , 8):     # incremeting i by 8 every step
            byte = padded_text[i:i+8]
            array.append(int(byte,2))
        return array    
    
    def compression(self):

        print("compression of file starts")
        #To access the file and extract text from that file.
        filename,file_extension = os.path.splitext(self.path)           #filename.ext splits into filename and exten
        output_path = filename + '.bin'
        with open (self.path,'r+') as file , open(output_path,'wb') as output:    # open current file in read mode and open output as write in binary
            text = file.read()
            text = text.rstrip()  # removes extra space

            frequency_dict = self.__frequency_from_text(text)
            #calculate freq of each char and store it in freq dict
            
            #construct min heap to find two min freq
            build_heap = self.__Build_heap(frequency_dict)
            #construct BT from heap
            self.__Build_Binary_Tree()
            #construct code from BT and store it in dict
            self.__Build_Tree_Code()
            #construct the encoded text
            encoded_text = self.__Build_Encoded_Text(text)
            #padding of encoded text
            padded_text = self.__Build_Padded_Text(encoded_text)
            #return Binary file as output
            bytes_array = self.__Build_Byte_Array(padded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
        print('compressed successfully')
        return output_path
    
    def __Remove_Padding(self,text):
        padded_info = text[:8]
        padding_value = int(padded_info,2)
        text = text[8:]
        padding_removed_text = text[:-1*padding_value]
        return padding_removed_text



    def __decoded_text(self,text):
        decoded_text = ''
        current_bits = ''
        for bit in text:
            current_bits += bit
            if current_bits in self.__reversecode:
                decoded_text +=  self.__reversecode[current_bits]
                current_bits=''
        return decoded_text   
                
         
    def decompress(self,input_path):
        filename,file_extension = os.path.splitext(input_path)
        output_path = filename + '_decompressed' + '.txt'
        with open(input_path,'rb') as file , open(output_path,'w') as output:
            bit_string = ''
            byte = file.read(1)       #read byte one by one 
            while byte:
                byte = ord(byte)       # Convert the byte (character) to its integer representation
                bits = bin(byte)[2:].rjust(8,'0')      #  int to binary from 2  because here we obtain eg: 0b10001 so we need to start from 0 ,  rjust ensure binary string length of 8, if needed pad with 0 eg banana is 6 letter so 00banana
                bit_string += bits
                byte = file.read(1)            # Read the next byte (character) from the file
            text_after_removing_data = self.__Remove_Padding(bit_string)
            actual_text = self.__decoded_text(text_after_removing_data)
            output.write(actual_text)
        return    
            
path = input("ENTER PATH OF FILE")
h = Huffmancode(path)
compressed_file=h.compression()
h.decompress(compressed_file)