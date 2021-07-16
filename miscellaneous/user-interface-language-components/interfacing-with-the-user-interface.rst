.. _sec:gui.functions:

Interfacing with the user interface
===================================

.. rubric:: Interface functions

At particular times, for instance during the execution of user-activated
procedures, you may have to specify an interaction between the model and
the user through dialog boxes and pages. To accommodate such
interaction, AIMMS offers a number of *interface functions* that perform
various interactive tasks such as

-  opening and closing pages,

-  printing pages,

-  file selection and management,

-  obtaining numeric, string-valued or element-valued data,

-  selecting, loading and saving cases, and

-  execution control.

.. rubric:: Return values

All interface functions have an integer return value. For most functions
the return value is 1 (success), or 0 (failure), which allows you to
specify logical conditions based on these values. If you are not
interested in the return value, the interface functions can still be
used as procedures.

.. rubric:: Limited use in certain cases

There are some interface functions that also return one or more output
arguments. In order to avoid possible side effects, the return values of
such functions can only be used in scalar assignments, and then they
must form the entire right hand side.

.. rubric:: Obtaining the error message

Whenever an interface function fails, an error message will be placed in
the predefined AIMMS string parameter :any:`CurrentErrorMessage`. The
contents of this identifier always refer to the message associated with
the last encountered error, i.e. AIMMS does not clear its contents.
Within the execution of your model, however, you are free to empty
:any:`CurrentErrorMessage` yourself.

.. rubric:: Example

The following statements illustrate valid examples of the use of the
interface functions :any:`FileExists`, :any:`DialogAsk`, and :any:`FileDelete`.

.. code-block:: aimms

	if ( FileExists( "Project.lock" ) ) then
	    Answer := DialogAsk( "Project is locked. Remove lock and continue?",
	                         Button1 : "Yes", Button2 : "No" ) ;

	    if ( Answer = 1 ) then
	        FileDelete( "Project.lock" ) ;
	    else
	        halt;
	    endif ;
	endif ;

The interface function :any:`DialogAsk` has a return value of 1 when the
first button is pressed, and 2 when the second button is pressed.

.. _sec:gui.functions.page:

Page Functions
~~~~~~~~~~~~~~

.. warning::

  The AIMMS WinUI is deprecated, and thus Page functions as well. Please refer to :doc:`deprecation-table`. 
  You may use the :doc:`webui/index` instead, and the :doc:`webui/library`.

.. rubric:: Model page control
   :name: page-function

The possibility of opening pages from within a model provides
flexibility compared to page tree-based navigation. Depending on a particular
condition you can decide whether or not to open a particular page, or
you can open different pages depending on the current status of your
model.

.. rubric:: Page functions

The following functions for manipulating pages are available in AIMMS.

-  :any:`PageOpen`\ (*page*) Opens page *page*.

-  :any:`PageOpenSingle`\ (*page*) Opens page *page* and closes all other.

-  :any:`PageClose`\ ([*page*]) Closes page *page*, if *page* is not
   specified, closes active page.

-  :any:`PageGetActive`\ (*page*) Returns the active page in *page*.

-  :any:`PageGetFocus`\ (*page*,\ *tag*) Returns the name of the page and
   object that have focus in *pagePar* and *tag*

-  :any:`PageSetFocus`\ (*page*,\ *tag*) Sets the focus to object *tag* on
   page *page*.

-  :any:`PageSetCursor`\ (*page*,\ *tag*,\ *scalar-reference*) Position the
   cursor of object *tag* on page *page* to *scalar-reference*.

-  :any:`PageRefreshAll` Ensure that the open pages are refreshed with the
   current data.

-  :any:`PageGetChild`\ (*page*, *childpage*) Return the name of the page
   that is the first child of *page* in *childpage*, if any.

-  :any:`PageGetParent`\ (*page*, *parentpage*) Return the name of the page
   that is the parent of *page* in *parentpage*.

-  :any:`PageGetPrevious`\ (*page*, *previouspage*) Return the name of the
   page that is the previous page of *page* in *previouspage*.

-  :any:`PageGetNext`\ (*page*, *result-page*) Return the name of the page
   that is the next page of *page* in *nextpage*.

-  :any:`PageGetNextInTreeWalk`\ (*page*, *nextpage*) Return the name of
   the page that is the next page of *page* in a depth first tree walk
   over the page tree.

-  :any:`PageGetTitle`\ (*pageName*, *pageTitle*) Return the title of a
   specific page.

-  :any:`PageGetUsedIdentifiers`\ (*page*, *identifier_set*) Return the
   identifiers used in *identifier_set*.

.. _sec:gui.functions.print:

