# Write your solution for algorithm 3 below
def sort_list_descending(lst):
    # Use the sorted() function with reverse=True to create a new sorted list in descending order
    sorted_descending_lst = sorted(lst, reverse=True)
    return sorted_descending_lst

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_descending_list = sort_list_descending(my_list)
print(sorted_descending_list)
