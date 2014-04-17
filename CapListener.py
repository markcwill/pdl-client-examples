#! /usr/bin/env python


import os
import sys
import datetime

# add ProductClient directory to path
sys.path.append(os.path.join('lib', 'ProductClient'))

# import Product, which parses ExternalNotificationListener arguments
from ExampleListener import Product



if __name__ == '__main__':
	# write data to a log file
	logfile = os.path.join('data', os.path.basename(sys.argv[0]) + '.log')
	f = open(logfile, 'ab+')
	# current time
	f.write('# ' + datetime.datetime.now().isoformat() + '\n');
	# command line arguments
	f.write('# arguments = ' + ' '.join(sys.argv))
	# parse command line arguments
	product = Product.getProduct()
	# output parsed product
	product.display(f)
	# add a blank line
	f.write('\n')

