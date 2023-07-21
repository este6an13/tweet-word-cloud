# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the required files into the container
COPY d3.layout.cloud.js .
COPY process_tweets.py .
COPY stopwords.txt .
COPY test_process_tweets.py .
COPY tweets.txt .
COPY word_cloud.py .
COPY test_word_cloud.py .

# Copy the bash script into the container
COPY run_scripts.sh .

# Make the bash script executable
RUN chmod +x run_scripts.sh

# Set the entry point to the bash script
ENTRYPOINT [ "./run_scripts.sh" ]

