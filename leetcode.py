# 1480 一维数组的动态和
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         L = []
#         num = 0
#         for i in range(len(nums)):
#             num = num + nums[i]
#             L.append(num)
#         print(L)
#
#
# solution = Solution()
# solution.runningSum([1, 2, 3, 4])

# 1512 好数对的数目
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     n = n + 1
#         print(n)
#
#
# solution = Solution()
# solution.numIdenticalPairs([1,2,3])

# 1431 拥有最多糖果的孩子
# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         """
#         :type candies: List[int]
#         :type extraCandies: int
#         :rtype: List[bool]
#         """
#         maxCandies = max(candies)
#         ret = [candy+extraCandies >= maxCandies for candy in candies]
#         print(ret)
#
#
# solution = Solution()
# solution.kidsWithCandies([2,3,5,1,3],3)


# 1470 重新排列数组
# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         j = 1
#         for i in range(1, len(nums)//2):
#             nums.insert(j, nums[n])
#             nums.pop(n+1)
#             j = j+2
#             n = n+1
#         print(nums)
#
#
# solution = Solution()
# solution.shuffle([1,1,2,2],2)


# 剑指 Offer 58 - II. 左旋转字符串
# class Solution(object):
#     def reverseLeftWords(self, s, n):
#         """
#         :type s: str
#         :type n: int
#         :rtype: str
#         """
#         ret = s[n:] + s[:n]
#         print(ret)
#
#
# solution = Solution()
# solution.reverseLeftWords("lrloseumgh", 6)

# 面试题 02.03. 删除中间节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         node.val = node.next.val
#         node.next = node.next.next

# LCP 01. 猜数字
# class Solution(object):
#     def game(self, guess, answer):
#         """
#         :type guess: List[int]
#         :type answer: List[int]
#         :rtype: int
#         """
#         count = 0
#         for i in range(3):
#             if guess[i] == answer[i]:
#                 count = count+1
#         return count

# 771. 宝石与石头
# class Solution(object):
#     def numJewelsInStones(self, J, S):
#         """
#         :type J: str
#         :type S: str
#         :rtype: int
#         """
#         j = list(J)
#         count = 0
#         for s in S:
#             if s in j:
#                 count = count + 1
#         print(count)
#
#
# solution = Solution()
# solution.numJewelsInStones("z", "ZZ")

# 1108. IP 地址无效化
# class Solution(object):
#     def defangIPaddr(self, address):
#         """
#         :type address: str
#         :rtype: str
#         """
#         ret = address.replace('.', '[.]')
#         print(ret)
#
# solution = Solution()
# solution.defangIPaddr('1.1.1.1')

# LCP 06. 拿硬币
# class Solution(object):
#     def minCount(self, coins):
#         """
#         :type coins: List[int]
#         :rtype: int
#         """
#         count = 0
#         for coin in coins:
#             if not coin % 2:
#                 count = count + coin//2
#             else:
#                 count = count + coin//2 + 1
#         print(count)


# solution = Solution()
# solution.minCount([2, 3, 10])


#
# class Solution(object):
#     def decompressRLElist(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ret = []
#         index = 0
#         for i in range(len(nums)//2):
#             res = nums[index] * [nums[index+1]]
#             ret.extend(res)
#             index = index + 2
#         print(ret)
#
#
# solution = Solution()
# solution.decompressRLElist([1, 1, 2, 3])

# 1389. 按既定顺序创建目标数组
# class Solution(object):
#     def createTargetArray(self, nums, index):
#         """
#         :type nums: List[int]
#         :type index: List[int]
#         :rtype: List[int]
#         """
#         new_nums = []
#         for i in range(len(nums)):
#             new_nums.insert(index[i],nums[i])
#
#         return new_nums
#
#
# solution = Solution()
# solution.createTargetArray([])

# 1342. 将数字变成 0 的操作次数
# class Solution(object):
#     def numberOfSteps (self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         count = 0
#         while num:
#             if not num % 2:
#                 num = num / 2
#                 count = count + 1
#             else:
#                 num = num - 1
#                 count = count + 1
#         print(count)
#
#
# solution = Solution()
# solution.numberOfSteps(8)


# 1365. 有多少小于当前数字的数字
# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         list1 = []
#         for i in nums:
#             count = 0
#             for j in nums:
#                 if j < i:
#                     count = count+1
#             list1.append(count)
#         print(list1)
#
#
# solution = Solution()
# solution.smallerNumbersThanCurrent([8,1,2,2,3])

# 1295. 统计位数为偶数的数字
# class Solution(object):
#     def findNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         for i in nums:
#             if not len(str(i)) % 2:
#                 count = count+1
#         print(count)
#
#
# solution = Solution()
# solution.findNumbers([12,345,2,6,7896])

# class Singleton:
#     __isinstance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__isinstance:
#             cls.__isinstance = object.__new__(cls)
#         return cls.__isinstance
#
#
# a = Singleton(18, 'a')
# b = Singleton(19, 'b')
# print(id(a))
# print(id(b))

