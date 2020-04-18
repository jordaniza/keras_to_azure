# choose a base image, in this case Python 3 with FROM

FROM python:3.6

# write commands to copy files and install dependencies:

# set a directory for the app WITHIN the Docker container
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command, equivalent to "python app.py"
CMD ["python", "./app.py", "runserver", "-h", "0.0.0.0"]
