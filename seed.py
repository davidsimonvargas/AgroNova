import hashlib
import sqlmodel

from src.models import Usuario

engine = sqlmodel.create_engine("sqlite:///db/agronova.db")
sqlmodel.SQLModel.metadata.create_all(engine)

with sqlmodel.Session(engine) as session:
    existente = session.exec(
        sqlmodel.select(Usuario).where(Usuario.correo == "admin@agronova.com")
    ).first()
    if not existente:
        usuario = Usuario(
            nombres="Admin",
            apellidos="AgroNova",
            correo="admin@agronova.com",
            contraseña_hash=hashlib.sha256("admin123".encode()).hexdigest(),
            telefono="555-0100",
            rol="administrador",
        )
        session.add(usuario)
        session.commit()
        print("Usuario de prueba creado: admin@agronova.com / admin123")
    else:
        print("El usuario de prueba ya existe")
