.. _sec:pagetool.pageman:

The Page Manager
================

.. rubric:: Page navigation

In large decision support systems with many pages, navigating your
end-users in a consistent manner through all the end-user screens is an
important part of setting up your application. One can think of several
organizational structures for all the available end-user screens in your
application that would help your end-users maintain a good overview of
their position. To help you set up, and modify, a clear navigational
organization quickly and easily, AIMMS provides a tool called the **Page
Manager**.

.. rubric:: The Page Manager

With the **Page Manager** you can organize all the existing pages of an
AIMMS application in a tree-like fashion, as illustrated in
:numref:`fig:pagetool.pageman`.

The tree in the **Page Manager** that holds all the pages of the main
AIMMS project is called the main *page tree*. Relative to a particular
page in this page tree, the positions of the other pages define common
page relationships such as *parent* page, *child* page, *next* page or
*previous* page.

.. rubric:: Library page trees

In addition to the main page tree, each library project included in the
main project can have its own tree of pages as illustrated in
:numref:`fig:pagetool.pageman`. :ref:`sec:pagetool.pageman.library`
discusses the facilities available in AIMMS that allow you to combine
the page structures in all trees to construct a single navigational
structure for the entire application.

.. figure:: pgman-pt-new.png
   :alt: The **Page Manager**
   :name: fig:pagetool.pageman
   
   The **Page Manager**

.. rubric:: Navigational controls

The page relationships defined by the page tree can be used in several
navigational interface components that can be added to a page or
end-user menu. These components include

-  *navigation objects*,

-  *navigation menus*,

-  *button actions*, and

-  *tabbed pages*.

These allow you to add dynamic navigation to the parent, child, next or
previous pages with respect to the position of either

-  the current page, or

-  a fixed page in the page tree.

:ref:`sec:pagetool.pageman.navigate` explains in detail how to set up
such automatic navigation aids.

.. rubric:: Aimed at ease of maintenance

The strength of the **Page Manager** tool lies in the fact that it
allows you to quickly add pages to the page tree, delete pages from it,
or modify the order of navigation without the need to make modifications
to hard-coded page links on the pages themselves. Thus, when a model
extension requires a new section of pages, you only need to construct
these pages, and store them at the appropriate position in the page
tree. With the appropriate navigational interface components added to
the parent page, the new page section will be available to the end-user
immediately without any modification of existing pages.

.. _sec:pagetool.pageman.library:

Pages in Library Projects
~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Pages in library projects

AIMMS allows you to develop a separate page tree for every library
project included in an AIMMS application. This is an important feature
of library projects because

-  it allows a developer to implement a fully functional end-user
   interface associated with a specific sub-project of the overall
   application completely independently of the main project, and

-  pages defined inside a library project can refer to all the
   identifiers declared in that library, whereas pages defined in the
   main project (or in any other library) can only refer to the public
   identifiers in the interface of that library (see
   :ref:`sec:proj-organization.working`).

.. rubric:: Duplicate names may occur

While AIMMS requires that the names of pages within a single (library)
project be unique, page names need not be unique across library
projects. To ensure global uniqueness of page names in the overall
application, AIMMS internally prefixes the names of all the pages
contained within a library with its associated library prefix (see
:ref:`sec:proj-organization.manager`). When you want to open an end-user
page programmatically, for instance through the :any:`PageOpen` function,
you need to provide the full page name including its library prefix.
Without a library prefix, AIMMS will only search for the page in the
main page tree.

.. rubric:: Separate page trees

The page trees associated with the main project and with all of its
library projects are initially completely separate. That is, any
navigational control (see :ref:`sec:pagetool.pageman.navigate`) that
refers to parent, child, next or previous pages can never navigate to a
page that is not part of the tree in which the originating page was
included.

.. rubric:: All pages are accessible

Other than for the identifier declarations in a libray, AIMMS puts no
restriction on which pages in the library can and cannot be shown from
within the main application, or from within other libraries. Stated
differently, the page tree of a library does not currently have a public
interface.

.. rubric:: Creating an application GUI

If an AIMMS project is composed of multiple libraries, then each of
these libraries contains its own separate page tree, which may be
combined to form the total end-user interface of the overall
application. The navigational controls offered by AIMMS, however, can
only reach the pages in the same tree in which an originating page is
included.

.. rubric:: Jumping to library pages

Without further measures, pages from different libraries would,
therefore, only be accessible through a unidirectional direct link,
which is very undesirable from an end-user perspective. After following
such a link moving to a parent, next or previous page may give
completely unexpected results, and getting back to the originating page
may be virtually impossible. For both developers and end-users a
situation in which all relevant pages can be reached from within a
single navigational structure is much more convenient.

.. rubric:: Page tree references

To address this problem, AIMMS offers a linkage mechanism called *page
tree references*. Through a page tree reference, you can *virtually*
move a subtree of pages from a library project to another location in
either the main project or any other library project included in the
AIMMS application. While physically the pages remain at their original
location, the navigational controls in AIMMS will act as if the tree of
pages has been moved to the destination location of the page tree
reference. At the original location AIMMS' navigational controls will
completely disregard the linked page tree.

.. rubric:: Creating a page tree reference

