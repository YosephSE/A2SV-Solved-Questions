class Solution(object):
    def intToRoman(self, num):
        res = []
        num = str(num)
        roman_map = {
        "1": "I",
        "5": "V",
        "10": "X",
        "50": "L",
        "100": "C",
        "500": "D",
        "1000": "M"
        }
        addition_ops = ['2', '3', '6', '7', '8']
        for i in range(len(num)):
            mul_of_10 = num[i] + '0' * len(num[i + 1:])
            print(mul_of_10)
            roman_val = ''
            if mul_of_10 in roman_map:
                res.append(roman_map[mul_of_10])
            elif mul_of_10[0] == '4':
                res.append(roman_map['1' + mul_of_10[1:]] + roman_map['5' + mul_of_10[1:]])
            elif mul_of_10[0] == '9':
                res.append(roman_map['1' + mul_of_10[1:]] + roman_map['10' + mul_of_10[1:]])
            elif int(mul_of_10[0]) in [2, 3]:
                res.extend([roman_map['1' + '0' * len(mul_of_10[1:])] * int(mul_of_10[0])])
            elif int(mul_of_10[0]) in [6, 7, 8]:
                res.extend([roman_map['5' + '0' * len(mul_of_10[1:])] + roman_map['1' + '0' * len(mul_of_10[1:])] * (int(mul_of_10[0]) - 5)])
        return ''.join(res)        