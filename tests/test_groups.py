# -*- coding: utf-8 -*-
from tests import BaseTestCase


class GroupTestCase(BaseTestCase):
    def setUp(self):
        super(GroupTestCase, self).setUp()

    def testAddGroupWithHost(self):
        self.hosts.create("a", "b", "c", "d", group="e")
        host = self.hosts.get("a")
        self.assertEqual("e", host.group)

    def testDefaultPassowrd(self):
        raise Exception("TODO")