#! /usr/bin/env python


import os
import sys
import datetime

# add ProductClient directory to path
sys.path.append(os.path.join('lib', 'ProductClient'))

# import Product, which parses ExternalNotificationListener arguments
from ExampleListener import Product



if __name__ == '__main__':
	logfile = os.path.join('data', os.path.basename(sys.argv[0]) + '.log')
	f = open(logfile, 'ab+')

	f.write('# ' + datetime.datetime.now().isoformat() + '\n');
	f.write('# arguments = ' + ' '.join(sys.argv))
	product = Product.getProduct()
	product.display(f)
	f.write('\n')

