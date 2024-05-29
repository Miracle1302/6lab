def print_squares_set(n):

    squares = {i ** 2 for i in range(1, 1001)}  #
    sorted_squares = sorted(squares)  # Sorting

    if len(sorted_squares) < n:
        print("To large a number. Total possible elements:", len(sorted_squares))
    else:

        result = sorted_squares[:n]
        print("A set of squares of integers:", result)



user_count = int(input("Enter the number of elements of the set you want to see: "))


print_squares_set(user_count)
