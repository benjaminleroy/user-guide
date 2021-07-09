.. _sec:setting.project:

End-user project setup
======================

.. rubric:: Setting up an end-user project

A number of options and settings are of particular importance when you
want to set up a project in such a manner that it is ready to be used by
end-users. You can find these options in the **Project-Startup &
authorization** and the **Project-Appearance** sections of the
**Options** dialog box. This section discusses the most important
options.

.. rubric:: Startup procedure

With the *startup procedure* option you can select a procedure within
your model which you want to be executed during the start up of your
project. Such a procedure can perform, for instance, all the necessary
data initialization for a proper initial display of the end-user GUI
automatically, thus preventing your end-users from having to perform
such an initialization step themselves.

.. rubric:: Startup page

With the *startup page* option, you can indicate the page which AIMMS
will display at start up. It is important to specify a startup page for
end-user projects, as all data communication with the model must take
place through end- user pages designed by you. Therefore, you should
also ensure that every relevant part of your application can be reached
through the startup page.

.. rubric:: Startup by-pass

In a developer project you can by-pass the startup sequence by holding
down the Shift key when you select the project to be opened.

.. rubric:: Project title

By default, AIMMS will display the name of the currently loaded project
in the title bar of the AIMMS window. Using the *project title* option
you can modify this title, for instance to provide a longer description
of your project.