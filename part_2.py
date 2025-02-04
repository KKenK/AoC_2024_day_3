import input_parser
from part_1 import extract_valid_multiple_pairs
from part_1 import seven_char_digit_pair_str_checker
import operator

def get_enabled_code(input):

    input = "do()" + input

    do_indexes = [(x, "do()")for x in find_instruction_indexes(input, "do()")]
 
    dont_indexes = [(x, "don't()")for x in find_instruction_indexes(input, "don't()")]

    sorted_instruction_indexes = sorted(do_indexes + dont_indexes, key= operator.itemgetter(0))

    sorted_instruction_indexes = remove_consecutive_duplicate_commands(sorted_instruction_indexes)

    enabled_input = slice_together_enabled_code_using_instruction_indexes(input, sorted_instruction_indexes)

    return enabled_input

def find_instruction_indexes(input, instruction_string):

    instruction_string_length = len(instruction_string)

    instruction_indexes = []

    for i in range(0, len(input) - instruction_string_length):

        if not input[i : i + instruction_string_length] == instruction_string:
            continue

        instruction_indexes.append(i)

    return instruction_indexes

def remove_consecutive_duplicate_commands(sorted_instruction_indexes):

    i = 0

    last_instruction_index = len(sorted_instruction_indexes) - 1

    while i < last_instruction_index:

        if not sorted_instruction_indexes[i][1] == sorted_instruction_indexes[i + 1][1]:
            i += 1
            continue

        sorted_instruction_indexes.pop(i + 1)

        last_instruction_index -= 1
    
    return sorted_instruction_indexes

def slice_together_enabled_code_using_instruction_indexes(input, sorted_instruction_indexes):
 
    enabled_input = ""

    for i in range(0, len(sorted_instruction_indexes) - 1, 2):
        
        enabled_input += input[sorted_instruction_indexes[i][0]: sorted_instruction_indexes[i + 1][0]] 

    if sorted_instruction_indexes[-1][1] == "do()":
        enabled_input += input[sorted_instruction_indexes[-1][0]: ]

    return enabled_input

if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_3\input.txt")

    enabled_input = get_enabled_code(input_parser.parsed_input)

    valid_multiple_pairs = []

    valid_multiple_pairs = extract_valid_multiple_pairs(enabled_input)

    total = 0

    for pair in valid_multiple_pairs:
        total += pair[0] * pair[1]

    print(total)