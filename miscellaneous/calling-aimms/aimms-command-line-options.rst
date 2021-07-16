AIMMS command line options
==========================

.. rubric:: Calling AIMMS
   :name: commandline

On the AIMMS command line, you can specify a number of options and
arguments that will influence the manner in which AIMMS is started. The
following line illustrates the general structure of a call to the AIMMS
program.

   *aimms.exe* [command-line-options] [project-file [session-arguments]]

.. rubric:: Command line options

:numref:`table:cmdline-options` provides an overview of the command line
options that you can specify. AIMMS offers both long and short option
names, and some options require a single argument. All short option
names start with a single minus (-) sign, followed by a single
character. By convention, short options that require an argument use
capital characters. The long option names are always preceded by a
double minus sign (\--), followed by a descriptive text. In general, the
long option names are easier to remember, while the short names permit a
more compact command line. Short option names without an argument may be
appended one after another with only a single minus sign at the
beginning.

.. _table:cmdline-options:

.. table:: AIMMS command line options

	========================= ============== =========================
	**Long name**             **Short name** **Argument**
	========================= ============== =========================
	*\--user*                 *-U*           user[:password]
	*\--backup-dir*           *-B*           backup directory
	*\--log-dir*              *-L*           log directory
	*\--config-dir*           *-C*           configuration directory
	*\--license*                             license name
	*\--license-wait-seconds*                seconds to wait
	*\--run-only*             *-R*           procedure name
	*\--user-database*                       user database file
	                                         maximum number of threads
	*\--minimized*            *-m*           /
	*\--maximized*            *-x*           /
	*\--hidden*                              /
	*\--as-server*                           /
	*\--end-user*             *-e*           /
	*\--no-solve*                            /
	*\--help*                 *-h*           /
	*\--unpack-folder*                       unpack folder
	*\--export-to*                           export aimmspack/folder
	========================= ============== =========================

.. rubric:: Specifying a user

When an AIMMS project is linked to an end-user database (see
:ref:`chap:security`), you must log on to the project before being able
to run it. Through the *\--user* command line option, you can specify a
user name and optionally a password with which you want to log on to the
system. When you specify just a user name, a log on screen will appear
with the provided user name already filled in. If you specify a password
as well, AIMMS will verify its correctness and skip the log on screen
altogether if the user name- password combination is acceptable.
Providing both the user name and the password is not recommended for
interactive use, but may be convenient when you want the model to run
unattended.

.. rubric:: Backup and log directories

With the *\--backup-dir* and *\--log-dir* options you can override the
default directories where AIMMS will store temporary information such as
case and model backups, the AIMMS and solver listings, and the message
log. You can modify the defaults for these directories using the project
options dialog box (see :ref:`sec:setting.options`).

.. rubric:: AIMMS configuration

By default, AIMMS stores a number of global configuration files, such as
the AIMMS license file and the solver configuration file, in the common
application area of your computer. If you want to store configuration
files in a different location, you can indicate this through the
*\--config-dir* option. You can use this option, for instance, to
indicate where the configuration files for your particular machine can
be found when the AIMMS system that you use is stored on a network disk,
and when you do not use a license server.

.. rubric:: License name

Through the *\--license* option you can select any AIMMS license that you
installed in the AIMMS **License Configuration** dialog box. 
The value that you specify for the
*\--license* option should match an entry in the **License** column in
the left pane of the **License Configuration** dialog box. In case you
are using a network license with different profiles, you should make a
different entry in the AIMMS **License Configuration** for each profile
you want to use and you can use the *\--license* option to open AIMMS
with a license with a specific profile.

.. rubric:: Network logon timeout

When you are using a network license, the license server may not have a
license available for you right away. Through the
*\--license-wait-seconds* option you can specify the number of seconds
you want AIMMS to wait for a network license to become available. If you
do not specify this option AIMMS will use a default timeout of 0
seconds. When reaching the given timeout, AIMMS will try the next
license in your license configuration, or will return with a license
error if no other licenses are available.

.. rubric:: User database location

When your application has been set up for use by multiple users, all
user and group information associated with the application is stored in
a separate (encrypted) user database (see :ref:`sec:security.auth` for
more details on this topic). Through the *\--user-database* option you
can move the location of this user database file (to for example a
single location that is shared among all users on the network) even
though you might not have developer rights to the application.

.. rubric:: Limiting the number of parallel threads

Through the option *\--max-threads* you can specify the maximum number of
(virtual) cores that AIMMS is allowed to use during the execution of
statements, the evaluation of definitions or during a parallel solve. By
default AIMMS uses the number of cores that are available on the
machine, but during a heavy load of multiple processes it might be
beneficial to limit the number of cores that AIMMS will use. This option
is ignored if you set it to a value that is larger than the actual
number of cores.

.. rubric:: Running minimized, maximized, hidden, or as server

