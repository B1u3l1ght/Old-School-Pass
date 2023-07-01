if __name__=='__main__':
	import sys
	with open(sys.argv[1],'r') as _:
		lines = _.readlines()

	for line in lines:
		#remove lead/trail whitespace; split on whitespace and rejoin without
		line = "".join(line.strip().split())
		counts = {}
		for c in line:
			counts.setdefault(c,0)
			counts[c] += 1
		print(' '.join((str(_) for _ in reversed(sorted(counts.values())))))