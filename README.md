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

In addition to checking the values in [defaults/main.yml](defaults/main.yml) here are a
few of the less obvious details of this role:

1. Multiple muttrc files can be specified with the `mutt_rc_files` value. Each
entry in this list will be composed of all of the values available at the top
level with the exception of `mutt_packages`, `mutt_owner` and `mutt_group`.

2. The top level `mutt_rc_filename` value will be placed relative to the
`mutt_owner`'s home directory unless this value starts with a leading slash
to indiate an absolute path. All `mutt_rc_filename` values listed in
`mutt_rc_files` will be placed under the `mutt_owner`/`mutt_dir` path unless
the path is absolute.

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
