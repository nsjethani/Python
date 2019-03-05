tc = 0
def mergeSort(alist):
   global tc
   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)
       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           l = len(lefthalf)
           if lefthalf[i] <= righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
               tc += (l-i)
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
alist = [1,3,5,2,4,6]
alist = [2,2,2,2,2,2]
mergeSort(alist)
print(alist)
print(tc)