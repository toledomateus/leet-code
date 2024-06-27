class Solution:
    def romanToInt(sidxf, s: str) -> int:
        romanToInt = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        num, idx, nextPos = 0,0, ''
        while idx < len(s):
            if idx + 1 < len(s):
                nextPos = s[idx+1]
                                
            pos = s[idx] + nextPos
            if pos in romanToInt:
                num += romanToInt[pos]
                idx += 1
            else:
                num += romanToInt[s[idx]]
            idx += 1
        return num