def lemonade_change(bills):
    # Variables to keep track of $5 and $10 bills
    five = 0
    ten = 0
    
    for bill in bills:
        if bill == 5:
            five += 1  # No change needed, just collect the $5 bill
        elif bill == 10:
            if five == 0:
                return False  # No $5 bill to give as change
            five -= 1  # Give one $5 bill as change
            ten += 1  # Collect the $10 bill
        elif bill == 20:
            # Prefer to give one $10 and one $5 as change
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                # If no $10 bill, give three $5 bills as change
                five -= 3
            else:
                return False  # Cannot give change
            
    return True

# Example usage:
bills = [5, 5, 5, 10, 20]
print(f"Can give correct change: {lemonade_change(bills)}")  # Output: True
