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
