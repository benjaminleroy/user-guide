Creating procedures and functions
=================================

.. _creating_procedures_and_functions:

.. rubric:: Procedures and functions

Procedures and functions are the main means of executing the sequential
tasks in your model that cannot be expressed by simple functional
relationships in the form of identifier definitions. Such tasks include
importing or exporting your model's data from or to an external data
source, the execution of data assignments, and giving AIMMS instructions
to optimize a system of simultaneous equations.

.. rubric:: Creating procedures and functions

Procedures and functions are added as a special type of node to the
model tree, and must be placed in the main model, or in any book
section. They cannot be part of declaration sections, which are
exclusively used for model identifiers. Procedures and functions are
represented by folder icons, which open up when the node is expanded.
:numref:`fig:proc.proc` illustrates an example of a procedure node in
the model tree.

.. rubric:: Naming and arguments

After you have inserted a procedure or function node into the tree, you
have to enter its name. If you want to add a procedure or function with
arguments, you can add the argument list here as well. Alternatively,
you can specify the argument list in the attribute window of the
procedure or function. The full details for adding arguments and their
declaration as identifiers, local to the procedure or function, are
discussed in :ref:`sec:proc.arg`. Whether or not the arguments are fully
visible in the tree is configurable using the **View** menu.

.. figure:: proc-node-new.png
   :alt: Example of a procedure node
   :name: fig:proc.proc
   
   Example of a procedure node

.. rubric:: Example of a procedure node

The attribute window of a procedure or function lets you specify or view
aspects such as its list of arguments, the index domain of its result,
or the actual body. The body may merely consists of a ``SOLVE``
statement to solve an optimization model, but can also consist of a
sequence of execution and flow control statements.

The contents of the ``Body`` attribute is application-specific, and is 
irrelevant to a further understanding of the material in this section.

.. rubric:: Specifying function domain and range

When the resulting value of a function is multidimensional, you can
specify the index domain and range of the result in the attribute form
of the function using the ``IndexDomain`` and ``Range`` attributes.
Inside the function body you can make assignments to the function name
as if it were a local (indexed) parameter, with the same dimension as
specified in the ``IndexDomain`` attribute. The most recently assigned
values are the values that are returned by the function.
