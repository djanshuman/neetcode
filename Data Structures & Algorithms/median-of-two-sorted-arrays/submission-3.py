class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. INITIALIZE TO A AND B
        A , B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # 2. VALIDATE LENGTH AND SWAP TO KEEP AS MIN , WE WILL PEFORM BINARY SEARCH ON SMALLER ARRAY
        if len(B) < len(A):
            A , B = B, A

        # 3. FIX THE POINTERS
        l , r = 0, len(A)

        #4 RUN BINARY SEARCH AND FIND THE PARTITION SIDE
        while l <= r:

            i = ( l + r) // 2 - 1 # -1 to include the -1 to m-1 range, where m is len(A) . This will enable to contribute nothing from A
            j = half - i - 2 # -2 to exclude 1 off from both A and B as index starts from 0

            aleft = A[i] if i >= 0 else float("-inf")
            aright = A[i + 1] if i < len(A) - 1 else float("inf")
            bleft = B[j] if j >= 0 else float("-inf")
            bright = B[j + 1] if j < len(B) - 1 else float("inf")

            if aleft <= bright and bleft <= aright:
                #ODD ELEMENTS
                if total % 2 == 1:
                    return min(aright, bright)
                #EVEN ELEMENTS
                else:
                    return (max(aleft,bleft) + min(aright,bright)) / 2.0

            elif aleft > bright:
                r = i
            else:
                l = i + 2
        
        