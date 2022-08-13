class script(object):
    START_TXT = """
    <b>Hi {}💖</b>

    <b>I am <a href="http://t.me/jerry_autofilterbot">Jᴇʀʀʏ⚡️</a></b>

    <b>Just a Simple Pre-Functioned Autofilter Bot🔥</b>

    <b>Add Me To Your Groups For Movies🎬</b>

    <b>Maintained By : <a href="http://t.me/abhiram_vf">AR⚡</a></b>
    """
    
    HELP_TXT = """
    <b>𝖧𝖾𝗒 {} 💖</b>

    <b>➠ ADD ME TO YOUR GROUP</b>

    <b>✯ You Can Check My status  Using This Command /Stats</b>

    <b>➠ Notice 📙:-</b>

    <b>✯ Dont Spam Me...🤒</b>

    <b>➠ Maintained By : <a href="http://t.me/abhiram_vf">AR⚡</a></b>
    """
    
    ABOUT_TXT = """
    <b>✯ My Name : {}</b>
    <b>✯ Creator : <a href="http://t.me/abhiram_vf">AR⚡</a></b>
    <b>✯ Credits : Everyone in this journey</b>
    <b>✯ Language : Python3</b>
    <b>✯ Library : Pyrogram 2.0.30</b>
    <b>✯ Supported Site : Only Telegram</b>
    <b>✯ Source Code : Not Available..🙁</b>
    <b>✯ Server : Heroku</b>
    <b>✯ Database : MongoDB</b>
    <b>✯ Build Status : V2.1 [BETA]</b>
       """
    SOURCE_TXT = """<b>Source</b>
    
<b>➠ Jᴇʀʀʏ⚡️ Is A Private Project⚠️</b>

<b>➠ Maintained By : <a href="http://t.me/abhiram_vf">AR⚡</a></b>  


"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Jᴇʀʀʏ⚡️ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Jᴇʀʀʏ⚡️ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Jᴇʀʀʏ⚡️ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Jᴇʀʀʏ⚡️

<b>➠ Commands and Usage :</b>

<b>➠ /id</b>
<b>✯ Get ID of a Specified User </b>

<b>➠ /info</b>
<b>✯ Get Information About a User</b>

<b>➠ /imdb</b>
<b>✯ Get The Film Information From IMDb Soource</b>

<b>➠ /search</b>
<b>✯ Get The Film Information From Various Sources</b>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """
    <b>➠ Current Status of Jᴇʀʀʏ⚡️</b>

    <b>★ Total Files: <code>{}</code></b>

    <b>★ Total Users: <code>{}</code></b>

    <b>★ Total Chats: <code>{}</code></b>

    <b>★ Used Storage: <code>{}</code></b>

    <b>★ Free Storage : <code>{}</code></b>
    """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
