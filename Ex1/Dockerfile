# STEP 3: Configure the docker container

# The image we are going to use from the Docker Hub
FROM python:3.11

# Creating a code directory inside our container and assign it as a working directory
WORKDIR /code

# Since our container is an isolated environment, we're going to need to copy
# all the necessary files that will need the container to execute
# and place it inside the code directory.
COPY ./requirements.txt /code/requirements.txt

# Now that it is copy, we are going to run the PIP install
# those requirements inside the container 
RUN pip install --no-cache-dir -r /code/requirements.txt

# And copy the application folder inside our working directory code
COPY ./app /code/app

# Expose some PORT because again this is isolated environment and 
# in order to interact with this we need to expose some endpoint
# to where we can send the data or interact with this container:
EXPOSE 8000

# run the application

# uvicorn 
# is a server gateway interface, it's the binning element that handles 
# the web connections from the browser or API client and then allows FastAPI
# to serve the actual request it also allows you to properly spawn many workers and scale
# your deployment properly 

# the app.create_api:app 
# is really simple it will just run the create_api.py file
# from the app directory and initialize our API which in this case also called an app (= FastAPI())

# "--host", "0.0.0.0"
# When we set the network ot host a container was share the host network stack and all the interfaces from the 
# host will be available to the container 

# "--port", "8000"
# and the last one will be the port which we have exposed in the previous step.
# This means that a request to a container on PORT 8000 will be forwarded to the application bound to PORT 8000
# inside the container.

CMD ["uvicorn", "app.create_api:app", "--host", "0.0.0.0", "--port", "8000"]