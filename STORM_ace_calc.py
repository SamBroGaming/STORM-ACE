y = 0
with open(F"STORM_DATA_TRACK.txt", "r") as f:
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)-1):
            if i % 2:
                row = data[i].split(',')
                x = ((round(round((float(row[8]) * 2.215 / 5) * 5 * 0.868976) / 5) * 5) ** 2) / 10000
                y += x

print(y)