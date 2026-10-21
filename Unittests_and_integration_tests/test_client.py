#!/usr/bin/env python3
"""Unit tests for GithubOrgClient."""

import unittest
from unittest.mock import patch, PropertyMock

from parameterized import parameterized

from client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
