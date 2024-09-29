def merge(intervals):
    if not intervals:
        return []
    
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    # Initialize the first interval as the current one to compare with
    current_interval = intervals[0]
    
    for next_interval in intervals[1:]:
        # If intervals overlap, merge them
        if current_interval[1] >= next_interval[0]:
            current_interval[1] = max(current_interval[1], next_interval[1])  # Merge intervals
        else:
            # Add the non-overlapping interval to the result list
            merged_intervals.append(current_interval)
            current_interval = next_interval  # Move to the next interval
    
    # Add the last merged interval
    merged_intervals.append(current_interval)
    
    return merged_intervals

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Merged intervals: {merge(intervals)}")
