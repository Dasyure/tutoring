# You will be given 5-10 minutes to analyse the current API specification
# for your project, and to (as a team) propose 2-3 new "route(s)" (i.e. url)
# to the interface to add some cool functionality to the product. Find something
# that you as a team get excited about. 

# A route (i.e. /this/url/name)
# A CRUD method (e.g. GET)
# Input parameters
# Return object
# Description of what it does
# Do 2 routes

# -----------------------------------------------------------------------------
# ALPACA
"""
Poke/Wave feature:
Description:
add a feature like "poke" or "wave" from facebook messenger to dms and channel (first message only).
A member of the channel/dm can send a wave, and any other members can send a wave back.

Input Error when:
1. channel id is invalid
2. The channel/dm already has messages in it

Access error when:
1. token is invalid
"""
@APP.route("/channel/poke/v1", methods=['POST'])
def poke_channel():
  data = request.get_json()
  token = data['token']
  channel_id = data['channel_id']
  user_id = check_valid_and_decrypt(token)
  
  poke_channel(user_id, channel_id)
  
  return dumps({})

@APP.route("/dm/poke/v1", methods=['POST'])
def poke_dm():
  data = request.get_json()
  token = data['token']
  channel_id = data['dm_id']
  user_id = check_valid_and_decrypt(token)
  
  poke_dm(user_id, dm_id)
  
  return dumps({})

"""
Birthday feature:
Description:
Automatically generates a birthday message and sends it to a specified user. 

Input Error when:
1. channel id is invalid

Access error when:
1. token is invalid
"""
@APP.route("user/birthday/message/v1", methods=['POST'])
def birthday_msg():
  data = request.get_json()
  token = data['token']
  channel_id = data['token']
  user_id = check_valid_and_decrypt(token)
  
  birthday_reminder_notification(user_id, whos_birthday_youre_interested_in)
  
  return dumps({})

# -----------------------------------------------------------------------------
# BEAGLE
@APP.route("/message/heart", methods=['POST'])
def message_heart(token, message_id):
	'''
    This function reacts to a message with a heart
      /message/heart - POST
      Arguments: 
        token, message_id
      Rreturn value:
        Return {}
	'''
    data = request.get_json()
  	token = data['token']
    message_id = data['message_id']
    #check if token is valid
    #check if message_id is valid
    
    message_id['react'] = 2
	return dumps({})

@APP.route("/user/relationship", methods=['POST'])
def user_relationship(token, relationship, u_id):
	'''
    This function add a relationship between two users
    /user/relationship - POST
    
    Arguments:
    token	
    relationship	(int)	
    	0 -> parent - child :}
    	1 -> lovers :)
    	2 -> haters :<
    u_id
    
    Return {}
	'''
    #Check if token is valid
    #Check if u_id is valid
    #Check if relationship is valid
    #Check if relationship is one of the numbers 0, 1, 2
    
    #get data_store
    data = data_store().get()
    
    #get the target users
    auth_user_id = decode.token()
    user_1 = data['users'][auth_user_id - 1]
    user_2 = data['users'][u_id - 1]
    
    #create new key
    user_1['relationship'] = []
    user_2['relationship'] = []
    
    #append the dicrionary to the list
    user_1['relationship'].append({relationship, u_id)
    user_2['relationship'].append({relationship, auth_user_id)  
	
    #set the data_store
    data_store.set()
    
    #return
    return dumps({})

# -----------------------------------------------------------------------------
# CAMEL
"""
Because not reacting is insufficient to show disapproval, we propose a dislike button

/message/dislike
- Method: POST
- Inputs: token, message_id
- Outputs: {}

Sister route: /message/undislike
"""

@APP.route("/message/dislike", methods = ['POST'])
def dislike_message(token, message_id):
  	# insert interesting code here
  	return dumps({})

"""
Allows a user to prevent another user from inviting them to channels/dms

/user/block/
- Method: POST
- Inputs: token, u_id 
- Outputs: {}

Sister route: /user/unblock
"""
  
@APP.route("/user/block", methods = ['POST'])
def user_block(token, u_id):
 	# insert interesting code here
	return dumps({})


# -----------------------------------------------------------------------------
# DODO
"""
/message/sendpicture
POST
Inputs
* token
* channel_id
* picture_url

Outputs
* { message_id }

Description
Create picture message from url in channel.

============================================

/channel/polls/v1
POST
Inputs
* token
* channel_id
* poll_title
* list_poll_options

Outputs
* { poll_id }

Description
Creates a poll the in the channel_id that the 
authorised user is apart of.

"""

# -----------------------------------------------------------------------------
# EAGLE
/fun/mirror/
@APP.route("/fun/mirror/", methods=['POST'])
'''
Input parameters: token
Returns object: {}
Description: Reverses all images and text on the screen (bit a of a fun/wacky inclusion that doesnt impact any other users)
'''

/user/addfriend/
@APP.route("/user/addfriend", methods=['POST'])
'''
Input parameters: token, u_id
Return object: {}
Description: For a valid user, it adds the u_id to the valid user's array of "friends"
			 the user with u_id will now be able to send dms to the valid user, unless they are a global owner
''' 

/user/unfriend/
@APP.route("/user/removefriend", methods=['POST'])
'''
Input parameters: token, u_id
Return object: {}
Description: for a valid user with the given token, it removes the user with u_id from the valid user's array of "friends".
			 the user with u_id will no longer be able to send dm's to valid user once unfriended, unless they are a global owner
'''	









