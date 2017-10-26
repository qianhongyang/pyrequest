
filename = 'D:\pyrequest-master\config\\base_url.csv'
with open(filename,'r') as f:
    for i in f.readlines():
        print (i.split()[0:2])

