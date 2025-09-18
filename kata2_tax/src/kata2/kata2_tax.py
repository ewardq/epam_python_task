"""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
How much will you spend?
Given a dictionary of items and their costs and an array specifying the items bought,
calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.

Python:
costs = {'socks':5, 'shoes':60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 = 65
#-> 65 + 0.09 of 65 = 70.85
#-> Output: 70.85
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""
def get_total(costs_dict, items_list, tax):
    total_cost = 0

    # Add item's cost. Ignore if not found
    for item in items_list:
        added_cost = costs_dict.get(item)
        # If item exists, add it to total sum
        if added_cost:
            total_cost += added_cost

    # Apply tax. If tax is negative, set tax to zero
    if tax < 0:
        tax = 0
    total_cost += total_cost*tax

    rounded_total_cost = round(total_cost, 2)
    print(rounded_total_cost)
    return rounded_total_cost

if __name__ == "__main__":
    costs = {'socks':5, 'shoes':60, 'sweater':30}
    get_total(costs, ['socks', 'shoes'], 0.09)