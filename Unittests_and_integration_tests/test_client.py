#!/usr/bin/env python3
"""Unit tests for GithubOrgClient."""

import unittest
import requests
from unittest.mock import Mock, patch, PropertyMock

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import (
    org_payload, repos_payload, expected_repos, apache2_repos
)


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """Test that org calls get_json with the expected URL."""
        test_client = GithubOrgClient(org)
        self.assertEqual(
            test_client.org,
            mock_get_json.return_value
        )
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )


    def test_public_repos_url(self):
        """Test the public repositories URL property."""
        payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            test_client = GithubOrgClient("google")
            self.assertEqual(
                test_client._public_repos_url,
                payload["repos_url"]
            )


    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method."""
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos",
        ) as mock_repos_url:
            test_client = GithubOrgClient("google")
            self.assertEqual(test_client.public_repos(), ["repo1", "repo2"])

        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
        )


    @parameterized.expand([
        (
            {"license": {"key": "my_license"}},
            "my_license",
            True,
        ),
        (
            {"license": {"key": "other_license"}},
            "my_license",
            False,
        ),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test whether a repository has the requested license."""
        test_client = GithubOrgClient("google")
        self.assertEqual(
            test_client.has_license(repo, license_key),
            expected,
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Start a mock for requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_payload(url):
            response = Mock()
            if url == "https://api.github.com/orgs/google":
                response.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                response.json.return_value = cls.repos_payload
            else:
                response.json.return_value = {}
            return response

        cls.mock_get.side_effect = get_payload

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns repositories from the fixtures."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repositories by Apache 2.0 license."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos("apache-2.0"),
            self.apache2_repos,
        )


if __name__ == "__main__":
    unittest.main()
