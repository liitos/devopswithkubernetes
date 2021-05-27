# syntax=docker/dockerfile:1
FROM alpine:3.7
WORKDIR /app
COPY . .
RUN apk --no-cache add curl
CMD [ "/bin/ash" , "dailytodos.sh"]

