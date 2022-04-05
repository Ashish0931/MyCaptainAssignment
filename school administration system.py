global ctr
ctr=0
import csv
def printer(name,Class,roll_no,dob,admission_no): #function to print the values given by the user
    print("---------------------------------------")
    print("your entered values are: ")
    print("Name: {}".format(name))
    print("Class: {}".format(Class))
    print("Roll No: {}".format(roll_no))
    print("DOB: {}".format(dob))
    print("Admission Number: {}".format(admission_no))
    print("---------------------------------------")

def checker(): #function to check and update the data
    check_=False
    
    import csv
    from csv import writer  
    with open('database.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
    
        while (check_==False):  #checker flag for the loop to continue if user wants to enter data gain
            print("Enter the details of the student:")  #taking details from the user
            name=input("Enter name: ")
            Class= input("Enter class: ")
            roll_no=input("Enter roll no: ")
            dob=input("enter date of birth ( in the following fromat : dd/mm//yyyy: ")
            admission_no= input("enter admission number: ")
            print(" the details you have entered are: ")
            printer(name,Class,roll_no,dob,admission_no)
            
            checker_2=False
            while checker_2==False: #checker flag for the loop to continue if user wants to make changes
                decider=input("Are you sure with this data? (yes/no): ")    #variable to decide if user wants to make any changes
                printer(name,Class,roll_no,dob,admission_no)    
                if decider=="yes":  #if user is sure about his data then append it in the list and update it in the file 
                    data_=[]
                    checker_2=True
                    data_.append(name)
                    data_.append(Class)
                    data_.append(roll_no)
                    data_.append(dob)
                    data_.append(admission_no)
                    writer_object.writerow(data_)  
                    continue
                elif (decider=="no"): #if user wants to make changes then ask him what to change and update that variable 
                    changer=input("which variable you want to edit? (name, class,rollno,DOB, admission number)" )
                    if changer=="name":
                        name= input("enter the correct name: ")
                        printer(name,Class,roll_no,dob,admission_no) #printing the updated values 
                    elif changer=="class":
                        Class=input("enter class: ")
                        printer(name,Class,roll_no,dob,admission_no)
                    elif changer=="rollno":
                        roll_no=input("Enter roll no: ")
                        printer(name,Class,roll_no,dob,admission_no)
                    elif changer=="DOB":
                        dob=input("please enter DOB: ")
                        printer(name,Class,roll_no,dob,admission_no)
                    elif changer=="admission number":
                        admission_no=input("please enter admission number: ")
                        printer(name,Class,roll_no,dob,admission_no)
                    else:
                        print("wrong value entered. try again!")
                else:
                    checker_2=False  #updating checker flag if user is not satisfied with his data 
            printer(name,Class,roll_no,dob,admission_no) #printing the output after final changes 
            decider=input("want to add another data? (press y to continue or another key to exit: )") #asking user if he wants to add another data
            if decider=='y':    #if he wants to then not updating the checker flag so while loop can continue
                check_=False 
            else:   #if he wants to then updating the checker flag so that loop ends. 
                check_=True
                print("Your data has been succesfully updated in the database. ")
                print("Thanks for using this! for any feedback ping me up! :) ")
                f_object.close() # Close the file object
        

checker() #calling the checker function to run the code
    





