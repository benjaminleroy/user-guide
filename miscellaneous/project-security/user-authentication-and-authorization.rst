.. _sec:security.auth:

User authentication and authorization
=====================================

.. rubric:: User authentication
   :name: auth

When an application is set up for use by multiple users through AIMMS
PRO, it is usually considered desirable to limit access to the
application to particular (groups of) users, make sure that users have
access to only those parts of the application that are of interest to
them, and can be given or denied the right of access to each others
data.

.. rubric:: Authorization via AIMMS PRO portal

When publishing an application on a AIMMS PRO server, you can manage
access to your application through the AIMMS PRO portal. The AIMMS PRO
documentation :doc:`pro/user-man` decribes more details about
the setup of users and groups for your application.

.. rubric:: Authorization via model

Next to arranging access to your application application-wide through
the PRO portal, the PRO system library extends your model with
functionality to access user- and group-related information from within
your AIMMS application. More, specifically, through the PRO library
function

   ``pro::GetCurrentUserInfo``

you can retrieve the currently connected PRO user name and the PRO group
membership of the currently connected user.

.. rubric:: Role-based security

Using the PRO user name and groups discussed above, you can set up your
own customized role-based security scheme within your application. You
can accomplish this by associating roles within your application with
group membership of particular groups defined through the user
management facilities in the AIMMS PRO portal. If PRO user management is
linked to your Active Directory environmoment, role-based authorization
to your application can also be arranged directly through your company's
Active Directory environment.

.. rubric:: Example

Assume that ``ExecutionAllowed`` is a two-dimensional parameter defined
over a set ``AllApplicationRoles`` declared in your model, of which the
actual set of PRO groups, retrieved via ``pro::GetCurrentUserInfo``, is
a subset, and a user-defined set of application-specific
``ActionTypes``. Then the following code illustrates the to allow or
forbid a certain statement to be executed in a role-based manner.

.. code-block:: aimms

	if ( exists(appRole | ExecutionAllowed(appRole, 'Solve') ) then
	    solve OptimizationModel;
	else
	    DialogError( "None of your application roles does allow you\n" +
	                 "to solve the optimization model" );
	endif;

.. rubric:: Use in the interface

You can also use parameters defined over ``AllApplicationRoles`` to
influence the appearance and behavior of the end-user interface. More
specifically, the following aspects of an AIMMS end-user interface can
be influenced through the nonzero status of (indexed) parameters:

-  the access to a page through the page tree-based navigational
   controls,

-  the visibility of graphical (data) objects on a page,

-  the read-only status of data in a data object, and

-  the visibility and enabled/disabled status of menu items and buttons.

Note that both the Windows and browser-based AIMMS UIs support such
dynamic model-based access controls.