#using summetion method
#natural num-sum of given number
# formula  find summetion formula num ---> n*(n+1)//2
# n is last num of given arr
# xor method

def get_missingnum_summation(a):
    n=a[-1]
    n_val=n*(n+1)//2
    sum1=sum(a)
    print(n_val-sum1)


a=[1, 2, 4, 5, 6, 7]
get_missingnum_summation(a)








