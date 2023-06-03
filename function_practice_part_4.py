
# Find the maximum of three numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Multiply all numbers in a list
def mult_list(num_list):
    product = 1
    for num in num_list:
        product *= num
    return product

# Reverse a string
def rev_string(string):
    return string[::-1]

# Check if a number is within a given range (inclusive)
def num_within(num, lower_bound, upper_bound):
    return num >= lower_bound and num <= upper_bound


# Print n rows of Pascal's triangle
def pascal(n):
    def pascal_recursion(num_list):
        pascal_line = [0]
        for index in range(len(num_list) - 1):
           pascal_line.append(num_list[index] + num_list[index+1])
        pascal_line.append(0)
        return pascal_line

    pascal_line = [0, 1, 0]
    print('-----------------------')
    for i in range(0, n):
        print(*pascal_line[1:-1])
        pascal_line = pascal_recursion(pascal_line)
    print('-----------------------')


print('TESTING max_num:')
print(f'(1, 2, 3): {max_num(1, 2, 3)}')
print(f'(3, 2, 1): {max_num(3, 2, 1)}')
print(f'(-1, 0, 1): {max_num(-1, 0, 1)}')
print(f'(54, 432, 432): {max_num(54, 432, 432)}')
print(f'(589, 2801, 490): {max_num(589, 2801, 490)}')

print('\nTESTING mult_list:')
print(f'[1, 2, 3, 4]: {mult_list([1, 2, 3, 4])}')
print(f'[]: {mult_list([])}')
print(f'[0, 2, 3, 5]: {mult_list([0, 2, 3, 5])}')
print(f'[-3, 2, 8, 1/3]: {mult_list([-3, 2, 8, 1/3])}')
print(f'[-5, -5, -5, -5]: {mult_list([-5, -5, -5, -5])}')
print(f'[2/3, 7/2, 6/17, 5, 8]: {mult_list([2/3, 7/2, 6/17, 5, 8])}')

print('\nTESTING rev_string:')
string = 'Hello'
print(f'\'{string}\': {rev_string(string)}')
string = ''
print(f'\'{string}\': {rev_string(string)}')
string = 'Can it reverse longer strings?'
print(f'\'{string}\': {rev_string(string)}')
string = 'racecar'
print(f'\'{string}\': {rev_string(string)}')
string = '\'Hello,\' she says.'
print(f'\'{string}\': {rev_string(string)}')

print('\nTESTING num_within:')
print(f'(1, 0, 2): {num_within(1, 0, 2)}')
print(f'(5, 3, 5): {num_within(5, 3, 5)}')
print(f'(3, -4, 4): {num_within(3, -4, 4)}')
print(f'(-2, -5, 0): {num_within(-2, -5, 0)}')
print(f'(-3, 0, 4): {num_within(-3, 0, 4)}')

print('\nTESTING pascal:')
print('0:')
pascal(0)
print('1:')
pascal(1)
print('2:')
pascal(2)
print('3:')
pascal(3)
print('7:')
pascal(7)
print('10:')
pascal(10)
