# Copyright (c) 2019 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

BP_INCLUDES_PATH = '/opt/manager/resources/blueprints/' \
                   '{tenant}/{blueprint}/{relative_path}'
HOSTS = 'hosts'
WORKSPACE = 'workspace'
SOURCES = 'sources'
IP = 'ansible_host'
USER = 'ansible_user'
KEY = 'ansible_ssh_private_key_file'
BECOME = 'ansible_become'
SSH_COMMON = 'ansible_ssh_common_args'
PLAYBOOK_VENV = 'playbook_venv'
LOCAL_VENV = 'local_venv'
INSTALLED_PACKAGES = 'installed_ansible_pyenv_packages'
INSTALLED_COLLECTIONS = 'installed_galaxy_collections'
COLLECTIONS_DIR = 'collections'
ANSIBLE_TO_INSTALL = 'ansible==4.10.0'
# ANSIBLE_TO_INSTALL = \
#     'https://cloudify-release-eu.s3.eu-west-1.amazonaws.com/' \
#     'cloudify/wagons/cloudify-ansible-plugin/' \
#     'ansible-2.9.5-py3-none-any.whl'
OPTION_HOST_CHECKING = 'ANSIBLE_HOST_KEY_CHECKING'
OPTION_TASK_FAILED_ATTRIBUTE = 'ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED'
OPTION_STDOUT_FORMAT = 'ANSIBLE_STDOUT_CALLBACK'
AVAILABLE_STEPS = '___AVAILABLE_STEPS'
COMPLETED_STEPS = '___COMPLETED_STEPS'
AVAILABLE_TAGS = '___AVAILABLE_STEPS'
COMPLETED_TAGS = '___COMPLETED_TAGS'
PLAYS = '___PLAYS'
NUMBER_OF_ATTEMPTS = 'number_of_attempts'
