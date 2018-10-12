FROM python:3

# WORKDIR /usr/src/app

COPY requirements.txt ./
COPY . /usr/src/app
ADD api.py ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY api.py ./
CMD [ "python", "api.py" ]