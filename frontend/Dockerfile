FROM node:12-alpine as builder

## Install build toolchain, install node deps and compile native add-ons
RUN apk add --no-cache python make g++
RUN npm install node-gyp node-sass

FROM node:12-alpine as app
COPY --from=builder node_modules .

# Create app directory
WORKDIR /usr/src/app
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]