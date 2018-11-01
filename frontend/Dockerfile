FROM node:8.12

COPY ./package.json /usr/app/src

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN npm install --save
COPY . /usr/src/app

RUN npm install -g @angular/cli@7.0.2 --save

# add app
# start app
CMD ng serve --host 0.0.0.0
EXPOSE 4200