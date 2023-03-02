FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/default.conf

#COPY --from=frontend_build /app/build /usr/share/nginx/html
#VOLUME /usr/share/nginx/html
VOLUME /etc/nginx

EXPOSE 80