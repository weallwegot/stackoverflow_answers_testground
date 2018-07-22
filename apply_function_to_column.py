import pandas as pd

df = pd.DataFrame({'A':['32435','45243','123']})

def stripstring(s):
	# put in try except in case string is short
	try:
		return s[:2] + s[4:]
	except IndexError:
		return s

df['A'] = df.apply(lambda row: stripstring(row['A']), axis=1)

print(df)