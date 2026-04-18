def findKthElement(nums1, nums2, k):
    # 1. INITIALIZE
    A, B = nums1, nums2

    # 2. SWAP TO KEEP A AS SMALLER ARRAY — BINARY SEARCH ON SMALLER
    if len(B) < len(A):
        A, B = B, A

    # 3. SETUP
    half = k - 1             # left side holds k-1 elements
    l, r = 0, len(A)         # r=len(A) allows i to reach -1

    # 4. BINARY SEARCH ON PARTITION
    while l <= r:
        i = (l + r) // 2 - 1  # i range: -1 to m-1
        j = half - i - 2       # -2 accounts for 0-indexing on both i and j

        aleft  = A[i]     if i >= 0          else float("-inf")
        aright = A[i + 1] if i < len(A) - 1  else float("inf")
        bleft  = B[j]     if j >= 0          else float("-inf")
        bright = B[j + 1] if j < len(B) - 1  else float("inf")

        # 5. VALID PARTITION — k-th sits at start of right side
        if aleft <= bright and bleft <= aright:
            return min(aright, bright)

        # 6. TOOK TOO MANY FROM A — SHRINK LEFT
        elif aleft > bright:
            r = i

        # 7. TOOK TOO FEW FROM A — GROW LEFT
        else:
            l = i + 2
