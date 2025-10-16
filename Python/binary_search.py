def binary_search(arr,target):
    start,end = 0, len(arr)-1
    while start<=end:
        middle = (start+end) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] > target:
            end = middle -1
        else:
            start= middle+1
    
    return False

if __name__=='__main__':
    nums = [1,2,3,4,5,6,7,8]
    target = 8
    print(binary_search(nums,target))