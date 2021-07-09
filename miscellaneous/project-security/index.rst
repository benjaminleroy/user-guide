.. _chap:security:

Project Security
================

.. _project_security:

.. rubric:: Project security

When you are creating a model-based end-user application there are a
number of security aspects that play an important role.

-  How can you protect the proprietary knowledge used in your model?

-  How can you prevent the end-users of your application from modifying
   the project (thereby creating a potential maintenance nightmare)?

-  How can you distinguish between the various end-users and their level
   of authorization within your application?



AIMMS offers several security-related features that address the security
issues listed above. These features allow you to

-  encrypt the source code of your model,

-  introduce authorization levels into your model, and

-  set up an authentication environment for your application.

This chapter describes these mechanisms in full detail, together with
the steps that are necessary to introduce them into your application.

.. toctree::

   encryption
   user-authentication-and-authorization
