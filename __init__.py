##########################
#### ________________ ####
##  |Python X Discord|  ##
#### ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ####
##########################

from requests import get as Get, post as Post, put as Put
from json import loads as Loads
try:
    from .database import data
except ImportError:
    from database import data
"""
Created by V.Karthik
started on 16-02-2022
ended on 18-02-2022
"""

HELP="""
 -CONTENTS-
¯¯¯¯¯¯¯¯¯¯¯¯
User()      [class]
   -send()  [class function]
   -get()   [class function]
   -react() [class function]

emojify()   [function]
find()      [function]


Assigning the user's account
    User(authorization)->used to Assign user's account in discord

Tutorial-
    me=User("your authorization ID")

════════════════════════════════════════════════════════════════════════════════

User.get(channel_id,n=20,types=[])
    •channel_id - id of the channel where you wish to get message data from
    •n          - number of messages(0<n<21)
    •types      - empty list(default) returns all types
                 You can specify required ones alone by adding them to the list
                 id, type, content, channel_id, author, attachments,
                 embeds, mentions, mention_roles, pinned, mention_everyone,
                 tts, timestamp, edited_timestamp, flags, components..
                 are the existing types

════════════════════════════════════════════════════════════════════════════════

User.send(channel_id,message)
    •channel_id - id of the channel where you wish to send a message
    •message    - message to send

════════════════════════════════════════════════════════════════════════════════

User.react(channel_id,message_id,emoji)
    •channel_id - id of the channel where the message to react has been sent
    •message_id - id of the message to add reaction
    •emoji      - emoji name eg:-':thumbs_up:' , ':keycap_1'

════════════════════════════════════════════════════════════════════════════════

find(emoji)
    •emoji-emoji character
════════════════════════════════════════════════════════════════════════════════
"""
#########################
#### _______________ ####
##  |Example-Program|  ##
#### ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ####
#########################

TUTORIAL="""
import pxd

authorization_id='YOUR_AUTHORIZATION-ID'
channel_id = 'YOUR CHANNEL-ID'

me=pxd.User(authorization_id)
r1=me.send(channel_id,'Hello 😐 🙂 😄')
r2=me.get(channel_id,n=1,types=['id','content'])
print(r2)
#r2 return a list with the message details in a dictionary
#in this case only one message so len(r2)=1
r3=me.react(channel_id,r2[0]['id'],':thumbs_up:')

n=pxd.find('😄')
print('name of emoji "😄" is ',n)
"""

class User:
    """assigning a user to a variable"""
    def __init__(self,authorization):
        """Authorization/Token"""
        self.AUTH=authorization
        self.LINK='https://discord.com/api/v9/channels/{}/messages'
        self.LINK_REACT='https://discord.com/api/v9/channels/{}/messages/{}/reactions/{}/%40me'
        self.types=['id', 'type', 'content', 'channel_id', 'author', 'attachments', 'embeds', 'mentions', 'mention_roles', 'pinned', 'mention_everyone', 'tts', 'timestamp', 'edited_timestamp', 'flags', 'components']
        self.emojis=data
        if type(self.AUTH) != str:
            raise TypeError(f'Authorization-ID is supposed to be a string not {str(type(self.AUTH))[8:-2]}')
            return
        if len(self.AUTH)!=59:
            raise ValueError(f'Authorization-ID has {["extra","less"][int(len(self.AUTH)<59)]} characters')
            return
        self.USER={'authorization':self.AUTH}

    def send(self,channel_id,message="Hello 🙂"):
        """send a message with content \"message\" to \"channel_id\""""
        if len(channel_id)!=18:
            raise ValueError('given channel_id is invalid')
            return
        
        return Post(self.LINK.format(str(channel_id)),data={'content':message},headers=self.USER)
        


    def get(self,channel_id,n=20,types=[]):
        """get last "n" for channel with id \"channel_id\""""
        if n>20 or n<0:
            raise ValueError(f'n must be {["less than 20","greater than 0"][int(n<20)]}')
            return False
        if len(channel_id)!=18:
            raise ValueError('given channel_id is invalid')
            return
        
        if len(types)==0:
            return Loads(Get(self.LINK.format(str(channel_id)),headers=self.USER).text)[0:n]
        else:
            msgs=Loads(Get(self.LINK.format(str(channel_id)),headers=self.USER).text)[0:n]
            ret_all=[]
            for x in msgs:
                ret=dict.fromkeys(types)
                for i in ret:
                    if i not in self.types:
                        raise TypeError(f'{i}, is not a valid type')
                        return 
                    ret[i]=x[i]
                ret_all.append(ret)
            del msgs,ret,x,i
            return ret_all

    def react(self,channel_id,message_id,emoji):
        """add a reaction "emoji" to message with id "message_id"
           of channel with id "channel_id".
           try the find() to get the name of the required emoji."""
        if len(str(channel_id))!=18:
            raise ValueError('given channel_id is invalid')
            return
        if len(str(message_id))!=18:
            raise ValueError('given message_id is invalid')
            return
        
        return Put(self.LINK_REACT.format(channel_id,message_id,emojify(emoji)),headers=self.USER)

    

def emojify(text):
    """returns the emoji of the text entered"""
    if not text.startswith(':'):text=':'+text
    if not text.endswith(':'):text=text+':'
    if text in data:
        return data[text]
    elif text[1:-1] in data.values():
        return text[1:-1]
    else:
        return NameError('emoji name not found ')
        

def find(emoji):
    """finds the name of a emoji"""
    return [i for i in data if data[i]==emoji]
        
def help():
    """instructions to use pxd, with a sample prgrm"""
    print(HELP)
    print('\n\n _______________ \n|Example-Program|\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n')
    print(TUTORIAL)
        
            
