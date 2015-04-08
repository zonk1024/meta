#!/usr/bin/env python

from __future__ import print_function
from six import with_metaclass, PY2, PY3
from inspect import getmro

class Meta(type):
    _Meta__classes = []

    def __init__(self, name, classes, class_dict):
        self._Meta__classes.append(self)
        print('Meta:', self)
        print('  Name:', name)
        print('  Inherited classes:', classes)
        print('  Class dict:', class_dict)

class Foo(object):
    _Foo__instances = []

    def __init__(self):
        print('Foo:', self)
        self._Foo__instances.append(self)

class Bar(object):
    _Bar__instances = []

    def __init__(self):
        print('Bar:', self)
        self._Bar__instances.append(self)

class Actual(with_metaclass(Meta, Foo, Bar)):
    _Actual__instances = []

    def __init__(self):
        print('Actual:', self)
        # This will only init your first base class
        super(Actual, self).__init__()
        # You can still init the second base class
        Bar.__init__(self)
        self._Actual__instances.append(self)

print('Creating instance')
instance = Actual()
print('Created instance:', instance)
print('type(instance):', type(instance))
print('Meta._Meta__classes:', Meta._Meta__classes)
print('Foo._Foo__instances:', Foo._Foo__instances)
print('Bar._Bar__instances:', Bar._Bar__instances)
print('Actual._Actual__instances:', Actual._Actual__instances)
print('dir(instance):', dir(instance))
print('instance.__class__:', instance.__class__)
print('instance.__class__.__class__:', instance.__class__.__class__)
print('getmro(Actual):', getmro(Actual))

print('\n\n')

####
#### The following sections have to be commented
if PY2:
    class Another(Foo, Bar):
        __metaclass__ = Meta
        _Another__instances = []

        def __init__(self):
            print('Another:', self)
            super(Another, self).__init__()
            Bar.__init__(self)
            self._Another__instances.append(self)


# if it's python2 this will throw a syntax error -- must comment manually
#class Another(Foo, Bar, metaclass=Meta):
#    _Another__instances = []
#
#    def __init__(self):
#        print('Another:', self)
#        super(Another, self).__init__()
#        Bar.__init__(self)
#        self._Another__instances.append(self)

print('Creating instance')
instance = Another()
print('Created instance:', instance)
print('type(instance):', type(instance))
print('Meta._Meta__classes:', Meta._Meta__classes)
print('Foo._Foo__instances:', Foo._Foo__instances)
print('Bar._Bar__instances:', Bar._Bar__instances)
print('Another._Another__instances:', Another._Another__instances)
print('dir(instance):', dir(instance))
print('instance.__class__:', instance.__class__)
print('instance.__class__.__class__:', instance.__class__.__class__)
print('getmro(Another):', getmro(Another))


#### Python2 output
#
# $  python2 classy.py
# Meta: <class '__main__.Actual'>
#   Name: Actual
#   Inherited classes: (<class '__main__.Foo'>, <class '__main__.Bar'>)
#   Class dict: {'__module__': '__main__', '_Actual__instances': [], '__init__': <function __init__ at 0x7f4689d29b18>}
# Creating instance
# Actual: <__main__.Actual object at 0x7f4689d4b890>
# Foo: <__main__.Actual object at 0x7f4689d4b890>
# Bar: <__main__.Actual object at 0x7f4689d4b890>
# Created instance: <__main__.Actual object at 0x7f4689d4b890>
# type(instance): <class '__main__.Actual'>
# Meta._Meta__classes: [<class '__main__.Actual'>]
# Foo._Foo__instances: [<__main__.Actual object at 0x7f4689d4b890>]
# Bar._Bar__instances: [<__main__.Actual object at 0x7f4689d4b890>]
# Actual._Actual__instances: [<__main__.Actual object at 0x7f4689d4b890>]
# dir(instance): ['_Actual__instances', '_Bar__instances', '_Foo__instances', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# instance.__class__: <class '__main__.Actual'>
# instance.__class__.__class__: <class '__main__.Meta'>
# getmro(Actual): (<class '__main__.Actual'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <type 'object'>)
#
#
# Meta: <class '__main__.Another'>
#   Name: Another
#   Inherited classes: (<class '__main__.Foo'>, <class '__main__.Bar'>)
#   Class dict: {'__module__': '__main__', '__metaclass__': <class '__main__.Meta'>, '_Another__instances': [], '__init__': <function __init__ at 0x7f4689d29b90>}
# Creating instance
# Another: <__main__.Another object at 0x7f4689d2e290>
# Foo: <__main__.Another object at 0x7f4689d2e290>
# Bar: <__main__.Another object at 0x7f4689d2e290>
# Created instance: <__main__.Another object at 0x7f4689d2e290>
# type(instance): <class '__main__.Another'>
# Meta._Meta__classes: [<class '__main__.Actual'>, <class '__main__.Another'>]
# Foo._Foo__instances: [<__main__.Actual object at 0x7f4689d4b890>, <__main__.Another object at 0x7f4689d2e290>]
# Bar._Bar__instances: [<__main__.Actual object at 0x7f4689d4b890>, <__main__.Another object at 0x7f4689d2e290>]
# Another._Another__instances: [<__main__.Another object at 0x7f4689d2e290>]
# dir(instance): ['_Another__instances', '_Bar__instances', '_Foo__instances', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__metaclass__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# instance.__class__: <class '__main__.Another'>
# instance.__class__.__class__: <class '__main__.Meta'>
# getmro(Another): (<class '__main__.Another'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <type 'object'>)

