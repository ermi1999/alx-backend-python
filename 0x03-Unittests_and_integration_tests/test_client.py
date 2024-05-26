#!/usr/bin/env python3
"""This module tests the client module."""
from unittest import mock
from parameterized import parameterized
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test case for GithubOrgClient class."""
    __payload = [
        {"name": "gmail", "repos_url": "https://api.github.com/orgs/google/gmail", "payload": True},
        {"name": "google_drive", "repos_url": "https://api.github.com/orgs/google/drive", "payload": True},
        ]
    @parameterized.expand([("google",), ("abc",)])
    @mock.patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mocked_get):
        """test case for org method."""
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"payload": True})
        mocked_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test for public_repos url method."""
        with mock.patch('client.GithubOrgClient.org', new_callable=mock.PropertyMock) as mocked:
            mocked.return_value = {"repos_url": "https://api.github.com/orgs/google", "payload": True, "name": "google"}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google")

    @mock.patch('client.get_json', return_value=__payload)
    def test_public_repos(self, mocked_get):
        with mock.patch('client.GithubOrgClient._public_repos_url', new_callable=mock.PropertyMock) as mocked:
            mocked.return_value = "https://api.github.com/orgs/google"
            client = GithubOrgClient("google")
            repos = client.public_repos()
            self.assertEqual(repos, ["gmail", "google_drive"])
            mocked.assert_called_once()
            mocked_get.assert_called_once()
