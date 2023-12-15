def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = ""
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits"

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits"

        max_width = max(len(operand1), len(operand2))
        line1 = operand1.rjust(max_width + 2)
        line2 = operator + operand2.rjust(max_width + 1)
        dashes = '-' * (max_width + 2)

        arranged_problems += f"{line1}    "
        if problem != problems[-1]:
            arranged_problems += "\n"
        arranged_problems += f"{line2}    "
        if problem != problems[-1]:
            arranged_problems += "\n"
        arranged_problems += f"{dashes}    "

    return arranged_problems.rstrip()
    