Print Functions
~~~~~~~~~~~~~~~

.. warning::

  The AIMMS WinUI is deprecated, please refer to :doc:`deprecation-table`. 
  You may use the :doc:`webui/index` instead.

.. rubric:: Printing facilities

AIMMS provides a printing capability in the form of *print pages*.

.. rubric:: Print functions

The following functions are available for printing print pages in AIMMS.

-  :any:`PrintPage`\ (*page*\ [,\ *filename*][,\ *from*][,\ *to*]) Print
   *page* to file *filename*.

-  :any:`PrintStartReport`\ (*title*\ [,\ *filename*]) Start a print job
   with name *title*.

-  :any:`PrintEndReport` End the current print job.

-  :any:`PrintPageCount`\ (*page*) The number of sheets needed to print
   *page*.

.. _sec:gui.functions.file:

File Functions
~~~~~~~~~~~~~~

.. rubric:: File manipulation

The interactive execution of your model may involve various forms of
file manipulation. For instance, the user might indicate which names to
use for particular input and output files, or in which directory they
are (to be) stored.

.. rubric:: File functions

The following functions are available for file manipulation in AIMMS.

-  :any:`FileSelect`\ (*filename*\ [,\ *directory*][,\ *extension*][,\ *title*])
   Dialog to select an existing file.

-  :any:`FileSelectNew`\ (*filename*\ [,\ *directory*][,\ *extension*][,\ *title*])
   Dialog to select a new file.

