class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string = s
        string_length = len(string)
        
        # Falso falso falso ... True
        dp = [False for _ in range(string_length + 1)]
        dp[-1] = True # caso base 
        
        # a b c 
        for string_index in range(string_length - 1, -1, -1):
            # abcd ->  
            #  bcd
            for word in wordDict: 
                string_position = string_index + len(word)
                if string_position <= string_length and string[string_index : string_position] == word:
                    dp[string_index] = dp[string_index + len(word)]
                if dp[string_index]:
                    break
        return dp[0]
                    
                

        
        