class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Step 1 : Initialization
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(idx , currStr):
            # Step 2 : base condition , if idx reaches last value that means all digits index have been exhausted.
            if idx == len(digits):
                res.append(currStr)
                return

            #Step 3 : Each call appends one character to the currStr
            for c in digitToChar[digits[idx]]:
                backtracking(idx + 1 , currStr + c)

        if digits:
            backtracking(0, "")
        return res
        


    '''
    backtracking(0, "")
├── c='a' → backtracking(1, "a")
│   ├── c='d' → backtracking(2, "ad") → len==2 ✓ append "ad"
│   ├── c='e' → backtracking(2, "ae") → len==2 ✓ append "ae"
│   └── c='f' → backtracking(2, "af") → len==2 ✓ append "af"
├── c='b' → backtracking(1, "b")
│   ├── c='d' → backtracking(2, "bd") → len==2 ✓ append "bd"
│   ├── c='e' → backtracking(2, "be") → len==2 ✓ append "be"
│   └── c='f' → backtracking(2, "bf") → len==2 ✓ append "bf"
└── c='c' → backtracking(1, "c")
    ├── c='d' → backtracking(2, "cd") → len==2 ✓ append "cd"
    ├── c='e' → backtracking(2, "ce") → len==2 ✓ append "ce"
    └── c='f' → backtracking(2, "cf") → len==2 ✓ append "cf"

res = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''