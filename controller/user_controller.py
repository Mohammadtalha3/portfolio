from user_model.user_model import User_model
from fastapi import APIRouter,Request
from starlette.responses import JSONResponse

obj=User_model()

router= APIRouter()

@router.get('/data')
def get_Data():
    return obj.getall()

@router.post('/details')
async def details_input(request:Request):
    result = await obj.details_db(request)
    return JSONResponse(content=result)

@router.get('/get_detail')
async def  get_details():
    result=  await obj.getall()
    return JSONResponse(content=result)