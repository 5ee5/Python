import csv

file_path = "/home/minka69btw/Code/Python/school_data/vps_ce_rezultati_vsk_2022_2023.csv"

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter = ";")
    
    sum = 0
    count = 0

    subjects = []
    sums = []
    counts = []

    for row in csv_reader:
        try:
            sum += int(row[9])
            count += 1

            if row[1] not in subjects:
                subjects.append(row[1])
                sums.append(0)
                counts.append(0)


            index = subjects.index(row[1])
            sums[index] += int(row[9])
            counts[index] += 1

        except:
            continue

print(sum / count)

for i in range(0, len(subjects)):
    print(f"{subjects[i]} {sums[i]/counts[i]}")