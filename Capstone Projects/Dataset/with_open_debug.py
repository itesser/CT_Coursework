asset_list = []
with open('test_assets.csv', 'r') as file:
    data = file.readlines()
    for item in data:
        asset_list.append(item.strip())

id_to_get = randint(0,len(asset_list)-1)
picked_id = asset_list.pop(id_to_get)

with open('test_assets.csv', 'w') as file:
    write = csv.writer(file)
    for asset in asset_list:
        write.writerow(asset)

with open('assets_used.txt', 'a') as file:
    file.write(picked_id+'\n')
