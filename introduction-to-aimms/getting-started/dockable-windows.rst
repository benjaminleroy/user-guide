.. _sec:start.dockable:

Dockable windows
================

.. rubric:: Support for dockable windows

Dockable windows are an ideal means to keep frequently used tool windows
in an development environment permanently visible, and are a common part
of modern **I**\ ntegrated **D**\ evelopment **E**\ nvironments (IDE)
such as *Visual Studio .NET*.

.. rubric:: Docking states

Dockable windows can be used in a *docked*, *auto-hidden*, or *floating*
state. Whether a dockable window is in a docked, auto-hidden or floating
state can be changed at runtime through drag-and-drop.

.. rubric:: Docked windows

When docked, the tool windows are attached to the left, right, top or
bottom edge of the client area of the main AIMMS window. By default, all
modeling tools discussed in :ref:`sec:start.tools` are docked at the
left edge of the AIMMS window, as illustrated in
:numref:`fig:start.docking`.

.. figure:: docking-new.png
   :alt: Example of a **Model Explorer** docked at the left edge
   :name: fig:start.docking

   Example of a **Model Explorer** docked at the left edge

.. rubric:: Tool windows persistence

AIMMS automatically stores the location and size of each tool window.
This information is used to restore the location and size of each tool
window whenever an AIMMS session is started.

.. rubric:: Dragging windows

By dragging the windows caption of a docked window and moving the cursor
around the edges of the AIMMS window, you can move the docked window to
another position. While hovering over a drop target, a blue rectangle
(as illustrated in Figure  :numref:`fig:start.dnd`) snaps into place at
the appropriate location, whenever a dockable window is ready to be
docked at the location corresponding to the drop target. The area of a
docked window can also be split into two by dragging another dockable
window into the upper, lower, left or right part of docked window. In
all these cases, a blue rectangle shows how a dockable window will be
docked when you release the mouse at that time.

.. figure:: drop-targets.png
   :alt: Drag-and-drop windows
   :name: fig:start.dnd

   Drag-and-drop windows

.. rubric:: Auto-hidden windows

In auto-hidden state, a dockable window is normally collapsed as a
button to the upper, lower, left or right edge of the main AIMMS window.
When you push the button associated with a collapsed window, it is
expanded. When an expanded tool window looses focus, it is collapsed
again. By clicking the pushpin button |auto-hide| in the caption of a
docked/collapsed window, you can change the window's state from docked
to auto-hide and back.

.. rubric:: Floating tool windows

By dragging a tool window away from an edge of the main AIMMS window, it
becomes floating. When AIMMS is the active application, floating tool
windows are always visible on top of all other (non-floating) AIMMS
windows. Floating windows can also be shown outside the main AIMMS
window frame.

.. rubric:: Tabbed MDI mode

By default, all pages and attribute forms are shown in *tabbed MDI*
mode. In :numref:`fig:start.docking` the main page of the application is
displayed in tabbed MDI mode, with the attribute windows of two
identifiers in the model accessible through tabs. Tabbed MDI windows
occupy the remaining space of the client area of the main AIMMS window
that is not occupied by docked windows. This implies that you do not
have control over the size of tabbed MDI windows. Therefore, if you use
tabbed MDI mode in your AIMMS application, it makes sense to make all
the pages in your model resizable (see :ref:`chap:resize`). However, the
display mode of a page can be changed to docked (by checking the **Allow
User Dockable** option on the **Page Properties** dialog box). This
would for example allow you to turn a page into a floating window and
display it on you second monitor.

.. rubric:: Tab groups

When you drag the tab associated with a document window in the document
window area, you can move the document window into a new or existing
*tab group*, at the left, right, top or bottom of the current tab group.
Tab groups effectively split the document window area into multiple
parts, each of which can hold one ore more tabbed MDI windows. As with
dragging dockable windows, a drag rectangle shows where the window will
be positioned if you drop it at that moment. Tab groups are very
convenient, for instance, if you want to view two attribute windows
simultaneously.

.. |auto-hide| image:: auto-hide.png