from typing import Any, Dict

import fastapi
import fastapi_chameleon
from starlette.requests import Request

from pypi.models.base import ViewModelBase
from pypi.models.home.index import IndexViewModel

router = fastapi.APIRouter()


@router.get('/')
@fastapi_chameleon.template()
async def index(request: Request) -> Dict[str, Any]:
    # returns json by default
    index_model = IndexViewModel(request)
    return index_model.to_dict()


@router.get('/about')
@fastapi_chameleon.template()
async def about(request: Request) -> Dict[str, Any]:
    vm = ViewModelBase(request)
    return vm.to_dict()
