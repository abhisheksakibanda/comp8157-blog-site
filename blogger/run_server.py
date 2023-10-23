if __name__ == '__main__':
    import uvicorn

    uvicorn.run("blogger.controller.controller:app", reload=True)
