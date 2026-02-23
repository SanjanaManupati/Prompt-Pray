from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def resume():
    return {"module": "resume"}