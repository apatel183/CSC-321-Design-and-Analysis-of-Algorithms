import random
import time
#import hybird
#Arpan Patel

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

def hybridSort(list):
    if len(list)<33:
       return insertionSort(list)
    else:
        mid= len(list) //2
        low = hybridSort(list[:mid])
        high = hybridSort(list[mid:])
        return merge(low, high)
#testing the hybirdsort
##user_input= input("Please enter numbers up to 33 or more: ")
##list = list(map(int,user_input.split(",")))
###random.shuffle(list)
##print("Beofore Hybird Sort: "+str(list))
##list=hybirdSort(list)
##print("After Hybird Sort: "+str(list))

def benchmark_insertionSort():
    lst=[]
    for a in range(1024):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = insertionSort(lst);
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for b in range(4096):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = insertionSort(lst);
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for c in range(16384):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = insertionSort(lst);
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for d in range(65536):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = insertionSort(lst);
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for e in range(262144):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = insertionSort(lst);
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))

def benchmark_mergeSort():
    lst=[]
    for a in range(1024):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = mergeSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for b in range(4096):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = mergeSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for c in range(16384):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = mergeSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for d in range(65536):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = mergeSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for e in range(262144):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = mergeSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))

def benchmark_hybrid():
    lst=[]
    for a in range(1024):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = hybridSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for b in range(4096):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = hybridSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for c in range(16384):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = hybridSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for d in range(65536):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = hybridSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))
    for e in range(262144):
        lst.append(random.randint(-1000000,1000000))
    start= time.time()
    lst = hybridSort(lst)
    end = time.time()
    print("start time: "+ str(start) + " end time: " + str(end) + " difference time: " + str(end-start))


#testing 
print("Hybrid Sort Benchmarks:\n")  
benchmark_hybrid()
print("\nMerge Sort Benchmarks:\n")  
benchmark_mergeSort()
print("\nInsertion Sort Benchmarks:\n")  
benchmark_insertionSort()

 
