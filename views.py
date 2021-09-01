#views.py
from Flex_msg import
message=[]
uid=event.source.user_id
profile=line_bot_api.get_profile(uid)
name=profile.display_name


if event.message.type=='text':
    mtext=event.message.text
    if 'records' in mtext:
        Redord = mtext.split(',')
        records.objects.create(uid=uid,
                            name=name,
                            mdt=Record[1],
                            description=Record[2],
        message.append(TextSendMessage(text='收到的工作內容為：'+str(Record)))
        message.append(TextSendMessage(text='建立工作內容完成'))
        line_bot_api.reply_message(event.reply_token,message)
    elif "身體紀錄" in mtext:
        message.append(jobs_progress(uid))
        line_bot_api.reply_message(event.reply_token,message)