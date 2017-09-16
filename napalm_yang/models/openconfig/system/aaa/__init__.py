
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

from . import authentication
from . import authorization
from . import accounting
from . import server_groups
class aaa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/aaa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for AAA services
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__authentication','__authorization','__accounting','__server_groups',)

  _yang_name = 'aaa'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__accounting = None
    self.__authentication = None
    self.__authorization = None
    self.__server_groups = None

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
      return [u'system', u'aaa']

  def _initialized_authentication(self):
    return self.__authentication is not None

  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /system/aaa/authentication (container)

    YANG Description: Top-level container for global authentication data
    """
    if self.__authentication is None:
        self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /system/aaa/authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.

    YANG Description: Top-level container for global authentication data
    """
    if self.__authentication is None:
        self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authentication.authentication, is_container='container', yang_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', yang_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _initialized_authorization(self):
    return self.__authorization is not None

  def _get_authorization(self):
    """
    Getter method for authorization, mapped from YANG variable /system/aaa/authorization (container)

    YANG Description: Top-level container for AAA authorization configuration
and operational state data
    """
    if self.__authorization is None:
        self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    return self.__authorization
      
  def _set_authorization(self, v, load=False):
    """
    Setter method for authorization, mapped from YANG variable /system/aaa/authorization (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authorization is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authorization() directly.

    YANG Description: Top-level container for AAA authorization configuration
and operational state data
    """
    if self.__authorization is None:
        self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authorization.authorization, is_container='container', yang_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authorization must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__authorization = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authorization(self):
    self.__authorization = YANGDynClass(base=authorization.authorization, is_container='container', yang_name="authorization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _initialized_accounting(self):
    return self.__accounting is not None

  def _get_accounting(self):
    """
    Getter method for accounting, mapped from YANG variable /system/aaa/accounting (container)

    YANG Description: Top-level container for AAA accounting
    """
    if self.__accounting is None:
        self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    return self.__accounting
      
  def _set_accounting(self, v, load=False):
    """
    Setter method for accounting, mapped from YANG variable /system/aaa/accounting (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accounting is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accounting() directly.

    YANG Description: Top-level container for AAA accounting
    """
    if self.__accounting is None:
        self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=accounting.accounting, is_container='container', yang_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accounting must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__accounting = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accounting(self):
    self.__accounting = YANGDynClass(base=accounting.accounting, is_container='container', yang_name="accounting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _initialized_server_groups(self):
    return self.__server_groups is not None

  def _get_server_groups(self):
    """
    Getter method for server_groups, mapped from YANG variable /system/aaa/server_groups (container)

    YANG Description: Enclosing container for AAA server groups
    """
    if self.__server_groups is None:
        self.__server_groups = YANGDynClass(base=server_groups.server_groups, is_container='container', yang_name="server-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    return self.__server_groups
      
  def _set_server_groups(self, v, load=False):
    """
    Setter method for server_groups, mapped from YANG variable /system/aaa/server_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_groups() directly.

    YANG Description: Enclosing container for AAA server groups
    """
    if self.__server_groups is None:
        self.__server_groups = YANGDynClass(base=server_groups.server_groups, is_container='container', yang_name="server-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=server_groups.server_groups, is_container='container', yang_name="server-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=server_groups.server_groups, is_container='container', yang_name="server-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__server_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_groups(self):
    self.__server_groups = YANGDynClass(base=server_groups.server_groups, is_container='container', yang_name="server-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  authentication = __builtin__.property(_get_authentication, _set_authentication)
  authorization = __builtin__.property(_get_authorization, _set_authorization)
  accounting = __builtin__.property(_get_accounting, _set_accounting)
  server_groups = __builtin__.property(_get_server_groups, _set_server_groups)


  _pyangbind_elements = {'authentication': authentication, 'authorization': authorization, 'accounting': accounting, 'server_groups': server_groups, }

