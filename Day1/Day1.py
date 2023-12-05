import pandas as pd

file = open("../input/day1/input.txt", "r")
content = file.read()

split_lines = content.splitlines()

#Part 1
answer = 0
for s in split_lines:

    left, right = 0, len(s) - 1

    # move left
    while not s[left].isnumeric():
        left+=1
    
    while not s[right].isnumeric():
        right-=1
    
    answer+=int(s[left]) * 10
    answer+=int(s[right])

        
############
# Part 2

number_map = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9} 
    
answer = 0
for s in split_lines:
    left_digit = 0
    right_digit = 0

    left, right = 0, len(s) - 1

    # determine left
    while left <= right:
        if s[left].isnumeric():
            left_digit = s[left]
            break
        else:
            if s[left] in ['o', 't', 'f', 's', 'e', 'n']:
                for number in number_map.keys():
                    curr_num = ""
                    if len(s[left:]) >= len(number) and s[left:left+(len(number))] == number:
                        left_digit = number_map[s[left:left+(len(number))]]
                        break
                if left_digit != 0: break
                left+=1
            else:
                if left_digit != 0: break
                left+=1
        if left_digit != 0: break

    # determine right
    while right >= 0:
        # print(right)
        if s[right].isnumeric():
            right_digit = s[right]
            break
        else:
            if s[right] in ['o', 't', 'r', 'x', 'e', 'n']:
                for number in number_map.keys():
                    print(number)
                    print(s[right - len(number):right+1] )
                    if len(s[0:right]) >= len(number) and s[right+1 - len(number):right+1] == number:
                        right_digit = number_map[s[right+1 - len(number):right+1]]
                        break
                if right_digit != 0: break
                right-=1
            else:
                if right_digit != 0: break
                right-=1
        if right_digit != 0: break 
    print(right_digit)
    
    
    
    # # move right
    # while not s[right].isnumeric():
    #     right-=1
    
    answer+=int(left_digit) * 10
    answer+=int(right_digit)
        
