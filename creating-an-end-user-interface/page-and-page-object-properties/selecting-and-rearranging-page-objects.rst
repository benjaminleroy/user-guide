.. _sec:prop.select:

Selecting and rearranging page objects
======================================

.. rubric:: Selecting an object

Before you can modify the properties of a page object, you must select
the object. This can be accomplished as follows:

-  make sure that the page is opened in edit mode (see
   :ref:`sec:page.object`),

-  press the **Select Object** button |btn-select| on the page toolbar,
   if it is not already pressed, and

-  click on the page object.

The selected object(s) on a page are marked with a small dark square on
each of its corners. This is illustrated in :numref:`fig:prop.selected`.

.. figure:: new-tbl-new.png
   :alt: Entering an expression for a page object
   :name: fig:prop.selected
   
   A selected page object

.. rubric:: No template objects

When a page depends on one or more templates (see also
:ref:`sec:pagetool.template`), AIMMS will only let you select those
objects that were placed on the page itself, and not those which are
contained in any of its templates. Template objects can only be edited
in the template page on which they are defined.

.. rubric:: Selecting overlapping objects

When two or more objects are overlapping, clicking on the overlapping
region will result in any one of the overlapping objects being selected.
By holding the **Shift** key down during clicking, AIMMS will cycle
through all the overlapping objects, allowing you to select the object
of your choice. Alternatively, you can press the **Tab** key repeatedly
to browse through all selectable objects on the page.

.. rubric:: Selecting multiple objects

In addition to selecting a single page object, AIMMS also allows you to
select multiple objects. You can do this by dragging a *select region*
on the page, after which AIMMS will mark all objects contained in that
region as selected. Alternatively, you can add or remove objects to form
a selection by clicking on the objects while holding down the **Shift**
key.

.. rubric:: Object alignment

With the **Edit-Alignment** menu of a page in edit mode, you can correct
the placement and sizes of all page objects that are currently selected.
The **Alignment** menu lets you perform actions such as:

-  give all selected objects the same height or width, i.e. the height
   or width of the largest object,

-  align all selected objects with the top, bottom, left or rightmost
   selected object,

-  center the selected objects horizontally or vertically, and

-  spread all selected objects equally between the top and bottommost
   objects or between the left and rightmost objects.

An alternative method of alignment is to define a grid on the page (see
:ref:`sec:page.object`), and align the borders of all objects with the
grid.

.. rubric:: Drawing order

With the **Drawing Order** item of the **Edit** menu, you can alter the
order in which overlapping objects are drawn. When applied to a selected
object, you can specify that the object at hand must be drawn as either
the top or bottommost object. Modifying the drawing order only makes
sense for drawing objects such as the text, rectangle, line, circle and
picture objects.

.. rubric:: Specifying the tab order

When there is a natural order in which an end-user has to enter data on
a particular page, you can use the **Tab Order** item from the **Edit**
menu, to specify this order. The **Tab Order** menu opens a dialog box
as illustrated in :numref:`fig:prop.tab-order`.

.. figure:: tab-ordr-new.png
   :alt: The **Tab Order** dialog box
   :name: fig:prop.tab-order

   The **Tab Order** dialog box

In this dialog box all page objects are displayed in a list which
determines the (cyclic) order in which AIMMS will select the next object
for editing when the user leaves another object on the page through the
**Tab** or **Enter** keys.

.. rubric:: Tabular objects

In tabular objects, the **Tab** and **Enter** keys can also be used to
move to the next table entry to the right or below, respectively. In
such cases, AIMMS will only go to the next object in the tab order, if
further movement to the right or below within the object is no longer
possible.

.. rubric:: Disabling tab order

In addition to modifying the tab order, you can also use dialog box of
:numref:`fig:prop.tab-order` to select the page objects that should not
be included in the tab order. Alternatively, you can remove a page
object from the tab order in the **Properties** dialog box of that
object as explained in the next section. Objects excluded from the tab
order are not accessible on the page by pressing the **Tab** or
**Enter** keys, but can still be selected using the mouse.

.. |btn-select| image:: btn-select.png