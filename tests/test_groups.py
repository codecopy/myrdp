# -*- coding: utf-8 -*-
from tests import BaseTestCase


class GroupTestCase(BaseTestCase):
    def setUp(self):
        super(GroupTestCase, self).setUp()

    def testAddGroup(self):
        host = self.hosts.create("a", "b", "c", "d", group="e")
        self.assertIsNotNone(host.group)
        # self.assertEqual(host.group, )
        groupedHostList = self.hosts.getHostsListByHostNameAndGroup(groupFilter=[])
        print groupedHostList