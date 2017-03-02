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


class Volume(object):
    """This object represent the volume that creates from any storage
    backend that Fuxi enables
    """
    _attrs = ['name', 'mountpoint', 'status', 'id', 'host', 'provider']

    def __init__(self, name, provider, mountpoint='', status=None,
                 id=None, host=None):
        """

        :param name: The unique flag for volume.
        :type name: str
        :param provider: the provider of this volume.
        :type provider: str
        :param mountpoint: The mountpoint that the volume existed in host.
        :type mountpoint: str
        :param status: The status of volume.
        :type status: dict
        :param id: The anther flag for volume could extract from backed volume.
        :type id: str
        :param host: in which the volume located.
        :type host: list
        """
        self.name = name
        self.provider = provider
        self.mountpoint = mountpoint
        if status is None:
            self.status = {}
        elif isinstance(status, dict):
            self.status = status
        else:
            raise Exception("")
        self.status = status
        self.id = id
        self.hosts = []

    def to_docker_volume(self):
        """Convert Fuxi volume to Docker volume object."""
        docker_volume = {
            'Name': self.name,
            'Mountpoint': self.mountpoint,
            'Status': self.status
        }
        return docker_volume


def from_dict(**kwargs):
    if 'name' not in kwargs or 'provider' not in kwargs:
            raise Exception()
    return Volume(name=kwargs['name'],
                      provider=kwargs['provider'],
                      mountpoint=kwargs.get('mountpoint', ''),
                      status=kwargs.get('status', {}),
                      id=kwargs.get('id', ''),
                      host=kwargs.get('host', []))