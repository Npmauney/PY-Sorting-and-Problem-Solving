# Write your solution for algorithm 5 below
def find_pair_with_sum(arr, target):
    # Create a dictionary to store the values we've seen
    seen = {}

    for num in arr:
        # Calculate the difference between the target and the current number
        difference = target - num

        # Check if the difference (complement) is in the 'seen' dictionary
        if difference in seen:
            # A pair with the given sum is found
            return [num, difference]

        # If not found, add the current number to the 'seen' dictionary
        seen[num] = True

    # If no pair is found, return a message indicating that
    return 'no pairs sum to the target'

# Example usage:
arr = [5, 10, 4, 7, 6, 2]
target = 9
result = find_pair_with_sum(arr, target)
print(result)
