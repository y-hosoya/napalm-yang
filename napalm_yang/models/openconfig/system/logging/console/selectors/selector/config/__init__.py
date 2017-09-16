
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
  from YANG module openconfig-system - based on the path /system/logging/console/selectors/selector/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__facility','__severity',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__severity = None
    self.__facility = None

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
      return [u'system', u'logging', u'console', u'selectors', u'selector', u'config']

  def _initialized_facility(self):
    return self.__facility is not None

  def _get_facility(self):
    """
    Getter method for facility, mapped from YANG variable /system/logging/console/selectors/selector/config/facility (identityref)

    YANG Description: Specifies the facility, or class of messages to log
    """
    if self.__facility is None:
        self.__facility = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-log:AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)
    return self.__facility
      
  def _set_facility(self, v, load=False):
    """
    Setter method for facility, mapped from YANG variable /system/logging/console/selectors/selector/config/facility (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_facility is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_facility() directly.

    YANG Description: Specifies the facility, or class of messages to log
    """
    if self.__facility is None:
        self.__facility = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-log:AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-log:AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """facility must be of a type compatible with identityref""",
          'defined-type': "openconfig-system:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-log:AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)""",
        })

    self.__facility = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_facility(self):
    self.__facility = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-log:AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSLOG': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUDIT': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:KERNEL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTHPRIV': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:USER': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:SYSTEM_DAEMON': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'ALL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'MAIL': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:CONSOLE': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'oc-log:AUTH': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'NTP': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL5': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL4': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL7': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL6': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL1': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL0': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL3': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}, u'LOCAL2': {'@namespace': u'http://openconfig.net/yang/system/logging', '@module': u'openconfig-system-logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)


  def _initialized_severity(self):
    return self.__severity is not None

  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /system/logging/console/selectors/selector/config/severity (syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) for the corresonding facility are logged
    """
    if self.__severity is None:
        self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NOTICE': {}, u'WARNING': {}, u'EMERGENCY': {}, u'ALERT': {}, u'CRITICAL': {}, u'ERROR': {}, u'DEBUG': {}, u'INFORMATIONAL': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='syslog-severity', is_config=True)
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /system/logging/console/selectors/selector/config/severity (syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) for the corresonding facility are logged
    """
    if self.__severity is None:
        self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NOTICE': {}, u'WARNING': {}, u'EMERGENCY': {}, u'ALERT': {}, u'CRITICAL': {}, u'ERROR': {}, u'DEBUG': {}, u'INFORMATIONAL': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='syslog-severity', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NOTICE': {}, u'WARNING': {}, u'EMERGENCY': {}, u'ALERT': {}, u'CRITICAL': {}, u'ERROR': {}, u'DEBUG': {}, u'INFORMATIONAL': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='syslog-severity', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with syslog-severity""",
          'defined-type': "openconfig-system:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NOTICE': {}, u'WARNING': {}, u'EMERGENCY': {}, u'ALERT': {}, u'CRITICAL': {}, u'ERROR': {}, u'DEBUG': {}, u'INFORMATIONAL': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='syslog-severity', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NOTICE': {}, u'WARNING': {}, u'EMERGENCY': {}, u'ALERT': {}, u'CRITICAL': {}, u'ERROR': {}, u'DEBUG': {}, u'INFORMATIONAL': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='syslog-severity', is_config=True)

  facility = __builtin__.property(_get_facility, _set_facility)
  severity = __builtin__.property(_get_severity, _set_severity)


  _pyangbind_elements = {'facility': facility, 'severity': severity, }

