def extend_list_from_both_ends(input_list, element_to_add):



    input_list.insert(0, element_to_add)

    input_list.append(element_to_add)

    print("new list:", input_list)


user_input = input("Enter elements of list: ")
input_list = user_input.split()


element_to_add = input("Enter the item to be added at both ends of the list: ")


extend_list_from_both_ends(input_list, element_to_add)

