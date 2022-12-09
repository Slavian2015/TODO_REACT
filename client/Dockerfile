FROM node:alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY ./ ./
RUN npm install -g npm@9.2.0
RUN npm i react-router-dom --save
CMD ["npm", "run", "start"]

