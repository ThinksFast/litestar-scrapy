import logging

from litestar import Litestar, Response, get
from litestar.background_tasks import BackgroundTask
from litestar.logging import LoggingConfig
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

logger = logging.getLogger("litestar")
configure_logging()


async def run_crawl() -> None:
    process = CrawlerProcess(get_project_settings())
    process.crawl("example")
    process.start(stop_after_crawl=False)


@get("/")
async def serveHomepage() -> Response:
    return Response("Hello World", background=BackgroundTask(run_crawl))


logging_config = LoggingConfig(propagate=False)

app = Litestar(
    route_handlers=[serveHomepage],
    lifespan=[],
    debug=True,
    logging_config=logging_config,
)
