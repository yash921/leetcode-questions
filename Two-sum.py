    class Solution:
    
    
##################################################################
    
     def twoSum(self,array,target):
         """
         Time O(n^2) and Space O(1)
         """
         for i in  range(len(array)-1):
             first_Number = array[i]
             for j in range(i+1,len(array)):
                 second_Number = array[j]
                 if first_Number + second_Number == target:
                     return [i,j]
         return []
    
    
    
##################################################################
     
     
      def twoSum(self,array,target):
         """
         Time O(n) and Space O(n)
         Using hashing{List}
         
         """
         nums=[]
         for num in range(len(array)):
             potentialSum = target - array[num]
             if potentialSum in nums:
                 return [array.index(potentialSum),num]
             else:
                 nums.append(array[num])
         return []
     
     
 #################################################################

    
     def twoSum(self,array,target):
         """
         Time O(n) and Space O(n)
         Using hashing{Dict}
         """
         nums={}
         for i in range(len(array)):
             num = array[i]
             potentialSum = target - num
             if num in nums:
                 return [nums[num],i]
             else:
                 nums[potentialSum]=i
        return []


###################################################################




