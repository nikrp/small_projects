"""
Project Name: Selection Sorting Algorithm

Authors: Nikhil Pellakuru

Updates:
    4.19.2023
"""

########### IMPORTS ###########

########### SWAP METHOD ###########
def swap(main_list:list, idx1, idx2):
    idx1_info = main_list[idx1]
        
    main_list[idx1] = main_list[idx2]
    main_list[idx2] = idx1_info
    
########### SORT METHOD ###########
def select_sort(unsorted_list:list):
    for min_index in range(0, len(unsorted_list) - 1):
        new_list = unsorted_list[min_index:len(unsorted_list)]
        smallest_val = min(new_list)
        swap(unsorted_list, min_index, new_list.index(smallest_val) + min_index)

########### MAIN ###########
if __name__ == "__main__":
    test_list = input("Enter a list with each number seperated by a space (1 2 3 4 5 6): ").split(" ")
    test_list = [int(i) for i in test_list]
       
    print(f"BEFORE: {test_list}")
    select_sort(test_list)
    print(f"AFTER: {test_list}")