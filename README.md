# Huffman-coding
## Overview
This Python project implements a text file compression utility that utilizes the Huffman coding algorithm to achieve a compression rate of approximately 53%. With this tool, you can convert plain text files (.txt) into compressed binary files (.bin).

## How it works
### Huffman Coding algorithm
Huffman coding is a variable-length prefix coding algorithm used for data compression. It works by assigning shorter codes to more frequent characters and longer codes to less frequent characters. Here's how the algorithm works:

  *Frequency Analysis:* The input text file is analyzed to determine the frequency of each character (or symbol). This step involves counting the occurrences of each character in the text.
  
  *Create Huffman Tree:* A binary tree called the Huffman tree is constructed based on the character frequencies. This tree is built bottom-up, starting with individual characters as leaves and combining them into nodes with a cumulative frequency.
  
  *Assign Codes:* Traverse the Huffman tree to assign binary codes to each character. Left branches typically represent '0', and right branches represent '1'. The codes are unique and allow for efficient decoding.
  
  *Encode Text:* Encode the entire text using the Huffman codes assigned to each character. Replace each character in the text with its corresponding Huffman code.
  
  *Compression:* The encoded text is then written to the binary file (.bin), which results in a compressed representation of the original text.
  
  *Decompression:* To decompress the binary file, the same Huffman tree used for encoding is required. The tree structure is stored in the compressed file or separately as needed.

## Usage
To test this project, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download this project repository.
3. Open a terminal/command prompt and navigate to the project directory.
4. Run the file titled "huffman.py"
5. Enter the name of the file you want to compress in the terminal "sample.txt"
6. The compressed binary and corresponding decompressed text file will be generated in the same directory as the script.

## Notes
This project provides a basic implementation of Huffman coding for educational purposes. For production use, you may want to consider more advanced error handling and optimizations
