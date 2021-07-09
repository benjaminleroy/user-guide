.. _sec:prop.color:

Defining user colors
====================

.. rubric:: User colors
   :name: user-color

As already explained in the previous section, AIMMS allows you to define
the color of particular objects in a graphical end-user interface from
within the execution of your model. In this section you will see how you
can define *user colors* which can be used within the model, and how you
can use them to provide model-computed coloring of page objects.

.. rubric:: Defining persistent user colors

To define user colors that persist across multiple sessions of a
project, you should open the **User Colors** dialog box as illustrated
in :numref:`fig:prop.color` from the **Tools** menu.

.. figure:: color-new.png
   :alt: The **User Colors** dialog box
   :name: fig:prop.color

   The **User Colors** dialog box

By pressing the **Add** or **Change Color** button, AIMMS will display
the standard Windows color selection dialog box, which you can use to
create a new user color or modify an existing user color. After you have
selected a color, AIMMS will request a name for the newly defined color
for further usage within the model.

.. rubric:: Functional color names

As with font names, you may prefer to choose functional color names
rather than names describing user colors. For instance, colors named
"Full tank color", "Partially filled color" and "Empty tank color" may
be a much better choice, from a maintenance point-of-view, than such
simple names as "Red", "Blue" and "Green". In addition, choosing
descriptive names may make the intention of any assignment to, or
definition of, color parameters in your model much clearer.

.. rubric:: User colors in library projects

Similar as with fonts, a library project can also contain its own set of
user colors. The list of colors shown in :numref:`fig:prop.color`
displays the user colors defined within the main project. For each
library included in the project the listbox contains a separate area
displaying the user colors that are associated with that library. You
can manage the list of user colors associated with a library by pressing
the buttons on the right-hand side of the dialog box, while the
selection in the listbox on the left-hand side is in the area associated
with the library.

.. rubric:: Use only in library pages

If you have defined user colors within a library project, you should
ideally only use these user colors in pages that are also part of the
library project. If you use the user colors in pages outside of the
library, such pages may fail to display properly after you have removed
the library project from the AIMMS project.

.. rubric:: Color names must be unique

AIMMS requires that all user color names be unique across the main
project and all library projects that are included in the main project.
If you include an existing library project, which contains a user color
name that is already present in the AIMMS project, AIMMS assumes that
both user colors are the same and will ignore the second color
definition.

.. rubric:: Runtime user colors

Persistent user colors cannot be modified or deleted programmatically.
However, you can add runtime colors (which only exist for the duration
of a project session) programmatically from within your model using the
function :any:`UserColorAdd`. In the **User Colors** dialog box, runtime
colors are shown under the header **Runtime colors**. You can modify or
delete such runtime colors using the functions :any:`UserColorModify` and
:any:`UserColorDelete`. These functions are discussed in full detail in
:ref:`sec:gui.color.func`.

.. rubric:: The set :any:`AllColors`

All persistent and non-persistent user colors are available in your
model as elements of the predefined set :any:`AllColors`. To work with
colors in your model you can simply define scalar and/or indexed element
parameters into the set :any:`AllColors`. Through simple assignments or
definitions to such parameters you can influence the coloring of
identifiers or individual identifier values on an end-user page.

.. rubric:: Example

Consider a set of ``Flows`` in a network with index ``f``. If a
mathematical program minimizes the errors in computed flows in respect
to a set of measured flow values, then the following simple assignment
to a color parameter ``FlowColor(f)`` marks all flows for which the
error exceeds a certain threshold with an appropriate color.

.. code-block:: aimms

	FlowColor(f) := if ( FlowError(f) >= ErrorThreshold ) then
	    'Red' else 'Black' endif;

.. rubric:: Use in interface

With the above assignment, any graphical display of ``Flows`` can be
colored individually according to the above assignment by specifying
that the color of the individual numbers or flows in the **Colors**
dialog box of the object be given by the value of the color parameter
``FlowColor(f)``. :numref:`fig:prop.unit` (on :numref:`fig:prop.unit`)
illustrates an example of an end-user page where the flows in the
network flow object, as well as the individual entries in the tables and
lists, are colored individually with respect to the parameter
``FlowColor(f)`` (the colors are only visible in the electronic version
of this book).

