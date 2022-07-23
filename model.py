
from pydantic import BaseModel




class ForgetPassword(BaseModel):
    email : str

class ResetCode(BaseModel):
    email : str
    code : str

