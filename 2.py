def unique_list(input_list):

    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)  #
            result.append(item)
    print("list without duplicates :", result)
    return result

user_input = input("Enter elements of list: ")

input_list = user_input.split()

unique_list(input_list)
