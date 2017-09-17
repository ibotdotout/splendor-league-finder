Splendor League Finder
==============================

# Example
- There are 16 player A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P
- 4 Player / games
- 5 Match for each player to face everyone and only once

P.S. edit your config in `league-finder.py`

# Run - last set of output is result

```
$ ./run.sh
	return seq[int(self.random() * len(seq))]  # raises IndexError if seq is empty
IndexError: list index out of range
4
(16, 'ABCDEFGHIJKLMNOP')
['BPFC', 'NDIO', 'LHGA', 'MJKE']
['EFGI', 'MNPA', 'BJDL', 'KHOC']
['HDPE', 'AJCI', 'FMOL', 'GBNK']
['PIKL', 'JHFN', 'GMCD', 'OEAB']
['ENLC', 'PJGO', 'FDKA', 'MBIH']
```

# How to solve
- using Numerical Method Technique(actully it random player each match until no error occur)
