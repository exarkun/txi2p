# Copyright (c) str4d <str4d@mail.i2p>
# See COPYING for details.

from twisted.internet.error import ConnectionLost, ConnectionRefusedError
from twisted.python import failure
from twisted.trial import unittest

from txi2p.test.util import FakeEndpoint
from txi2p import client, server


connectionLostFailure = failure.Failure(ConnectionLost())
connectionRefusedFailure = failure.Failure(ConnectionRefusedError())


class TestI2PClientEndpoint(unittest.TestCase):
    def test_bobConnectionFailed(self):
        bobEndpoint = FakeEndpoint(failure=connectionRefusedFailure)
        endpoint = client.I2PClientEndpoint('', bobEndpoint)
        d = endpoint.connect(None)
        return self.assertFailure(d, ConnectionRefusedError)

    def test_destination(self):
        bobEndpoint = FakeEndpoint()
        endpoint = client.I2PClientEndpoint('foo.i2p', bobEndpoint)
        endpoint.connect(None)
        self.assertEqual(proxy.transport.value(), 'foo.i2p') # TODO: Fix.