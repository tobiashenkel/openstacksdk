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

import uuid

from openstack.load_balancer.v2 import _proxy
from openstack.load_balancer.v2 import listener
from openstack.load_balancer.v2 import load_balancer as lb
from openstack.load_balancer.v2 import member
from openstack.load_balancer.v2 import pool
from openstack.tests.unit import test_proxy_base2


class TestLoadBalancerProxy(test_proxy_base2.TestProxyBase):

    POOL_ID = uuid.uuid4()

    def setUp(self):
        super(TestLoadBalancerProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_load_balancers(self):
        self.verify_list(self.proxy.load_balancers,
                         lb.LoadBalancer,
                         paginated=True)

    def test_load_balancer_get(self):
        self.verify_get(self.proxy.get_load_balancer,
                        lb.LoadBalancer)

    def test_load_balancer_create(self):
        self.verify_create(self.proxy.create_load_balancer,
                           lb.LoadBalancer)

    def test_load_balancer_delete(self):
        self.verify_delete(self.proxy.delete_load_balancer,
                           lb.LoadBalancer, True)

    def test_load_balancer_find(self):
        self.verify_find(self.proxy.find_load_balancer,
                         lb.LoadBalancer)

    def test_load_balancer_update(self):
        self.verify_update(self.proxy.update_load_balancer,
                           lb.LoadBalancer)

    def test_listeners(self):
        self.verify_list(self.proxy.listeners,
                         listener.Listener,
                         paginated=True)

    def test_listener_get(self):
        self.verify_get(self.proxy.get_listener,
                        listener.Listener)

    def test_listener_create(self):
        self.verify_create(self.proxy.create_listener,
                           listener.Listener)

    def test_listener_delete(self):
        self.verify_delete(self.proxy.delete_listener,
                           listener.Listener, True)

    def test_listener_find(self):
        self.verify_find(self.proxy.find_listener,
                         listener.Listener)

    def test_listener_update(self):
        self.verify_update(self.proxy.update_listener,
                           listener.Listener)

    def test_pools(self):
        self.verify_list(self.proxy.pools,
                         pool.Pool,
                         paginated=True)

    def test_pool_get(self):
        self.verify_get(self.proxy.get_pool,
                        pool.Pool)

    def test_pool_create(self):
        self.verify_create(self.proxy.create_pool,
                           pool.Pool)

    def test_pool_delete(self):
        self.verify_delete(self.proxy.delete_pool,
                           pool.Pool, True)

    def test_pool_find(self):
        self.verify_find(self.proxy.find_pool,
                         pool.Pool)

    def test_pool_update(self):
        self.verify_update(self.proxy.update_pool,
                           pool.Pool)

    def test_members(self):
        self.verify_list(self.proxy.members,
                         member.Member,
                         paginated=True,
                         method_kwargs={'pool': self.POOL_ID},
                         expected_kwargs={'pool_id': self.POOL_ID})

    def test_member_get(self):
        self.verify_get(self.proxy.get_member,
                        member.Member,
                        method_kwargs={'pool': self.POOL_ID},
                        expected_kwargs={'pool_id': self.POOL_ID})

    def test_member_create(self):
        self.verify_create(self.proxy.create_member,
                           member.Member,
                           method_kwargs={'pool': self.POOL_ID},
                           expected_kwargs={'pool_id': self.POOL_ID})

    def test_member_delete(self):
        self.verify_delete(self.proxy.delete_member,
                           member.Member,
                           True,
                           method_kwargs={'pool': self.POOL_ID},
                           expected_kwargs={'pool_id': self.POOL_ID})

    def test_member_find(self):
        self._verify2('openstack.proxy2.BaseProxy._find',
                      self.proxy.find_member,
                      method_args=["MEMBER", self.POOL_ID],
                      expected_args=[member.Member, "MEMBER"],
                      expected_kwargs={"pool_id": self.POOL_ID,
                                       "ignore_missing": True})

    def test_member_update(self):
        self._verify2('openstack.proxy2.BaseProxy._update',
                      self.proxy.update_member,
                      method_args=["MEMBER", self.POOL_ID],
                      expected_args=[member.Member, "MEMBER"],
                      expected_kwargs={"pool_id": self.POOL_ID})
