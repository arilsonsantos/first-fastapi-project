import uvicorn

if __name__ == "__main__":
    dev = 1
    if dev == 1:
        uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info", reload=True, debug=True)