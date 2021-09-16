## Leave 
"""
◇ Command  -
• {i}crf (crf value {0-51})
   **Encode video with your desired crf value 
    Now support with queue**
   
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

compressor_queue = []


@ultroid_cmd(pattern="crf ?(.*)")
async def _(e):
    cr = e.pattern_match.group(1)
    crf = 30
    to_stream = False
    if cr:
        k = e.text.split()
        if len(k) == 2:
            crf = int(k[1]) if k[1].isdigit() else 27
        elif len(k) > 2:
            crf = int(k[1]) if k[1].isdigit() else 27
            to_stream = "stream" in k[2]
    vido = await e.get_reply_message()
    if vido and vido.media and "video" in mediainfo(vido.media):
        if hasattr(vido.media, "document"):
            vfile = vido.media.document
            name = vido.file.name
        else:
            vfile = vido.media
            name = ""
        if not name:
            name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
        xxx = await eor(e, "Downloading...📥")
        c_time = time.time()
        file = await downloader(
            "resources/downloads/" + name,
            vfile,
            xxx,
            c_time,
            "Downloading " + name + "...",
        )
        o_size = os.path.getsize(file.name)
        d_time = time.time()
        diff = time_formatter((d_time - c_time) * 1000)
        file_name = (file.name).split("/")[-1]
        out = file_name.replace(file_name.split(".")[-1], "compressed.mkv")
        await xxx.edit(
            f"`Downloaded {file.name} of {humanbytes(o_size)} in {diff}.\n📀Now Encoding📀"
        )
        x, y = await bash(
            f'mediainfo --fullscan """{file.name}""" | grep "Frame count"'
        )
        total_frames = x.split(":")[1].split("\n")[0]
        number = random.randint(1, 10000)
        progress = f"progress-{number}.txt"
        with open(progress, "w") as fk:
            pass
        compressor_queue.append(progress)
        while os.path.exists(progress) and len(compressor_queue) != 0:
            proce = await asyncio.create_subprocess_shell(
                f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{file.name}""" -preset veryfast -c:v libx265 -s 856x480 -pix_fmt yuv420p -c:a libopus -b:a 36k -crf {crf} """{out}""" -y',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            while proce.returncode != 0:
                await asyncio.sleep(3)
                with open(progress, "r+") as fil:
                    text = fil.read()
                    frames = re.findall("frame=(\\d+)", text)
                    size = re.findall("total_size=(\\d+)", text)

                    if len(frames):
                        elapse = int(frames[-1])
                    if len(size):
                        size = int(size[-1])
                        per = elapse * 100 / int(total_frames)
                        time_diff = time.time() - int(d_time)
                        speed = round(elapse / time_diff, 2)
                    if int(speed) != 0:
                        some_eta = ((int(total_frames) - elapse) / speed) * 1000
                        text = f"`Compressing {file_name} at {crf} CRF.\n`"
                        progress_str = "`[{0}{1}] {2}%\n\n`".format(
                            "".join("》" for i in range(math.floor(per / 5))),
                            "".join("" for i in range(20 - math.floor(per / 5))),
                            round(per, 2),
                        )

                        e_size = (
                            humanbytes(size) + " of ~" + humanbytes((size / per) * 100)
                        )
                        eta = "~" + time_formatter(some_eta)
async def stats(e):
    try:
        wah = progress
        await e.answer(ans, cache_time=0, alert=True)
    except BaseException:
        await e.answer("Compressing stopped (resend media)", cache_time=0, alert=True)


async def encc(e):
    try:
        es = dt.now()
        COUNT.append(e.chat_id)
        wah = progress
        nn = await e.edit(
            "**Compressing**",
            buttons=[
                [Button.inline("STATS", data=f"stats{wah}")],
                [Button.inline("CHANNEL", url="t.me/Animes_Encoded")],
            ],
        )
                        
                        except MessageNotModifiedError:
                            pass
            os.remove(file.name)
            c_size = os.path.getsize(out)
            f_time = time.time()
            difff = time_formatter((f_time - d_time) * 1000)
            await xxx.edit(
                f"`Compressed {humanbytes(o_size)} to {humanbytes(c_size)} in {difff}\nUploading...📤"
            )
            differ = 100 - ((c_size / o_size) * 100)
            caption = f"**Original Size: **`{humanbytes(o_size)}`\n"
            caption += f"**Encoded Size: **`{humanbytes(c_size)}`\n"
            caption += f"**Compression Ratio: **`{differ:.2f}%`\n"
            caption += f"\n**Time Taken To Encode: **`{difff}`"
            mmmm = await uploader(
                out,
                out,
                f_time,
                xxx,
                "Uploading " + out + "...",
            )
            if to_stream:
                metadata = extractMetadata(createParser(out))
                duration = metadata.get("duration").seconds
                hi, _ = await bash(f'mediainfo "{out}" | grep "Height"')
                wi, _ = await bash(f'mediainfo "{out}" | grep "Width"')
                height = int(hi.split(":")[1].split("pixels")[0].replace(" ", ""))
                width = int(wi.split(":")[1].split("pixels")[0].replace(" ", ""))
                attributes = [
                    DocumentAttributeVideo(
                        duration=duration, w=width, h=height, supports_streaming=True
                    )
                ]
                await e.client.send_file(
                    e.chat_id,
                    mmmm,
                    thumb="resources/extras/ultroid.jpg",
                    caption=caption,
                    attributes=attributes,
                    force_document=False,
                    reply_to=e.reply_to_msg_id,
                )
            else:
                await e.client.send_file(
                    e.chat_id,
                    mmmm,
                    thumb="resources/extras/ultroid.jpg",
                    caption=caption,
                    force_document=True,
                    reply_to=e.reply_to_msg_id,
                )
            await xxx.delete()
            os.remove(out)
            os.remove(progress)
            compressor_queue.remove(progress)
    else:
        await eor(e, "`Reply To Video File Only`", time=5)
