
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    result = customers[
        ~customers['id'].isin(orders['customerId'])
    ]

    result = result[['name']].rename(
        columns={'name': 'Customers'}
    )

    return result


# Input data
customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders = pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})


# Function call
output = find_customers(customers, orders)

# Display output
print(output)
