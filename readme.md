# Litestar + Scrapy

This is an MRE that highlights a problem running Scrapy/Twisted within an ASGI framework, Litestar. This MRE automatically runs the `scrapy` example crawler, which was installed using the scrapy CLI.

- https://github.com/litestar-org/litestar
- https://github.com/scrapy/scrapy

## The issue

Twisted's `AsyncioSelectorReactor` throws an exception when it's passed an existing event loop: `RuntimeError: this event loop is already running.`

- This is caused by telling an existing loop to run forever: `self._asyncioEventloop.run_forever()`

There is also an issue on shutdown: `RuntimeError: Event loop stopped before Future completed.`

- Cause of the shutdown error is TBD.

## To Reproduce

- Copy this git locally and install using Poetry or the requirements.txt file.
- In termial, type `litestar run` or `uvicorn app:app`. There is also an included debug config for `vscode`.
- Open `http://127.0.0.1:8000` in your browser, it will automatically trigger a `scrapy`` crawl
- View the logs, you should see the exceptions
- Shut down the app with CTRL+C and you should see the shutdown exceptions.
