.. _chap:proj-organization:

Collaborative Project Development
=================================

.. _multi_developer:



This chapter discusses the options you have in AIMMS to organize a
project in such a way that it becomes possible to effectively work on
the project with multiple developers. While it is very natural to start
working on a project with a single developer, at some time during the
development of an AIMMS application, the operational requirements of the
problem you are modeling may become so demanding that it requires
multiple developers to accomplish the task.

.. rubric:: From prototyping phase...

During the initial prototyping phase of a model, an AIMMS project is
usually still quite small, allowing a single developer to take care of
the complete development of the prototype. The productivity tools of
AIMMS allow you to quickly implement different formulations and analyze
their results, while you are avoiding the overhead of having to
synchronize the efforts of multiple people working on the prototype.

.. rubric:: ...to operational phase

During the development of an operational AIMMS application this
situation may change drastically. When an AIMMS application is intended
to be used on a daily basis, it usually involves one or more of the
following tasks:

-  retrieving the input data from one or more data sources,

-  validation and transformation of input data,

-  extending the core optimization application with various,
   computationally possibly demanding, operational requirements,

-  preparing and writing output data to one or more data sources,

-  building a professionally looking end-user GUI, and/or

-  integrating the application into the existing business environment.

Depending on the size of the application, implementing all of these
tasks may become too demanding for a single developer.

.. rubric:: Dividing a project into sub-projects

One possible approach to allow multiple developers to work on a single
AIMMS application is to divide the project into several logical
sub-projects, either based on the tasks listed in the previous
paragraph, or more closely related to the logic of your application.
AIMMS supports sub-projects in the form of model libraries. Using
libraries especially makes sense, if the functionality developed in a
library can be re-used by multiple AIMMS applications. If a library is
small enough, indivual developers may take on the development of the
library.

.. rubric:: Managing project source using a VCS

In the software development world teams commonly use a *V*\ ersion
*C*\ ontrol *S*\ ystem, such as
`git <http://en.wikipedia.org/wiki/Git_(software)>`__,
`subversion <http://en.wikipedia.org/wiki/Apache_Subversion>`__, or
`TFS <http://en.wikipedia.org/wiki/Team_Foundation_Server>`__, to share
and merge their coding work to a common repository. As all development
sources of an AIMMS application are stored as readable text files
(a.o. ``.aimms``, ``.ams`` and ``.xml``), AIMMS projects can be easily
managed using the version control system of your choice. Using a version
control system will make it straightforward to work together on a single
code base in parallel by merging the contributions of the various team
members, and to use branches to differentiate between development and
production code, or to work on multiple developments independently.
Using version control for your AIMMS projects will usually result in
higher productivity and more control.

.. rubric:: No VCS integration

Although AIMMS effectively supports the use of a version control system
for the development of your AIMMS applications, the AIMMS IDE does not
offer integration with any specific version control system. All version
control systems come with commandline and/or graphical tools for regular
version control tasks such as committing, showing logs, diffing two
versions, merging, creating branches and tags, and so on. You should use
these tools, whenever you want to commit your changes to an AIMMS
project under version control.

.. toctree::

   library-projects-and-the-library-manager
   guidelines-for-working-with-library-projects
