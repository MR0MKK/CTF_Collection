def calculate_length(string):
    return len(string)

def print_string(string):
    print(string)

def is_digit(string):
    return string.isdigit()

def process_eating(eat):
    return str(int(eat) * calculate_length(eat))

def process_eat(eat, eats):
    index1 = 0
    index2 = 0
    combined_index = 0
    result = ""
    while index1 < calculate_length(eat) and index2 < calculate_length(eats):
        if combined_index % EATEATEAT == EATEATEATEATEAT // EATEATEATEAT:
            result += eats[index2]
            index2 += 1
        else:
            result += eat[index1]
            index1 += 1
        combined_index += 1
    return result

def reverse_string(string):
    return string[::EATEATEAT - EATEATEATEAT]

def process_eaT(eat):
    return process_eating(eat[:EATEATEAT]) + reverse_string(eat)

def process_aTE(eat):
    return eat

def process_Ate(eat):
    return "Eat" + str(calculate_length(eat)) + eat[:EATEATEAT]

def process_Eat(eat):
    if calculate_length(eat) == 9:
        if is_digit(eat[:EATEATEAT]) and is_digit(eat[calculate_length(eat) - EATEATEAT + 1:]):
            combined_string = process_eat(process_eaT(eat), process_Ate(process_aTE(reverse_string(eat))))
            if combined_string == "E10a23t9090t9ae0140":
                flag = "eaten_" + eat
                print_string("absolutely EATEN!!! CTFlearn{" + flag + "}")
EATEATEAT = 3
EATEATEATEAT = EATEATEAT + 1
EATEATEATEATEAT = EATEATEAT - 1
for num in range(100000, 999999 + 1):
    num_str = str(num)
    num1 = num_str[:3]
    num2 = num_str[3:]
    process_Eat(num1 + "eat" + num2)
