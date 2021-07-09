Resizable templates
===================

.. rubric:: Creating resizable templates

When you are creating an AIMMS-based application with many resizable
pages, all based on a number of page templates, you should also consider
defining the basic resize properties of these templates. As templates
behave as ordinary pages in the template tree, you can add split lines
to templates as described in the previous section.

.. rubric:: Inherited resizability

All templates and end-user pages based upon a resizable template inherit
the resize properties of that template, i.e. all split lines in the
template are also applicable to its child templates and pages.
Generally, such inherited split lines should take care of the resize
properties of those objects that are contained in the template itself.

.. rubric:: Adding split lines

On any page (either template or end-user page) you can always add
additional split lines to those inherited from its ancestor template(s).
The added split lines are used to specify the resize properties of the
additional objects that have been placed on the page. In this manner,
the template tree can be used to define the entire look-and-feel of your
pages in a hierarchical manner, and their resize properties.

.. rubric:: Example revisited

The example page in :numref:`fig:resize.shaded` and
:numref:`fig:resize.page` already illustrates the inherited resizability
from templates. In fact, :numref:`fig:resize.shaded` displays the split
line configuration of a template defining the common header and footer
area of all its child pages. The page in :numref:`fig:resize.page`,
which uses this template, automatically inherits its resize properties.
Therefore, the table in the "data area" of this page automatically grows
or shrinks in relation to the page size as dictated by the template.
