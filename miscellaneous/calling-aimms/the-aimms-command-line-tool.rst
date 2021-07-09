.. _sec:cmdline-tool:

The AIMMS Command Line Tool
---------------------------

.. rubric:: AIMMS command line tool

Next to accessing AIMMS from within your own programs through the AIMMS
component technologies, AIMMS also supports a command line tool through
which you can control an AIMMS project externally. You can start the
AIMMS command line tool by running

   ``AimmsCmd`` project-path

The ``AimmsCmd`` program is located in the ``Bin`` directory of your
AIMMS installation.

.. rubric:: Commands

The AIMMS command line tool offers commands to

-  assign values to sets, and to scalar and multidimensional identifier
   slices,

-  display the contents of sets, and the values of scalar and
   multidimensional identifier slices,

-  empty sets or multidimensional identifier slices,

-  retrieve the cardinality of sets or multidimensional identifier
   slices,

-  run procedures,

-  execute system commands, and

-  close the AIMMS project and quit the program.

Each command is terminated by a semicolon.

.. rubric:: Assignments

You can assign a value to sets and multidimensional identifiers and
slices thereof through one of the commands

   | ``Let`` reference ``:=`` data-expression ``;``
   | ``Let`` reference ``+=`` data-expression ``;``

where the ``:=`` operator refers to completely replacing the contents of
*reference* and the ``+=`` operator refers to a merge operation.

.. rubric:: References

A *reference* in an assignment is either

-  an identifier name such as "``Transport``", or

-  a reference to an identifier slice such as

      ``Transport('Amsterdam',j)``

   where each sliced dimension must refer to a quoted set element.

.. rubric:: Data expressions

The *data expressions* allowed in an assignment are

-  a set expression preceded by the keyword ``Set`` as in

      ``Set {'Amsterdam', 'Rotterdam'}``

   where all set elements must be quoted,

-  a ranged integer set preceded by the keyword ``Set`` as in

      ``Set {1 .. 10}``

-  a scalar numeric, element or string value as in

      | ``10``
      | ``11.7``
      | ``'an element'``
      | ``"a string"``

-  a tuple list of numeric, element or string values preceded by the
   keyword ``List`` as in

      ``List {('Amsterdam','Paris') : 10, ('Paris','London') : 20}``

   | ``List`` keyword may be optionally preceded by the keyword
     ``Strict``. In this case using an element name not present in the
     domain set will trigger an error (it will be added automatically to
     the domain set otherwise),

-  a dense multidimensional array of numeric, element or string values
   preceded by the keyword ``Array`` as in

      ``Array [[1,2],[3,4],[5,6]]``

.. rubric:: Value display

You can request AIMMS to display the contents of sets and
multidimensional identifier slices in your model through the command

   ``Display`` reference [:precision] [as Array] ``;``

For multidimensional identifier data AIMMS will, by default, use the
``List`` format described above. Through the optional "``as Array``"
clause you can instruct AIMMS to display the identifier data as a dense
array.

.. rubric:: Empty identifiers

To empty the data of sets and multidimensional identifier slices in your
model you can use the command

   ``Empty`` reference ``;``

.. rubric:: Identifier cardinality

You can request AIMMS to retrieve the cardinality of sets and
multidimensional identifier slices in your model through the command

   :any:`Card` reference ``;``

.. rubric:: Run procedures

With the command

   ``Run`` procedure-name ``;``

you can request AIMMS to run a procedure (without arguments). When
finished, AIMMS will display the return value of the procedure.

.. rubric:: Executing system commands

You can let AIMMS execute a system command through the command

   ``System`` system-command ``;``

where *system-command* is a string to be executed by command shell.

.. rubric:: Help

Through the ``Help`` command, a list with a brief description all
available commands will be displayed.

.. rubric:: Closing the project

You can close the AIMMS project and quit the command line tool through
the command

   ``Quit`` ``;``