Adapting to changing screen resolutions
=======================================

.. rubric:: Coping with different resolutions
   :name: resize-screen

AIMMS allows you to create pages in such a manner that they will
automatically adapt to changing screen resolutions. Thus, given a
sensible configuration of split lines, you can create an application
than can be run in resolutions other than the base resolution for which
you developed the pages.

.. rubric:: Page properties

To specify the behavior of pages and templates, open the **Properties**
dialog box for the page (template), as illustrated in
:numref:`fig:resize.dialog`.

.. figure:: prop-rsz-new.png
   :alt: The page **Properties** dialog box
   :name: fig:resize.dialog

   The page **Properties** dialog box

In the **Position & Size** area of this dialog box, you can select the
default position and size of the page, which AIMMS will use when opening
the page.

.. rubric:: Opening modes

For every page in your application, you can select one of the four
following standard page opening modes:

-  get the position and size from the template used by the page,

-  open the page at maximum size, but with visible page borders,

-  open the page at maximum size, but without visible page borders, and

-  open the page using the last saved position and size.

.. rubric:: Inherited modes

If you specify that a page should obtain its position and page size from
its template, the page will use the page open mode as specified for that
template. When, in turn, this template has been specified to open
according to its last saved position and size, an interesting
interaction between the template and all its dependent pages will take
place. Changing the position and size of *any* page using such a
template will cause all the other pages using that template to be opened
using the new position and size.

.. rubric:: Resizable root template

As an application for the above, you could decide to make every page and
page template dependent on the position and size of the root template.
In this manner, changing the size of any page, will automatically result
in the adjustment of every other page.

.. rubric:: Save over sessions

When you have specified that a page or page template should save its
last position, this position is stored between sessions. That is, the
next time you open the same project, AIMMS will open such pages in the
same positions as used in the previous sessions on the same computer.

