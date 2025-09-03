def calculate_income_tax(income):
    """
    Calculates income tax based on the following rules:
    - First $10,000: 0% tax
    - Next $10,000: 10% tax
    - The remaining: 20% tax

    Args:
        income (float): The total taxable income.

    Returns:
        float: The calculated income tax.
    """
    tax = 0
    if income <= 0:
        return 0

    # First $10,000
    if income <= 10000:
        tax = 0
    else:
        # Taxable income beyond the first $10,000
        remaining_income_after_first_10k = income - 10000

        # Next $10,000 (from $10,001 to $20,000)
        if remaining_income_after_first_10k <= 10000:
            tax += remaining_income_after_first_10k * 0.10
        else:
            tax += 10000 * 0.10  # Tax on the next $10,000 (10% of $10,000)

            # The remaining income (beyond $20,000)
            remaining_income_after_20k = remaining_income_after_first_10k - 10000
            tax += remaining_income_after_20k * 0.20

    return tax

# Example Usage:
income1 = 5000
income2 = 15000
income3 = 25000
income4 = 45000

print(f"Income: ${income1}, Tax: ${calculate_income_tax(income1):,.2f}")
print(f"Income: ${income2}, Tax: ${calculate_income_tax(income2):,.2f}")
print(f"Income: ${income3}, Tax: ${calculate_income_tax(income3):,.2f}")
print(f"Income: ${income4}, Tax: ${calculate_income_tax(income4):,.2f}")
