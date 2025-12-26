from service.graph import Neo4jGraph
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

graph = Neo4jGraph(uri, username, password)

graph.create_graph_node(node_name="Act",node_properties={"name":"Ciao"})
