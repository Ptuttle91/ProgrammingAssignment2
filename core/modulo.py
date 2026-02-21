# This module contains the formulas build to answer tasks 1 - 6. 
# See ReadMe.md for references used.



def congruent_mod(b:int, n: int, lower: int, upper: int) -> list[int]:
    # This is the logic for task 1, returning all integeers x in [lower, upper] such that x = b (mod n)
    return [x for x in range(lower, upper+1) if (x-b) % n == 0]



def divisors(x: int) -> list[int]:
    # This is the log for task 2, returning the positive divisors of x in the form of a list.
    x = abs(x)
    if x == 0:
        return []
    divs: list[int] = []
    for d in range(1, x+1):
        if x % d == 0:
            divs.append(d)
    return divs



def greatest_common_divisor(a: int, b:int) -> int:
    # This is the logic for task 3, returning the GCD(a, b), computing the |a| and |b| divisors from Task 2.
    da = set(divisors(a))
    bd = set(divisors(b))
    common = da.intersection(bd)
    if not common:
        return 0
    else:
        return max(common)



def multiplicative_inverse(a: int, b: int, n: int) -> bool:
    # This holds the logic for task 4. It will return True is a and b are multiplicative inverses mod n, else will return false.
    return(a*b) % n == 1



def relatively_prime(a:int, b:int) -> bool:
    # This is the logic for task 5. It will return true is a and b are relatively prime (coprime), otherwise it will return false
    # NOTE: This must use the divisors from task 2 and GCD from task 3.
    _=divisors(a)
    _=divisors(b)

    return greatest_common_divisor(a,b) == 1



def task6a_euclidean_writeup()-> str:
    # This is the logic for task 6a, a writeup to describe a Euclidean Algorithm in the form of a string.
    # NOTE: This should return a text output. Ensure that there is no required input, or if so, see if button name can change to 'view' instead of 'submit'.
    return(
        "Task 6.A: Euclidean Algorithm: \n"
        "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n"
        "The purpose of the Euclidean Algorithm is to efficiently \n"
        "find the greatest common divisor (gcd) of two integers. \n"
        "This is performed by repeatedly replacing a pair until \n"
        "the remainder is 0, and with that, we find that the last \n"
        "non-zero divisor is the greatest common divisor (gcd).\n"
        " \n"
        "The formula can be expressed as taking a pair (a, b) and \n"
        "repeatedly replacing it with (b, a mod b) until \n"
        "a mod b = 0. \n"
        " \n"
        "This is efficient as the numbers rapidly reduce with each \n"
        "recursion or repeat. Each each repeat is one division with \n"
        "remainder. This means that even large numbers are rapidly \n"
        "reduced with each recursion.\n"
        " \n"
        "The number of calls is equal to the number of times we do \n"
        "the replacement of (a,b) to (b, a mod b) before reaching 0. \n"
        "This is bound by the rule O(log(min(a,b)))\n"
        "\n"
        "This can be used in many programming situations, from creating\n"
        "a 'tick' or turn system for cooldowns in a game, finding shared\n"
        "factors, or calculating a way for animation loops with different \n"
        "lengths to align.\n"
    )


    #NOTE: These next two functions are both part of Task 6B


def euclid_gcd(a: int, b: int) -> int:
    # This is part 1 of Task 6b, which will use a Euclidean algorithm subroutine, and return the gdc using repeated remainder
    a = abs(a)
    b = abs(b)
    while b !=0:
        a, b = b, a%b
    return a

def relatively_prime_euclid(a: int, b: int)->bool:
    # This is part 3 of the logic for task 6b, which calls for us to rewrite task 5 using the Euclidean algorith as a subroutine.
    # Part 2 will return True if a and b are relatively prime using the algorithm formed in part 1.
    return euclid_gcd(a,b)==1
