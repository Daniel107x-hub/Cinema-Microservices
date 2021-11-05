FROM openjdk:11
COPY ./target/component-movies-1.0-SNAPSHOT.jar /tmp
WORKDIR /tmp
EXPOSE 50000
ENTRYPOINT ["java","-jar","component-movies-1.0-SNAPSHOT.jar"]