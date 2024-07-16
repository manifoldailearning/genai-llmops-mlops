#base image
FROM python:3.8-slim-buster
# upgrade pip
RUN pip install --upgrade pip 

# Copiying all the files to source directory
COPY . /src

# Set working directory to previously added source directory
WORKDIR /src

# Giving permissions to python file
RUN chmod +x dist/prediction_model_manifoldailearning-1.0.0.tar.gz
RUN pip install dist/prediction_model_manifoldailearning-1.0.0.tar.gz

RUN chmod +x prediction_model/training_pipeline.py

RUN python prediction_model/training_pipeline.py

# Install required python dependencies from requirements file
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app","--host", "0.0.0.0" ,"--port", "8080"]