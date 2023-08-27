from fastapi import APIRouter
import singlepane_api.container as container


router = APIRouter(include_in_schema=False)


@router.get("")
async def get():
    return {"message": "success"}
