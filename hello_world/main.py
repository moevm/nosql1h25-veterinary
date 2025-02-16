from neo4j import GraphDatabase

# Подключение к базе
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "testtest")

def create_and_read_example():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            # Создание узла
            session.run("CREATE (:Hello {message: 'test message'})")

            # Чтение узла
            result = session.run("MATCH (h:Hello) RETURN h.message AS message")
            for record in result:
                print(record["message"])

if __name__ == "__main__":
    create_and_read_example()