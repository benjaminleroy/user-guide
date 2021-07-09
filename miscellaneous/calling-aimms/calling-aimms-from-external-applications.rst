.. _sec:calling.aimms:

Calling AIMMS from External Applications
----------------------------------------

.. rubric:: Use AIMMS as a component

In addition to starting the AIMMS program itself, you can also link
AIMMS, as a component, to your own application. Using AIMMS as a
component has the advantage that, from within your program, you can
easily access data with AIMMS and run procedures in the associated AIMMS
project. Thus, for instance, when your program requires optimization,
and you do not want to bother writing the interface to a linear or
nonlinear solver yourself, you can

-  specify the optimization model algebraically in AIMMS,

-  feed it with data from your application, and

-  retrieve the solution after the model has been solved successfully.

.. rubric:: Several options

When linking AIMMS as a component to your own application, you have
several options:

-  link through a REST API using :doc:`dataexchange/index` and :doc:`httpclient/index`

-  link directly against the AIMMS API (see :ref:`lr:chap:api` of the
   Language Reference).

.. rubric:: Programming required

Through the AIMMS component technologies described above you have
varying degrees of control over the data inside your model. Use of these
technologies requires, however, that you set up the interface to your
model in a programming language such as ``C``, ``C++``, ``Java`` or ``.NET``. While
the control offered by these technologies may be relevant for advanced
or real-time applications where efficiency in data communication is of
the utmost importance, these technologies come with a certain learning
curve, and if you only want to perform simple tasks such as
communicating data in a blockwise manner and running procedures inside
the model, you might consider setting up the communication using either
text data files or databases.

.. rubric:: Using the AIMMS API

Please note that using the AIMMS API to start up a new AIMMS session
from within an external application that also performs other significant
tasks than starting up that AIMMS session, is *not recommended*. Opening
an AIMMS project from within another application may, especially under
Windows, lead to unwanted interactions between the AIMMS and the
original application. The AIMMS API is also not particularly suited to
start up an AIMMS session from within the same process multiple times.
In such cases we advise to use a technology that starts up an AIMMS
session in a separate process.