#### Python3 output
#
# $  python3 classy.py
# Meta: <class 'six.NewBase'>
#   Name: NewBase
#   Inherited classes: (<class '__main__.Foo'>, <class '__main__.Bar'>)
#   Class dict: {}
# Meta: <class '__main__.Actual'>
#   Name: Actual
#   Inherited classes: (<class 'six.NewBase'>,)
#   Class dict: {'__module__': '__main__', '_Actual__instances': [], '__qualname__': 'Actual', '__init__': <function Actual.__init__ at 0x7fb03d54c510>}
# Creating instance
# Actual: <__main__.Actual object at 0x7fb03f0b4cc0>
# Foo: <__main__.Actual object at 0x7fb03f0b4cc0>
# Bar: <__main__.Actual object at 0x7fb03f0b4cc0>
# Created instance: <__main__.Actual object at 0x7fb03f0b4cc0>
# type(instance): <class '__main__.Actual'>
# Meta._Meta__classes: [<class 'six.NewBase'>, <class '__main__.Actual'>]
# Foo._Foo__instances: [<__main__.Actual object at 0x7fb03f0b4cc0>]
# Bar._Bar__instances: [<__main__.Actual object at 0x7fb03f0b4cc0>]
# Actual._Actual__instances: [<__main__.Actual object at 0x7fb03f0b4cc0>]
# dir(instance): ['_Actual__instances', '_Bar__instances', '_Foo__instances', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# instance.__class__: <class '__main__.Actual'>
# instance.__class__.__class__: <class '__main__.Meta'>
# getmro(Actual): (<class '__main__.Actual'>, <class 'six.NewBase'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>)
#
#
# Meta: <class '__main__.Another'>
#   Name: Another
#   Inherited classes: (<class '__main__.Foo'>, <class '__main__.Bar'>)
#   Class dict: {'__module__': '__main__', '_Another__instances': [], '__qualname__': 'Another', '__init__': <function Another.__init__ at 0x7fb03d54c598>}
# Creating instance
# Another: <__main__.Another object at 0x7fb03f0bf630>
# Foo: <__main__.Another object at 0x7fb03f0bf630>
# Bar: <__main__.Another object at 0x7fb03f0bf630>
# Created instance: <__main__.Another object at 0x7fb03f0bf630>
# type(instance): <class '__main__.Another'>
# Meta._Meta__classes: [<class 'six.NewBase'>, <class '__main__.Actual'>, <class '__main__.Another'>]
# Foo._Foo__instances: [<__main__.Actual object at 0x7fb03f0b4cc0>, <__main__.Another object at 0x7fb03f0bf630>]
# Bar._Bar__instances: [<__main__.Actual object at 0x7fb03f0b4cc0>, <__main__.Another object at 0x7fb03f0bf630>]
# Another._Another__instances: [<__main__.Another object at 0x7fb03f0bf630>]
# dir(instance): ['_Another__instances', '_Bar__instances', '_Foo__instances', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# instance.__class__: <class '__main__.Another'>
# instance.__class__.__class__: <class '__main__.Meta'>
# getmro(Another): (<class '__main__.Another'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>)
