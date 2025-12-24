"""
Configuration file containing all constants and settings
"""



# Base URL
BASE_URL = 'https://www.flipkart.com/'

# Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 30

# Browser settings
BROWSER = "chrome"  # chrome, firefox, edge
HEADLESS = False

# Test credentials (use environment variables in real projects)
TEST_MOBILE = "9999999999"
TEST_EMAIL = "test@example.com"
TEST_PASSWORD = "TestPassword123"

# Paths
SCREENSHOTS_PATH = "screenshots/"
REPORTS_PATH = "reports/"

