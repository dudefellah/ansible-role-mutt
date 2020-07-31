import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_user_configs(host):
    for f in ['.mutt/gpg.include', '.mutt/myhost.com', '.muttrc']:
        muttrc_file = host.file(
            '/home/testuser/{muttrc_file}'.format(muttrc_file=f)
        )

        assert muttrc_file.exists
        assert muttrc_file.user == 'testuser'
        assert muttrc_file.group == 'testuser'
