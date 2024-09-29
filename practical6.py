def maximum_units(boxTypes, truckSize):
    # Sort boxTypes by number of units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    max_units = 0  # To store the maximum units we can load
    for boxes, units_per_box in boxTypes:
        if truckSize <= 0:
            break  # Stop if truck is already full
        
        # Take as many boxes as the truck can fit
        boxes_to_take = min(truckSize, boxes)
        max_units += boxes_to_take * units_per_box  # Add the units from these boxes
        truckSize -= boxes_to_take  # Reduce the remaining capacity of the truck
    
    return max_units

# Example usage:
boxTypes = [[1, 3], [2, 2], [3, 1]]  # [numberOfBoxes, numberOfUnitsPerBox]
truckSize = 4  # Truck can carry 4 boxes

print(f"Maximum units on truck: {maximum_units(boxTypes, truckSize)}")
