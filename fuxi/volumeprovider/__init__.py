# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import collections

from oslo_log import log
from oslo_utils import importutils

from fuxi.i18n import _LE, _LI, _LW

LOG = log.getLogger(__name__)

CINDER = 'cinder'
MANILA = 'manila'

MAPPING = {
    CINDER: 'fuxi.volumeprovider.cinder.Cinder',
    MANILA: 'fuxi.volumeprovider.cinder.Manila',
}


def load_providers(conf_providers):
    if not conf_providers:
        return None
    volume_providers = collections.OrderedDict()
    for provider in conf_providers:
        try:
            if provider in MAPPING:
                volume_providers[provider] = importutils \
                    .import_object(MAPPING[provider])
                LOG.info(_LI("Load volume provider: %s"), provider)
            else:
                LOG.warning(_LW("Could not find volume provider: %s"), provider)
        except Exception as e:
            LOG.error(_LE("Load volume provider %(p)s failed, %(err)s"),
                      {'p': provider, 'err': e})
