.. _sec:gui.color:

Setting colors within the model
===============================

.. rubric:: Color as indicator

An important aspect of an end-user interface is the use of color. Color
helps to visualize certain properties of the data contained in the
interface. As an example, you might want to show in red all those
numbers that are negative or exceed a certain threshold.

.. rubric:: Setting colors in the model

AIMMS provides a flexible way to specify colors for individual data
elements. The color of data in every graphical object in the graphical
interface can be defined through an (indexed) "color" parameter. Inside
your model you can make assignments to such color parameters based on
any condition.

.. rubric:: The set :any:`AllColors`

In AIMMS, all *named* colors are contained in the predefined set
:any:`AllColors`. This set contains all colors predefined by AIMMS, as well
as the set of logical color names defined by you for the project.
Whenever you add a new logical color name to your project through the
color dialog box, the contents of the set :any:`AllColors` will be updated
automatically.

.. rubric:: Color parameters

Every (indexed) element parameter with the set :any:`AllColors` as its
range can be used as a color parameter. You can simply associate the
appropriate colors with such a parameter through either its definition
or through an assignment statement.

.. rubric:: Example

Assume that ``ColorOfTransport(i,j)`` is a color parameter defining the
color of the variable ``Transport(i,j)`` in an object in the end-user
interface. The following assignment to ``ColorOfTransport`` will cause
all elements of ``Transport(i,j)`` that exceed the threshold
``LargeTransportThreshold`` to appear in red.

.. code-block:: aimms

	ColorOfTransport((i,j) | Transport(i,j) >= LargeTransportThreshold) := 'Red' ;

.. _sec:gui.color.func:

Creating Non-Persistent User Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Non-persistent user colors

During the start up of an AIMMS project, the set :any:`AllColors` is filled
initially with the collection of persistent user colors defined through
the **Tools-User Colors** dialog box (see also :ref:`sec:prop.color`).
Through the functions listed below, you can extend the set :any:`AllColors`
programmatically with a collection of non-persistent colors, whose
lifespan is limited to a single session of a project.

-  :any:`UserColorAdd`\ (*colorname*,\ *red*,\ *green*,\ *blue*)

-  :any:`UserColorDelete`\ (*colorname*)

-  :any:`UserColorModify`\ (*colorname*,\ *red*,\ *green*,\ *blue*)

-  :any:`UserColorGetRGB`\ (*colorname*,\ *red*,\ *green*,\ *blue*)

The argument *colorname* must be a string or an element in the set
:any:`AllColors`. The arguments *red*, *green* and *blue* must be scalars
between 0 and 255.

.. rubric:: Adding non-persistent colors

You can use the function :any:`UserColorAdd` to add a non-persistent color
*colorname* to the set :any:`AllColors`. The RGB-value associated with the
newly added user color must be specified through the arguments *red*,
*green* and *blue*. The function will fail if the color already exists,
either as a persistent or non-persistent color.

.. rubric:: Deleting and modifying colors

Through the functions :any:`UserColorDelete` and :any:`UserColorModify` you
can delete or modify the RGB-value of an existing non-persistent color.
The function will fail if the color does not exist, or if the specified
color is a persistent color. Persistent colors can only be modified or
deleted through the **Tools- User Colors** dialog box.

.. rubric:: Retrieving RGB-values

You can obtain the RGB-values associated with both persistent and
non-persistent user colors using the function :any:`UserColorGetRGB`. The
function will fail if the specified color does not exist.