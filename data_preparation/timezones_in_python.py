import json
from collections import defaultdict


def count_occurrences(sequence):
    counts = defaultdict(int)
    for item in sequence:
        counts[item] += 1
    return counts

# import json data
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

# timezone is "tz" where applicable
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
tz_set = set(time_zones)
counts = count_occurrences(time_zones)
for tz in tz_set:
    print(':'.join([tz, str(counts[tz])]))

