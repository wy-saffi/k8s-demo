FROM openjdk:11

EXPOSE 8080

WORKDIR /applications

COPY target/demo-0.0.1-SNAPSHOT.jar /applications/demo-0.0.1-SNAPSHOT.jar

ENTRYPOINT ["java","-jar", "demo-0.0.1-SNAPSHOT.jar"]