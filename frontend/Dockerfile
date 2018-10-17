FROM node:8.12

COPY ./package.json /usr/app/src

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
COPY . /usr/src/app
COPY angular.json /usr/src/app/angular.json

RUN npm install --save
RUN npm install -g @angular/cli@6.2.5 --save

# add app

# start app
CMD ng serve --host 0.0.0.0