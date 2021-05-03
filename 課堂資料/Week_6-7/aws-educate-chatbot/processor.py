from TelegramFunction.features import Tool

class TelegramBot(Tool):
    def run_process(self,event):
        """
        To catch and deconstruct the data response from Telegram Server.

        params:
            *event : dict : user message from Telegram server.
        """
        try:
            if event.get('message'):
                event = event['message']
                self.content = event['text']
            elif event.get('callback_query'):
                event = event['callback_query']
                self.content = event['data']
            else:
                print('Error(run_process): Nothing')
        except Exception as err:
            print('Error(run_process): ',event,err)

        # Assign to variable
        self.chat_id = event['from']['id']
        self.first_name = event['from']['first_name']
    
    def run_data(self):
        # Write your statement
        pass
