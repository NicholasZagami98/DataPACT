from neo4j import GraphDatabase
from query import NodeQueries

class Neo4jGraph:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def verify_connection(self):
        """Test database connection"""
        self.driver.verify_connectivity()
        print("✓ Connected to Neo4j successfully!")

    def clear_database(self):
        """Clear all nodes and relationships"""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            print("✓ Database cleared")

    def create_graph_node(self, node_name, node_properties):
        with self.driver.session() as session:
            query = NodeQueries.CREATE_NODE.format(node_name=node_name, node_properties=node_properties)
            result = session.run(query)
            node_id = result.single()["node_id"]
            print(f"✓ Created {node_name} node (ID: {node_id})")
            return node_id

    def create_relationship(self):
        pass

    def create_graph(self):
        pass



