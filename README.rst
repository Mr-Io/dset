dset - Fast Disjoint-Set in Python
==================================
.. ini-badges

|Python| |Version| |License|

.. |Python| image:: https://img.shields.io/pypi/pyversions/dset.svg
    :target: https://pypi.org/project/dset/

.. |Version| image:: https://img.shields.io/pypi/v/dset.svg
    :target: https://pypi.org/project/dset/

.. |License| image:: https://img.shields.io/github/license/Mr-Io/dset.svg
    :target: https://pypi.org/project/dset/

.. end-badges

**A Disjoint-Set implementation which makes use of the the "Union by Rank" and "Path Compression" heuristic
optimizations while being as simple and effective as possible.**

It support the following operations:

* **Find-Set** in *O(1)* amortized running time
* **Union** in *O(1)* amortized running time

*Check end notes for additional information about running times*

Why?
----
Sometimes, specially  during algorithm competitions, a Union-Find data structure is needed
to solve a certain problem (e.g. when implementing Kruskal's MST algorithm) In those cases,
we usually use whatever off-the-shelf implementation we happen to find in PyPI and, many times,
we get the infamous submission fail *Time Limit Exceed(TLE)* because that specific
Disjoint-Set implementation is not fast enough...

Worry not! A fast and simple enough (you can copy paste the code `here`_) disjoint-set implementation
is now available:

Installation
------------
.. code-block:: console

    $ pip install dset

Usage
-----
.. code-block:: python

    >>> import dset
    >>> s1 = dset.Set()                 # To create new sets objects (it runs in O(1))
    >>> s2 = dset.Set()
    >>> s3 = dset.Set()
    >>> dset.groups()                   # To check the number of different groups (it runs in O(1))
    3
    >>> dset.find(s1) == dset.find(s2)  # To check if two sets are in the same group
    False
    >>> dset.union(s1, s2)              # to group s1 and s2 sets together
    >>> dset.groups()                   # Now there are only 2 groups: s1-s2 and s3
    2
    >>> dset.find(s1) == dset.find(s2)  # They are in the same group s1-s2
    True
    >>> dset.find(s2) == dset.find(s3)  # They are in distinct groups s1-s2 and s3
    False
    >>> dset.union(s2, s1)              # do nothing (no need to check if s1 and s2 belong to the same group)
    >>> dset.groups()                   # Same as before only 2: s1-s2 and s3
    2
    >>> dset.union(s1, s3)              # group s1-s2 and s3 together.
    >>> dset.groups()                   # Now there is only one group: s1-s2-s3
    1
    >>> dset.find(s1) == dset.find(s2)  # All the sets are in the same groups s1-s2-s3
    ... dset.find(s2) == dset.find(s3)
    ... dset.find(s1) == dset.find(s3)
    True
    True
    True

Future improvements
-------------------
* Make official Sphinx Documentation. (minor releases)
* Make test suite. (minor releases)
* Change to a list-based implementation (major-minor release)
    * Improve running time (constant terms)
    * Improve memory space (constant terms)

* Make the package C-based. (major-minor release)
    * Improve running time (constant terms)

.. _notes:

Notes on Complexity Running Times
---------------------------------
Separately, either "Union by Rank" or "Path Compression" improves the running time of
the operations on disjoint-sets. Alone, "Union by Rank" yields a running time
of *O(m log n)*, where *m* is the number of Union and Find-Set operations and *n* is the number
of sets.

The improvement is even greater when we use the two heuristics together; the worst-case running
time is *O(m f(n)),*  where *f(n)* is a very slowly growing function, the Inverse Ackermann function
(e.g. for *n* equal to the number atoms in the universe, *f(n)* is only 4)
So for any conceivable application, we can consider the running time of *m* Union + Find-Set operations to be
*O(m)* and therefore both Union and Find-Set operations have *O(1)* amortized running time in practice.


.. _`here`: https://github.com/Mr-Io/dset/blob/master/dset.py
