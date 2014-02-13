import requests

# These are the accounts/handles for which you will fetch data from.
list_of_handles = [
    'angrybirds',
    'assassinscreed'
]

# Facebook Graph API base URL.
base_url = 'https://graph.facebook.com/'

# Iterate over the handles and trigger the API with each.
for handle in list_of_handles:
    url = base_url + handle
    print 'Fetching: ' + handle
    response = requests.get(url)
    profile = response.json()
    print profile
    print '\n'
# End of for loop.
