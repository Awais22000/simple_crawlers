import requests

# These are the accounts/handles for which you will fetch data from.
names_list = [
    'angrybirds',
    'assassinscreed'
]

# Facebook Graph API base URL.
base_url = 'https://graph.facebook.com/'

# Iterate over the handles and trigger the API with each.
for user in names_list:
    url = base_url + user
    print 'Fetching: ' + user
    response = requests.get(url)
    profile = response.json()
    print profile
    print '\n'
# End of for loop.
