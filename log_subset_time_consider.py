# -*- coding: UTF-8 -*-

import itertools
from collections import Counter
import copy


	
def drop_repeated_logs(list_of_dicts):
	"""
	drop the repeated text in logs and compute a new time range
	"""
	only_logs = [d['log'] for d in list_of_dicts]
	original_range = list_of_dicts[-1]['time'] - list_of_dicts[0]['time']
	counts = Counter(only_logs)
	original_max_count = counts[max(counts,key=lambda i:counts[i])]
	original_len = len(list_of_dicts)

	print(counts)
	for log_txt in only_logs:
		num_occ = counts[log_txt]
		if num_occ > 1:
			# list of matching log subsets without repeats
			new_d = [entry for entry in list_of_dicts if entry['log']!=log_txt]
			print new_d
			# repeating log subset entries
			entries_to_try = [entry for entry in list_of_dicts if entry['log']==log_txt]
			print entries_to_try
			for repeat in entries_to_try:
				temp_d_list = copy.copy(new_d)
				temp_d_list.append(repeat)
				newly_sorted = sorted(temp_d_list, key=lambda k:k["time"])
				new_range = newly_sorted[-1]['time'] - newly_sorted[0]['time']
				print "Newly computed range of {}: {}\n".format(newly_sorted,new_range)
				new_len = len(newly_sorted)

				# we should return an updated list if the range is lower or we were able to get one repeated entry out
				if new_range < original_range :
					print("Found a smaller range, returning: {}".format(new_range))
					return (new_range,newly_sorted)
			if new_range == original_range and new_len < original_len:
				print("The range is unchanged, but got rid of a duplicate log text")
				return (new_range,newly_sorted)

	return original_range,list_of_dicts

# data example provided
b = [{"log": "abc", 'time': 0},
{'log': 'def', 'time': 1},
{'log': 'ghi', 'time': 2}
]

a = [
	{'log': 'abc', 'time': 0},
	{'log': '123', 'time': 1},
	{'log': 'def', 'time': 2},
	{'log': 'abc', 'time': 2},
	{'log': 'ghi', 'time': 3},
	{'log': 'def', 'time': 3}
]



# only get the log text from the data provided
a_logs = [d['log'] for d in a]
b_logs = [d['log'] for d in b]


# find the intersection of two lists
def intersection(a,b):
	return list(set(a)&set(b))

# the repeating logs between the a and b sets of data
logs_of_interest = intersection(a_logs,b_logs)

# find all the entry in a that match with an entry in b
matches_in_a = [entry for entry in a if entry['log'] in logs_of_interest]

# sort matched entries in order of time key
sorted_matches = sorted(matches_in_a, key=lambda k: k['time']) 
print(sorted_matches)

# find range of times (this is the parameter to minimize)
rnge = sorted_matches[-1]['time']-sorted_matches[0]['time']

sorted_logs = [d['log'] for d in sorted_matches]

log_counts = Counter(sorted_logs)
max_count = log_counts[max(log_counts,key=lambda i:log_counts[i])]
print "max count: {}".format(max_count)

# intitialize a lower range to get the while loop going
lower_range = rnge+1

while lower_range > rnge or max_count > 1:
	lower_range, sorted_matches = drop_repeated_logs(sorted_matches)
	sorted_logs = [d['log'] for d in sorted_matches]
	log_counts = Counter(sorted_logs)
	print("log counts: {}".format(log_counts))
	max_count = log_counts[max(log_counts,key=lambda i:log_counts[i])]
	print "MAX COUNT: {}".format(max_count)
	print "NEW LOWER RANGE: {}".format(lower_range)


print("FINAL ANSWER: range: {}; {}".format(lower_range,sorted_matches))







