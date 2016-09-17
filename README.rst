===========
structmaker
===========

Overview
========

Automatically generate random C structures. Structmaker contains an internal
probabilistic model of what a sensible (subset) of C structure looks like, and
uses that model to generate new code.

Future work will include exposing the model details for configuration.

|license|

   

Installing
==========

You can install the latest stable version from github

.. code:: console

    $ git clone https://github.com/AndrewWalker/structmaker
    $ cd structmaker
    $ pip install . --user


Examples
========

Generate some random structures.

.. code:: console

    $ structmaker -n 20 

For example, generating three random structures might give something like.

.. code:: console

    $ structmaker -n 3

    #ifndef STRUCTMAKER_AUTOGEN_H
    #define STRUCTMAKER_AUTOGEN_H

    #include <cstdint>

    struct S0
    {
        uint8_t f0;
        uint32_t f1;
    };

    struct S1
    {
        int16_t f0;
        uint32_t f1;
        uint16_t f2;
        uint32_t f3;
        int16_t f4;
        S0 f5;
        double f6;
    };

    struct S2
    {
        S0 f0;
        int8_t f1;
        uint16_t f2;
        int32_t f3;
        double f4;
    };

    #endif



Contributing
============

If you experience problems , `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.



.. _log them on Github: https://github.com/AndrewWalker/structmaker/issues
.. _fork the code: https://github.com/AndrewWalker/structmaker
.. _submit a pull request: https://github.com/AndrewWalker/structmaker/pulls

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/andrewwalker/glud/master/LICENSE
   :alt: MIT License


