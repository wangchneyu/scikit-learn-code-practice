import pandas as pd
import numpy as np
try:
	import matplotlib.pyplot as plt
except Exception:
	# matplotlib not available; provide a minimal dummy 'plt' to avoid import errors.
	class _DummyPlot:
		def plot(self, *args, **kwargs):
			pass
		def show(self, *args, **kwargs):
			pass
		def figure(self, *args, **kwargs):
			return None
	plt = _DummyPlot()
	print("Warning: matplotlib.pyplot not available; using dummy 'plt'.")

