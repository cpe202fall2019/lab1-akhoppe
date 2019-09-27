
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list == None:
      raise ValueError('list is None')
   elif len(int_list) == 0:
      return None
   else:
      max = 0
      for val in int_list:
         if val > max:
            max = val
      return max


def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError('list is none')
   elif (len(int_list) == 0 or len(int_list) == 1):
      return int_list
   else:
      return int_list[-1:] + reverse_rec(int_list[:-1])
      

def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError('list is none')
   elif high >= low:
      middle = int(low + (high-low)/2)
      if int_list[middle] == target:
         return middle
      elif int_list[middle] > target:
         return bin_search(target, low, middle-1, int_list)
      else:
         return bin_search(target, middle+1, high, int_list)
   else:
      return None   
         

