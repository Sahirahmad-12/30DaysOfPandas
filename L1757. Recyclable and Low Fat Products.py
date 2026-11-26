
import pandas as pd

# Sample Input
data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
}

# Create DataFrame
products = pd.DataFrame(data)

# LeetCode Solution
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ]

    return result[['product_id']]


# Function Call
output = find_products(products)

# Display Output
print(output)
