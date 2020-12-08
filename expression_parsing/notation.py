class Notation:

    def in_to_pre(self, equation):
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

    def calculate_priority(self, char):
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

    def str_to_arr_postfix(self, string):
        return string.split(" ")

    def isOpperand(self, string):
        opperands = ['*', '/', '+', '-', '^', '(', ')']
        return string not in opperands

    def pre_to_in(self, equation):
        equation = self.str_to_arr_postfix(equation)
        output = []
        for c in equation:
            if self.isOpperand(c):
                output.insert(0, c)
            else:
                op1 = output[0]
                output.pop(0)
                op2 = output[0]
                output.pop(0)
                output.insert(0, "(" + op2 + c + op1 + ")")
        return output

    def pre_to_post(self, equation):
        equation = self.str_to_arr_postfix(equation)
        stack = []
        i = len(equation) - 1
        while (True):

            c = equation[i]
            print('stack: ', stack, '    equation: ', equation, '  c: ', c, '  i: ', i, 'len: ', len(equation))
            if not self.isOpperand(c):
                i -= 2
                operator1 = equation.pop()
                operator2 = equation.pop()
                opperand = stack.pop()
                print(operator1, operator2, opperand)
                stack.append(operator1)
                stack.append(operator2)
                stack.append(opperand)
            else:
                stack.append(equation.pop())
                i -= 1
