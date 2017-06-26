#Arpan Patel
#CSC 321 Homework 3#
#For sort answer a,b,c please look at the word doc of written answers#

#running time of this algo is O(n^2)# 
def counting_Inversions_pairs(list):
    count = 0;
    for i in range(len(list)):
        for j in range(i,len(list)):
            if (list[i]>list[j]):
                count=count+1
    return count
    
user_input = eval(input("Please enter numbers as list ex:[4,3,5,2,1]: "))
list= counting_Inversions_pairs(user_input)
print("Total Inverted Pairs: ",list)               
                
