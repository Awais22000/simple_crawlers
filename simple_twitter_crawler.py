import twitter  # uses the python-twitter library to fetch the profile data.

# Initialize the API.
api = twitter.Api(consumer_key='your-consumer-key',
                  consumer_secret='your-consumer-secret',
                  access_token_key='your-access-token-key',
                  access_token_secret='your-access-token-secret')
 
# These are the accounts/handles for which you will fetch data from.
list_of_handles = [
    'mattgemmell',
    'angrybirds'
]

# Iterate over the handles and trigger the API with each.
for handle in list_of_handles:
    print ''
    user = api.GetUser(screen_name=handle)  # Get info on a user.
 
    print 'Name: ',             user.GetName()
    print 'Description: ',      user.GetDescription()
    print 'Followers Count: ',  user.GetFollowersCount()
    print 'Friends Count: ',    user.GetFriendsCount()
    print 'Status Count: ',     user.GetStatusesCount()
    print 'Favourites Count: ', user.GetFavouritesCount()
    print 'Personal URL: ',     user.GetUrl()
 
    statuses = api.GetUserTimeline(screen_name=handle, count=5)  # get a user timeline
    print 'Latest Tweets:'
    for index, s in enumerate(statuses):
        print '\t' + str(index+1) + ') ' + s.text.strip()
    # End of for loop.
# End of for loop.
