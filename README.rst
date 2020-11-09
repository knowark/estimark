Estimark
########

Frictionless estimation.

Installation
============

.. sourcecode::

    pip install estimark

Usage
=====

Inside a requirements directory containing *.rst* files marked with
*estimark* estimation fields, run the **init** command to populate the
population parameters. Then you'll be ready to issue the **estimate** command
to compute the requirements estimation.

.. sourcecode::

    estimark init
    estimark estimate

Plot
----

To plot the estimation results, just run the plot command.

.. sourcecode::

    estimark plot
