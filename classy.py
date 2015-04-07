#!/usr/bin/env python

from __future__ import print_function
from six import with_metaclass
from inspect import getmro

class BlahMeta(type):
    _BlahMeta__classes = []

    def __init__(self, *args, **kwargs):
        self._BlahMeta__classes.append(self)
        print('BlahMeta:', self)

class BlahBase1(object):
    _BlahBase1__instances = []

    def __init__(self):
        self._BlahBase1__instances.append(self)
        print('BlahBase1:', self)

class BlahBase2(object):
    _BlahBase2__instances = []

    def __init__(self):
        self._BlahBase2__instances.append(self)
        print('BlahBase2:', self)

class BlahActual(with_metaclass(BlahMeta, BlahBase1, BlahBase2)):
    _BlahActual__instances = []

    def __init__(self):
        super(BlahActual, self).__init__()
        self._BlahActual__instances.append(self)
        print('BlahActual:', self)

b = BlahActual()
print('Created b:', b)
print('type(b):', type(b))
print('BlahMeta._BlahMeta__classes:', BlahMeta._BlahMeta__classes)
print('BlahBase1._BlahBase1__instances:', BlahBase1._BlahBase1__instances)
print('BlahBase2._BlahBase2__instances:', BlahBase2._BlahBase2__instances)
print('BlahActual._BlahActual__instances:', BlahActual._BlahActual__instances)
print('dir(b):', dir(b))
print('b.__class__:', b.__class__)
print('b.__class__.__class__:', b.__class__.__class__)
print('getmro(BlahActual):', getmro(BlahActual))

#### Python2 output
# Notice there is no six?
#
# $  python2 do_eet.py
# BlahMeta: <class '__main__.BlahActual'>
# BlahBase1: <__main__.BlahActual object at 0x7f1ed42026d0>
# BlahActual: <__main__.BlahActual object at 0x7f1ed42026d0>
# Created b: <__main__.BlahActual object at 0x7f1ed42026d0>
# type(b): <class '__main__.BlahActual'>
# BlahMeta._BlahMeta__classes: [<class '__main__.BlahActual'>]
# BlahBase1._BlahBase1__instances: [<__main__.BlahActual object at 0x7f1ed42026d0>]
# BlahBase2._BlahBase2__instances: []
# BlahActual._BlahActual__instances: [<__main__.BlahActual object at 0x7f1ed42026d0>]
# dir(b): ['_BlahActual__instances', '_BlahBase1__instances',
# '_BlahBase2__instances', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# b.__class__: <class '__main__.BlahActual'>
# b.__class__.__class__: <class '__main__.BlahMeta'>
# getmro(BlahActual): (<class '__main__.BlahActual'>, <class '__main__.BlahBase1'>, <class '__main__.BlahBase2'>, <type 'object'>)

#### Python3 output
# Notice the use of six?
#
# $  python3 do_eet.py
# BlahMeta: <class 'six.NewBase'>
# BlahMeta: <class '__main__.BlahActual'>
# BlahBase1: <__main__.BlahActual object at 0x7f482a922c18>
# BlahActual: <__main__.BlahActual object at 0x7f482a922c18>
# Created b: <__main__.BlahActual object at 0x7f482a922c18>
# type(b): <class '__main__.BlahActual'>
# BlahMeta._BlahMeta__classes: [<class 'six.NewBase'>, <class '__main__.BlahActual'>]
# BlahBase1._BlahBase1__instances: [<__main__.BlahActual object at 0x7f482a922c18>]
# BlahBase2._BlahBase2__instances: []
# BlahActual._BlahActual__instances: [<__main__.BlahActual object at 0x7f482a922c18>]
# dir(b): ['_BlahActual__instances', '_BlahBase1__instances',
# '_BlahBase2__instances', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# b.__class__: <class '__main__.BlahActual'>
# b.__class__.__class__: <class '__main__.BlahMeta'>
# getmro(BlahActual): (<class '__main__.BlahActual'>, <class 'six.NewBase'>, <class '__main__.BlahBase1'>, <class '__main__.BlahBase2'>, <class 'object'>)
