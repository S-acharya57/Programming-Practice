# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # getting each hourglass and getting their sum 
    # since the array size is fixed to be 6x6 
    
    all_sums = []
    for i in range(4):
        
        # hourglass_index = [[[i][i]], [[i][i+1]], [[i][i+2]],
        #                     [[i][i+1]],
        #                     [[i+1][i]], [[i+1][i+1]], [[i+1][i+2]]]


        # for index in hourglass_index:
        #     for ind in index:
        #         if(ind < 6 ):
        #             func = True
        #     if(func):
        #         sum+=arr[index]
        #     print(sum)
        #     all_sums.append(sum)
        for j in range(4):

            zero_ = j
            one_ = j + 1
            two_ = j + 2

            # print(f'j->{j}')
            sum_ = 0
            # print(f'Arr [zero_][:3]-> {arr[zero_][i:i+3]}')
            # print(one_)
            # print(f'Arr [one_][one_]-> {arr[one_][i+1]}')
            # print(f'Arr [two_][:3]-> {arr[two_][i:i+3]}')

            sum_ += sum(arr[zero_][i:i+3])
            sum_ += arr[one_][i+1]
            sum_ += sum(arr[two_][i:i+3])
            
            
            all_sums.append(sum_)

    return max(all_sums)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
