from datetime import datetime
import requests 

class LineNotify():

    def __init__(self,Token:str) -> None:
        # Set Value Default
        self.DateTimeFlag = True
        self.DateTimeFormat = '%d/%m/%Y %X'
        self.URL = 'https://notify-api.line.me/api/notify'
        self.Token = Token

        # Set Default
        self.Messages = None
        self.ImagePath = None
        self.TemplateMessage = "{} {}"

    def sendMessage(self):

        # Check Datetime Flag
        if self.DateTimeFlag:
            DateTime = f'[{self.now()}] '
        else : 
            DateTime = ""

        # Set Messages For Template
        messages = self.TemplateMessage.format(DateTime,self.Messages)

        header = {'Authorization' : f'Bearer {self.Token}'} # Set Header
        payload = {"message": messages} # Set Payload
        files = {'imageFile': open(self.ImagePath, 'rb')} if self.ImagePath else None # Set File For Request

        # Call API To Line Notify
        res = requests.post(self.URL, headers=header, params=payload, files=files)

        # Check File Then Close
        if files:
            files['imageFile'].close()
        
        # Return Status
        if res.status_code == 200 :
            return True
        else : 
            return False

    # Set Methon
    def setToken(self,Token:str):
        self.Token = Token

    def setMessages(self,Messages:str):
        self.Messages = Messages
    
    def setImages(self,ImagePath:str):
        self.ImagePath = ImagePath
    
    def setDateTimeFormat(self,Format:str):
        try : 
            datetime.strftime(datetime.now(),Format)
            self.DateTimeFormat = Format
        except :
            print("Can't set Format Datetime")

    # Switch on/off Datetime For Messages
    def disableDatetime(self):
        self.DateTimeFlag = False
    
    def enablaDatetime(self):
        self.DateTimeFlag = True

    # Get Methon
    def getToken(self):
        return self.Token

    def getMessages(self):
        return self.Messages
    
    def getImages(self):
        return self.ImagePath

    def getDatetimeFormat(self):
        return self.DateTimeFormat
    
    # Othen Function
    def now(self):
        return datetime.strftime(datetime.now(),self.DateTimeFormat)

    
