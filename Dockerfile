# This file defines the Docker container that will contain the Crawler app.
# From the source image #python
FROM python:3.6-slim
# Identify maintainer
LABEL maintainer = "robertclerc@outlook.fr"
# Set the default working directory
WORKDIR /app/
COPY city.list.json weather_api_formation.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python","./weather_api_formation.py"]
# When the container starts, run this
ENTRYPOINT python ./weather_api_formation.py
