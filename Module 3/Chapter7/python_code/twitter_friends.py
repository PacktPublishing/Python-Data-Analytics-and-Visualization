import cPickle
import os
import twitter  # https://github.com/ianozsvald/python-twitter

# Usage:
# $ # setup CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
# as environment variables
# $ python get_data.py  # downloads friend and follower data to ./data

DATA_DIR = "data"  # storage directory for friend/follower data

# list of screen names that we'll want to analyse
screen_names = [ 'KirthiRaman', 'Lebron' ]

def get_filenames(screen_name):
    """Build the friends and followers filenames"""
    return os.path.join(DATA_DIR, "%s.friends.pickle" % (screen_name)), os.path.join(DATA_DIR, "%s.followers.pickle" % (screen_name))

if __name__ == "__main__":

    # deliberately stripped my keys
    t = twitter.Api(consumer_key='k7atkBNgoGrioMS...',
                  consumer_secret='eBOx1ikHMkFc...',
                  access_token_key='8959...',
                  access_token_secret='O7it0...');

    print t.VerifyCredentials()

    for screen_name in screen_names:
        fr_filename, fo_filename = get_filenames(screen_name)
        print "Checking for:", fr_filename, fo_filename
        if not os.path.exists(fr_filename):
            print "Getting friends for", screen_name
            fr = t.GetFriends(screen_name=screen_name)
            cPickle.dump(fr, open(fr_filename, "w"), protocol=2)
        if not os.path.exists(fo_filename):
            print "Getting followers for", screen_name
            fo = t.GetFollowers(screen_name=screen_name)
            cPickle.dump(fo, open(fo_filename, "w"), protocol=2)


