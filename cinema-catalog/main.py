import py_eureka_client.eureka_client as eureka_client

my_server_port=50001
eureka_client.init(
    eureka_server="http://localhost:50000",
    app_name="cinema-catalog",
    instance_port=my_server_port
)

response=eureka_client.do_service("movies-service","/movies/all")
print("Result of the ")