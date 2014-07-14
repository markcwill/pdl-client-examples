PDL Client Examples
===================

Example configurations for PDL clients, stored in separate branches:

- [CAP Alert Listener](https://github.com/jmfee-usgs/pdl-client-examples/tree/cap-listener)
- [Moment Tensor Listener](https://github.com/jmfee-usgs/pdl-client-examples/tree/moment-tensor-listener)
- [EIDS Input Wedge](https://github.com/jmfee-usgs/pdl-client-examples/tree/eids-input-wedge)
- [Indexer](https://github.com/jmfee-usgs/pdl-client-examples/tree/indexer)


[Additional PDL Documentation](http://ehppdl1.cr.usgs.gov/)


lib/ProductClient was created using the following commands:

```bash
mkdir lib
cd lib
curl -O http://ehppdl1.cr.usgs.gov/ProductClient.zip
unzip ProductClient.zip
rm ProductClient.zip
chmod +x ProductClient/init.sh
```
