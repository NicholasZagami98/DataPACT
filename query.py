"""
Neo4j Cypher query repository
"""

# rel: https://community.neo4j.com/t/creating-a-relationship-between-2-nodes/38408/2
# rel optimal way: https://stackoverflow.com/questions/69702238/neo4j-cypher-iteratively-creating-relationships-in-optimal-way
# https://www.quackit.com/neo4j/tutorial/neo4j_create_a_relationship_using_cypher.cfm


class NodeQueries:
    """Queries for node operations"""

    CREATE_NODE = """
    CREATE (n:{node_name})
    SET n = $node_properties
    RETURN id(n) as node_id
    """

class RelationQueries:
    """Queries for relation operations"""

    CREATE_RELATIONSHIP = """
    MATCH (ln:{left_node_name}), (rn:{right_node_name})
    WHERE ln.id = rn.id
    CREATE (ln)-[:$relationship]->(rn);
    
    """