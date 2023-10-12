def write_query(string):
    with open(r'ready_queries.txt', 'a') as output:
        output.write(f'CREATE TABLE IF NOT EXISTS {string[0]}(\n')
        for tup in string[1]:
            if tup[2] == 'PK':
                key = 'PRIMARY KEY'
            elif tup[2] == 'FK':
                key = f',\n FOREIGN KEY({tup[0]}) REFERENCES ____({tup[0]})'
            else:
                key = ''
            output.write(f'{tup[0]} {tup[1]} {key},\n')
        output.write(');\n\n')
    pass

raw = ('snack_details', [('sale_id', 'INTEGER', 'FK'), ('snack_id', 'INTEGER', 'FK'), ('qty', 'INTEGER', '')])

write_query(raw)

'''
with open(r'ready_tables.csv') as file:
    data = file.readlines()
    for line in data:
        write_query(line)
'''