import os

CLIENT_ID = "9e4707c8-15cb-4fc6-8bb9-656eabe5cb6c"
CLIENT_SECRET = "O_F8Q~grJe362k_pBzOlH36HlTAsXAm6dixx_cTG"
AUTHORITY = "https://login.microsoftonline.com/5d7e4366-1b9b-45cf-8e79-b14b27df46e1"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
