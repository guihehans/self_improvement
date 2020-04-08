# 000 two sum  
## 思路

1. 简单遍历
    ```python
       for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               if(nums[i]+nums[j]==target):
                   return [i,j]
    ```

    内外循环， 外层循环对每个元素nums[i] ,在内层循环内寻找是否有nums[j]
    > 时间复杂度 O(n*n)
       空间复杂度 O(1)
2. 使用hashmap存储每个元素的index，
   - 第一遍遍历,存储每个元素的index到value，key是每个元素.
    
   - 第二遍遍历,对nums[i]寻找target-nums[i]是否在map内,检查其index j不能是i本身。
   若找到，则返回i，j
    > 时间复杂度 O(n+n)
    > 空间复杂度 O(n)
    ```python
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            b = target - nums[i]
            if b in d and d[b] != i:
                return [i, d[b]]
               
    ```
3. 单次遍历
    ```python
        d = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in d:
                return [d[b],i]
            d[nums[i]]=i
               
    ```
    when searching a+b=target, iterating the whole list, will ensure every
  element shall be visited once. for a valid pair(a,b),b's pair shall be visited already.
  .so in one pass iteration, store each elements values as index,indices as index into hashmap{} d
  . search current element b's pair if a in d. if in d, return []
  > 时间复杂度 O(n) 一遍遍历，one pass
  > 空间复杂度 O(n) 
    



