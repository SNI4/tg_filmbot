from keyboards.user_keyboards.subscribe_channels import create_subscribe
from utils.json_worker.channels import get_channels, del_channel
from utils.misc.markreplace import markdowned


async def action_cd(callback):
    try:
        data = await get_channels()
        channel_id = callback.data.split('?')[1]
        channel_title = data[channel_id]['title']
        await del_channel(channel_id)
        await callback.message.answer(await markdowned(f'Канал *{channel_title}* успешно удален!'),
                                      reply_markup=await create_subscribe(url=False, cancel=True),
                                      parse_mode="MarkdownV2")

    except Exception as e:
        await callback.message.reply('ERROR!\n' + str(e))
