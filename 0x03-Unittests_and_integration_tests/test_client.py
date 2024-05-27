#!/usr/bin/env python3
"""This module tests the client module."""
from unittest import mock
from parameterized import parameterized, parameterized_class
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """test case for GithubOrgClient class."""
    __payload = [
        {"name": "gmail", "repos_url":
         "https://api.github.com/orgs/google/gmail", "payload": True},
        {"name": "google_drive", "repos_url":
         "https://api.github.com/orgs/google/drive", "payload": True},
        ]

    @parameterized.expand([("google",), ("abc",)])
    @mock.patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name: str, mocked_get: mock.MagicMock) -> None:
        """test case for org method."""
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"payload": True})
        mocked_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self) -> None:
        """Test for public_repos url method."""
        with mock.patch(
             'client.GithubOrgClient.org',
             new_callable=mock.PropertyMock) as mocked:
            mocked.return_value = {
                "repos_url": "https://api.github.com/orgs/google",
                "payload": True, "name": "google"}
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url, "https://api.github.com/orgs/google")

    @mock.patch('client.get_json', return_value=__payload)
    def test_public_repos(self, mocked_get: mock.MagicMock) -> None:
        """test for public repos method"""
        with mock.patch(
             'client.GithubOrgClient._public_repos_url',
             new_callable=mock.PropertyMock) as mocked:
            mocked.return_value = "https://api.github.com/orgs/google"
            client = GithubOrgClient("google")
            repos = client.public_repos()
            self.assertEqual(repos, ["gmail", "google_drive"])
            mocked.assert_called_once()
            mocked_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, licence_key, expected):
        """test for licence"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, licence_key),
            expected
            )


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.get_patcher = mock.patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set the side effect of the mock object
        cls.mock_get.side_effect = [
            cls.org_payload,
            cls.repos_payload,
            cls.expected_repos,
            cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        cls.get_patcher.stop()
