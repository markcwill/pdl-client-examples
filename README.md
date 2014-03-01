EIDS Input Wedge Example
========================

Run the EIDSInputWedge in polling mode, to send quakeml formatted messages to EHP development systems.


Getting started
---------------

- Create (or configure) ssh keypair in config.ini, by default privateKeyFile = id_dsa .

[Creating a keypair](http://ehppdl1.cr.usgs.gov/userguide/sending.html#keypair)


- Ensure firewalls are open to configured senders.

Email (jmfee at usgs dot gov) for more information.


- Create ANSS compliant Quakeml messages, and place them in data/polldir to send

[ANSS Quakeml Standards](https://github.com/usgs/quakeml)
