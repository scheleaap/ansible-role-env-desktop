import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_apt_packages_are_installed(Package):
    packages = [
        ("atom", "1.17.0-1~webupd8"),
        ("chromium-browser", None),
        ("thunderbird", None),
        ("gitg", None),
        ]

    for package_name, package_version in packages:
        package = Package(package_name)
        assert package.is_installed
        if package_version is not None:
            assert package.version == package_version
