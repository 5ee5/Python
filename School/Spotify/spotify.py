import csv

file_path = "/home/minka69btw/Code/Python/spotify/spotify.csv"

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)     
    for row in csv_reader:
        print(f"{row[0]} - {row[1]}")

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)     
    
    total_duration = 0
    track_count = 0
    for row in csv_reader:
        try:
            total_duration += int(row[4])
            track_count += 1
        except:
            continue
    
    print(f"Average song duration is: {(total_duration / track_count) / 1000} s")