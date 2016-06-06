#! /usr/bin/env python


import os
import sys
import datetime

# add ProductClient directory to path
sys.path.append(os.path.join('lib', 'ProductClient'))

# import IndexerAction, which parses ExternalIndexerListener arguments
from ExampleListener import IndexerAction



if __name__ == '__main__':
	# write data to a log file
	logfile = os.path.join('data', os.path.basename(sys.argv[0]) + '.log')
	f = open(logfile, 'ab+')
	# current time
	f.write('# ' + datetime.datetime.now().isoformat() + '\n');
	# command line arguments
	f.write('# arguments = ' + ' '.join(sys.argv) + '\n');
	# parse command line arguments
	action = IndexerAction.getIndexerAction()
	# output parsed action
	f.write('action=' + action.action + '\n')
	# output associated product
	product = action.product
	product.display(f)
	props = product.properties
	# check if moment tensor is Mww
	if product['type'] == 'moment-tensor':
		f.write('moment-tensor, ')
		if 'derived-magnitude-type' in props and props['derived-magnitude-type'] == 'Mww':
			f.write('wphase\n')
		else:
			f.write('not wphase\n')
	# add a blank line
	f.write('\n')

