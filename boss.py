import time
import os 
import asyncio 
import re


@ultroid_cmd(pattern="hiboss ?(.*)")
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "đ"
    await edit_or_reply(
        event,
        f"{ult}â¨â¨{ult}â¨{ult}{ult}{ult}\n{ult}â¨â¨{ult}â¨â¨{ult}â¨\n{ult}{ult}{ult}{ult}â¨â¨{ult}â¨\n{ult}â¨â¨{ult}â¨â¨{ult}â¨\n{ult}â¨â¨{ult}â¨{ult}{ult}{ult}\nââââââââ",
    )
    await asyncio.sleep(1)
    await edit_or_reply("Boss")

    
