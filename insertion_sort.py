"""
Project Name: Selection Sorting Algorithm

Authors: Nikhil Pellakuru

Updates:
    4.20.2023
"""

########### IMPORTS ###########

########### SWAP METHOD ###########
def swap(main_list:list, idx1, idx2):
    idx1_info = main_list[idx1]
        
    main_list[idx1] = main_list[idx2]
    main_list[idx2] = idx1_info

########### SORT METHOD ###########
def insert_sort(unsorted_list:list):
    index_value = 0
    for min_index in range(len(unsorted_list) - 1):
        print("TEST 1 - ", unsorted_list[min_index + 1], unsorted_list[min_index], min_index)
        while unsorted_list[index_value + 1] <= unsorted_list[index_value]:
            index_value - 1
            if index_value == 0:
                break
        
        index_value = min_index - 1

        swap(unsorted_list, unsorted_list.index(unsorted_list[min_index]), unsorted_list.index(unsorted_list[min_index + 1]))
        while unsorted_list[index_value] < unsorted_list[index_value - 1]:
            swap(unsorted_list, unsorted_list.index(unsorted_list[index_value]), unsorted_list.index(unsorted_list[index_value - 1]))
        print("Unsorted List Swapped", unsorted_list, unsorted_list[min_index], unsorted_list[min_index + 1])
    
    print("SORTED LIST", unsorted_list)
            

########### MAIN ###########
if __name__ == "__main__":
    insert_sort([4, 3, 2, 1])