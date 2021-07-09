Introduction and motivation
===========================

.. rubric:: Unforeseen surprises ...

Even though you have taken the utmost care in constructing your linear
optimization model, there are often unforeseen surprises that force you
to take a further look at the particular generated model at hand. Why is
the model infeasible or unbounded? Why is the objective function value
so much different from what you were expecting? Are the individual
constraints generated as intended? Why is the number of individual
constraints so large? Why are the observed shadow prices so
unrealistically high (or low)? These and several other related questions
about the matrix and the solution need further investigation.

.. rubric:: ... are not easily explained

The answer to many model validation questions is not easily discovered,
especially when the underlying optimization model has a large number of
individual constraints and variables. The amount of information to be
examined is often daunting, and an answer to a question usually requires
extensive analysis involving several steps. The functionality of the
math program inspector is designed to facilitate such analysis.

.. rubric:: Some of the causes

There are many causes of unforeseen surprises that have been observed in
practice. Several are related to the values in the matrix. Matrix input
coefficients may be incorrect due to a wrong sign, a typing error, an
incorrect unit of measurement, or a calculation flaw. Bounds on
variables may have been omitted unintentionally. Other causes are
related to structural information. The direction of a constraint may be
accidentally misspecified. The subsets of constraints and variables may
contain incorrect elements causing either missing blocks of constraints
and variables, or unwanted blocks. Even if the blocks are the correct
ones, their index domain restrictions may be missing or incorrect. As a
result, the model may contain unwanted and/or missing constraints and/or
variables.

.. rubric:: Purpose

The purpose of the mathematical program inspector included in AIMMS is
to provide you with

-  insight into the (structure of the) generated model and its solution
   (if present), and

-  a collection of tools to help you discover errors in your model ,
