from decos import timeit
import io
import requests

def url_download(url):
    r = requests.get(url, allow_redirects=True)
    io.BytesIO(r.content)  # write to file simulation

def cpu_hard_function(unsorted_list):
    """
    buble sort
    """
    for i in range(len(unsorted_list)-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, len(unsorted_list)-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if unsorted_list[j] > unsorted_list[j+1] : 
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j] 
    return unsorted_list