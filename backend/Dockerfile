FROM node:18-alpine

WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY package*.json ./
RUN npm install --production

COPY src/ ./src/
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 5000
CMD ["node", "src/index.js"]
