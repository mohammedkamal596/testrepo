# test_secrets.py
# These are intentionally fake credentials for testing scanners.

AWS_ACCESS_KEY_ID = "AKIA1234567890EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

SLACK_TOKEN = "xoxb-123456789012-123456789012-abcdefghijklmnopqrstuvwxyz"

DATABASE_PASSWORD = "SuperSecretPassword123!"

API_KEY = "sk_test_51ExampleFakeKeyForScannerDetection"

def connect():
    return {
        "user": "admin",
        "password": DATABASE_PASSWORD
    }
