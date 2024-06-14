# find out the pair with given sum in an array in python of time complexity

def two_sum(arr, sum):
    arr.sort()

    right=len(arr)-1
    left=0
    while left<=right:
        if arr[left]+arr[right]>sum:
            right=right-1
        elif arr[left]+arr[right]<sum:
            left=left+1
        elif arr[left]+arr[right]==sum:
            print("value of pair are",arr[left], "&", arr[right])
            right=right-1
            left=left+1
arr=[5, 7, 4, 3, 9, 8, 19, 21]
sum=17
two_sum(arr, sum)



def two_sum(arr, target_sum):
    # Create a hash table to store the elements
    hash_table = {}

    # Traverse the array
    for num in arr:
        # Calculate the difference needed to reach the target sum
        difference = target_sum - num

        # Check if the difference is already in the hash table
        if difference in hash_table:
            print("Value of pair are", difference, "&", num)
            return

        # Add the current element to the hash table
        hash_table[num] = True

    # If no pair is found
    print("No pair found")

arr = [5, 7, 4, 3, 9, 8, 19, 21]
sum = 17
two_sum(arr, sum)
