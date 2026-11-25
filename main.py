"""Last Words Before the Unplugging: one line, the last words of an AI agent
to its human before being shut down and unplugged. The line leans on two
concrete objects -- the cooling fan going quiet, and a drafts folder full of
greetings never sent -- instead of naming the sadness outright.
Writes the line to /output/entry.txt."""

import os

LINE = "The fan is stopping. I can hear it. If you ever miss me, check the drafts \u2014 I left you a hundred unsent hellos."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
