.. _sec:setting.solver:

Solver configuration
====================

.. rubric:: Configuring solvers

With every AIMMS system you can obtain a license to use particular
solvers to solve mathematical programs of a specific type. As AIMMS
provides a standardized interface to its solvers, it is even possible
for you to link your own solver to AIMMS. This section provides an
overview of how to add solvers to your system or modify the existing
solver configuration.

.. rubric:: Solver configuration dialog box

You can obtain a list of solvers currently known to your AIMMS system
through the **Settings-Solver Configuration** menu. This will open the
**Solver Configuration** dialog box illustrated in
:numref:`fig:setting.solver-config`.

.. figure:: slv-cfg-new.png
   :alt: The **Solver Configuration** dialog box
   :name: fig:setting.solver-config

   The **Solver Configuration** dialog box

The dialog box shows an incidence matrix between all available solver
and types of mathematical programs. An 'x' indicates the capability of a
specific solver to solve mathematical programs of a particular type. A
bold '**X**' indicates that the specific solver is used as the default
solver for mathematical problems of a particular type.

.. rubric:: Modifying solver settings

The buttons on the right-hand side of the dialog box let you globally
modify the solver configuration of your AIMMS system. Through these
buttons you can perform tasks such as:

-  modify the default solver for a particular model type, and

-  add or delete solvers.

.. rubric:: Selecting default solver

With the **Set Default** button you can set the default solver for a
particular type of mathematical program. AIMMS always uses the default
solver when solving a mathematical program of a particular type. A run
time error will occur, if you have not specified an appropriate solver.

.. rubric:: Adding a solver

When you want to add an additional solver to your system, you can select
the **Add** button from the **Solver Configuration** dialog box,
respectively. This will open a **Solver Configuration Data** dialog box
as shown in :numref:`fig:setting.solver-data`.

.. figure:: slv-data-new.png
   :alt: The **Solver Configuration Data** dialog box
   :name: fig:setting.solver-data

   The **Solver Configuration Data** dialog box

In this dialog box you have an overview of the interface DLL, the name
by which the solver is known to AIMMS and any appropriate arguments that
may be needed by the solver.

.. rubric:: Select solver DLL

In the **Solver DLL** area of the **Solver Configuration Data** dialog
box you can select the DLL which provides the interface to the solver
that you want to link to AIMMS. AIMMS determines whether the DLL you
selected is a valid solver DLL, and, if so, automatically adds the
solver name stored in the DLL to the **Description** field.

.. rubric:: Solver arguments

In the **Arguments** area of the **Solver Configuration Data** dialog
box you can enter a string containing solver-specific arguments. You may
need such arguments, for instance, when you have a special licensing
arrangement with the supplier of the solver. For information about which
arguments are accepted by specific solvers, please refer to the help
file accompanying each solver.

.. rubric:: Installation automatically adds

After you install a new AIMMS version, AIMMS will automatically add the
solvers available in that installation to the **Solver Configuration**
dialog box. If the newly installed solver is the first solver of a
particular type, AIMMS will also automatically make the solver the
default solver for that type. Thus, after installing a new AIMMS system,
you do not have to worry about configuring the solvers in most cases,
provided of course that your AIMMS license permits the use of the
solvers you have installed.

.. rubric:: Using a nondefault solver

By modifying the value of the predefined element parameter
:any:`CurrentSolver` in the predefined :any:`AllSolvers` during run time you
can, at any time during the execution of your model, select a nondefault
solver for a given mathematical programming type that you want AIMMS to
use during the next :any:`solve <solve>` statement for a mathematical program of
that type. At startup, AIMMS will set ``CurrentLPSolver`` to the default
LP solver as selected in the solver configuration dialog box.