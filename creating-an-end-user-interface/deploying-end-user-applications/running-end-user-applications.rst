.. _sec:deploy.end-user:

Running end-user applications
=============================

.. rubric:: Running end-user projects
   :name: end-user-app

An AIMMS project can run in two different modes, *developer* mode and
*end-user* mode. While the developer mode allows you to use the full
functionality described in this `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__, the end-user mode only
allows you to *access* the end-user pages of the AIMMS project that were
created in developer mode.

.. rubric:: Disabled functionality

The AIMMS end-user mode lacks the essential tools for creating and
modifying model-based applications. More specifically, the following
tools are not available in end-user mode:

-  the **Model Explorer**,

-  the **Identifier Selector**,

-  the **Page Manager**,

-  the **Template Manager**, and

-  the **Menu Builder** tool.

Thus, in end-user mode, there is no way in which an end-user can modify
the contents of your AIMMS-based application.

.. rubric:: Allowed usage

AIMMS end-users can only perform tasks specified by you as an
application developer. Such tasks must be performed through data
objects, buttons and the standard, or custom, end-user menus associated
with the end-user pages in your project. They include:

-  modifying the input data for your model in the end-user interface,

-  executing procedures within your model to read data from an external
   data source, or performing a computation or optimization step,

-  viewing model results in the end-user interface,

-  writing model results to external data sources or in the form of
   printed reports, and

-  performing case management tasks within the given framework of case
   types.

Thus, an end-user of your application does not need to acquire any
AIMMS- specific knowledge. The only requirement is that the interface
that you have created around your application is sufficiently intuitive
and clear.

.. rubric:: Requirements

Before you can distribute your AIMMS project as an end-user application,
two requirements have to be fulfilled:

-  you must have exported your application as an *end-user project* (see
   :ref:`sec:security.encrypt`), and

-  you need to associate a *startup page* with your application which
   will be displayed when your application is started by an end-user.

.. rubric:: Assigning a startup page

For every end-user project, you must associate a single page within the
project so that it becomes the project's *startup page*. Such an
association can either be made directly by selecting a page for the
'Startup Page' option in the AIMMS **Options** dialog box (see
:ref:`sec:setting.options`), or implicitly as the first opened page in
the *startup procedure* of the project using a call to the :any:`PageOpen`
function.

.. rubric:: Role of startup page

After opening your project in end-user mode, AIMMS will display the
startup page. As all communication between the end-user and your model
is conducted through end-user pages of your design, this first page
and/or its menus must provide access to all the other parts of your
AIMMS application that are relevant for your end-users. If all pages are
closed during a session, the end- user can still re-open the startup
page using the first page button |firstpage| on the **Project** toolbar,
or via the **View-First Page** menu.

.. rubric:: Startup procedure

In addition to a startup page you can also provide a startup procedure
in the project-related AIMMS options. Inside the startup procedure you
can perform any initializations necessary for an end-user to start
working with the project. Such initializations can include setting up
date or user related aspects of the project, or reading the data for
particular identifiers from a database.

.. rubric:: Replacing the splash screen

By default, AIMMS will display a splash screen during startup. When you
are opening AIMMS with a particular project, you can replace AIMMS' own
splash screen with a bitmap of your choice. If the project directory
contains a bitmap (``.bmp``) file with the same name as the project
file, AIMMS will display this bitmap file on the splash screen. In such
a bitmap you can display, for instance, version information about your
project.

.. |firstpage| image:: firstpage.png