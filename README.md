# Arithmetic Formatter

This is the boilerplate for the Arithmetic Formatter project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter


# My collaboration in the project:

# Arithmetic Arranger

This Python function, `arithmetic_arranger`, takes a list of arithmetic problems and arranges them vertically in a formatted way. The function follows specific rules for formatting and returns the arranged problems or meaningful error messages.

## Functionality

### Error Conditions

1. **Too Many Problems:**
   - If there are more than five problems, the function returns: `Error: Too many problems`.

2. **Invalid Operator:**
   - The function only accepts addition (`+`) and subtraction (`-`) operators. Multiplication and division will result in: `Error: Operator must be '+' or '-'`.

3. **Invalid Operands:**
   - Each number (operand) must only contain digits. Otherwise, the function returns: `Error: Numbers must only contain digits`.

4. **Exceeding Digit Limit:**
   - Each operand has a maximum width of four digits. If exceeded, the function returns: `Error: Numbers cannot be more than four digits`.

### Successful Formatting

- If the user supplies the correct format, the conversion will follow these rules:
  - There is a single space between the operator and the longest of the two operands.
  - The operator is on the same line as the second operand.
  - Numbers are right-aligned.
  - There are four spaces between each problem.
  - Dashes are present at the bottom of each problem.

## Example Usage

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems)
print(result)