You can create a page tree reference by inserting a page tree reference
node at the destination location through the **Edit-New-Page Tree
Reference** menu. In :numref:`fig:pagetool.pageman` the *Reconciliation
Wrapper* node illustrates an example of a page tree reference node. It
is linked to the tree of pages starting at the *Reconciliation* page in
the *CoreModel* library. Note that AIMMS uses a special overlay of the
page icon to visualize that a page is linked to a page tree reference
node, and hence, at its original location, is not reachable anymore
through AIMMS' navigational controls.

.. rubric:: Linking a page tree reference

To create a link between a page tree reference node and a subtree of
pages anywhere else in your application you have to select both the page
tree reference node and the node that is at the root of the subtree that
you want to link to, and select the **Edit-Page Tree Reference-Link**
menu. You can unlink an existing link through the **Edit-Page Tree
Reference-Unlink** menu.

.. _sec:pagetool.pageman.navigate:

Navigational Interface Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Navigational control
   :name: nav-control

The page tree can be used to directly control the navigational structure
within an AIMMS-based end-user application. This can be accomplished
either by special button actions or through the navigation object and
menus. As an example, :numref:`fig:pagetool.nav`

illustrates the *Process Topology* page contained in the page tree of
:numref:`fig:pagetool.pageman`. In the lower left corner, the page
contains three navigational buttons that are linked, from left to right,
to the previous, parent and next page. Above this, the page contains a
navigation object which, in this instance, automatically displays a list
of buttons that corresponds exactly to the set of direct child nodes of
the *Process Topology* page in the page tree.

.. figure:: nav-win-new.png
   :alt: Page containing navigation buttons and a navigation object
   :name: fig:pagetool.nav

   Page containing navigation buttons and a navigation object

.. rubric:: Button actions

To add a page tree-based navigational control to a button, you only need
to add a **Goto Page** action to the **Actions** tab in the button
**Properties** dialog box, as illustrated in
:numref:`fig:pagetool.nav-button`.

.. figure:: nav-but-new.png
   :alt: Adding navigational control to a button
   :name: fig:pagetool.nav-button

   Adding navigational control to a button

You can request AIMMS to open the previous, next, parent or (first)
child page relative to the position of the current page in the page
tree. If you want the current page to be closed after opening the new
page, you should additionally insert a **Close Page** action as in
:numref:`fig:pagetool.nav-button`.

.. rubric:: Cycling

When there is no longer a next or previous page to open in a particular
branch of a page tree, AIMMS will cycle to the first or last page within
that branch, respectively. You can further modify the result of a
previous or next page action by placing special *separator* nodes into
the page tree, given that AIMMS will never jump past a separator node.
You will find the full details of separator nodes in the online help on
the **Page Manager**.

.. rubric:: Navigation object

The second way to include a navigational control in an end-user page is
by means of a custom *navigation* object. A navigation object can
display a subtree of the entire page tree in several formats, such as:

-  a list of buttons containing the page titles (as in
   :numref:`fig:pagetool.nav`),

-  a list of buttons accompanied by the page titles,

-  a list of clickable or non-clickable page titles without buttons, or

-  a tree display similar to the page tree itself.

.. rubric:: Object properties

After adding a navigation object to a page, you must specify the subtree
to be displayed through the **Properties** dialog box as displayed in
:numref:`fig:pagetool.nav-object`.

.. figure:: nav-obj-new.png
   :alt: Navigation object **Properties** dialog box
   :name: fig:pagetool.nav-object

   Navigation object **Properties** dialog box

What is displayed in the navigation object is completely determined by
the reference page, together with the number of ancestor (parent) and
child generations specified in this dialog box.

.. rubric:: Display only

If you set a navigation object to read-only using the **Input** tab of
the **Properties** dialog box, then you can use the navigation object
for display- only purposes. Thus, you can use it to display the current
page title as a page header, or the title of one or more parent pages in
the header or footer area of the page. The "*Process Topology*" page
header of the end-user page displayed in :numref:`fig:pagetool.nav` is
an example of a display-only navigation object.

.. rubric:: Navigation menus

Finally, you can add special navigation (sub)menus to your application
in which the menu items and submenus represent a subtree structure of
the page tree. :numref:`fig:pagetool.nav-menu` illustrates an example of
a navigation menu linked to the page tree displayed in
:numref:`fig:pagetool.pageman`.

.. figure:: nav-men-new.png
   :alt: Example of a navigation menu
   :name: fig:pagetool.nav-menu

   Example of a navigation menu

.. rubric:: Adding navigation menus

You can add a navigation menu to any menu in the **Menu Builder** tool
(see :ref:`sec:pagetool.menu`). For each navigation menu you must
specify a reference page and the scope of the subtree to be displayed in
a similar fashion to that illustrated for the navigation object in
:numref:`fig:pagetool.nav-object`.

.. rubric:: Hiding pages

Pages can be statically or dynamically hidden using the page
**Properties** dialog box (see also :ref:`sec:prop.property`), as
illustrated in :numref:`fig:pagetool.disable`.

.. figure:: pag-dis-new.png
   :alt: Hiding a page
   :name: fig:pagetool.disable

   Hiding a page

In the **Hidden** field, you must enter a scalar value, identifier or
identifier slice. Whenever the property assumes a nonzero value the page
is hidden, and automatically removed from any navigational interface
component in which it would otherwise be included.

.. rubric:: Authorizing access

For larger applications, end-users can usually be divided into groups of
users with different levels of authorization within the application.
Disabling pages based on the level of authorization of the user
(explained in :ref:`chap:security`) then provides a perfect means of
preventing users from accessing those data to which they should not have
access. You can still open a hidden page via a hard-coded page link.