n=int(input("enter the number of terms you want: ")) #Taking input from user for the number of terms
previous_no=0 #used to store the previous term
current_no=1    #used to store the current term
next_no= None   #used to store the addition of previous and current term
ctr=0   #Counter variable 
print(0)    #since every series will have bydefault 0 at first, so printing 0 
while ctr<n-1:  #since 0 is already printed so we need 1 term less, so n-1. 
    next_no=previous_no+current_no  #next term is addition of previous and current term
    previous_no=current_no      #updated previous term with current term for next iteration
    print(current_no)           #printing the current term
    current_no=next_no          #Updating the current term with next term for next iteration  
    ctr+=1                      #Updating the counter variable 
    