
class Parser:

    def replacer(self, s, newstring, index, nofail=False):
        # raise an error if index is outside of the string
        if not nofail and index not in range(len(s)):
            raise ValueError("index outside given string")

        # if not erroring, but the index is still not in the correct range..
        if index < 0:  # add it to the beginning
            return newstring + s
        if index > len(s):  # add it to the end
            return s + newstring

        # insert the new string between "slices" of the original
        return s[:index] + newstring + s[index + 1:]

    def parse(self, expression):
       # stack = []
        expression_list = list(expression)
        print(expression,  expression_list)
        i = 0
        while i < len(expression_list):
            if '*' in expression_list:
                k = expression_list.index("*")
                num1 = int(expression_list[k - 1])
                num2 = int(expression_list[k + 1])
                result = self.operation(num1, num2, '*')
               # stack.append(result)
                del expression_list[k]
                del expression_list[k]
                del expression_list[k - 1]
                expression_list.insert(k-1, result)
            if expression_list[i] == '+' or expression_list[i] == '-':
                num1 = int(expression_list[i - 1])
                num2 = int(expression_list[ i + 1])
                result = self.operation(num1, num2, expression_list[i])
                # del expression_list[i - 1]
                del expression_list[i]
                del expression_list[i]
                del expression_list[i - 1]
                expression_list.insert(i - 1, result)
                i = 0

            i += 1
        print(expression)
        return expression_list.pop()

    def operation(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1 * num2

