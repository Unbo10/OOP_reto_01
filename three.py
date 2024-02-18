def is_prime(n: int) -> bool:
    if abs(n) <= 1:
        return False
    i = 2
    while i <= (abs(n) ** 0.5):
        if n % i == 0:
            return False
        i += 1
    return True

def filter_primes(l: list) -> list:
    odd_nums = [i for i in l if (i % 2 != 0) or (i == 2) or (i == -2)]
    prime_nums = [i for i in odd_nums if is_prime(i)]
    return prime_nums

if __name__ == "__main__":
    int_list = []
    done: bool = False
    print("To stop entering numbers, enter a non-numeric value. This program will return the prime numbers that you enter.")
    while done == False:
        n = input("Enter a number: ")
        try:
            int_list.append(int(n))
        except ValueError:
            done = True
    print("The prime numbers in {} are:".format(int_list), filter_primes(int_list))

    # ? Should there be a single instance of a number in the list?

