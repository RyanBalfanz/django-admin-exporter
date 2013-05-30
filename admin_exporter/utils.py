import csv
import json
from contextlib import closing

try:
	import cStringIO as StringIO
except ImportError:
	import StringIO


def json_to_csv(jsonData, fieldnames=None):
	"""
	Returns a CSV string from the given JSON data string.
	"""
	d = json.loads(jsonData)
	fieldnames = fieldnames or d[0].keys()
	return dict_to_csv(d, fieldnames)

def dict_to_csv(d, fieldnames):
	"""
	Returns a CSV string from the given dictionary.

	This assumes that each dictionary is simple and each contains the same keys.
	"""
	buf = None
	with closing(StringIO.StringIO()) as f:
		dictWriter = csv.DictWriter(f, fieldnames)
		dictWriter.writeheader()
		dictWriter.writerows(d)

		buf = f.getvalue()

	return buf


if __name__ == "__main__":
	data = [
		{"col2": "foo", "col1": "foo"},
		{"col2": "bar", "col1": "bar"},
		{"col2": "baz", "col1": "baz"},
	]

	jsonString = json.dumps(data)
	print json_to_csv(json.dumps(data), data[0].keys())
