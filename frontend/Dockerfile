FROM node:lts-alpine

COPY . /var/www/html

WORKDIR /var/www/html

RUN npm install

CMD ["npm", "run", "serve"]