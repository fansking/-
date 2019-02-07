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

s=Solution()
print(s.myAtoi("4193 with words"))