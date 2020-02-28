def binarySearch(arr,val):
    if len(arr) == 0:
        return False
    
    else:
        mid = len(arr)//2
        
        if arr[mid] == val:
            return True
        else:
            if val > arr[mid]:
                return binarySearch(arr[mid+1:],val)
            else:
                return binarySearch(arr[:mid],val)


def rec_bin_search(arr,ele):
    
    # Base Case!
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        
        mid = len(arr)//2
        
        # If match found
        if arr[mid]==ele:
            return True
        
        else:
            
            # Call again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:],ele)                
            