import numpy as np

def csv_to_mtx(path, delimiter=","):
	mtx = []
	try:
		with open(path) as file:
			for line in file.readlines():
				line = line.strip()
				if not line:  # Skip empty lines
					continue
				try:
					mtx.append([float(x) for x in line.split(delimiter)])
				except ValueError:
					raise ValueError(f"Non-numeric data encountered in line: '{line}'")
	except FileNotFoundError:
		raise FileNotFoundError(f"File not found, path tested: '{path}'")
	return np.array(mtx)
