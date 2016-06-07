#! /usr/bin/env python

import os
import sys
import datetime
import json
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', filename='/tmp/fido.log',level=logging.DEBUG)
logging.debug("Starting up...")

import redis

# add ProductClient directory to path
sys.path.append(os.path.join('lib', 'ProductClient'))

# import IndexerAction, which parses ExternalIndexerListener arguments
from ExampleListener import IndexerAction


if __name__ == '__main__':
    try:
        PDL_INDEX_CHANNEL = 'pdlindex'
        dt = datetime.datetime.now().isoformat()  
        # parse command line arguments
        action = IndexerAction.getIndexerAction()
        # output associated product
        product = action.product
        props = product.properties
        # redis
        logging.debug("Got message {0}, {1}".format(dt, product.code))
        msg = {
            'action': product.action,
            'code': product.code,
            'properties': props,
            'source': product.source,
            'status': product.status,
            'updateTime': product.updateTime,
        }
        RC = redis.from_url('redis://localhost/1')
        RC.publish(PDL_INDEX_CHANNEL, json.dumps(msg))
    except Exception as e:
        logging.exception(e)
    finally:
        sys.exit(0)

