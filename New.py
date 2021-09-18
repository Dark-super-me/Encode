#Lol
"""
Usage - 
 Reply to a file/video with {i}start
 
 To know more click help button ...
 If your original file is 1080p u can encode it in ur desired resolution!
 Dont use 480p files to encode !
 Join @Animes_Encoded for animes and support @TeamUltroid
"""

import asyncio
import os
import re
import time
from datetime import datetime as dt

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo

from . import *
  
async def ihelp(event):
  await event.edit(
       "**To use encode videos, try {i}480p, {i}720p and {i}1080p for encoding files",
   buttons=[
    Button.inline("Back", data="beck")],
   )

async def beck(event):
 ok = await event.client(GetFullUserRequest(event.sender_id))
 await event.edit(
  f"Hi ! Boss .... Click the below button to get started...",
  buttons=[
   Button.inline("HELP", data="ihelp")]
  )
 
# Let's make {i}start the ultroid plugins!
@ultroid_cmd(pattern="start ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
     

  f"Hi ! Boss .... Click the below button to get started...",
  buttons=[
    Button.inline("HELP", data="ihelp")],
  )
  
    
   
  
  







 
