
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    result = views[
        views['author_id'] == views['viewer_id']
    ]

    result = result[['author_id']].drop_duplicates()

    result = result.rename(columns={'author_id': 'id'})

    result = result.sort_values(by='id')

    return result


# Sample Input
data = {
    'article_id': [1, 1, 2, 2, 4, 3, 3],
    'author_id':  [3, 3, 7, 7, 7, 4, 4],
    'viewer_id':  [5, 6, 7, 6, 1, 4, 4],
    'view_date': [
        '2019-08-01',
        '2019-08-02',
        '2019-08-01',
        '2019-08-02',
        '2019-07-22',
        '2019-07-21',
        '2019-07-21'
    ]
}

views = pd.DataFrame(data)

# Function Call
result = article_views(views)

# Print Output
print(result.to_string(index=False))
