import re

with open('day1/input.txt') as input:
    lines = input.read().splitlines()
    output_nums = []
    for line in lines:
        num_strings = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        nums = []
        for string in num_strings:
            if len(string) > 1:
                first_num = 0
                last_num = 0
                match string:
                    case 'one':
                        nums.append(1)
                    case 'two':
                        nums.append(2)
                    case 'three':
                        nums.append(3)
                    case 'four':
                        nums.append(4)
                    case 'five': 
                        nums.append(5)
                    case 'six':
                        nums.append(6)
                    case 'seven':
                        nums.append(7)
                    case 'eight':
                        nums.append(8)
                    case 'nine':
                        nums.append(9)
            else:
                nums.append(int(string))    
        output_nums.append(nums[0] * 10 + nums[-1])

    
    total = 0
    for num in output_nums:
        total += num
    
    print(total)