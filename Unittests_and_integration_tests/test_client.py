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


if __name__ == "__main__":
    unittest.main()
