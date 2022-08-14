from aiohttp import web

from giphynavigator.containers import Container
from giphynavigator import handlers


def create_app() -> web.Application:
    container = Container()
    # container.config.giphy.api_key.from_env("GIPHY_API_KEY") # 외부 환경 변수에서 값을 가져오는 경우

    # aio
    app = web.Application()
    app.container = container
    app.add_routes([
        web.get("/", handlers.index),
    ])
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
