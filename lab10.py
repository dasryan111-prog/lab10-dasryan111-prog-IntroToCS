# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    '''
    Go through every index of tokens and check if the index is a number. If it isn't, check
    if the holder (stack) doesn't have 2 or more elements in it, which if it doesn't, add the
    current token to the list. Otherwise pull out the two most recent indices from the holder,
    and determine what kind of operator it is. Apply the operator to the indices from the
    holder. Then append the result to the holder. If the token is a number, add it to the
    holder. Return the first index of the holder.
    '''

    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    holder = []
    operators = {'*', '/', '+', '-'}
    for token in tokens:
        if token in operators:
            if len(holder) >= 2:
                right = holder.pop()
                left = holder.pop()

                if token == "+":
                    result = left + right

                elif token == "-":
                    result = left - right

                elif token == "*":
                    result = left * right

                elif token == "/":
                    result = int(left / right)

                holder.append(result)

            else:
                holder.append(token)

        else:
            holder.append(int(token))

    return holder[0]


def decode_string(s):
    # Outline:
    #   ...
    '''
    1. Make three variables - One a stack, another current_str, which will store the string, 
    and the current_num, which will store the current number.
    2. Check through every element of the string. If the character is a number, multiply 
    current_num by 10 (incase of multiple digit numbers) and add the char to current_num.
    3. If it is [, store the current_str and current_num to the stack, and reset them
    4. If it is ], pull out the stored values from the stack, and set current_str to the
    previous string added to the current string multiplied by the number from the stack.
    5. If it is none of the above, add the character to the current_str
    6. Return current_str
    '''
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    
    stack = []
    current_str = "" # Stores the characters at the current nest level
    current_num = 0

    for char in s:
        if char.isnumeric():
            # Multiplies by 10 in case of multi digit numbers
            current_num = current_num * 10 + int(char)
        elif char == "[":
            # Appends to the stack and resets the current values incase of a nested version
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == "]":
            # Takes the values from the stack and combines it with the nested values
            prev_str, repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            current_str += char

    return current_str

def daily_temperatures(temps):
    # Outline:
    #   ...
    '''
    1. Make two empty lists - One stored with zeros based on the size of temps, the other
    an empty list (a stack).
    2. Loop through the temps and while the stack is not empty and the current temperature
    is greater than that of the last in the stack, pull out the most recent value from the
    stack, and using that value, set that index of the answer list (initially stored
    with 0s) to the outer loop's index subtract the index from the stack.
    3. Outside the while loop, add the index i to the stack.
    4. Return the list answer
    '''

    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]

    answer = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)

    return answer



''' Non-stack method
    holder = []
    for i in range(len(temps)):
        if i == len(temps) - 1:
            holder.append(0)
        else:
            for j in range(i + 1, len(temps)):
                if temps[i] < temps[j]:
                    holder.append(j-i)
                    break
            else:
                holder.append(0)
                
    return holder
'''


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
