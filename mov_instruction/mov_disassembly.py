"""
REG W=0 W=1
000 AL AX
001 CL CX
010 DL DX
011 BL BX
100 AH SP
101 CH BP
110 DH SI
111 BH DI
"""

register_dict = {
    '000': {"word": "ax", "byte": "al"},
    '001': {"word": "cx", "byte": "cl"},
    '010': {"word": "dx", "byte": "dl"},
    '011': {"word": "bx", "byte": "bl"},
    '100': {"word": "sp", "byte": "ah"},
    '101': {"word": "bp", "byte": "ch"},
    '110': {"word": "si", "byte": "dh"},
    '111': {"word": "di", "byte": "bh"}
}


def mov(second_byte: int, is_word: bool) -> None:
    """
    This function takes a second_byte as input and a flag is_word and prints the assembly instruction for moving data.

    Args:
        second_byte: The second byte of the instruction.
        is_word: A flag indicating whether the operation is a word or byte move.
    """
    source = bin(second_byte)[4:7]  # Extract bits 3 to 6 for source register
    destination = bin(second_byte)[-3:]  # Extract bits 0 to 2 for destination register
    register_name = register_dict[destination][f"word" if is_word else "byte"]
    print(f"mov {register_name}, {register_dict[source][f'word' if is_word else 'byte']}")


operators = {0b10001000: mov}


def decode_asm():
    """
    Reads the binary file and decodes each instruction.
    """
    mask = 0b11111100  # first 6 bits from the left for the operator encoding
    file = open("many_register_mov.txt", "rb")
    while True:
        while byte := file.read(2):
            is_words = bool(byte[0] & 0b00000001)
            operator = byte[0] & mask
            print("bin op", bin(operator), "is words", is_words)
            if operator in operators:
                operators[operator](byte[1], is_words)


def main():
    decode_asm()


if __name__ == "__main__":
    main()
