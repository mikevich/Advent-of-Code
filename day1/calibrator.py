import re

with open('day1/input.txt') as input:
    lines = input.read().splitlines()
    output_nums = []
    for line in lines:
        num_strings = re.findall(r'\d', line)
        nums = []
        for string in num_strings:
            nums.append(int(string))
        output_nums.append(nums[0] * 10 + nums[-1])
    
    total = 0
    for num in output_nums:
        total += num
    
    print(total)