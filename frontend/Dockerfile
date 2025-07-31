FROM node:18

WORKDIR /app

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app code
COPY . .

EXPOSE 3000

CMD ["npm", "start"]

