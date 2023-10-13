def write_query(string):
    with open(r'ready_queries_th.txt', 'a') as output:
        output.write(f'CREATE TABLE IF NOT EXISTS {string[0]}(\n')
        string = string[1:]
        while len(string)>0:
            if string[0] == 'PK':
                key = ' PRIMARY KEY'
            elif string[0] == 'FK':
                key = f',\n FOREIGN KEY({string[1]}) REFERENCES ____({string[1]})'
            else:
                key = ''
            output.write(f'{string[1]} {string[2]}{key},\n')
            string = string[3:]
        output.write(');\n\n')
    pass

raw = ['car_sales','PK','invoice_id','SERIAL','FK','employee_id','INTEGER','','sale_date','DATETIME','FK','car_id','INTEGER','FK','owner_id','INTEGER']

write_query(raw)

'''
with open(r'ready_tables.csv') as file:
    data = file.readlines()
    for line in data:
        write_query(line)
'''