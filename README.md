Mutt
=========

Use this role to automate mutt installation and its configuration for a
specified user.

Requirements
------------

None.

Role Variables
--------------

Values are commented in [defaults/main.yml](defaults/main.yml).

The entirety of mutt's configuration options are not yet represented by this
role and may never be. Anything not convered by this role can be added as a
string to `mutt_extra_config` which will be added to the end of your muttrc
file.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: clients
      roles:
         - role: dudefellah.mutt
           vars:
             mutt_owner: myuser
             mutt_group: myuser
             mutt_binds:
               - key: j
                 map:
                   - index
                   - pager
                 function: next-line

License
-------

GPLv3
