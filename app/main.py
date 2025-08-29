from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.logger import logger
from app.api.questions import router as questions_router
from app.api.answers import router as answers_router

app = FastAPI(title="Q&A API Service", version="0.1.0")
app.include_router(questions_router)
app.include_router(answers_router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc} | path={request.url.path}")
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}
