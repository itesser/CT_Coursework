def make_table(arr):
    header = arr.pop(0)
    cols = []
    while len(arr) > 0:
        cols.append((arr[1], arr[2], arr[0]))
        arr = arr[3:]
    return header, cols
'''
CREATE TABLE IF NOT EXISTS customers(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    address VARCHAR(150),
    billing_invo VARCHAR(100)
);
'''
raw = [
'snack_details','FK','sale_id','INTEGER','FK','snack_id','INTEGER','','qty','INTEGER'
]
print(make_table(raw))