#Arpan Patel
import random
#insertion sort
def insertionSort(list):
    for index in range (1, len(list)):
        given_val = list[index]
        i = index - 1
        while i >= 0:
            if given_val < list[i]:
                list[i+1] = list[i] #rightshift
                list[i] = given_val #leftshift
                i = i -1
            else:
                break
    return list
#for only testing
#a = [10,9,8,7,6,5,4,3,2,1]
#print("Before Insertion Sort" + str(a))
#a=insertionSort(a)
#print("After Insertion Sort" + str(a))
def mergeSort(list):
    if len(list) < 2:
        return(list)
    mid= len(list) //2

    low = mergeSort(list[:mid])
    high = mergeSort(list[mid:])
    return merge(low,high)
def merge(low, high):
    final = []
    start = 0
    end = 0
    while (start < len(low) and end < len(high)):
        if(low[start] <= high[end]):
            final.append(low[start])
            start = start + 1
        else:
            final.append(high[end])
            end = end + 1
    final = final + low[start:]
    final = final + high[end:]
    return final
#for only testing
#a = [10,9,7,8,3,4,1,2,5,6]
#print("Before Merge Sort" + str(a))
#a=mergeSort(a)
#print("After Merge Sort" + str(a))


def hybridSort(list):
    if len(list)<33:
       return insertionSort(list)
    else:
        mid= len(list) //2
        low = hybridSort(list[:mid])
        high = hybridSort(list[mid:])
        return merge(low, high)
#for only testing   
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,65493,31232, 2324, 231231, 5343,123121234221]
#print("this is list is a 33" + str(a))
#a= hybirdSort(a)
#print("this is list is less than 33" + str(a))
#a = int[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
#hybirdSort(a)
##a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
##print("this is list is greater than 33" + str(a))
##a=hybirdSort(a)


user_input= input("Please enter numbers up to 33 or more: ")
list = list(map(int,user_input.split(",")))
random.shuffle(list)
print("Beofore Hybird Sort: "+str(list))
list=hybridSort(list)
print("After Hybird Sort: "+str(list))

        
                
                
 
