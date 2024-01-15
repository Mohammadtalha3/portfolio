from user_model.user_model import User_model
from fastapi import APIRouter

obj=User_model()

router= APIRouter()

@router.get('/data')
def get_Data():
    return obj.getall()
