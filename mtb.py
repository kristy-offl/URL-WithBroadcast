from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<i>Hello {},๐

I'm a Telegram URL Uploader Bot

I Can Upload Direct Link To Telegram Without Using Your Data File Limit Is 1.95GB

Use help Button For More Details

๐งจDevoloped & Maintained By : : <a href='https://t.me/Itz_Me_Malayali'>โฏยฐโข Kสษชsแดส O๊ฐ๊ฐแดษชแดส โขยฐโฏ ใโTแดโใ #Broken Sed Life ๐</a></i>
  """
  HELP_TXT = """
  
  **Hey ๐โโ๏ธIt's Not Complicated To Use Me.

I Can Support zippyshare, filesim, hxfile, fembed, mediafire, sbembed, streamtape, uservideo support Too

โฉ Send Me The Custom Thumbnail To Save It Permanently.
โฉ Now Send Me The Ytdl Or Direct Link.
โฉ Select The Desired Option.
โฉ Then Be Relaxed Your File Will Be Uploaded Soon..

๐Powerded By : @HiroshiBots**
"""
  
  ABOUT_TXT = """
  
<b>๐My Name : <a href='https://t.me/URLHiroshiBot'>URL Uploader Hiroshi Bot</a></b>\n
<b>๐ฉโ๐ฆฝVersion : <a href='https://t.me/URLHiroshiBot'>0.9.2 beta</a></b>\n
<b>โSource : <a href='https://t.me/WantSourceCode'>Click Here</a></b>\n
<b>โ๏ธServer : <a href='https://heroku.com'>Heroku</a></b>\n
<b>๐กLibrary : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>๐ชLanguage : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>๐Developer : <a href='https://t.me/Itz_Me_Malayaali'>โฏยฐโข Kสษชsแดส O๊ฐ๊ฐแดษชแดส โขยฐโฏ</a></b>\n
<b>๐Channel : <a href='https://t.me/HiroshiBots'>๐๐ถ๐ฟ๐ผ๐๐ต๐ถ ๐๐ผ๐๐</a></b>\n
"""
  
  START_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("๐๐ป ๐ด๐ ๐ญ๐๐๐๐๐", url="https://t.me/Itz_Me_Malayali"),
      InlineKeyboardButton("โ๏ธ ๐ฏ๐๐๐", callback_data="help")
     ],[
      InlineKeyboardButton("๐จ๐๐๐๐ ๐", callback_data="about"),
      InlineKeyboardButton("๐ช๐๐๐๐ ๐", callback_data="close")
    ]]
    )
      
  HELP_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("๐ ๐ฉ๐๐๐", callback_data="home"),
      InlineKeyboardButton("๐ช๐๐๐๐ ๐", callback_data="close")
    ]]
    )
  
  ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("๐ ๐ฉ๐๐๐", callback_data="home"),
      InlineKeyboardButton("๐ช๐๐๐๐ ๐", callback_data="close")
    ]]
    )
