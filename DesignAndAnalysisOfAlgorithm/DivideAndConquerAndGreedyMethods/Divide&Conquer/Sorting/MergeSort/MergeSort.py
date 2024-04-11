arr=[50,1,7,6,2,9,77,1,0]
def MergeSort(arr):
   if len(arr)<=1:
      return arr
   mid=len(arr)//2
   left=MergeSort(arr[:mid])
   right=MergeSort(arr[mid:])
   merged=[]
   i,j=0,0
   while len(left)>i and len(right)>j:
      if left[i]<=right[j]:
         merged.append(left[i])
         i+=1
      else:
         merged.append(right[j])
         j+=1
   while len(left)>i:
      merged.append(left[i])
      i+=1
   while len(right)>j:
      merged.append(right[j])
      j+=1
   return merged
print(MergeSort(arr))
