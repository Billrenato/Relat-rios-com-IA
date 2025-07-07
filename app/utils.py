def validar_query(sql):
    proibidos = ["drop", "delete", "update"]
    if any(p in sql.lower() for p in proibidos):
        raise Exception("Query perigosa detectada!")