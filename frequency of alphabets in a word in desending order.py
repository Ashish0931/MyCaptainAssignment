def most_frequent(test_string): #taking the string as input
    
    for i in test_string:   #looping in the string
        ctr=1   #setting a counter to count the frequency of alphabets
        for j in test_string:   #sub loop
            if i==j:    #comparing one element with each every other element in the string
                test_dict[i]=ctr;   #entering this data in the dictionary
                ctr+=1  #incrementing the counter. 
    

user_string ="Mississippi" #taking a test string from user 
test_string= user_string.lower() #converting the string to lower case
test_dict={} #creating a test dictionary to process the data
final_dict={}   #creating a final dictonary to give the output
most_frequent(test_string)  #processing the text in frequent function
dic_val=list(test_dict.values())    #taking the values from dictionary
(dic_val.sort(reverse=True))    #sorting the values in the dictonary in reverse order
print("In string", test_string , ":")   
for i in dic_val:   #looping the sorted dictonary of values 
    for j in test_dict: #looping in the test dictionary 
        if test_dict[j]==i: #if the value in test dictonary same as in dic_val dictionary, then add it in the final dictionary
            final_dict[j]=i;   # adding in the final dictionary
        else:
            continue    #else skip the loop
for i in final_dict:    #printing the final dictionary 
    print(i +"'s","=", final_dict[i]," ", end="")
