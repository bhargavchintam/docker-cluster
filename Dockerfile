FROM ubuntu:latest
COPY . ./

# Importing Libraries and Packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
RUN apt-get install -y awscli
RUN apt-get install -y xvfb
RUN apt-get install -y scrot
RUN apt-get install -y python3-tk
RUN apt-get install -y python3-dev

# Configurations for Virtual Display
RUN export DISPLAY=":0"
RUN echo "DISPLAY=:0" >> ~/.bashrc
RUN touch ~/.Xauthority

# Installing Chrome
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt install -y wget
RUN apt install -y unzip
RUN wget --version
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get update && apt-get install -y ./google-chrome-stable_current_amd64.deb

# Importing Chromedriver for selenium
RUN wget https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip

# Removing unwanted files
RUN rm google-chrome-stable_current_amd64.deb
RUN rm chromedriver_linux64.zip

# Run Python Script
CMD ["python3", "app.py"]
