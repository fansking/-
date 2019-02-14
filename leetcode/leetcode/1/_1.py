class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    return [i,j]

 
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinWei=0
        l3=ListNode(0)
        while l1!=None and l2!=None:
            num1=l1.val
            num2=l2.val
            l1=l1.next
            l2=l2.next
            sum=num1+num2+jinWei
            if sum>=10:
                sum=sum-10
                l3.next=ListNode(sum)
                if "output" not in locals().keys():
                    output=l3.next
                l3=l3.next
                jinWei=1
            else:
                l3.next=ListNode(sum)
                if "output" not in locals().keys():
                    output=l3.next
                l3=l3.next
                jinWei=0
        if l1!=None:
            while l1!=None:
                sum=l1.val+jinWei
                l1=l1.next
                if sum>=10:
                    sum=sum-10
                    l3.next=ListNode(sum)
                    l3=l3.next
                    jinWei=1
                else:
                    l3.next=ListNode(sum)
                    l3=l3.next
                    l3.next=l1
                    jinWei=0
                    break
        else:
            while l2!=None:
                sum=l2.val+jinWei
                l2=l2.next
                if sum>=10:
                    sum=sum-10
                    l3.next=ListNode(sum)
                    l3=l3.next
                    jinWei=1
                else:
                    l3.next=ListNode(sum)
                    l3=l3.next
                    l3.next=l2
                    jinWei=0
                    break
        if jinWei==1:
            l3.next=ListNode(1)
        return output
 
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        length=0
        if len(s)!=0:
            max=1
        else:
            max=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in d.keys():
                    length=length+1
                    d[s[j]]=1
                elif s[j] in d.keys():
                    if length>max:
                         max=length
                    else:
                       max=max
                    length=0
                    d={}
                    break

        return max

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i=i+1
            else:
                nums3.append(nums2[j])
                j=j+1
        if i<len(nums1):
            for k in range(i,len(nums1)):
                nums3.append(nums1[k])
        else:
            for k in range(j,len(nums2)):
                nums3.append(nums2[k])
        if len(nums3)%2==0:
            return float(nums3[int(len(nums3)/2)-1]+nums3[int(len(nums3)/2)])/2
        else:
            return float(nums3[int(len(nums3)/2)])
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s,left,right):
            L=left
            R=right
            while L>=0 and R<len(s) and s[L]==s[R]:
                L-=1
                R+=1
            return R-L-1
        if len(s)==0 or s==None:
            return ""
        start=0
        end=0
        for i in range(len(s)):
            len1=expand(s,i,i)
            len2=expand(s,i,i+1)
            if len1>len2:
                length=len1
            else:
                length=len2
            if length>end-start:
                start=i-int((length-1)/2)
                end=i+int(length/2)
        return s[start:end+1]
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        s=str(x)
        num=0
        if s[0]=="-":
            for i in range(1,len(s)):
               num+=int(s[i])* math.pow(10,i-1)
            num=-1*num
        elif s[0]=="+":
            for i in range(1,len(s)):
               num+=int(s[i])* math.pow(10,i-1)
        elif s[0].isdigit():
            for i in range(0,len(s)):
               num+=int(s[i])* math.pow(10,i)
        else:
            return 0
        if num>math.pow(2,31)-1:
            return 0
        elif num<-math.pow(2,31):
            return 0
        else:
            return int(num)       


    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import math
        num=0
        str=str.lstrip()
        if len(str)==0:
            return 0
        if str[0]=="+" or str[0]=="-":
            i=1
            while i<len(str) and str[i].isdigit():
                i=i+1
            for j in range(1,i):
                num+=int(str[j])*math.pow(10,i-j-1)
            if str[0]=="-":
                num=-1*num
        elif str[0].isdigit():
            i=0
            while i<len(str) and str[i].isdigit():
                i=i+1
            for j in range(0,i):
                num+=int(str[j])*math.pow(10,i-j-1)
        else:
            return 0
        if num>math.pow(2,31)-1:
            return int(math.pow(2,31)-1)
        elif num<-math.pow(2,31):
            return -int(math.pow(2,31))
        else:
            return int(num)
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #不转为字符串解决
        import math
        if x<0:
            return False
        elif x<10:
            return True
        else:
            length=int(math.log10(x))+1
            flag=True
            if length%2==0:
                for i in range(int(length/2)):
                    if int(x/math.pow(10,i))%10!=int(x/math.pow(10,length-i-1))%10:
                        flag=False
            else:
                for i in range(int(length/2)):
                    if int(x/math.pow(10,i))%10!=int(x/math.pow(10,length-i-1))%10:
                        flag=False
        return flag

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def min(x,y):
            if x<y:
                return x
            else:
                return y
        def max(x,y):
            if x>y:
                return x
            else:
                return y
        start=0
        end=len(height)-1
        Area=0
        length=end-start
        while start<=end:
            Area=max(Area,length*min(height[start],height[end]))
            length-=1
            if height[start]>height[end]:
                end-=1
            else:
                start+=1
        return Area

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        result=""
        if len(strs)==0:

            return ""
        while True:
            for k in range(len(strs)):
                if i>=len(strs[k]) or strs[k][i]!=strs[0][i]:
                    return result
            result+=strs[0][i]
            i+=1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res =None
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if res==None or abs(s-target)<abs(res-target):
                        res=s

                    if s>target:
                        r -=1
                    elif s==target:
                        return s
                    else :
                        l +=1
        return res

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        stack=[]
        i=0
        while i<len(s):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            if s[i]==")" or s[i]=="}" or s[i]=="]":
                if len(stack)!=0:
                    if (s[i]==")" and stack.pop()!="(") or (s[i]=="}" and stack.pop()!="{") or (s[i]=="]" and stack.pop()!="["):
                        return False
                else:
                    return False
            i+=1
        if len(stack)==0:
            return True
        else:
            return False
s=Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))