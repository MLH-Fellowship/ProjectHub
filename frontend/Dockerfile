FROM node:15.2.1-alpine3.12

# Print build information
RUN printf "I am running on ${BUILDPLATFORM:-linux/amd64}, building for ${TARGETPLATFORM:-linux/amd64}\n$(uname -a)\n"

ARG DOCKER_BACKEND_HOST
ARG GITHUB_CLIENT_ID
ARG FRONTEND_BASE_URL

# Copy CloudProxy code
USER node
RUN mkdir -p /home/node/frontend
WORKDIR /home/node/frontend

COPY --chown=node:node ./package.json ./
COPY --chown=node:node ./package-lock.json ./
RUN npm install

ENV GITHUB_CLIENT_ID=$GITHUB_CLIENT_ID FRONTEND_BASE_URL=$FRONTEND_BASE_URL DOCKER_BACKEND_HOST=$DOCKER_BACKEND_HOST
RUN printf "ENV: GITHUB_CLIENT_ID=${GITHUB_CLIENT_ID}, FRONTEND_BASE_URL=${FRONTEND_BASE_URL}, DOCKER_BACKEND_HOST=${DOCKER_BACKEND_HOST}\n"

COPY --chown=node:node . ./
RUN npm run build
# && npm prune --production



EXPOSE 3000
CMD ["npm", "start", "--", "--hostname", "0.0.0.0"]
