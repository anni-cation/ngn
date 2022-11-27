# import HTTP/1.1 and time library
import requests
import time 

# access key: page ID Test NGN (App)
page_id_1 = 123

# access token, needed to provide access to page: we use https --> encrypted
facebook_access_token_1 = 'xxx'
# message that the facebook post should contain
msg = ''
planned_msgs = [
    "Hey guys, wish me luck for my presentation today!", 
    "Oh wait, I'm just a Webservice and Annika did all the work before...",
    "Hmm, I could have some breakfast...",
    "I hope Annika is doing well!",
    "Wow! 20 Minutes are already over, that was fast!",
    ""
]

# provide URL
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)

def posting_loop():
    # insert random get command

    for i in range(6):
        # create messages depending on counter value
        msg = planned_msgs[i]

        # create message in json format
        payload = {
        'message': msg,
        'access_token': facebook_access_token_1
        }

        # http POST command
        r = requests.post(post_url, data=payload)

        # print server response 
        print(r)
        print(r.text)
        
        # wait 5 minutes (300 sec)
        time.sleep(300)
    

if __name__ == "__main__":

    posting_loop()
    