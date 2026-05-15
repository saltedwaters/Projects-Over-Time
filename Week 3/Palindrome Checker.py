class Solution(object):
    def isPalindrome(self, x):
        digits = []
        if x < 0:
            return False
        x = str(x)
        for nums in x:
            digits.append(nums)
            mid = len(digits) // 2
        for i in range(mid):
            if digits[i] != digits[-(i + 1)]:
                return False
        return True

s = Solution()
print("--------PALINDROME CHECKER--------")
pain = True
while pain:
    try:
        num = input("Enter a number: ")
        if num.upper() == "Q":
            pain = False
        num = int(num)
        print(s.isPalindrome(num))
    except Exception:
        print("Input a valid number!")


