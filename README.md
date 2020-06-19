![Permafrost CI](https://github.com/renderbox/django-permafrost/workflows/Permafrost%20CI/badge.svg?branch=master)

# Django Permafrost

Django Permafrost is an extention to Django's Permissions framework.

It adds:
- A View Mixin that supports user permissions based on different HTTP method types (GET, POST, PUT, etc) for extra granular control.
- A View Mixin that captures into Django's logging setup any failed permission checks.
- An App that supports Client User defineable roles and permissions.  This uses the underlying Django Permission system and controls which permissions are exposed to the users.
  - Developers can have both require permissions for the permission classes or optional permission that can be set by the Client.

For example, you have a SAAS platform where you have Administrators Clients.  They manage the other users on their master account in the system (like Employees, etc) and want to be able to define different permissions for various users.  They might have one Employee they want to be able to manage email lists but not let them invite users but both are considered in the staff category.

The Goal of Django Permafrost is to allow Clients to create their own Permafrost Roles, under developer defined Categories with developer defined required and optional permissions.

An example of a developer defined categories looks like this:

```python
Sample Cetegory Permission Format:

PERMAFROST_CATEGORIES = {
    'user': {
        'label': _("User"),
        'access_level': 1,
        'optional': [
            {'label':_('Can Add Users to Role'), 'permission': ('add_user_to_role', 'permafrost', 'permafrostrole')},
        ],
        'required': [
            {'label':_('Can add Role'), 'permission': ('add_permafrostrole', 'permafrost', 'permafrostrole')},
        ],
    },
}
```

This would be added to your Django `settings.py` file (or, at least, included into).  

In the above, we define the User category, give it the localizeable label of "User" and provide two permissions in the "Natural Key" format (since PKs can be unreliable with permissions), the first is optional and the second is required.

There is also an access_level setting to help make sorting access levels more easily.

## Convenience tools
There is a tool to help the devloper list out the permissions available in the format permafrost expects.

```shell
> ./manage permalist
```

using the command will produce a list like this

```shell
> ./manage.py permalist

Permlist formatted for your PermafrostRoles configuration
{'label':_('Can add email address'), 'permission': ('add_emailaddress', 'account', 'emailaddress')},
{'label':_('Can change email address'), 'permission': ('change_emailaddress', 'account', 'emailaddress')},
{'label':_('Can delete email address'), 'permission': ('delete_emailaddress', 'account', 'emailaddress')},
...
```

Each line can be copied into the PERMAFROST_CATEGORIES config in the correct format.
 