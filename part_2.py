import input_parser
import part_1

def append_periods(string, number):

    return string + "." * number

def get_enabled_code(input):

    input = append_periods(input, 5)

def find_instruction_indexs(input, instuction_string):

    instuction_string_length = len(instuction_string)

    instruction_indexs = []

    for i in range(0, len(input) - instuction_string_length):

        if not input[i : i + instuction_string_length] == instuction_string:
            continue

        instruction_indexs.append(i)
    
    return instruction_indexs

if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_3\input.txt")

    valid_multiple_pairs = []

    total = 0

    for pair in valid_multiple_pairs:
        total += pair[0] * pair[1]

    print(total)