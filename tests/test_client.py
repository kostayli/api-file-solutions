import os
import unittest
from pathlib import Path

import app.clients


class ClientTest(unittest.TestCase):

    def test_get_list_file(self):
        p = Path(__file__).parents[1].__str__()
        with open(p + "./tmp/test_get_list.txt", 'w+') as f:
            f.write("qwerty")
        result = app.clients.get_list_file("127.0.0.1:8008")
        self.assertNotEqual(0, len(result))

    def test_get_file(self):
        p = Path(__file__).parents[1].__str__()
        with open(p + "./tmp/test_get_file_server.txt", 'w+') as f:
            f.write("qwerty")
        result = app.clients.get_file("test_get_file_server.txt", "test_get_file_client.txt", "127.0.0.1:8008")
        self.assertEqual(1, result)

    def test_upload(self):
        with open("test_upload.txt", 'w+') as f:
            f.write("qwerty")
        result = app.clients.upload("test_upload.txt", "127.0.0.1:8008")
        self.assertEqual(1, result)

    def test_update(self):
        p = Path(__file__).parents[1].__str__()
        os.remove(p + "/tmp/test_update.txt")
        with open("test_update.txt", 'w+') as f:
            f.write("qwerty")
        result = app.clients.update("test_update.txt", "127.0.0.1:8008")
        self.assertEqual(1, result)

    def test_delete(self):
        p = Path(__file__).parents[1].__str__()
        with open(p + "./tmp/test_delete.txt", 'w+') as f:
            f.write("qwerty")
        result = app.clients.delete("test_delete.txt", "127.0.0.1:8008")
        self.assertEqual(1, result)
