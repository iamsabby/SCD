
test_list = [1, 2, 3, 2, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
 
test_list = list(set(test_list))
 
print ("The list after removing duplicates : "
        + str(test_list))