FROM python:3-slim
WORKDIR /cisco-dnac-healthcheck-netconf/
COPY ./run.py ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]
