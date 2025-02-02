import input_parser
from part_1 import extract_valid_multiple_pairs
from part_1 import seven_char_digit_pair_str_checker
import operator

def get_enabled_code(input):

    input = "do()" + input

    do_indexs = [(x, "do()")for x in find_instruction_indexs(input, "do()")]
 
    dont_indexs = [(x, "don't()")for x in find_instruction_indexs(input, "don't()")]

    sorted_instruction_indexs = sorted(do_indexs + dont_indexs, key= operator.itemgetter(0))

    sorted_instruction_indexs = remove_consecutive_duplicate_commands(sorted_instruction_indexs)

    enabled_input = slice_together_enabled_code_using_instruction_indexs(input, sorted_instruction_indexs)

    return enabled_input

def find_instruction_indexs(input, instuction_string):

    instuction_string_length = len(instuction_string)

    instruction_indexs = []

    for i in range(0, len(input) - instuction_string_length):

        if not input[i : i + instuction_string_length] == instuction_string:
            continue

        instruction_indexs.append(i)

    return instruction_indexs

def remove_consecutive_duplicate_commands(sorted_instruction_indexs):

    i = 0

    last_instruction_index = len(sorted_instruction_indexs) - 1

    while i < last_instruction_index:

        if not sorted_instruction_indexs[i][1] == sorted_instruction_indexs[i + 1][1]:
            i += 1
            continue

        sorted_instruction_indexs.pop(i + 1)

        last_instruction_index -= 1
    
    return sorted_instruction_indexs

def slice_together_enabled_code_using_instruction_indexs(input, sorted_instruction_indexs):
 
    enabled_input = ""

    for i in range(0, len(sorted_instruction_indexs) - 1, 2):
        
        enabled_input += input[sorted_instruction_indexs[i][0]: sorted_instruction_indexs[i + 1][0]] 

    if sorted_instruction_indexs[-1][1] == "do()":
        enabled_input += input[sorted_instruction_indexs[-1][0]: ]

    return enabled_input

if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_3\input.txt")

    enabled_input = get_enabled_code(input_parser.parsed_input)
    
    valid_multiple_pairs = []

    valid_multiple_pairs =extract_valid_multiple_pairs(enabled_input)

    total = 0

    for pair in valid_multiple_pairs:
        total += pair[0] * pair[1]

    print(total)