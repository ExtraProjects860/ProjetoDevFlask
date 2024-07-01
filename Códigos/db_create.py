from comunidade import app, database

with app.app_context():    
    database.create_all()

    # usuario = Usuario(username="Davi", email="davi@gmail.com", senha="123456")
    # usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123456")

    # database.session.add(usuario)
    # database.session.add(usuario2)

    # database.session.commit()
    # meus_usuarios = Usuario.query.all()
    # print(meus_usuarios[0].id)
    # print(meus_usuarios[0].email)
    # print(meus_usuarios[0].posts)
    
    # usuario_teste = Usuario.query.filter_by(id=2).first()
    # print(usuario_teste.email)
    
    # meu_post = Post(id_usuario=1, titulo="Primeiro Post do Davi", corpo="Testando!")
    # database.session.add(meu_post)
    # database.session.commit()
    
    # post = Post.query.first()
    # print(post.titulo)
    # print(post.autor.email)