Working with Cases
==================

.. rubric:: Case management tasks

A case file is a single file containing the data of some identifiers in
an AIMMS model. The **Data** menu is the main tool through which you can
accomplish tasks such as saving, loading, merging, and comparing case
files. This menu item is part of the developer menu and is available by
default on all end-user pages.

.. rubric:: The active case

In AIMMS, all the data that you are currently working with, is referred
to as the *active* case. If you have not yet loaded or saved a case
file, the active case is *unnamed*, otherwise the active case is *named*
after the name of the last loaded or saved case file on disk. If the
active case is named, its name is displayed in the status bar at the
bottom of the AIMMS window.

.. rubric:: Saving a case file

When you save a named active case, AIMMS will save it to the associated
case file on disk by default, thereby overwriting its previous contents.
If the active case is unnamed, or when you try to save a case using the
**Data-Save Case As** menu, AIMMS will open the **Save Case** dialog box
illustrated in :ref:`fig:cases.case-save`.

.. _case-save:
.. figure:: case-save.png
   :alt: The **Save Case File** dialog box
   :name: fig:cases.case-save

   The **Save Case File** dialog box

In the **Save Case File** dialog box you can enter the name of the case
file, and, optionally, select the folder in which the case file is to be
stored. After successfully saving a case file through the **Save Case
File** dialog box, the active case will become named.

.. rubric:: Loading a case file

AIMMS supports three modes for loading the data of a case file, as
summarized in the following table:

.. container:: center

  +-------------------+----------------+-----------+---------+
  | mode              | changes name   | replaces  | merges  |
  |                   |                |           |         |
  |                   | of active case | data      | data    |
  +===================+================+===========+=========+
  | load as active    |      ✓         |     ✓     |         |
  +-------------------+----------------+-----------+---------+
  | load into active  |                |     ✓     |         |
  +-------------------+----------------+-----------+---------+
  | merge into active |                |           |    ✓    |
  +-------------------+----------------+-----------+---------+

The modes are explained in more detail below.

.. rubric:: Load as active

The most frequently used mode for loading a case file is loading the
case file *as active*, through the **Data-Load Case-As Active** menu.
Loading a case file as active completely replaces the active data of all
identifiers in the case file being loaded. Data of identifiers that are
not stored in the case file, remain unchanged. In addition, the active
case will be named after the loaded case file. Before loading a case
file as active, AIMMS will ask you whether the current active case data
needs to be saved whenever this is necessary.

.. rubric:: Load into active

Loading a case file *into active*, through the **Data-Load Case-Into
Active** menu, is completely identical to loading a case as active, with
the exception that the name of the active case will not be changed.
Thus, by loading data into the active case you can replace part, or all,
of the contents of the active case with data obtained from another case
file.

.. rubric:: Merge into active

*Merging* a case file *into active*, through the **Data-Load Case-Merge
Into Active** menu, does not change the name of the active case either.
Merging a case file into the active case partially replaces the data in
the active case with only the nondefault values stored in the loaded
case file. Data in the active case, for which no associated nondefault
values exist in the merged case file, remain unchanged.

.. rubric:: Starting a new case

Using the **Data-New Case** menu item, you can instruct AIMMS to start a
new, unnamed, active case. However, the data in the active case will
remain *unchanged*. Before starting a new case, AIMMS will ask you
whether the current active case data needs to be saved.