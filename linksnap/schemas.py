from pydantic import BaseModel

class URLInput(BaseModel):
    recieved_url : str
