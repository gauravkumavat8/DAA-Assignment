def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    
    # Create a DP table with dimensions (m+1) x (n+1) initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # If the characters match, increment the LCS length
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Otherwise, take the maximum value from the previous rows or columns
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The value at dp[m][n] will be the length of the LCS
    return dp[m][n]

# Example usage:
text1 = "abcde"
text2 = "ace"
print(f"Length of LCS: {longest_common_subsequence(text1, text2)}")  # Output: 3
