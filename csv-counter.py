import csv
import sys

csv.field_size_limit(sys.maxsize)

print("All counts exclude header row. One header row is assumed per file.\n")
for arg in sys.argv[1:]:
    line_count = 0
    with open(arg) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            line_count += 1
        arg_short = arg.rsplit('/', 1)[-1]
        print(f'{arg_short:50}: {line_count-1:,d}')
print("\nDone.")
