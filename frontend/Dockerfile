# Use an official Node runtime as a parent image
FROM node:20.12.2

# Set the working directory
WORKDIR /app

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Install Angular CLI
RUN npm install -g @angular/cli

# Install app dependencies by copying
# package.json and package-lock.json
COPY package*.json /app/

# Install dependencies
RUN npm install

# Add app
COPY . /app

# Expose the port the app runs on
EXPOSE 4200

# Serve the app
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll", "2000"]
