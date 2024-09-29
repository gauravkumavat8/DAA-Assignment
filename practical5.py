def find_content_children(g, s):
    # Sort the greed factors and the cookie sizes
    g.sort()
    s.sort()
    
    child_i = 0  # Pointer for children
    cookie_j = 0  # Pointer for cookies
    
    # Iterate until we either run out of children or cookies
    while child_i < len(g) and cookie_j < len(s):
        # If the cookie can satisfy the current child's greed
        if s[cookie_j] >= g[child_i]:
            child_i += 1  # Move to the next child
        # Always move to the next cookie, whether it was used or not
        cookie_j += 1
    
    # The number of satisfied children
    return child_i

# Example usage:
g = [1, 2, 3]  # Greed factors of children
s = [1, 1]     # Sizes of cookies

print(f"Number of satisfied children: {find_content_children(g, s)}")
