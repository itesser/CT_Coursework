def write_insert(line):
    arr = line.split(',')
    for i in range(2,len(arr)):
        try:
            float(arr[i])
        except:
            arr[i] = f"'{arr[i]}'"
    with open(r'sql_to_insert_2.txt', 'a') as output:
        output.write(f'INSERT INTO {arr[0]}\nVALUES(\n')
        for i in range(int(arr[1])-1):
            output.write(f'{arr[i+2]},\n')
        output.write(f'{arr[int(arr[1])+1]}\n')
        output.write(');\n\n')    


with open(r'data_to_add.csv') as file:
    data = file.readlines()
    for line in data:    
        write_insert(line)

