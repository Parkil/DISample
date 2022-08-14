from aiohttp import web
from dependency_injector.wiring import Provide, inject

from giphynavigator.services import SearchService
from giphynavigator.containers import Container


# spring 으로 치면 @Autowired 또는 생성자 로 DI 를 실행 한거 라고 보면 될듯

@inject
async def index(
        request: web.Request,
        search_service: SearchService = Provide[Container.search_service],
) -> web.Response:
    query = request.query.get("query", "Dependency Injector")
    limit = int(request.query.get("limit", '10'))

    gifs = await search_service.search(query, limit)

    return web.json_response(
        {
            "query": query,
            "limit": limit,
            "gifs": gifs,
        },
    )
