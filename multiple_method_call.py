"""
down vote
favorite
So recently I was working with matplotlib here is my code
"""

import matplotlib.pyplot as plt 
from collections import OrderedDict


def call_these_funcs_with_args(mod,ordered_funcs_and_args):
	"""
	calls the functions provided as keys with the values provided as arguments
	for the module provided
	"""

	for attr,args in attrs_and_args.iteritems():
		if attr in dir(mod):
			args = attrs_and_args[attr]
			if isinstance(args,list):
				getattr(mod,attr)(*args)
			elif args:
				getattr(mod,attr)(args)
			else:
				getattr(mod,attr)()
			if "{}_kwargs".format(attr) in attrs_and_args.keys() and isinstance(args,list):
				kwargs = attrs_and_args["{}_kwargs".format(attr)]
				getattr(mod,attr)(*args,**kwargs)


attrs_and_args = OrderedDict(
				 {'plot':[[1,2,3],[2,4,6]],
				  'plot_kwargs': {'label':'line'},
				  'xlabel':"x",
				  'ylabel':"y",
				  'title':"Interesting Graph",
				  'legend':None}
				  )


call_these_funcs_with_args(plt,attrs_and_args)
plt.show()
