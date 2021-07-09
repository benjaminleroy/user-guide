.. _sec:start.tools:

Modeling tools
==============

.. rubric:: Modeling tools

Once you have created a new project and associated a model file with it,
AIMMS offers a number of graphical tree-based tools to help you further
develop the model and its associated end-user interface. The available
tools are:

-  the *Model Explorer*,

-  the *Identifier Selector*,

-  the *Page Manager*,

-  the *Template Manager*, and

-  the *Menu Builder* tool.

These tools can be accessed either through the **Tools** menu or via the
project toolbar. They are all aimed at reducing the amount of work
involved in developing, modifying and maintaining particular aspects of
your model-based end-user application.
:numref:`fig:start.tools-overview` provides an overview of the windows
associated with each of these tools.

.. figure:: start-overview.png
   :alt: Overview of Aimms tools
   :name: fig:start.tools-overview

   Overview of Aimms tools


.. rubric:: The Model Explorer

The AIMMS **Model Explorer** provides you with a simple graphical
representation of all the identifiers, procedures and functions in your
model. All relevant information is stored in the form of a tree, which
can be subdivided into named sections to store pieces of similar
information in a directory-like structure. The leaf nodes of the tree
contain the actual declarations and the procedure and function bodies
that make up the core of your modeling application. The **Model
Explorer** is discussed in full detail in :ref:`chap:model`.

.. rubric:: The Identifier Selector

While the **Model Explorer** is a very convenient tool to organize all
the information in your model, the **Identifier Selector** allows you to
select and simultaneously view the attributes of groups of identifiers
that share certain functional aspects in your model. By mutual
comparison of the important attributes, such overviews may help you to
further structure and edit the contents of your model, or to discover
oversights in a formulation. The **Identifier Selector** is discussed in
full detail in :ref:`chap:view`

.. rubric:: The Page Manager

The **Page Manager** allows you to organize all end-user windows
associated with an AIMMS application (also referred to as end-user
pages) in a tree-like fashion. The organization of pages in the page
tree directly defines the navigational structure of the end-user
interface. Relative to a particular page in the page tree, the positions
of the other pages define common relationships such as *parent* page,
*child* page, *next* page or *previous* page, which can used in
navigational controls such as buttons and menus. The **Page Manager** is
discussed in full detail in :ref:`sec:pagetool.pageman`.

.. rubric:: The Template Manager

Within the **Template Manager**, you can make sure that all end-user
pages have the same size and possess the same look and feel. You can
accomplish this by creating page templates which define the page
properties and objects common to a group of end-user pages, and by
subsequently placing all end-user pages into the tree of page templates.
The **Template Manager** is discussed in full detail in
:ref:`sec:pagetool.template`.

.. rubric:: The Menu Builder

With the **Menu Builder** you can create customized menu bars, pop-up
menus and toolbars that can be linked to either template pages or
end-user pages in your application. In the menu builder window you can
define menus and toolbars in a tree-like structure similar to the other
page-related tools, to indicate the hierarchical ordering of menus,
submenus and menu items. The **Menu Builder** is discussed in full
detail in :ref:`sec:pagetool.menu`.