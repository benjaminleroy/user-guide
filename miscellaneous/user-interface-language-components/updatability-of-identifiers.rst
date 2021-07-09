.. _sec:gui.updatability:

Updatability of identifiers
===========================

.. rubric:: Dynamic control required

In many applications you, as a modeler, might need to have dynamic
control over the updatability of identifiers in the graphical end-user
interface of your model. AIMMS provides several ways to accomplish this.

.. rubric:: Multiple phases in your application

A typical example of dynamically changing inputs and outputs is when
your model is naturally divided into multiple decision phases. Think of
a planning application where one phase is the preparation of input, the
next phase is making an initial plan, and the final phase is making
adjustments to the initial plan. In such a three-layered application,
the computed output of the initial plan becomes the updatable input of
the adjustment phase.

.. rubric:: Indicating input and output status

To change the updatability status of an identifier in the graphical
interface you have two options.

-  You can indicate in the object **Properties** dialog box whether all
   or selected values of a particular identifier in the object are
   updatable or read-only.

-  With the set :any:`CurrentInputs` you can change the global updatability
   status of an identifier. That is, AIMMS will never allow updates to
   identifiers that are not in the set :any:`CurrentInputs`, regardless of
   your choice in the properties form of a graphical object.

.. rubric:: The set :any:`CurrentInputs`

The set :any:`CurrentInputs` (which is a subset of the predefined set
:any:`AllUpdatableIdentifiers`) ultimately determines whether a certain
identifier can be treated as an input identifier for objects in an
end-user interface. You can change the contents of the set
:any:`CurrentInputs` from within your model. By default, AIMMS initializes
it to :any:`AllUpdatableIdentifiers`.

.. rubric:: The set :any:`AllUpdatableIdentifiers`

The set :any:`AllUpdatableIdentifiers` is computed by AIMMS when your model
is compiled, and contains the following identifiers:

-  all *sets* and *parameters* without definitions, and

-  all *variables* and *arcs*.

Thus, sets and parameters which have a definition can never be made
updatable from within the user interface.