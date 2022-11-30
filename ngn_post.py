# import HTTP/1.1 and time library
import requests
import time 

# access key: page ID Test NGN (App)
page_id_1 = '101484006137344'

# access token, needed to provide access to page: we use https --> encrypted
facebook_access_token_1 = 'xxx'

# messages that the facebook post should contain
# last message creates an error --> empty post
msg = ''
planned_msgs = [
    "Hey guys, wish me luck for my presentation today!", 
    "Oh wait, I'm just a Webservice and Annika did all the work before...",
    "Hmm, I could have some breakfast... ",
    "Watch out for the picture!",
    ""
]

# provide URL
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)

def posting_loop():
    for i in range(5):
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

        # return if status code == 400
        if r.status_code == 400: 
            return
        
        # wait 5 minutes (300 sec)
        time.sleep(300)

def post_image():
    # prepare image 
    image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
    image_location = 'https://m.media-amazon.com/images/I/914EEhrnMmL._SS500_.jpg'
    img_payload = {
    'url': image_location,
    'access_token': facebook_access_token_1
    }

    # send the POST request
    r = requests.post(image_url, data=img_payload)
    print(r)
    print(r.text)

if __name__ == "__main__":
    posting_loop()
    post_image()




