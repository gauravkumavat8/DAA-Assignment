# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to get the maximum total value in the knapsack
def fractional_knapsack(W, items):
    # Sorting items by value/weight ratio in decreasing order
    items.sort(key=lambda x: (x.value / x.weight), reverse=True)

    total_value = 0.0  # Total value in the knapsack
    for item in items:
        if W >= item.weight:
            # If we can take the whole item, we take it
            W -= item.weight
            total_value += item.value
        else:
            # If we can't take the whole item, we take the fraction
            fraction = W / item.weight
            total_value += item.value * fraction
            W = 0
            break  # Knapsack is full
    
    return total_value

# Example usage:
if __name__ == "__main__":
    # List of items (value, weight)
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    # Maximum weight of knapsack
    W = 50

    # Function call
    max_value = fractional_knapsack(W, items)
    
    print(f"Maximum value in Knapsack = {max_value}")
