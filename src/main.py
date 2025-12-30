from dotenv import load_dotenv
from config import Config
load_dotenv()
Config.init()

import uvicorn

if __name__ == '__main__': # pragma: no cover
    uvicorn.run(
        "api.server.fast:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )