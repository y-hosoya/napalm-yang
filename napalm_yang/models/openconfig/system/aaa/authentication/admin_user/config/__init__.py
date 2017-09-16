
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
  from YANG module openconfig-system - based on the path /system/aaa/authentication/admin-user/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for the root user account
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__admin_password','__admin_password_encrypted',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__admin_password = None
    self.__admin_password_encrypted = None

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
      return [u'system', u'aaa', u'authentication', u'admin-user', u'config']

  def _initialized_admin_password(self):
    return self.__admin_password is not None

  def _get_admin_password(self):
    """
    Getter method for admin_password, mapped from YANG variable /system/aaa/authentication/admin_user/config/admin_password (string)

    YANG Description: The admin/root password, supplied as a cleartext string.
The system should encrypt and only store the password as an
encrypted value.
    """
    if self.__admin_password is None:
        self.__admin_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    return self.__admin_password
      
  def _set_admin_password(self, v, load=False):
    """
    Setter method for admin_password, mapped from YANG variable /system/aaa/authentication/admin_user/config/admin_password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_password() directly.

    YANG Description: The admin/root password, supplied as a cleartext string.
The system should encrypt and only store the password as an
encrypted value.
    """
    if self.__admin_password is None:
        self.__admin_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="admin-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__admin_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_password(self):
    self.__admin_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _initialized_admin_password_encrypted(self):
    return self.__admin_password_encrypted is not None

  def _get_admin_password_encrypted(self):
    """
    Getter method for admin_password_encrypted, mapped from YANG variable /system/aaa/authentication/admin_user/config/admin_password_encrypted (oc-aaa-types:crypt-password-type)

    YANG Description: The admin/root password, supplied as an encrypted value
using the notation described in the definition of the
crypt-password-type.
    """
    if self.__admin_password_encrypted is None:
        self.__admin_password_encrypted = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    return self.__admin_password_encrypted
      
  def _set_admin_password_encrypted(self, v, load=False):
    """
    Setter method for admin_password_encrypted, mapped from YANG variable /system/aaa/authentication/admin_user/config/admin_password_encrypted (oc-aaa-types:crypt-password-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_password_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_password_encrypted() directly.

    YANG Description: The admin/root password, supplied as an encrypted value
using the notation described in the definition of the
crypt-password-type.
    """
    if self.__admin_password_encrypted is None:
        self.__admin_password_encrypted = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="admin-password-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_password_encrypted must be of a type compatible with oc-aaa-types:crypt-password-type""",
          'defined-type': "oc-aaa-types:crypt-password-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)""",
        })

    self.__admin_password_encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_password_encrypted(self):
    self.__admin_password_encrypted = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-password-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-aaa-types:crypt-password-type', is_config=True)

  admin_password = __builtin__.property(_get_admin_password, _set_admin_password)
  admin_password_encrypted = __builtin__.property(_get_admin_password_encrypted, _set_admin_password_encrypted)


  _pyangbind_elements = {'admin_password': admin_password, 'admin_password_encrypted': admin_password_encrypted, }

