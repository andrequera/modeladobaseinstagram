import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

 
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombreusuario = Column(String(250))
    nombre = Column(String(250))
    apellido = Column(String(250))
    email = Column(String(250))

class Seguidor(Base):
    __tablename__ = 'seguidor'
    id = Column(Integer, primary_key=True)   
    user_from_id = Column(Integer, ForeignKey('usuario.id'))
    user_to_id = Column(Integer, ForeignKey('usuario.id'))
    usuario= relationship(Usuario)
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    
class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    texto_comentario = Column(String(250))
    autor_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    tipo = Column(Integer)
    post_id= Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
