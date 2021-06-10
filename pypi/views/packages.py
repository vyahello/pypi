from typing import Any, Dict

import fastapi
import fastapi_chameleon
from starlette.requests import Request

from pypi.models.packages.details import DetailsViewModel

router = fastapi.APIRouter()


@router.get('/project/{package_name}')
@fastapi_chameleon.template(template_file='packages/details.pt')
async def details(package_name: str, request: Request) -> Dict[str, Any]:
    index_model = DetailsViewModel(package_name, request)
    return index_model.to_dict()
