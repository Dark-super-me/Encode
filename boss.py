import time
import os 
import asyncio 
import re


@ultroid_cmd(pattern="hiboss ?(.*)")
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "🙄"
    await edit_or_reply(
        event,
        f"{ult}✨✨{ult}✨{ult}{ult}{ult}\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}{ult}{ult}{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨{ult}{ult}{ult}\n☁☁☁☁☁☁☁☁",
    )
    await asyncio.sleep(1)
    await edit_or_reply("Boss")

    
