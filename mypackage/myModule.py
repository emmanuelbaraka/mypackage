def top_n(items, n):
    """ Return top n items in an array in descending order.

    Args:
        items (array): list of array like objects
        n (int): number of items to return
    
    Return:
        array: Top n items in descending order
        
    Egs:
        >>> top_n([8,6,9,4,2,5,1], 4)
        [9,8,6,5]
    """
    
    for i in range (n): # keep sorting untill we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: # if tis is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two
     
    # get the last n items           
    top_n = items[-n:]
    
    # return in descending oder
    return top_n[::-1]