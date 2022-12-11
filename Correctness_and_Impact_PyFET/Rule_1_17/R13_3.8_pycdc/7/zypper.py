
from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version',
                    'status',
                    'supported_by'}


DOCUMENTATION = '''
---
module: zypper
author:
    - "Patrick Callahan (@dirtyharrycallahan)"
    - "Alexander Gubin (@alxgu)"
    - "Thomas O'Donnell (@andytom)"
    - "Robin Roth (@robinro)"
    - "Andrii Radyk (@AnderEnder)"
version_added: "1.2"
short_description: Manage packages on SUSE and openSUSE
description:
    - Manage packages on SUSE and openSUSE using the zypper and rpm tools.
options:
    name:
        description:
        - Package name C(name) or package specifier or a list of either.
        - Can include a version like C(name=1.0), C(name>3.4) or C(name<=2.7). If a version is given, C(oldpackage) is implied and zypper is allowed to
          update the package within the version range given.
        - You can also pass a url or a local path to a rpm file.
        - When using state=latest, this can be '*', which updates all installed packages.
        required: true
        aliases: [ 'pkg' ]
    state:
        description:
          - C(present) will make sure the package is installed.
            C(latest)  will make sure the latest version of the package is installed.
            C(absent)  will make sure the specified package is not installed.
            C(dist-upgrade) will make sure the latest version of all installed packages from all enabled repositories is installed.
          - When using C(dist-upgrade), I(name) should be C('*').
        required: false
        choices: [ present, latest, absent, dist-upgrade ]
        default: "present"
    type:
        description:
          - The type of package to be operated on.
        required: false
        choices: [ package, patch, pattern, product, srcpackage, application ]
        default: "package"
        version_added: "2.0"
    extra_args_precommand:
       version_added: "2.6"
       required: false
       description:
         - Add additional global target options to C(zypper).
         - Options should be supplied in a single line as if given in the command line.
    disable_gpg_check:
        description:
          - Whether to disable to GPG signature checking of the package
            signature being installed. Has an effect only if state is
            I(present) or I(latest).
        required: false
        default: "no"
        type: bool
    disable_recommends:
        version_added: "1.8"
        description:
          - Corresponds to the C(--no-recommends) option for I(zypper). Default behavior (C(yes)) modifies zypper's default behavior; C(no) does
            install recommended packages.
        required: false
        default: "yes"
        type: bool
    force:
        version_added: "2.2"
        description:
          - Adds C(--force) option to I(zypper). Allows to downgrade packages and change vendor or architecture.
        required: false
        default: "no"
        type: bool
    force_resolution:
        version_added: "2.10"
        description:
          - Adds C(--force-resolution) option to I(zypper). Allows to (un)install packages with conflicting requirements (resolver will choose a solution).
        required: false
        default: "no"
        type: bool
    update_cache:
        version_added: "2.2"
        description:
          - Run the equivalent of C(zypper refresh) before the operation. Disabled in check mode.
        required: false
        default: "no"
        type: bool
        aliases: [ "refresh" ]
    oldpackage:
        version_added: "2.2"
        description:
          - Adds C(--oldpackage) option to I(zypper). Allows to downgrade packages with less side-effects than force. This is implied as soon as a
            version is specified as part of the package name.
        required: false
        default: "no"
        type: bool
    extra_args:
        version_added: "2.4"
        required: false
        description:
          - Add additional options to C(zypper) command.
          - Options should be supplied in a single line as if given in the command line.
notes:
  - When used with a `loop:` each package will be processed individually,
    it is much more efficient to pass the list directly to the `name` option.
# informational: requirements for nodes
requirements:
    - "zypper >= 1.0  # included in openSUSE >= 11.1 or SUSE Linux Enterprise Server/Desktop >= 11.0"
    - python-xml
    - rpm
'''