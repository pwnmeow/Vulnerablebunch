FROM node:12-alpine
ENV WORKDIR /usr/src/app/
WORKDIR $WORKDIR
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && apk add --update --no-cache g++ && apk add --update --no-cache make
COPY package*.json $WORKDIR
RUN npm install --production --build-from-source 

FROM node:12-alpine
ENV USER node
ENV WORKDIR /home/$USER/app
WORKDIR $WORKDIR
COPY --from=0 /usr/src/app/node_modules node_modules
RUN chown $USER:$USER $WORKDIR
COPY --chown=node . $WORKDIR
# In production environment uncomment the next line
#RUN chown -R $USER:$USER /home/$USER && chmod -R g-s,o-rx /home/$USER && chmod -R o-wrx $WORKDIR
# Then all further actions including running the containers should be done under non-root user.
USER $USER
EXPOSE 4000
