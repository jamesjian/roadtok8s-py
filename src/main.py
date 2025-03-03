from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_index():
	"""
	Return a  Python Dictionary that supports JSON serialization.
	"""
	return {"Hello":"World 04/03"}


@app.get("/api/v1/hello-world")
def read_index_v1():
	"""
	Return a  Python Dictionary that supports JSON serialization.
	"""
	return {"Hello":"World", "version": "v1"}


