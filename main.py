class Solution:
    def romanToInt(self, s: str) -> int:

        y = 0  # output Integer number
        prev = 'A'  # for the principle of subtraction

        x = list(s)

        for i in range(len(x)):
            if x[i] == 'M':
                if prev == 'C':
                    y -= 200
                y += 1000
                prev = 'M'
            elif x[i] == 'D':
                if prev == 'C':
                    y -= 200
                y += 500
                prev = 'D'
            elif x[i] == 'C':
                if prev == 'X':
                    y -= 20
                y += 100
                prev = 'C'
            elif x[i] == 'L':
                if prev == 'X':
                    y -= 20
                y += 50
                prev = 'L'
            elif x[i] == "X":
                if prev == 'I':
                    y -= 2
                y += 10
                prev = 'X'
            elif x[i] == "V":
                if prev == 'I':
                    y -= 2
                y += 5
                prev = 'V'
            elif x[i] == "I":
                y += 1
                prev = 'I'

        return y