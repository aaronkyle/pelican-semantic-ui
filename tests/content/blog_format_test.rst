################
Blog Format Test
################

:date: 2010-10-03
:modified: 2010-10-04 18:40
:tags: rst
:category: test
:slug: blog-format-test
:summary: Test rst format

Inline Markup
=============

- *emphasis*
- **strong emphasis**
- `interpreted text`
- ``inline literal``

中文 Inline Markup
++++++++++++++++++

- 這是\ *強調*\ 用法
- 這是\ **強調**\ 用法
- 這是\ `解譯文`\ 用法
- 這是\ ``行內``\ 用法

Hyper Link
==========

External hyperlinks, like Python_.

.. _Python: http://www.python.org/

External hyperlinks (embedded URIs), like `Python <http://www.python.org/>`_.

`phrase reference`_

inline internal target _`phrase reference` 。

Internal crossreferences, like example_.

.. _example:

This is an example crossreference target.

Footnote references, like [5]_. 
Note that footnotes may get 
rearranged, e.g., to the bottom of 
the "page".

.. [5] A numerical footnote. Note 
   there's no colon after the ``]``.


Autonumbered footnotes are 
possible, like using [#]_ and [#]_.

.. [#] This is the first one. 
.. [#] This is the second one.

They may be assigned 'autonumber 
labels' - for instance, 
[#fourth]_ and [#third]_.

.. [#third] a.k.a. third_

.. [#fourth] a.k.a. fourth_


Citation references, like [CIT2002]_. 
Note that citations may get 
rearranged, e.g., to the bottom of 
the "page".

.. [CIT2002] A citation 
   (as often used in journals).

Citation labels contain alphanumerics, 
underlines, hyphens and fullstops. 
Case is not significant.

Given a citation like [this]_, one 
can also refer to it like this_.

.. [this] here.


Implicit Hyperlink Targets:

- section titles `中文 Inline Markup`_
- footnotes 5_
- citations this_

Lists
=====

- This is item 1 
- This is item 2

+ This is item 1 
+ This is item 2

3. This is the first item 
4. This is the second item
5. This item is auto-enumerated

what 
  Definition lists associate a term with 
  a definition. 

:Authors: 
    Tony J. (Tibs) Ibbs, 
    David Goodger
    (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08 
:Dedication: To my father.

Blocks
======

Block quotes are just:

    Indented paragraphs,

        and they may nest.

A paragraph containing only two colons 
indicates that the following indented 
or quoted text is a literal block. 

:: 

  Whitespace, newlines, blank lines, and 
  all kinds of markup (like *this* or 
  \this) is preserved by literal blocks. 

  The paragraph containing only '::' 
  will be omitted from the result. 

| Line blocks are useful for addresses, 
| verse, and adornment-free lists. 
| 
| Each new line begins with a 
| vertical bar ("|"). 
|     Line breaks and initial indents 
|     are preserved. 
| Continuation lines are wrapped 


Tables
======

Grid table:

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

Simple table:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======

Other
=====

.. This text will not be shown 
   (but, for instance, in HTML might be 
   rendered as an HTML comment)

----

Inline Role
===========

Basically, it was almost rewritten. :code:`run('pelican -s pelicanconf.py')` Some dependencies from the old version are dead. Swig is officialy dead, and AngularJS, well, it's not dead, but it's migrating to Angular 2, so it was more easy to remove it.

- E = mc\ :sup:`2`

Block Directive
===============

.. code-block:: python

    @task
    def build():
        """Build local version of site"""
        run('pelican -s pelicanconf.py')

.. DANGER::
   Beware killer rabbits!

.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

.. figure:: https://snap-photos.s3.amazonaws.com/img-thumbs/960w/DLIRRCCYBR.jpg
   :scale: 25 %
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).