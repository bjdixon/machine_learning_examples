from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json


# import json data
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
tz_counts = frame['tz']
# replace empty values with string: 'Unknown'
tz_counts[tz_counts == ''] = 'Unknown'
tz_counts = tz_counts.value_counts()
# print timezones with number of occurrences
print(tz_counts[:20])

