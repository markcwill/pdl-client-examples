EIDS Input Wedge Example
========================

Run the EIDSInputWedge in polling mode, to send quakeml formatted messages to EHP development systems.


Getting started
---------------

- [Create a DSA SSH keypair](http://ehppdl1.cr.usgs.gov/userguide/sending.html#keypair) named id_dsa in the root directory of this project, or update privateKeyFile configuration in config.ini.

- Ensure firewalls are open to configured senders.  Email (jmfee at usgs dot gov) for more information.

- Create [ANSS Quakeml Standards](https://github.com/usgs/quakeml) compliant messages, and place them in data/polldir to send
