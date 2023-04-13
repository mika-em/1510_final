"""
FUNCTION:
________

Define a function called add_matrices that accepts two matrices called
first and second and returns the sum matrix.

Each parameter must be a 2D list of integers represents a 2D matrix of
integers, described in detail below.

Your function will return a new 2D list that contains the sum matrix.

For full marks, your solution must use list comprehensions to add the matrices
efficiently.

The original 2D lists passed as arguments may not be changed, not even temporarily.

DESCRIPTION:
___________

This matrix has 3 rows and 4 columns:

1 2 3 4
2 3 4 5
3 4 5 6

[ [ 1, 2, 3, 4 ], [ 2, 3, 4, 5 ], [ 3, 4, 5, 6 ] ]

This matrix has 2 rows and 2 columns:

1 2
3 4

[ [ 1, 2], [ 3, 4 ]

This matrix has 1 row and 1 column:

4

[ [ 4 ] ]

We can add matrices that have the same dimensions:

1 3 + 8 3 = 9 6
0 4   5 3   5 7

[ [ 1, 3 ], [ 0, 4] ] + [ [ 8, 3 ], [ 5, 3 ] ] = [ [ 9, 6 ], [ 5, 7 ] ]

1 2 3 4 + 8 3 is an "Exceptional Situation" the matrices are not the same size!
2 3 4 5   5 3
3 4 5 6

SAMPLE USAGE:
____________

some_matrix = [ [ 1, 2 ], [ 3, 4 ] ]
some_other_matrix = [ [ 5, 6 ], [ 7, 8 ] ]

result_matrix = add_matrices(some_matrix, some_other_matrix)

print(result_matrix)

[ [ 6, 8 ], [ 10, 12 ] ]

1 2 + 5 6 =  6  8
3 4   7 8   10 12

DOCSTRINGS:
__________

Yes. Full docstrings are needed. Include pre- and post-conditions.

EXCEPTION HANDLING:
__________________

Yes. Employ defensive programming. Raise an appropriate exception whenever a
function's preconditions are not met.

Your function is only required to add the two matrices if they contain
integers and are represented as 2D lists and are the same dimensions.

Reject anything else.

DESIGN:
______

Design small atomic functions that are easy to test. Don't forget your main function, etc.

All the usual style rules apply.

DOCTESTS:
________

Yes. Two simple doctests please.

MAIN FUNCTION:
_____________

Yes. In main, deliberately pass two mismatched matrices to your function so that it
raises an exception, and show me how to avoid a program crash using try-except-else.

UNIT TESTS:
__________

Yes. For full marks write unit tests that add the following:

 a) two square matrices that are 1x1
 b) two square matrices that are 2x2
 c) two square matrices that are 3x3
 d) two rectangular matrices that are 3x4 or 4x3
 e) two homogenous matrices (matrices whose elements are all the same value)
 f) two matrices of size 1x4 or 4x1 (vectors, some would call them!)
 g) one exceptional situation.

Note that:

[ 1, 2, 3, 4 ] IS NOT  a matrix of size 1x4.

[ [ 1, 2, 3, 4 ] ] IS  a matrix of size 1x4 (1 row, 4 columns) also called a row-vector

[ [ 1 ], [ 2 ], [ 3 ], [ 4 ] ] is a matrix of size 4x1 (4 rows, 1 column) also called a column-
vector.

GRADING:
_______

4 points for correctly adding two matrices in your function and returning
         the sum as a 2D list from your function
2 points for correct use and handling of exceptions in your function(s) and main
2 points for correct docstring(s)
2 points for correct doctests
2 points for code quality and style including functional decomposition, brevity,
         identifiers, etc.
3 points for unit tests

-1 penalty for a solution that does not use list comprehensions efficiently.
"""


def add_matrices(first, second):
    pass  # Replace this pass statement with your code.


def main():
    pass  # Replace this pass statement with your code.


if __name__ == "__main__":
    main()
