```
#!/usr/bin/env python
import ldap
def authenticate(address, username, password):

    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)

    try:								# Methods not ending in _s are asynchronous methods. Those that do end in _s are synchronous.
        result = conn.simple_bind_s(username, password)			# These methods are used to bind to a server. The methods are bind, bind_s, sasl_interactive_bind_s, simple_bind and simple_bind_s.
    except ldap.INVALID_CREDENTIALS:
        return "Invalid credentials"
    except ldap.SERVER_DOWN:
        return "Server down"
    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            return "Other LDAP error: " + e.message['desc']
        else: 
            return "Other LDAP error: " + e
    finally:
        conn.unbind_s()							# Unbinding will disconnect from the LDAP server and free up resources. 

    return "Succesfully authenticated"
```

# Demo Project

```
from django.contrib.auth.decorators import login_required
 
def public(request):
    return HttpResponse("Welcome to public page")
 
@login_required
def private(request):
    return HttpResponse("Welcome to private page")
```

# Basic Authentication with LDAP

Add following lines to your settings.py for basic authentication.

```
import ldap
AUTH_LDAP_SERVER_URI = "ldap://ldap.forumsys.com"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,dc=example,dc=com"
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',					# LDAP users can only connect through MyLDAPBackend;
    'django.contrib.auth.backends.ModelBackend',				# Django users can connect through MyAuthBackend.
)
```

# Django admin access using LDAP

In order to handle admin access using LDAP, group level settings are required. Add following lines to your settings.py

```
from django_auth_ldap.config import LDAPSearch,GroupOfUniqueNamesType
 
#Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=example,dc=com",
ldap.SCOPE_SUBTREE, "(objectClass=GroupOfUniqueNames)"
)
 
AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType()
 
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
 "is_active": ("ou=mathematicians,dc=example,dc=com",
 "ou=scientists,dc=example,dc=com", ),
 "is_staff": ("ou=mathematicians,dc=example,dc=com",
 "ou=scientists,dc=example,dc=com", )
}
```


# LDAP authentication backend
This LDAP backend has two goals :

	Save user password in django database, thus he'll be able to log in django if LDAP authentication backend is disabled;
	Force from_ldap field to True when a user is created by this way.
```
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import get_user_model

class MyLDAPBackend(LDAPBackend):
    """ A custom LDAP authentication backend """

    def authenticate(self, username, password):
        """ Overrides LDAPBackend.authenticate to save user password in django """

        user = LDAPBackend.authenticate(self, username, password)

        # If user has successfully logged, save his password in django database
        if user:
            user.set_password(password)
            user.save()

        return user

    def get_or_create_user(self, username, ldap_user):
        """ Overrides LDAPBackend.get_or_create_user to force from_ldap to True """
        kwargs = {
            'username': username,
            'defaults': {'from_ldap': True}
        }
        user_model = get_user_model()
        return user_model.objects.get_or_create(**kwargs)
```

# Classical authentication backend
We override django.contrib.auth.backends.ModelBackend to ensure LDAP users can't logged in with this one if MyLDAPBackend is available.

```
from django.contrib.auth import get_backends, get_user_model
from django.contrib.auth.backends import ModelBackend

class MyAuthBackend(ModelBackend):
    """ A custom authentication backend overriding django ModelBackend """

    @staticmethod
    def _is_ldap_backend_activated():
        """ Returns True if MyLDAPBackend is activated """
        return MyLDAPBackend in [b.__class__ for b in get_backends()]

    def authenticate(self, username, password):
        """ Overrides ModelBackend to refuse LDAP users if MyLDAPBackend is activated """

        if self._is_ldap_backend_activated():
            user_model = get_user_model()
            try:
                user_model.objects.get(username=username, from_ldap=False)
            except:
                return None

        user = ModelBackend.authenticate(self, username, password)

        return user
```

