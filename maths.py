################################################################################
## MIT License
##
## Copyright (C) 2023 Duck McSouls <quacksouls [AT] gmail [DOT] com>
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
################################################################################

from random import randint

# Some basic mathematics problems.

def is_valid_sub_operands(a: int, b: int) -> bool:
    """
    Whether two numbers are valid subtraction operands.  Two numbers a and b are
    valid subtraction operands if a >= b.

    @param a The first operand for subtraction.
    @param b The second operand for subtraction.
    """
    return a >= b

def random_add_problems() -> list:
    """
    Generate random addition problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for an
        addition problem.
    """
    # Simple problems
    simple_low = 10
    simple_high = 99
    simple_n = 2
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # Intermediate problems
    inter_low = 100
    inter_high = 999
    inter_n = 2
    inter_a = random_operands(inter_low, inter_high, inter_n)
    inter_b = random_operands(inter_low, inter_high, inter_n)

    # Advanced problem
    adv_low = 1000
    adv_high = 9999
    adv_n = 1
    adv_a = random_operands(adv_low, adv_high, adv_n)
    adv_b = random_operands(adv_low, adv_high, adv_n)

    a = simple_a + inter_a + adv_a
    b = simple_b + inter_b + adv_b
    return list(zip(a, b))

def random_mult_problems() -> list:
    """
    Generate random multiplication problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for a
        multiplication problem.
    """
    # Simple problems involving the times table from 2 to 12.
    simple_low = 2
    simple_high = 12
    simple_n = 3
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # Intermediate problems involving the multiplication of two 2-digit numbers.
    inter_low = 13
    inter_high = 99
    inter_n = 3
    inter_a = random_operands(inter_low, inter_high, inter_n)
    inter_b = random_operands(inter_low, inter_high, inter_n)

    # Advanced problems involving the multiplication of a 3-digit number by a
    # 2-digit number.
    adv_low = 100
    adv_high = 999
    adv_n = 3
    adv_a = random_operands(adv_low, adv_high, adv_n)
    adv_b = random_operands(inter_low, inter_high, adv_n)

    # Difficult problems involving the multiplication of two 3-digit numbers.
    diff_low = 100
    diff_high = 999
    diff_n = 1
    diff_a = random_operands(diff_low, diff_high, diff_n)
    diff_b = random_operands(diff_low, diff_high, diff_n)

    a = simple_a + inter_a + adv_a + diff_a
    b = simple_b + inter_b + adv_b + diff_b
    return list(zip(a, b))

def __sub_problems() -> list:
    """
    Generate random subtraction problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for a
        subtraction problem.
    """
    # Simple problems
    simple_low = 10
    simple_high = 99
    simple_n = 2
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # Intermediate problems
    inter_low = 100
    inter_high = 999
    inter_n = 2
    inter_a = random_operands(inter_low, inter_high, inter_n)
    inter_b = random_operands(inter_low, inter_high, inter_n)

    # Advanced problem
    adv_low = 1000
    adv_high = 9999
    adv_n = 1
    adv_a = random_operands(adv_low, adv_high, adv_n)
    adv_b = random_operands(adv_low, adv_high, adv_n)

    a = simple_a + inter_a + adv_a
    b = simple_b + inter_b + adv_b
    return list(zip(a, b))

def random_sub_problems() -> list:
    """
    Generate random subtraction problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for a
        subtraction problem.
    """
    problem = []
    good_problems = False
    while not good_problems:
        problem = __sub_problems()
        valid = [is_valid_sub_operands(x, y) for x, y in problem]
        good_problems = all(valid)
    return problem

def random_operands(low: int, high: int, how_many: int) -> list:
    """
    Generate random operands for a mathematics problem.

    @param low Minimum value for operand.
    @param high Maximum value for operand.
    @param how_many How many operands to generate.
    @returns A list of random operands.
    """
    return [randint(low, high) for _ in range(how_many)]

def unique_problems(n: int, kind: str) -> list:
    """
    Generate unique, random mathematics problems.

    @param n Generate this many problems.
    @param kind The type of mathematics problem.  Currently supporting these:
        * "+" -- An addition problem.
        * "-" -- A subtraction problem.
        * "x" -- A multiplication problem.
    @returns A list of 2-tuples.  Each tuple contains the operands for a
        mathematics problem.
    """
    if n < 1:
        raise ValueError("Must generate at least 1 problem")

    problem = []
    match kind:
        case "x":
            while len(set(problem)) < n:
                problem = random_mult_problems()
        case "+":
            while len(set(problem)) < n:
                problem = random_add_problems()
        case "-":
            while len(set(problem)) < n:
                problem = random_sub_problems()
        case _:
            raise ValueError("Invalid problem type")

    return problem

################################################################################
# Start here
################################################################################

def main():
    """
    Generate various mathematics problems.
    """
    how_many_add = 5
    how_many_sub = 5
    how_many_mult = 10
    print("Addition")
    for x, y in unique_problems(how_many_add, "+"):
        print(x, y)
    print("\nSubtraction")
    for x, y in unique_problems(how_many_sub, "-"):
        print(x, y)
    print("\nMultiplication")
    for x, y in unique_problems(how_many_mult, "x"):
        print(x, y)

if __name__ == "__main__":
    main()
