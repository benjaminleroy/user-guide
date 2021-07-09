.. _sec:deploy.aimmspack:

Preparing an AIMMS application for distribution
===============================================

.. rubric:: .aimmspack project files...

A complete AIMMS application consists of several files (see
:ref:`sec:start.files` for an overview of these files), all of which
should also be distributed to the user of the application. To make the
distribution of an AIMMS application easier, AIMMS offers the
possibility to distribute your project as a single-file project, by
packing all relevant files into a single file with the
.aimmspack extension.

.. rubric:: Creating a .aimmspack file

Turning your project into a single-file, end-user project is very
straightforward. Just select the **File-Export End User Project** menu
command which will open the **Select destination .aimmspack File**
dialog box which allows you to specify the name and location of the file
to be exported.

.. rubric:: Encryption

After having specified a destination file, the **Encryption of Exported
End-User Project** dialog box opens which allows you the security
setting for your end-user project. Encryption is described in more
detail in :ref:`sec:security.encrypt`.

.. rubric:: The .aimmspack file contents

By default AIMMS will select all files in the project directory to be
included in the .aimmspack file while ignoring all files in the
``Backup`` and :any:`Log` directories. All files associated with referenced
library projects will also be included. The project (``.aimms``) and all
source files (e.g. ``.ams`` and ``.xml`` files) for the main project and
all of the library projects involved are mandatory while the settings
for all other files can be changed through the **Select Files for
Export** dialog box (see :numref:`fig:deploy.export-select`. Note that
only include files (and folders) that are contained in the main project
folder and folders of library projects. If your project refers to files
in other locations you must make sure that these files exist on the
destination computer.

.. figure:: zipprj-select-new.png
   :alt: The **Select Files for Export** dialog box
   :name: fig:deploy.export-select

   The **Select Files for Export** dialog box

.. rubric:: Running an .aimmspack project file

The .aimmspack project files are dealt with as if they were ordinary
AIMMS project files. Both the developer and end-user version of AIMMS
are capable of running both ``.aimms`` and .aimmspack files.

.. rubric:: Unpacking an .aimmspack project file :math:`\ldots`

When a *developer* opens an .aimmspack project file, he will *always* be
prompted for a location where to unpack to. On the other hand, when an
*end-user* opens an .aimmspack project file, only the *first time*, he
will be prompted for a location where to unpack to. Any subsequent time
an end-user opens the .aimmspack file, AIMMS will look whether the
location where the .aimmspack file was unpacked previously contains the
unpacked version of the same .aimmspack file. If so, AIMMS will open the
unpacked version without user interaction. Otherwise, AIMMS will prompt
the end-user for a (new) location, unpack the .aimmspack project and run
it with AIMMS. So, when you send your end-user an updated version of a
packed project, AIMMS will notice the version change and prompt the
end-user with a question whether or not to overwrite the existing
project with the new version.

.. rubric:: :math:`\ldots` using the command line

Alternatively, you can indicate where you want the .aimmspack file to be
unpacked via the commandline argument *--unpack-folder*.

.. rubric:: Selecting an AIMMS version

If multiple AIMMS versions have been installed on the computer, you can
select the particular AIMMS version to use on an ``.aimms`` or
.aimmspack file through the right-mouse popup menu in Windows Explorer.
If you double-click an ``.aimms`` or .aimmspack the ``AimmsLauncher``
utility program will try to open the AIMMS version that most closely
matches the AIMMS version that was used to create the project.

.. |firstpage| image:: firstpage.png