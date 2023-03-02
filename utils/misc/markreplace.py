async def markdowned(text: str) -> str:
    chars = "\\`_{}[]()<>#+-.!$|?=~'\"%^&/:"
    for c in chars:
        text = text.replace(c, "\\" + c)

    return text
