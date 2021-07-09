.. _sec:proj-organization.working:

Guidelines for working with library projects
============================================

.. rubric:: Identifying independent tasks

Unless you started using library projects from scratch, you need to
convert the contents of your AIMMS project as soon as you decide to
divide the project into multiple library projects. The first step in
this process is to decide which logical tasks in your application you
can discern that meet the following criteria:

-  the task represents a logical unit within your application that is
   rather self-contained and can possible be shared with other AIMMS
   projects,

-  the task can be comfortably and independently worked on by a separate
   developer or developer team, and

-  the task provides a limited interface to the main application and/or
   the other tasks you have identified.

Good examples of generic tasks that meet these criteria are the tasks
listed on :ref:`chap:proj-organization`. Once your team of developers
agrees on the specific tasks that are relevant for your application, you
can set up a library project for each of them.

.. rubric:: Library interface...

The idea behind library projects is to be able to minimize the
interaction between the library, the main project and other library
projects. At the language level AIMMS supports this by letting you
define an *interface* to the library, i.e. the set of public identifiers
and procedures through which the outside world is allowed to connect to
the library. Library identifiers not in the interface are strictly
private and cannot be referenced outside of the library. The precise
semantics of the interface of a library module is discussed in
:ref:`lr:sec:module.library` of the Language Reference.

.. rubric:: ... used in model and GUI

This notion of public and private identifiers of a library module does
not only apply to the model source itself, but also propagates to the
end-user interface. Pages defined in a library can access the library's
private identifiers, while paged defined outside of the library only
have access to identifiers in the interface of the library.

.. rubric:: Minimal dependency

The concept of an interface allows you to work independently on a
library. As long as you do not change the declaration of the identifiers
and procedures in its interface, you have complete freedom to change
their implementation without disturbing any other project that uses
identifiers from the library interface. Similarly, as long as a page or
a tree of pages defined in a library project is internally consistent,
any other project can add a reference to such pages in its own page
tree. Pages outside of the library can only refer to identifiers in the
library interface, and hence are not influenced by changes you make to
the library's internal implementation.

.. rubric:: Conversion to library projects

If your application already contains model source and pages associated
with the tasks you have identified in the previous step, the next step
is to move the relevant parts of your AIMMS project to the appropriate
libraries. You can accomplish this by simply dragging the relevant nodes
or subtrees from any of the trees tree in the main project to associate
tree in a library project. What should remain in the global project are
the those parts of the application that define the overall behavior of
your application and that glue together the functionality provided by
the separate library projects.
