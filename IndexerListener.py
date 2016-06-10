#! /usr/bin/env python
"""
RedisIndexer - Simple PDL Indexer for Redis

- Mark Williams, Nevada Seismological Laboratory
- University of Nevada, Reno (2016)

This takes PDL products as processed by the example Listener classes and
publishes them to a Redis PUBSUB channel (called 'pdlindex')

Becuase it's a hook script, called from PDL, no easy way to pass in flags,
could either 1) use config file in /etc, ./, et cetera, or 2) use environment 
vars to set things like redisURL, error log, channel name.

TODO
----
1) Set up generic messaging functionality for easy porting to GCP
2) Maybe refactor ExampleListener classes, but they work well for now

"""
import os
import sys
import datetime
import json
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', filename='/tmp/fido.log',level=logging.DEBUG)
logging.debug("Starting up...") # TODO: remove

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
            'action': action.action,
            'code': product.code,
            'properties': props,
            'source': product.source,
            'status': product.status,
            'updateTime': product.updateTime.isoformat(),
        }
        RC = redis.from_url('redis://localhost/1')
        RC.publish(PDL_INDEX_CHANNEL, json.dumps(msg))
    except Exception as e:
        logging.exception(e)
    finally:
        sys.exit(0)

