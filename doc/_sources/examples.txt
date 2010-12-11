****************************
  Examples
****************************

A basic program that uses ``python-bitcoin`` looks like this:

First, import the library and exceptions.

::

    import bitcoin
    from bitcoin.exceptions import InsufficientFunds

Then, we connect to the currently running ``bitcoin`` instance of the current user on the local machine
with one call to
:func:`~bitcoin.connect_to_local`. This returns a :class:`~bitcoin.connection.BitcoinConnection` objects:

::

    conn = bitcoin.connect_to_local()

Try to move one bitcoin from account ``testaccount`` to account ``testaccount2`` using 
:func:`~bitcoin.connection.BitcoinConnection.move`. Catch the :class:`~bitcoin.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~bitcoin.connection.BitcoinConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

