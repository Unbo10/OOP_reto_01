def find_greatest_consecutive_sum(l: list) -> int:
    gsum = 0
    i = 0
    while i < len(l) - 2:
        gsum = max(gsum, l[i] + l[i + 1])
        i += 1
    return gsum

if __name__ == "__main__":
    int_list = []
    done: bool = False
    print("To stop entering numbers, enter a non-numeric value. This program will return the greatest sum between two consecutive elements that you enter.")
    while done == False:
        n = input("Enter a number: ")
        try:
            int_list.append(int(n))
        except ValueError:
            done = True
    print("The greatest consecutive sum between two elements in {} is:".format(int_list), find_greatest_consecutive_sum(int_list))