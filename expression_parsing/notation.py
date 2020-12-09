class Notation:

    def infix_postfix(self, equation):
        equation = self.str_to_arr_infix(equation)
        output = []
        stack = []
        last_priority = -1

        for c in equation:
            priority = self.calculate_priority(c)
            if priority == -1:
                output.append(c)
            elif priority == 0:
                if c == '(':
                    stack.append(c)
                    last_priority = priority
                else:
                    while (True):
                        if len(stack) <= 0:
                            break
                        popped = stack.pop()
                        if popped == '(':
                            break
                        else:
                            output.append(popped)
            elif priority > last_priority:
                stack.append(c)
                last_priority = priority
            else:
                if len(stack) > 0:
                    popped = stack.pop()
                    output.append(popped)
                stack.append(c)
                last_priority = priority
            # print('input: ', c, '   output: ', output, '   stack: ', stack)
        while (True):
            if len(stack) <= 0:
                break
            else:
                output.append(stack.pop())

        result = ' '.join(map(str, output))
        return result

    def postfix_infix(self, equation):
        equation = self.str_to_arr_postfix(equation)
        output = []
        for c in equation:
            if self.is_opperand(c):
                output.insert(0, c)
            else:
                op1 = output[0]
                output.pop(0)
                op2 = output[0]
                output.pop(0)
                output.insert(0, "(" + op2 + c + op1 + ")")
        result = ""
        for x in ''.join(map(str, output)):
            result += x + ' '
        return result

    def prefix_postfix(self, equation):
        equation = self.str_to_arr_postfix(equation)
        equation = reversed(equation)
        stack = []
        for c in equation:
            # print(c, stack)
            if self.is_operator(c):
                opperand1 = stack.pop()
                opperand2 = stack.pop()
                temp = opperand1 + opperand2 + c
                stack.append(temp)
            else:
                stack.append(c)
        result = ""
        for x in ''.join(map(str, stack)):
            result += x + ' '
        return result

    def postfix_prefix(self, equation):
        equation = self.str_to_arr_postfix(equation)
        s = []
        length = len(equation)
        for i in range(length):
            if self.is_operator(equation[i]):
                op1 = s.pop()
                op2 = s.pop()
                temp = equation[i] + op2 + op1
                s.append(temp)
            else:
                s.append(equation[i])
        result = ""
        for x in ''.join(map(str, s)):
            result += x + ' '
        return result

    @staticmethod
    def str_to_arr_postfix(string):
        return string.split(" ")

    @staticmethod
    def is_opperand(string):
        operators = ['*', '/', '+', '-', '^', '(', ')']
        return string not in operators

    @staticmethod
    def is_operator(string):
        operators = ['*', '/', '+', '-', '^', '(', ')']
        return string in operators

    @staticmethod
    def calculate_priority(char):
        if char == '(' or char == ')':
            return 0
        elif char == '^':
            return 3
        elif char == '*' or char == '/':
            return 2
        elif char == '+' or char == '-':
            return 1
        else:
            return -1

    def str_to_arr_infix(self, string):
        string = string.replace(" ", "")
        connector = ""
        result = []
        for x in string:
            if self.calculate_priority(x) == -1:
                connector += x
            else:
                if len(connector) > 0:
                    result.append(connector)
                    connector = ""
                result.append(x)
        if len(connector) > 0:
            result.append(connector)
        return result
