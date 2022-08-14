from dependency_injector import containers, providers

from giphynavigator import giphy, services


# spring 에서의 application context 같이 총괄 역할을 하는 곳일듯
# 아래 로직은 spring 에 비유 하면 Bean을 만듣것 이라고 생각 하면 될듯

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".handlers"])

    config = providers.Configuration(yaml_files=["config.yml"])

    # api_key, timeout 은 생성자에 들어가는 파라메터
    giphy_client = providers.Factory(
        giphy.GiphyClient,
        api_key=config.giphy.api_key,
        timeout=config.giphy.request_timeout,
    )

    # giphy_client 는 생성자에 들어가는 파라메터
    search_service = providers.Factory(
        services.SearchService2,
        giphy_client=giphy_client,
    )

