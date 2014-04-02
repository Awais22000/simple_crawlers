import requests

# These are the accounts/handles for which you will fetch data from.
list_of_handles = [
    'JovianLin',
    'BarackObama',
]

# Google Plus API base URL.
base_url = 'https://www.googleapis.com/plus/v1/people/'
api_key  = 'SOME_KEY'  # Create this key via "Public API access" in https://console.developers.google.com

# Iterate over the handles and trigger the API with each.
for handle in list_of_handles:
    url = base_url + '+' + handle + '?key=' + api_key
    response = requests.get(url)
    profile = response.json()
    print profile
    print '\n'
# End of for loop.
