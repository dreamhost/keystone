TENANTS = [
    {'id': 'bar', 'name': 'BAR'},
    {'id': 'baz', 'name': 'BAZ'},
    ]

USERS = [
    {'id': 'foo', 'name': 'FOO', 'password': 'foo2', 'tenants': ['bar',]},
    ]

EXTRAS = [
    {'user_id': 'foo', 'tenant_id': 'bar', 'extra': 'extra'},
    ]

ROLES = [
    {'id': 'keystone_admin', 'name': 'Keystone Admin'},
    {'id': 'useless', 'name': 'Useless'},
    ]