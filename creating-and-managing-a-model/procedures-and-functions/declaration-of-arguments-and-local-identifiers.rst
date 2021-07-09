.. _sec:proc.arg:

Declaration of arguments and local identifiers
==============================================

.. rubric:: Specifying arguments

All (formal) arguments of a procedure or function must be specified as a
parenthesized, comma-separated, list of non-indexed identifier names.
All formal arguments must also be declared as local identifiers in a
declaration section local to the procedure or function. These local
declarations then specify the further domain and range information of
the arguments. If an argument has not been declared when you create (or
modify) a procedure or function, AIMMS will open the dialog box
illustrated in :numref:`fig:proc.loc-arg` which helps you add the
appropriate declaration quickly and easily.

.. figure:: loc-arg-new.png
   :alt: **Argument Declaration** dialog box
   :name: fig:proc.loc-arg

   **Argument Declaration** dialog box

After completing the dialog box, AIMMS will automatically add a
declaration section to the procedure or function, and add the arguments
displayed in the dialog box to it, as illustrated in
:numref:`fig:proc.proc`.

.. rubric:: Input-output type

An important aspect of any argument is its input-output type, which can
be specified by selecting one of the ``Input``, ``InOut``, ``Output`` or
``Optional`` properties in the **Argument Declaration** dialog box. The
input- output type determines whether any data changes you make to the
formal arguments are passed back to the actual arguments on leaving the
procedure. The precise semantic meaning of each of these properties is
discussed in the AIMMS Language Reference book.

.. rubric:: Argument attributes

The choices made in the **Argument Declaration** dialog box are directly
reflected in the attribute form of the local identifier added to the
model tree by AIMMS. As an example, :numref:`fig:proc.proc-arg` shows
the attribute form of the single argument ``mf`` of the procedure
``CheckComputableFlow`` added in :numref:`fig:proc.loc-arg`.

In the dialog box of :numref:`fig:proc.loc-arg` it is not possible to
modify the dimension of a procedure or function argument directly. If
your procedure or function has a multidimensional argument, you can
specify this with the ``IndexDomain`` attribute of the argument after
the argument has been added as a local identifier to the model tree.

.. figure:: proc-arg-new.png
   :alt: Declaration form of a procedure argument
   :name: fig:proc.proc-arg

   Declaration form of a procedure argument

.. rubric:: Prototype checking

For every call to the procedure or function, AIMMS will verify whether
the types of all the actual arguments match the prototypes supplied for
the formal arguments, including the supplied index domain and range. For
full details about argument declaration refer to the AIMMS Language
Reference book.

.. rubric:: Local declarations

In addition to arguments, you can also add other local identifiers to
declaration sections within procedures and functions. Such local
identifiers are only known inside the function or procedure. They are
convenient for storing temporary data that is only useful within the
context of the procedure or function, and have no global meaning or
interpretation.

.. rubric:: Not all types supported

Not all identifier types can be declared as local identifiers of a
procedure or function, because of the global implications they may have
for the AIMMS execution engine. When you try to add a local identifier
to a procedure or function, AIMMS will only offer those identifier types
that are actually supported within a procedure or function. An example
of an identifier type that cannot be declared locally is a constraint.

.. rubric:: Not all attributes supported

In addition, for local identifiers, AIMMS may only support a subset of
the attributes that are supported for global identifiers of the same
type. For instance, AIMMS does not allow you to specify a ``Definition``
attribute for local sets and parameters. In the attribute window of
local identifiers such non-supported attributes are automatically
removed when you open the associated attribute form.