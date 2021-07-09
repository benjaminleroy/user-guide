.. _sec:decl.add:

Adding identifier declarations
==============================

.. rubric:: Identifiers

Identifiers form the heart of your model. All data are stored in
identifiers, and the bodies of all functions and procedures consist of
statements which compute the values of one identifier based on the data
associated with other identifiers.

.. rubric:: Adding identifiers

Adding an identifier declaration to your model is as simple as adding a
node of the desired type to a global declaration section (or to a
declaration section local to a particular procedure or function), as
explained in :ref:`sec:model.trees`. AIMMS will only allow you to add
identifier declarations inside declaration sections.

.. rubric:: Identifier types

There are many different types of identifiers. Each identifier type
corresponds to a leaf node in the model tree and has its own icon,
consisting of a white box containing one or more letters representing
the identifier type. When you add an identifier to a declaration section
of your model in the model tree, you must first select its identifier
type from the dialog box as presented in :numref:`fig:decl.id-type`.

.. figure:: ins-iden-new.png
   :alt: Choosing an identifier type
   :name: fig:decl.id-type

   Choosing an identifier type

.. rubric:: Identifier name

After you have selected the identifier type, AIMMS adds a node of the
specified type to the model tree. Initially, the node name is left
empty, and you have to enter a unique identifier name. If you enter a
name that is an AIMMS keyword, an identifier predeclared by AIMMS
itself, or an existing identifier in your model, AIMMS will warn you of
this fact. By pressing the **Esc** key while you are entering the
identifier name, the newly created node is removed from the tree.

.. rubric:: Meaningful names are preferable

There is no strict limit to the length of an identifier name. Therefore,
you are advised to use clear and meaningful names, and not to worry
about either word length or the intermingling of small and capital
letters. AIMMS offers special features for name completion such as
**Ctrl-Spacebar** (see :ref:`sec:decl.attr`), which allow you to write
subsequent statements without having to retype the complete identifier
names. Name completion in AIMMS is also case consistent.

.. rubric:: Index domain

In addition, when an identifier is multidimensional, you can immediately
add the index domain to the identifier name as a parenthesized list of
indices that have already been declared in the model tree.
Alternatively, you can provide the index domain as a separate attribute
of the identifier in its attribute form. :numref:`fig:decl.index-domain`
illustrates the two ways in which you can enter the index domain of an
identifier.

.. figure:: dom-form-new-cumul.png
   :alt: Specifying an index domain
   :name: fig:decl.index-domain

   Specifying an index domain

In both cases the resulting list of indices will appear in the model
tree as well as in the ``IndexDomain`` attribute of the attribute form
of that identifier. In the ``IndexDomain`` attribute it is possible,
however, to provide a further restriction to the domain of definition of
the identifier by providing one or more domain conditions (as explained
in full detail in the Language Reference). Such conditions will not
appear in the model tree.

.. rubric:: Unrestricted order of declarations

The identifier declarations in the model tree can be used independently
of the order in which they have been declared. This allows you to use an
identifier anywhere in the tree. This order independence makes it
possible to store identifiers where you think they should be stored
logically. This is different to most other systems where the order of
identifier declarations is dictated by the order in which they are used
inside the model description.

.. rubric:: Identifier scope

In general, all identifiers in an AIMMS model are known globally, unless
they have been declared inside a local declaration section of a
procedure or function. Such identifiers are only known inside the
procedure or function in which they have been declared. When you declare
a local identifier with the same name as a global identifier, references
to such identifiers in the procedure or function will evaluate using the
local rather than the global identifier.

.. rubric:: Local declarations

Local identifiers declared in procedures and functions are restricted to
particular types of identifier. For example, AIMMS does not allow you to
declare constraints as local identifiers in a procedure or function, as
these identifier types are always global. Therefore, when you try to add
declarations to a declaration section somewhere in the model tree, AIMMS
only lists those types of nodes that can be inserted at that position in
the model tree.

.. rubric:: Declarations via attributes

As an alternative to explicitly adding identifier nodes to the model
tree, it is sometimes possible that AIMMS will implicitly define one or
more identifiers on the basis of attribute values of other identifiers.
The most notable examples are indices and (scalar) element parameters,
which are most naturally declared along with the declaration of an index
set. These identifiers can, therefore, be specified implicitly via the
``Index`` and ``Parameter`` attributes in the attribute form of a set.
Implicitly declared identifiers do not appear as separate nodes in the
model tree.

