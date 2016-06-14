PDL Client Examples
===================

Example configurations for PDL clients, stored in separate branches. This branch, `redisindex`, pushes new indexer updates to Redis

[Additional PDL Documentation](http://ehppdl1.cr.usgs.gov/)

Indexer Listener Example
==============================

Run a python ExternalIndexerListener configured to process indexer changes. Respond to each change by creating a JSON product consisting of product and property attributes and push it to a Redis PUBSUB channel


Getting Started
---------------

- Run `./init.sh start`

- Subscribe to Redis PUBSUB channel `pdlindex` and watch the JSON products roll in...

