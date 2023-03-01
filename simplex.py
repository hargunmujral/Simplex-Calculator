import numpy as np
import scipy.linalg as la
import math


def canonical_form(A, b, c, k, basis):
    """
    Return the canonical form of the objective function and the constraint function

        A: A matrix of integers
        b: A vector of integers
        c: A vector of integers
        k: A constant
        basis: A list of integers
    """

    # Reduce all the basis by 1 to fix the index
    basis = [x - 1 for x in basis]

    # A_B will be the matrix A with columns corresponding to the basis
    A_B = A[:, basis]
    print(A_B)

    # Multiply the inverse of A_B with Ax to get A'x
    A_prime = np.dot(la.inv(A_B), A)
    b_prime = np.dot(la.inv(A_B), b)

    A_prime = np.around(A_prime, 4)
    b_prime = np.around(b_prime, 4)

    c_prime = c[basis].reshape((-1, 1))
    # print(c_prime.shape)

    # Find values of y
    y = np.dot(la.inv(A_B.T), (c[basis]).T)

    # Round y to the nearest integer
    y = np.around(y, 4)

    # Rewrite the canonical form of the objective function, from c^Tx to (c')^Tx + z
    z_x = (c - np.dot(y.T, A))
    z_k = k + np.dot(y.T, b)

    z_x = np.around(z_x, 4)
    z_k = np.around(z_k, 4)

    print("The canonical form of the objective function is: ")
    print(z_x, "x +", z_k)

    print("The canonical form of the constraint function is: ")
    print(A_prime, "x =", b_prime)

    return A_prime, b_prime, z_x, z_k


def simplex_with_blanks_rule(A, b, c, k, starting_basis):

    A_start, b_start, z_x_start, z_k_start = canonical_form(
        A, b, c, k, starting_basis)

    if np.all(z_x_start <= 0):
        print("The problem is optimal")
        x = [b if np.all(A_start[:, b - 1] >
             0) and sum(A_start[:, b - 1]) == 1 else 0 for b in starting_basis]
        return A_start, b_start, z_x_start, z_k_start

    # the entering variable is the smallest positive index of z_x
    entering_variable = np.argmin(
        [x if x > 1e-3 else 1e6 for x in z_x_start]) + 1

    # the leaving variable is the index in the basis, of the smallest ratio of b_prime to A_prime
    # where A_prime > 0 and b_prime >= 0
    # any negative or zero values of A_prime are removed
    # any negative values of b_prime are removed

    A_prime = A_start[:, entering_variable - 1]
    x_over_y = [x / y if y > 1e-3 and x >=
                0 else 1e6 for x, y in zip(b_start, A_prime)]
    if np.all([x == 1e6 for x in x_over_y]):
        print("The problem is unbounded")
        return
    # print(x_over_y)
    leaving_variable = np.argmin(x_over_y) + 1
    print("entering and leaving:", entering_variable,
          starting_basis[leaving_variable-1])

    # the new basis is the basis with the leaving variable replaced by the entering variable
    new_basis = starting_basis.copy()
    new_basis[leaving_variable - 1] = entering_variable

    print("The new basis is: ", new_basis)

    # recursively call the function with the new basis
    simplex_with_blanks_rule(A_start, b_start, z_x_start, z_k_start, new_basis)


def main():
    # Define the matrix A
    A = np.array([[1, 1, 2, 0], [0, 1, 1, 1]])

    # Define the vector b
    b = np.array([2, 5])

    # Define the vector c
    c = np.array([0, 1, 3, 0])

    # Define the constant k at the start
    k = 0

    # Define a basis
    basis = [2, 4]

    # Call the function
    simplex_with_blanks_rule(A, b, c, k, basis)


if __name__ == "__main__":
    main()
