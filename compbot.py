

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

 
 lst=[
   Button.inline("Help", data="ihelp")]
  
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
   Button.inline("HELP", data="ihelp")],
  )
 
# Let's make {i}start the ultroid plugins!
@ultroid_cmd(pattern="compbot")
async def okboss(ult):
 await ult.edit("**This is an ultroid\nvideo compressor plugin**")
 await asyncio.sleep(3)
 await ult.edit(f"Hi ! Boss .... Click the below button to get started...", buttons=lst)
  
  
  
   
  
 
 
 
     
    
     
      
     
  
    
 
    
  
      
   
     
    
    
    
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
