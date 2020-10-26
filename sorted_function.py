#sorted() function returns a sorted list of the specified iterable object.
#Usage You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
# You cannot sort a list that contains BOTH string values AND numeric values.
#Syntax: sorted(iterable, key=key, reverse=reverse)
    #iterable "Required". The sequence to sort, list, dictionary, tuple etc.
    #key "Optional". A Function to execute to decide the order. Default is None
    #reverse "Optional". A Boolean. False will sort ascending, True will sort descending. Default is False

#sort tuple of number =>result is a list
tuple_nbr=(10,-80,-150,0,14)
print("before: ",tuple_nbr)
list_sorted=sorted(tuple_nbr)
print("after: ",list_sorted)

#sort tuple of string
tuple_string=("zineb","khadiza","asmae","fatima","zoubida","manal")
print("before: ",tuple_string)
list_ascending=sorted(tuple_string)
print("after 'sorted asceding:'' ",list_ascending)
list_descending=sorted(tuple_string,reverse=True)
print("after 'sorted descending:'' ",list_descending)

