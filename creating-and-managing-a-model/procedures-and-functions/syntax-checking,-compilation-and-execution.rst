.. _sec:proc.compile:

Syntax checking, compilation and execution
==========================================

.. rubric:: Performing a syntax check

Using either **Check and commit** or **Check, commit and close** as
discussed in :ref:`sec:decl.commit` AIMMS will compile the procedure or
function in hand, and point out any syntax error in its body. If you do
not want to compile a procedure or function, but still want to commit
the changes, you should use the **Commit and close** button. All edits
are ignored when you close the window using the **Discard** button.

.. rubric:: Partial recompilation

Before executing any procedure in your model, AIMMS will automatically
verify whether your model needs to be recompiled, either partially or
fully. In most cases, there is no need for AIMMS to recompile the entire
model after a modification or addition of a new identifier, a procedure
or a function. For instance, when you have only changed the body of a
procedure, AIMMS needs only to recompile that particular procedure.

.. rubric:: Complete recompilation

However, if you change the index domain of an identifier or the number
of arguments of a procedure or function, each reference to such an
identifier, procedure or function needs to be verified for correctness
and possibly changed. In such cases, AIMMS will (automatically)
recompile the entire model before any further execution can take place.
Depending on the size of your model, complete recompilation may take
some time. Note that either partial or complete recompilation will only
retain the data of all identifiers present prior to compilation, to the
extent possible (data cannot be retained when, for instance, the
dimension of an identifier has changed).

.. rubric:: Running a procedure

AIMMS supports several methods to initiate procedural model execution.
More specifically, you can run procedures

-  from within another procedure of your model,

-  from within the graphical user interface by pressing a button, or
   when changing a particular identifier value, or

-  by selecting the **Run procedure** item from the right-mouse menu for
   any procedure selected in the **Model Explorer**.

The first two methods of running a procedure are applicable to both
developers and end-users. Running a procedure from within the **Model
Explorer** a useful method for testing the correct operation of a newly
added or modified procedure.

