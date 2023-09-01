# Delete Duplicate Emails

# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

# For Pandas users, please note that you are supposed to modify Person in place.

# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

# The result format is in the following example.

# Example 1:

# Input: 
# Person table:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Output: 
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+
# Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform('min')
    removed_person = person[person['id'] != min_id] 
    person.drop(removed_person.index, inplace=True)
    return