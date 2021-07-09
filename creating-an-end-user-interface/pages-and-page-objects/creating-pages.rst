.. _sec:page.create:

Creating pages
==============

.. rubric:: Creating pages

Creating an end-user page is as easy as adding a new node to the page
tree in the **Page Manager** (see :ref:`chap:pagetool`).
:numref:`fig:page.pagetree` illustrates the page tree associated with
the example application used throughout this guide.

.. figure:: page-man-new.png
   :alt: Example of a page tree
   :name: fig:page.pagetree

   Example of a page tree

As all the trees in the AIMMS modeling tools work alike, you can use any
of the methods described in :ref:`sec:model.trees` to add a new page
node to the page tree.

.. rubric:: Copying pages

In addition to inserting a new empty page into the page tree, you can
also copy an existing page or an entire subtree of pages, by either a
simple cut, copy and paste or a drag-and-drop action in the tree (see
:ref:`sec:model.trees`). All copied pages will have the same content as
their originals.

.. rubric:: Page name

The node name of every page (as displayed in the page tree) is the
unique name or description by which the page is identified in the
system. When you add new pages to the tree, AIMMS will name these *Page
1*, *Page 2*, etc. You can change this name using the standard methods
for changing names of tree nodes as described in :ref:`sec:model.trees`.

.. rubric:: Page title

By default, the node name is the title that will be displayed in the
frame of the page window when the page is opened. In the page
**Properties** dialog box (see :ref:`sec:prop.property`) you can,
however, specify a different page title to be displayed, which can
either be a constant string or a reference to a string parameter in the
model. The latter is useful, for instance, if you intend to set up an
end-user interface in multiple languages.

.. rubric:: Position in page tree

Its position in the page tree determines the navigational properties of
the page. It will determine how any button with references to the next
or previous page, or any navigation object or menu linked to the page,
will behave. These navigational aspects of the **Page Manager** tool are
discussed in more detail in :ref:`chap:pagetool`.

.. rubric:: Using templates

Every page that you add to the page tree, is also automatically added to
the template tree in the **Template Manager**. By moving the page to a
different position in the template tree, the page automatically inherits
all the properties such as page size or background, and all objects
specified on the template pages hierarchically above it. The **Template
Manager** and the use of templates is explained in full detail in
:ref:`chap:pagetool`.