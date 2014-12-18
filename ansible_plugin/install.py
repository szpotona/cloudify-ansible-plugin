########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License,  Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#                http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,  software
# distributed under the License is distributed on an 'AS IS' BASIS,
#   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,  either express or implied.
#   * See the License for the specific language governing permissions and
#   * limitations under the License.

# for running shell commands
import subprocess
import os
import errno

# ctx is imported and used in operations
from cloudify import ctx
# put the operation decorator on any function that is a task
from cloudify.decorators import operation
# Import Cloudify exception
from cloudify.exceptions import NonRecoverableError


def _run_shell_command(command):
    """Runs a shell command
    """

    ctx.logger.info('Running shell command: {0}'.format(command))
    try:
        run = subprocess.check_call(
            command)
    except subprocess.CalledProcessError:
        ctx.logger.error('Unable to run shell command: {0}'.format(command))
        raise NonRecoverableError('Command failed: {0}'.format(command))
    return run


def _run(package):
    """ Installs a Package
    """

    _validate_installation(package)
    _create_folders()


def _validate_installation(package):
    """ validate the installation
    """

    ctx.logger.info('Begin validation: {0}: '.format(package))
    command = [package, '--version']
    code = _run_shell_command(command)

    if code > 0:
        ctx.logger.info('Installation was unsuccessful')
    else:
        ctx.logger.info('Installation was successful')


def _create_folders():
    paths = ['/etc/ansible/',
             '/etc/ansible/group_vars',
             '/etc/ansible/host_vars',
             '/etc/ansible/library',
             '/etc/ansible/filter_plugins',
             '/etc/ansible/roles',
             '/etc/ansible/roles/common',
             '/etc/ansible/roles/common/tasks',
             '/etc/ansible/roles/common/handlers',
             '/etc/ansible/roles/common/templates',
             '/etc/ansible/roles/common/files',
             '/etc/ansible/roles/common/vars',
             '/etc/ansible/roles/common/defaults'
             '/etc/ansible/roles/common/meta',
             '/etc/ansible/webtier',
             '/etc/ansible/monitoring']

    for path in paths:
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


@operation
def install(**kwargs):
    """ Wraps _install_package
    """

    package = 'ansible'
    _run(package)
