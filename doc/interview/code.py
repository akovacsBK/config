#/*******************************************************
#BlueKai have developed a new parallel systems that process users we collect in parallel. We assign users with unique integer ID that is in increasing order.  To make the system embarrassingly parallel we decide to create a function that takes a range of users to process.  You may pass into the function any arbitrary ranges.  Your job to create a function that when given the arbitrary ranges, figure out what range of users have been processed.  The input maybe contains additional spaces and each range is separated with comma (",")
#
#You may use anything in the language routines that is in any standard distributions. 
#
#implement UserRangeCompactor method.
#
# 
#
#For example. 
#
#when the input is "1-2,2-3,4-5" the output should be  1-5
#
#when the input is "1-5, 3-8" the output should be  1-8
#
#when the input is "1-5 , 9-11 , 6-7" the output should be "1-7, 9-11"
#
#State your program complexity, write a few test cases
#**********************************************************/

def UserRangeCompactor(input):
    input.replace(' ','') #removing extra spaces that might exist
    ranges=[[int(n) for n in range.split('-')] for range in input.split(',')] #parse time O(n)
    ranges.sort(key=lambda range: range[0]) #sort time O(nlogn) using ,mergesort
    import ipdb
    ipdb.set_trace()

    compacted=[ranges.pop(0)]
    while ranges:
        low = compacted.pop()
        high = ranges.pop(0)
        if low[1]>=high[0]-1:
            compacted.append([low[0],max(low[1],high[1])])
        else:
            compacted.append(low)
            compacted.append(high)
    
    #Complexity O(2n) time to go through array compacting overlapping ranges

    compacted_string=''
    for range in compacted:
        compacted_string=compacted_string+str(range[0])+'-'+str(range[1])+', '
    compacted_string=compacted_string[:-2]
    #O(n) time to format string

    #total complexity O(n+n+nlogn+2n+n) = complexity O(n(logn))
    return compacted_string

    

input="1-2,2-3,4-5"
print input,'-->',UserRangeCompactor(input)
input="1-5, 3-8"
print input,'-->',UserRangeCompactor(input)
input="1-5 , 9-11 , 6-7"
print input,'-->',UserRangeCompactor(input)
input="1-5 , 2-3, 7-8"
print input,'-->',UserRangeCompactor(input)
