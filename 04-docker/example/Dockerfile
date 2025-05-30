FROM nginx:1.28.0-bookworm

WORKDIR /usr/share/nginx/html

RUN apt-get update

COPY index.html .

EXPOSE 8080

CMD ["nginx","-g","daemon off;"]
