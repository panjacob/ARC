class Notation:

    def in_to_pre(self, equation):
        equation = equation.replace(" ", "")
        output = []
        stack = []
        last_priority = -1
        connector = ""
        for c in equation:
            priority = self.calculate_priority(c)
            if priority == -1:
                connector += c
            elif connector != '':
                output.append(connector)
                connector = ''

            if priority == 0:
                if c == '(':
                    stack.append(c)
                else:
                    while (True):
                        if len(stack) <= 0:
                            break
                        popped = stack.pop()
                        print(popped, len(stack))
                        if popped == '(':
                            break
                        else:
                            output.append(popped)

            elif priority > last_priority and priority > -1:
                stack.append(c)
                last_priority = priority
            elif priority > -1:
                if len(stack) > 0:
                        popped = stack.pop()
                        output.append(popped)
                stack.append(c)
                last_priority = priority

            print('input: ', c, '   output: ', output, '   stack: ', stack, "   connector: ", connector)

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