-  :any:`FileDelete`\ (*filename*\ [,\ *delete_readonly_files*) Delete a
   file.

-  :any:`FileCopy`\ (*oldname*,\ *newname*\ [,\ *confirm*]) Copy a file.

-  :any:`FileMove`\ (*oldname*,\ *newname*\ [,\ *confirm*]) Rename or move
   a file.

-  :any:`FileAppend`\ (*filename*,\ *appendname*) Append to an existing
   file.

-  :any:`FileExists`\ (*filename*) Is *filename* an existing file?

-  :any:`FileView`\ (*filename*\ [,\ *find*]) Opens *filename* in read only
   mode.

-  :any:`FileEdit`\ (*filename*\ [,\ *find*]) Opens *filename* for text
   editing.

-  :any:`FilePrint`\ (*filename*) Print a text file to printer.

-  :any:`FileTime`\ (*filename*,\ *filetime*) Return the modification time.

-  :any:`FileTouch`\ (*filename*,\ *newtime*) Set the modification time to
   now.

.. rubric:: Directory functions

The following functions are available for directory manipulation.

-  :any:`DirectorySelect`\ (*directoryname*\ [,\ *directory*][,\ *title*])
   Select an existing directory.

-  :any:`DirectoryCreate`\ (*directoryname*) Create a directory

-  :any:`DirectoryExists`\ (*directoryname*) Is *directoryname* an existing
   directory.

-  :any:`DirectoryGetCurrent`\ (*directoryname*) Return the directory.

-  :any:`DirectoryDelete`\ (*directoryname*\ [,\ *delete_readonly_files*)
   Delete a directory.

-  :any:`DirectoryCopy`\ (*oldname*,\ *newname*\ [,\ *confirm*]) Copy a
   directory

-  :any:`DirectoryMove`\ (*oldname*,\ *newname*\ [,\ *confirm*]) Move or
   rename a directory.

.. _sec:gui.functions.dialog:

Dialog Box Functions
~~~~~~~~~~~~~~~~~~~~

.. warning::

  The AIMMS WinUI is deprecated, please refer to :doc:`deprecation-table`. 
  You may use the :doc:`webui/index` instead, and use :doc:`webui/dialog-pages`, :doc:`webui/status-bar`, :doc:`webui/download-widget` and :doc:`webui/upload-widget`.

.. rubric:: Two types of dialog boxes

During the execution of your model, it is very likely that you must
communicate particular information with your user at some point in time.
AIMMS supports two types of dialog boxes for user communication:

-  information dialog boxes, and

-  data entry dialog boxes.

In addition to these standard dialog boxes available in AIMMS, it is
also possible to create customized dialog boxes using dialog pages, and open these using the :any:`PageOpen` function
discussed in :ref:`sec:gui.functions.page`.

.. rubric:: Information dialog boxes

The following functions are available in AIMMS for displaying
information to the user.

-  :any:`DialogMessage`\ (*message*\ [,\ *title*]), and
   :any:`DialogError`\ (*message*\ [,\ *title*]) Both show *message* until
   **OK** button is pressed. They differ in icons displayed.

-  :any:`DialogAsk`\ (*message*,\ *button1*,\ *button2*\ [,\ *button3*])
   Show *message* and offer two or three choices.

-  :any:`DialogProgress`\ (*message*\ [,\ *percentage*]) Show *message* and
   progress bar. Execution is continued.

-  :any:`StatusMessage`\ (*message*) Show *message* at the bottom of the
   AIMMS window.

.. rubric:: Data entry dialog boxes

The following functions are available in AIMMS for scalar data entry
dialog boxes.

-  :any:`DialogGetString`\ (*message*,\ *reference*\ [,\ *title*]) Get a
   string.

-  :any:`DialogGetElement`\ (*title*,\ *reference*)

-  :any:`DialogGetElementByText`\ (*title*,\ *reference*,\ *element-text*)

-  :any:`DialogGetElementByData`\ (*title*,\ *reference*,\ *element-data*)

-  :any:`DialogGetNumber`\ (*message*,\ *reference*\ [,\ *decimals*][,\ *title*])

-  :any:`DialogGetPassword`\ (*message*,\ *reference*\ [,\ *title*])

-  :any:`DialogGetDate`\ (*title*,\ *date-format*,\ *date*\ [,\ *nr-rows*][,\ *nr-columns*])

.. _sec:gui.functions.case:

Case Management Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

There are several functions and identifiers available to support case
management tasks. The functions can be divided into three groups:

-  *Basic* - These functions perform the core case management tasks;
   they do not involve any dialogs.

-  *Dialog* - These functions handle the dialogs around case management
   functions; they do not do any basic case management tasks.

-  *Menu Replacement* - These functions execute similarly as the default
   actions behind the **data** menu.

Each of these three groups of functions, and the predeclared
identifiers, are briefly presented below. For details about a particular
function or identifier, the reader is referred to the Function
Reference.

.. rubric:: Basic case functions

The following functions are available in AIMMS for performing basic case
management tasks without invoking dialogs.

-  :any:`CaseFileLoad`\ (*url*\ [,\ *keepUnreferencedRuntimeLibs*]) Load a
   case file and use its name as the active case.

-  :any:`CaseFileMerge`\ (*url*\ [,\ *keepUnreferencedRuntimeLibs*]) Merge
   a case file in.

-  :any:`CaseFileSave`\ (*url*,\ *contents*) Save the data to a file.

-  :any:`CaseFileGetContentType`\ (*url*,\ *contentType*) Get the current
   content type.

-  :any:`CaseFileURLtoElement`\ (*url*\ [,\ *caseFileElement*]) Find or
   create an element in corresponding to *url*.

-  :any:`CaseCompareIdentifier`\ (*case1*,\ *case2*,\ *identifier*,\ *suffix*,\ *mode*)
   Check whether the data of an identifier differs in two case files.

-  | :any:`CaseCreateDifferenceFile`\ (*case*,\ *filename*,\ *diff-types*
   | .8cm,\ *absolute-tolerance*,\ *relative-tolerance*,\ *output-precision*)

Here the arguments are:

-  *case*, *case1* and *case2* are element parameters in :any:`AllCases`.

-  *url*, *case-path*, and *filename* are strings.

-  *contents* an element of :any:`AllCaseFileContentTypes`

-  *contentType* an element parameter in ``AllSubsetsOfAllIdentifiers``

-  *keepUnreferencedRuntimeLibs*, 0 or 1, default 1.

-  *identifier* in :any:`AllIdentifiers`

-  *suffix* in :any:`AllSuffixNames`

-  *mode* in :any:`AllCaseComparisonModes`

-  *diff-type* in :any:`AllDifferencingModes`

-  *absolute-tolerance*, *relative-tolerance* and *output-precision*
   arguments are numerical, scalar values.

.. rubric:: Case dialog functions

The following functions are available that handle the dialogs around
case management, but do not perform the actual case management tasks:

-  :any:`CaseDialogConfirmAndSave`\ () Handles the standard "Save your data
   before continuing" dialog.

-  :any:`CaseDialogSelectForLoad`\ (*url*) Handles the dialog for selecting
   a case file.

-  :any:`CaseDialogSelectForSave`\ (*url*, *contentType*) Handles the
   dialog for saving data and selecting a content type.

-  :any:`CaseDialogSelectMultiple`\ (*caseSelection*) Handles the selection
   of multiple cases.

Here the arguments are:

-  *url* a string parameter

-  *contentType* an element parameter in :any:`AllCaseFileContentTypes`

-  *caseSelection* a subset of :any:`AllCases`,

.. rubric:: Data manamement functions

The function :any:`DataManagementExit`\ () checks whether any data should
be saved according to the active data management style. If any of the
data needs saving, a dialog box is displayed, in which the user can
select to save the data, not to save the data, or to cancel the current
operation.

.. rubric:: Data menu functions

These functions emulate the default menu items of the **Data** menu,
they do not have any arguments.

-  :any:`CaseCommandLoadAsActive`\ () The default action behind the **Data - Load Case - As Active**
   menu item.

-  :any:`CaseCommandLoadIntoActive`\ () The default action behind the **Data - Load Case - Into Active**
   menu item.

-  :any:`CaseCommandMergeIntoActive`\ () The default action behind the **Data - Load Case - Merging into
   Active** menu item.

-  :any:`CaseCommandNew`\ () The default action behind the **Data - New Case** menu item.

-  :any:`CaseCommandSave`\ () The default action behind the **Data - Save Case** menu item.

-  :any:`CaseCommandSaveAs`\ () The default action behind the **Data - Save Case As** menu item.

.. rubric:: Case file related identifiers

There are a number of predeclared identifiers available for the
management of case files. They are:

-  the set :any:`AllCases`, a subset of :any:`AllDataFiles`, contains the references to the case files
   accessed during the current AIMMS session,

-  the parameter :any:`CurrentCase` in :any:`AllCases` is the reference to the current case,

-  The parameter :any:`CurrentCaseFileContentType` specifies the default case content type,

-  the set :any:`AllCaseFileContentTypes` contains those subsets of :any:`AllIdentifiers` that are used to save data, and

-  the string parameter :any:`CaseFileURL` contains, for each case file referenced, the url
   as a string.

.. _sec:gui.functions.control:

Execution Control Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Execution control
   :name: exec-control

During the execution of your AIMMS application you may need to execute
other programs, delay the execution of your model, get the command line
arguments of the call to AIMMS, or even close your AIMMS application.

.. rubric:: Control functions

The following execution control functions are available in AIMMS.

-  :any:`Execute`\ (*executable*\ [,\ *commandline*][,\ *workdir*][,\ *wait*][,\ *minimized*])

-  :any:`ShowHelpTopic`\ (*topic*\ [,\ *filename*])

-  :any:`OpenDocument`\ (*document*)

-  :any:`Delay`\ (*delaytime*)

-  :any:`ScheduleAt`\ (*starttime*,\ *procedure*)

-  :any:`ProjectDeveloperMode`

-  :any:`SessionArgument`\ (*argno*, *argument*)

-  :any:`ExitAimms`\ ([*interactive*])

.. _sec:gui.functions.debug:

Debugging Information Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Debugging information
   :name: debug-info

To help you investigate the execution of your model AIMMS offers several
functions to control the debugger and profiler from within your model.
In addition, a number of functions are available that help you
investigate memory issues during execution of your model.

.. rubric:: Execution information functions

The following execution information functions are available in AIMMS.

-  :any:`IdentifierMemory`\ (*identifier*\ [,\ *include-permutations*])

-  | :any:`MemoryStatistics`\ (*filename*\ [,\ *append-mode*][,\ *marker-text*][,\ *show-leaks-only*
     ]
   | .8cm[,\ *show-totals*][,\ *show-since-last-dump*][,\ *show-mem-peak*][,\ *show-small-
     .8cm block-usage*])

-  | :any:`IdentifierMemoryStatistics`\ (*identifier-set*,\ *filename*\ [,\ *append-mode*]
   | .8cm[,\ *marker-text*][,\ *show-leaks-only*
     ][,\ *show-totals*][,\ *show-since-last-dump*]
   | .8cm[,\ *show-mem-peak*][,\ *show-small-block-usage*][,\ *aggregate*])

.. rubric:: Profiler control

The following profiler control functions are available in AIMMS.

-  :any:`ProfilerStart`\ ()

-  :any:`ProfilerPause`\ ()

-  :any:`ProfilerContinue`\ ()

-  :any:`ProfilerRestart`\ ()

.. _sec:gui.functions.license:

Obtaining License Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: License information functions

The licensing functions discussed in this section allow you to retrieve
licensing information during the execution of your model. Based on this
information you may want to issue warnings to your end-user regarding
various expiration dates, or adapt the execution of your model according
to the capabilities of the license.

.. rubric:: License functions

The following licensing functions are available in AIMMS.

-  :any:`LicenseNumber`\ (*license*)

-  :any:`LicenseStartDate`\ (*date*)

-  :any:`LicenseExpirationDate`\ (*date*)

-  :any:`LicenseMaintenanceExpirationDate`\ (*date*)

-  :any:`LicenseType`\ (*type*,\ *size*)

-  :any:`AimmsRevisionString`\ (*revision*)