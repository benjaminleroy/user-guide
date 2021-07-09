.. _chap:deploy:

Deploying End-User Applications
===============================

.. _deploying_end_user_applications:

.. rubric:: Deployment considerations

After a successful development phase of your AIMMS application, you have
to start thinking about its deployment. For the application to become a
successful end-user application too, you, as the application developer,
need to consider issues like *protecting your intellectual property*,
*authenticating your end-users*, and *distribution* of your application.
AIMMS offers various tools to help you in all of these areas.

.. rubric:: Application protection and authentication

AIMMS offers several levels of protection that can be applied to your
application. To protect the content of your model from being viewed by
the unauthorized users, AIMMS allows you to encrypt (parts of) your
model. To protect the application against unauthorized access you can
encrypt your application using the public keys of all authorized users.
To further arrange the appropriate level of access within an
organization, you can associate a user database with your AIMMS
application, which can then be used to authenticate individual users and
provide their level of access to your application. Protecting your AIMMS
application and authenticating its use are discussed in full detail in
:ref:`chap:security`.

.. rubric:: Application distribution

To be able to run an AIMMS project, your users will need a copy of the
project itself. To support easy project distribution, an AIMMS project
can be compacted and distributed as a single-file project. In addition,
your users need to have installed AIMMS on their computer. In order to
enter input data and/or run the model, end-users need a commercial
license of AIMMS.

.. rubric:: AIMMS PRO

A more convenient way to distribute your application to your end-users
is to use the AIMMS *P*\ ublishing and *R*\ emote *O*\ ptimization
platform. AIMMS PRO makes it possible to deploy AIMMS applications to
end-users quickly and efficiently through the AIMMS PRO Portal. More
importantly, the AIMMS PRO Portal assures end-users can access the
latest version of these AIMMS applications (and the corresponding
versions of the AIMMS software) at all times through a web browser. More
information on AIMMS PRO can be found in the AIMMS PRO `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.



This chapter gives some background on AIMMS end-user mode, and discusses
.aimmspack project files, which you can use to distribute your AIMMS
project as a single file.

.. toctree::

   running-end-user-applications
   preparing-an-aimms-application-for-distribution
