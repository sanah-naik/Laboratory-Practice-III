import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency_map = defaultdict(int)
    
    for char in data:
        frequency_map[char] += 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(root):
    codes = {}
    def generate_codes(node, current_code=""):
        if node.char is not None:
            codes[node.char] = current_code
        if node.left is not None:
            generate_codes(node.left, current_code + "0")
        if node.right is not None:
            generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return codes

def huffman_encoding(data):
    if not data:
        return "", None

    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    encoded_data = "".join([codes[char] for char in data])

    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return ""

    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

if __name__ == "__main__":
    user_input = input("Enter a string to encode: ")
    
    encoded_data, huffman_tree = huffman_encoding(user_input)
    print(f"Encoded data: {encoded_data}")
    
    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f"Decoded data: {decoded_data}")
