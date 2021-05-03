from .config import TELEGRAM_BASE
import requests, json

class Tool:
    def tool_keyboard(self,item_list:dict,           \
                split_count:list or str=2,           \
                before:str='',after:str='',          \
                keyboard_method:str='inline_keyboard'):
        
        reply_keyboard,temp = [],[]
        len_ = len(item_list)
        split_method = 'str'
        
        if isinstance(split_count,list):
            if len_ != len(split_count):
                print(f'Error(Tool/tool_keyboard): The length of split_count is incorrect.')
                return
            else:
                split_method = 'list'
            
        if keyboard_method not in ['inline_keyboard','keyboard']:
            print(f"Error(Tool/tool_keyboard): Telegram dosn't support others keyboard method.")
            return
        
        for no,item in enumerate(item_list.keys()):
            json_ = self.tool_to_dict(text = item,callback_data = before+item_list[item]+after)
            temp.append(json_)
            if split_method == 'str':
                if (((no+1) % split_count) == 0) | (no+1 == len_):
                    reply_keyboard.append(temp)
                    temp = []
            elif split_method == 'list':
                try:
                    if (no == len_-1) or (split_count[no] != split_count[no+1]):
                        reply_keyboard.append(temp)
                        temp = []
                except IndexError: pass
                except Exception as err:
                    print(f'Error(Tool/tool_keyboard): ',err)
        return { keyboard_method : reply_keyboard }

    def tool_to_dict(self,**kwargs):
        return kwargs

    def tool_to_json(self,**kwargs):
        return json.dumps(kwargs)

    def send_msg(self,payload:list):
        """
        To response client by sending message to Telegram server.

        parmas:
            *payload : list : The message to be send.

        format:
            *payload = [{
                "type" : "sendMessage",
                "data" : "{"chat_id":1046886930, "text":"hi"}",
                "files" : ""
            },{
                "type" : "sendPhoto",
                "data" : "{"chat_id":1046886930, "text":"hi"}",
                "files" : open('candle_stick.png','rb')
            }]
        """
        headers = {"Content-Type": "application/json"}
        status_list = list()
        try:
            for action in payload:
                url = TELEGRAM_BASE + '/' + action['type']
                res = requests.post(url,
                    headers = headers,
                    data = action['data'],
                    files = action['files']
                )
                status_list.append(True if res.status_code == 200 else False)
            return True if False not in status_list else False
        except Exception as err:
            print('Error(Engine/send_data): ',err)

    @staticmethod
    def webhook_init(webhook_link):
        """
        To connect the API gateway service.

        params:
            *webhook_link : str : to get connection to Telegram server
        """
        requests.get(webhook_link)

    @staticmethod
    def webhook_del(telegram_token):
        """
        To delete current connection to Telegram server.

        params:
            *telegram_token : str : a token of Telegram chatbot to disconnect
        """
        requests.get(f'https://api.telegram.org/bot{telegram_token}/deleteWebhook')