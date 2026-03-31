class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        right_product = [1]
        left_product = [1] 

        for num in nums[:-1]:
            product *= num
            right_product.append(product) 

        product = 1
        for num in nums[:0:-1]:
            product *= num
            left_product.insert(0, product)

        for i in range(len(nums)):
            result.append(right_product[i] * left_product[i])

        print(">>> left", left_product)
        print(">>> right", right_product)

        return result
    