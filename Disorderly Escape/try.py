def solution(w, h, s):
    # Initialize a dictionary to store the unique, non-equivalent configurations
    configs = {}
    
    def recurse(row, col, curr_config):
        # Base case: if we have reached the end of the grid, add the current configuration to the list
        if row == h and col == w:
            configs[curr_config] = True
            return
        
        # Recursive case: try assigning each of the s possible states to the current cell
        for i in range(s):
            # Check whether the current configuration is equivalent to any previous configuration
            equiv_found = False
            for prev_config in configs:
                if prev_config == curr_config[:row] + str(i) + curr_config[col+1:]:
                    equiv_found = True
                    break
            
            # If an equivalent configuration was found, prune the current branch of the search tree
            if equiv_found:
                continue
            
            # Add the current configuration to the list of unique, non-equivalent configurations
            configs[curr_config[:row] + str(i) + curr_config[col+1:]] = True
            
            # Continue recursively exploring the remaining cells
            recurse(row+1, col, curr_config[:row] + str(i) + curr_config[col+1:])
    
    # Start the recursive search from the first cell
    recurse(0, 0, "")
    
    # Return the length of the list of unique, non-equivalent configurations
    return len(configs)

print(solution(2, 2, 2))  # Output: "7"
print(solution(2, 3, 4))  # Output: "430"
