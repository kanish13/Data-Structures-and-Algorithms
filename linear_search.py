def linear(arr,search):
    for i in range(len(arr)):
        if arr[i]==search:
            print("Element found at",i)
            return
    print("Not Found")

a=[1,2,3,4,5]

linear(a,9)