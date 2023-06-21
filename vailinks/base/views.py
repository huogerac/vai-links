from ninja import Router, Schema

router = Router()


class Error(Schema):
    message: str


@router.get("/dapau", response={500: Error})
def dapau(request):
    raise Exception("break on purpose")
