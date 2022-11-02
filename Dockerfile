FROM python:3.10

ENV DASH_DEBUG_MODE False
RUN apt update && apt install -y libudunits2-dev
COPY ./app /app
WORKDIR /app
RUN set -ex && pip install -r requirements.txt
EXPOSE 8050
CMD ["gunicorn", "-b", "0.0.0.0:8050", "--reload", "app:server"]