Through the *\--minimized*, *\--hidden* and *\--maximized* options you can
indicate whether you want AIMMS to start in a minimized or hidden state
(i.e. just as a button on the task bar, or not visible at all), or to
fill up the entire screen. Running AIMMS minimized or hidden may be
convenient when AIMMS is called non-interactively from within another
program through the AIMMS API (see :ref:`lr:chap:api` of the Language
Reference). In this way, your program can use AIMMS to solve an
optimization model after which it resumes its own execution. The
``--as-server`` option extends the ``--hidden`` option, and should be
used when AIMMS is started with limited privileges by a system service
(e.g. through the Internet Information Server). It suppresses all dialog
boxes that may appear during startup of AIMMS, as well as during the
execution of your model.

.. rubric:: Developer versus end-user mode

With the *\--end-user* option you can force AIMMS to start up a project
in end-user mode using a developer license, allowing you to preview your
application as if you were an end-user without the need to explicitly
export an end-user project.
Please note that the option to emulate end-user model using an AIMMS
developer license will not work, unless it has been enabled in your
AIMMS developer license.

.. rubric:: Exporting an end-user project

Through the *\--export-to* option you can instruct AIMMS to create an
encrypted end-user project either packed to the AIMMSfile file
specified, or unpacked into a specified folder. When using this
commandline option, AIMMS will use the export settings as saved by the
previous call to the **File-Export End-User Project** menu. You can use
this commandline option, for instance, within the context of a
continuous integration server, to automate the deployment of your AIMMS
application after new commits have been pushed to the version control
repository managing the project.

.. rubric:: Specifying the unpack folder

When running an AIMMSfile file, AIMMS will ask for the folder where you
want the AIMMSfile file to be unpacked. Alteratively, you can already
specify the unpack folder through the *\--unpack-folder* commandline
option.

.. rubric:: Solverless AIMMS sessions

AIMMS strictly enforces that the number of AIMMS sessions with full
solving capabilities running on your computer simultaneously is in
accordance with your AIMMS license. Typically, for a single-user
license, this means that you can only start up a single AIMMS session
that is capable of solving optimization programs at a time. However, for
every fully capable AIMMS session, AIMMS also allows you to start up an
additional AIMMS session without solving capabilities. You can use such
a session, for instance, to make modifications to your model, while a
first session is executing an optimization run. In that case, AIMMS will
present a dialog box during start up to indicate that the session has no
solving capabilities. You can suppress this dialog box, by specifying
the *\--no-solve* command line option.

.. rubric:: Executing a procedure and terminating AIMMS

When you want to run an AIMMS project unattended, you can call AIMMS
with the *\--run-only* option. This option requires the name of a
procedure in the model, which will be executed after the project is
opened. When you use the *\--run-only* option, all other initial project
settings, such as the initial case, procedure and page settings, will be ignored. AIMMS will, however, call
the procedures ``MainInitialization``, ``PostMainInitialization``,
``PreMainTermination``, ``MainTermination``, and all library
initialization and termination procedures as usual. Once the procedure
has finished, the AIMMS session will be terminated. You can only specify
the *\--run-only* option if you also specify a project file on the
command line.

.. rubric:: Opening a project to run

AIMMS will interpret the first non-option argument on the command line
as the name of the project file with which you want to open AIMMS. If
you specify a project file, the settings of the project may initiate
model-related execution or automatically open a page within the project.

.. rubric:: Opening a project to edit

If you want to open a project for editing purposes only, you should hold
down the **Shift** key when opening the project. The initial actions
will also not be performed if the command line contains the *\--run-only*
option. In this case execution takes place from within the specified
procedure only.

.. rubric:: Passing session arguments

Directly after the name of the project file, AIMMS allows you to specify
an arbitrary number of string arguments which are not interpreted by
AIMMS, but can be used to pass command line information to the project.
In the model, you can obtain the values of these string arguments one at
a time through the predefined function :any:`SessionArgument`, which is
explained in more detail in :ref:`sec:gui.functions.control`.

.. rubric:: Example

The following call to AIMMS, will cause AIMMS to start the project
called ``transport.aimms`` in a minimized state using the user name
``batchuser`` with password ``batchpw``, run the procedure
``ComputeTransport``, and subsequently end the session. A single
argument ``"Transport Data"`` is provided as a session argument for the
model itself.

.. code-block:: batch

	aimms --minimized --user batchuser:batchpw --run-only ComputeTransport \
	      transport.aimms "Transport Data"

Note that the ``\`` character at the end of the first line serves as the
continuation character to form a single command line. Using the short
option names, you can specify the same command line more compactly as

.. code-block:: batch

	aimms -mUbatchuser:batchpw -RComputeTransport transport.aimms "Transport Data"

In this command line, the ``-m`` and ``-U`` options are combined. No
space is required between a short option name and its argument.

.. rubric:: Using session arguments

Given the above AIMMS call, you can use the function :any:`SessionArgument`
to fetch the first session argument and assign it to the string
parameter ``ODBCDataSource`` as follows.

.. code-block:: aimms

	if ( SessionArgument(1, ODBCDataSource) ) then
	    /*
	     *  Execute a number of READ statements from ODBCDataSource
	     */
	endif;

Following this statement, the string parameter ``ODBCDataSource`` will
hold the string ``"Transport Data"``. In this example, the string
parameter ``ODBCDataSource`` is intended to serve as the data source
name in one or more ``DATABASE TABLE`` identifiers, from which the input
data of the model must be read.