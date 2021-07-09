.. _chap:debug:

Debugging and Profiling an AIMMS Model
======================================



After you have developed an (optimization) model in AIMMS, it will most
probably contain some unnoticed logical and/or programming errors. These
errors can cause infeasible solutions or results that are not entirely
what you expected. Also, you may find that the execution times of some
procedures in your model are unacceptably high for their intended
purpose, quite often as the result of only a few inefficiently
formulated statements. To help you isolate and resolve such problems,
AIMMS offers a number of diagnostic tools, such as a debugger and a
profiler, which will be discussed in this chapter.

.. toctree::

   the-aimms-debugger
   the-aimms-profiler
   observing-identifier-cardinalities
