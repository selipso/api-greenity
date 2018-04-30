FROM keymetrics/pm2:8-alpine
# Create folder to host the project
RUN mkdir -p /var/www/build
WORKDIR /var/www
# Add assets from the build folder
# into the container's server folder
COPY ./app/build /var/www/build
COPY ./*.js* /var/www/
# Install static server and monitor
RUN npm install
CMD [ "pm2-runtime", "npm", "--", "start" ]
