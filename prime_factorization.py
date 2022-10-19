"""
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""


def prime_numbers(user_num: int) -> list:
    """
    Function to find all prime numbers till asked number
    """
    list_of_primes = [2]
    check_prime = 3
    if user_num < 2:
        return 0
    while check_prime <= user_num:
        for prime_number in list_of_primes:
            if check_prime % prime_number == 0:
                check_prime += 2
                break
        else:
            list_of_primes.append(check_prime)
            check_prime += 2
    return list_of_primes


def get_num() -> int:
    """
    Function to get number from input and check if it meet a conditions
    """

    while True:
        try:
            user_num = int(input("""
            \rPlease, enter a integer number greater then 1
            \rto find all Prime Factors (if there are any)
            \rLimit is 1000.
            \rYour number is: """))
            if 1 < user_num <= 1000:
                return user_num
            print("\nError. The number does not meet the conditions.")
            continue
        except ValueError:
            print("\nError. Please use integer numbers")
            continue


CHOICE = "y"
while CHOICE == "y":
    check_num = get_num()
    big_list = prime_numbers(check_num)
    factors_list = []
    while True:
        if check_num in big_list:
            factors_list.append(int(check_num))
            print(factors_list)
            break
        while check_num not in big_list:
            for prime_factor in big_list:
                if check_num % prime_factor == 0:
                    check_num = check_num / prime_factor
                    factors_list.append(prime_factor)
                    break
    while True:
        CHOICE = input("One more number? y/n :  ")
        if CHOICE in ("y", "n"):
            break
        print("Please type 'y' to continue and 'n' to quit")
