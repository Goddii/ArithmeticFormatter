
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'ERROR!! Too many problems to solve'

    arranged_problems = ''
    top_line = ''
    bottom_line = ''
    dash_line = ''
    results_line = ''

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return f'Error: Invalid problem - {problem}'

        num1, operator, num2 = parts

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Number must contain digits'

        if operator not in ['+', '-']:
            return 'Error: Operator must be + or -'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Number must contain 4 digits'

        width = max(len(num1), len(num2)) + 2

        top_line += ' ' + num1.rjust(width) + '    '
        bottom_line += operator + num2.rjust(width) + '    '
        dash_line += '-' * (width+1) + '     '

        if show_answers:
            if operator == '+':
                results = str(int(num1) + int(num2))
            else:
                results = str(int(num1) - int(num2))

            results_line += ' '+ results.rjust(width) + '    '

    arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()

    if show_answers:
        arranged_problems += '\n' + results_line.rstrip()

    return arranged_problems

problem1 = ['32 + 8','3801 - 1','45 + 43', '123 + 49']
print(arithmetic_arranger(problem1))
print()
problem2 = ['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49']
print(arithmetic_arranger(problem2, True))