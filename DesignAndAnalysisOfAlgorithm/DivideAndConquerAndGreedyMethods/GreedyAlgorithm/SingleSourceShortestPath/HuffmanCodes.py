import heapq
from collections import Counter, namedtuple

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_counter = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = Node(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(root):
    Code = namedtuple('Code', ['char', 'code'])
    codes = []

    def traverse(node, code):
        if node:
            if node.char:
                codes.append(Code(node.char, code))
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes

def encode_message(text, codes):
    encoding_dict = {code.char: code.code for code in codes}
    encoded_text = ''.join(encoding_dict[char] for char in text)
    return encoded_text

def decode_message(encoded_text, root):
    decoded_text = ''
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

if __name__ == "__main__":
    message = "hello world"
    huffman_tree = build_huffman_tree(message)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_message = encode_message(message, huffman_codes)
    decoded_message = decode_message(encoded_message, huffman_tree)

    print("Original Message:", message)
    print("Encoded Message:", encoded_message)
    print("Decoded Message:", decoded_message)
