fname = input("enter file name: ")
extsn=((fname.split("."))[1]) #seperating extension after dot
extsn_dict={"py":"Python","js":"Java","Doc":"Word","xlsx":"Excel","html":"HTML"} #storing extension as dictionary
print("your file format is:",extsn_dict[extsn])

