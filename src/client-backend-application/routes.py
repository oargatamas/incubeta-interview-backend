from fastapi import FastAPI
import service as service

app = FastAPI()


@app.get("/offers")
async def get_offers(origin, destination, date_of_departure):
    return service.get_offers(origin, destination, date_of_departure)