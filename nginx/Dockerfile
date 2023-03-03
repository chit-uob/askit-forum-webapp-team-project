FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/default.conf

#COPY --from=frontend_build /app/build /usr/share/nginx/html
#VOLUME /usr/share/nginx/html
VOLUME /etc/nginx
# add a volumn which maps from /home/ec2-user/teamai55-22.bham.team to /etc/nginx
#VOLUME /home/ec2-user/teamai55-22.bham.team

EXPOSE 80
EXPOSE 443