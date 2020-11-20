FROM node:15.2.1-alpine3.12

# Print build information
RUN printf "I am running on ${BUILDPLATFORM:-linux/amd64}, building for ${TARGETPLATFORM:-linux/amd64}\n$(uname -a)\n"

ARG GITHUB_CLIENT_ID
ARG APP_HOSTNAME=localhost

# Copy CloudProxy code
USER node
RUN mkdir -p /home/node/frontend
WORKDIR /home/node/frontend
COPY --chown=node:node . ./

ENV GITHUB_CLIENT_ID=$GITHUB_CLIENT_ID APP_HOSTNAME=$APP_HOSTNAME

# Install package, build, and prune dev deps
RUN npm install \
  && npm run build \
  && npm prune --production

EXPOSE 3000
CMD ["npm", "start", "--", "--hostname", "0.0.0.0"]
