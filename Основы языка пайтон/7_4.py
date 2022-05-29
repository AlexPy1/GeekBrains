import os

h = 0
th = 0
tth = 0
oht = 0
# folder = os.getcwd()
folder = r'c:\users\79162\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages'
# folder = r'C:\Users\79162\Desktop\GeekBrains\Support'
for root, dirs, files in os.walk(folder):
    for file in files:
        file = os.stat(os.path.join(root, file)).st_size
        if file < 100:
            h += 1
        elif file < 1000:
            th += 1
        elif file < 10000:
            tth += 1
        elif file < 100000:
            oht += 1

res = {100: h, 1000: th, 10000: tth, 100000: oht}
print(res)