
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/dns/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for the DNS resolver
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__search',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__search = None

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'system', u'dns', u'config']

  def _initialized_search(self):
    return self.__search is not None

  def _get_search(self):
    """
    Getter method for search, mapped from YANG variable /system/dns/config/search (inet:domain-name)

    YANG Description: [adapted from IETF system model RFC 7317]

An ordered list of domains to search when resolving
a host name.
    """
    if self.__search is None:
        self.__search = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']})), is_leaf=False, yang_name="search", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:domain-name', is_config=True)
    return self.__search
      
  def _set_search(self, v, load=False):
    """
    Setter method for search, mapped from YANG variable /system/dns/config/search (inet:domain-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_search is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_search() directly.

    YANG Description: [adapted from IETF system model RFC 7317]

An ordered list of domains to search when resolving
a host name.
    """
    if self.__search is None:
        self.__search = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']})), is_leaf=False, yang_name="search", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:domain-name', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']})), is_leaf=False, yang_name="search", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:domain-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """search must be of a type compatible with inet:domain-name""",
          'defined-type': "inet:domain-name",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']})), is_leaf=False, yang_name="search", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:domain-name', is_config=True)""",
        })

    self.__search = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_search(self):
    self.__search = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']})), is_leaf=False, yang_name="search", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:domain-name', is_config=True)

  search = __builtin__.property(_get_search, _set_search)


  _pyangbind_elements = {'search': search, }

