import input_parser

def extract_valid_multiple_pairs(input):
    
    potentially_valid_pairs = []
    
    for x in range(len(input)):

        if input[x : x + 4] != "mul(":
            
            continue
        
        potentially_valid_int_pair_str = seven_char_digit_pair_str_checker(input[x + 4: ])
        
        if not potentially_valid_int_pair_str:
            continue

        potentially_valid_pairs.append(potentially_valid_int_pair_str)

    potentially_valid_pairs = [x.split(",") for x in potentially_valid_pairs if len(x.split(",")) == 2]
    potentially_valid_pairs = [(x[0], x[1]) for x in potentially_valid_pairs if x[0] and x[1]]

    valid_pairs = [(int(x[0]), int(x[1])) for x in potentially_valid_pairs 
                               if len(x[0]) <= 3 and len(x[1]) <= 3] 

    return valid_pairs

def seven_char_digit_pair_str_checker(chars):

    potentially_valid_int_pair_str = ""

    last_char_index = len(chars) - 1

    if last_char_index > 8:
        last_char_index = 8 

    for x in range(last_char_index):
        
        current_char = chars[x]

        if not current_char.isdigit() and not current_char == ",":
            
            if current_char == ")":
                return potentially_valid_int_pair_str
            
            return ""
        
        potentially_valid_int_pair_str += current_char
    
    if not chars[last_char_index] == ")":
        return ""
    
    return potentially_valid_int_pair_str

if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_3\input.txt")

    valid_multiple_pairs = extract_valid_multiple_pairs(input_parser.parsed_input)

    total = 0

    for pair in valid_multiple_pairs:
        total += pair[0] * pair[1]

    print(total)