#Program to check if an array is sorted or not
def check(arr):
    
    n = len(arr)
    if n<=1:
        return True
    return arr[0]<arr[1] and check(arr[1:])
arr = [1,7,100,1100]
print (check(arr))

#linear search in array using reursion
def search(arr, k, i):
  
    if i == len(arr):
        return False
    return arr[i]==k or search(arr, k, i+1)
    

i = 0
k = 100
arr = [1,7,100,1100]
print (search(arr, k, i))


#reverse a stack recursion
def Reverse(stack):
  
    if len(stack)==1:
        return 
    temp = stack.pop()
    Reverse(stack)
    insert(stack, temp)

def insert(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return
    top = stack.pop()
    insert(stack, element)
    stack.append(top)
   
stack= [1,7,100,1100]
(Reverse(stack))
print(stack)
