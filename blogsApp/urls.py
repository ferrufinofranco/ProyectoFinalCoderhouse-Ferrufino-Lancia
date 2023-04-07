from django.urls import path
from blogsApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #pagina de inicio
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
    #gestion de usuarios
    path('registroUsuarios/', registro_usuario, name='blogsAppRegistroUsuarios'),
    path('loginUsuario/', login_usuario, name='blogsAppLoginUsuario'),
    path('logoutUsuario/', LogoutView.as_view(template_name='blog/logoutUsuario.html'), name='blogsAppLogoutUsuario'),
    #gestion de blogs
    path('registroBlogs/', crear_blog, name='blogsAppCrearBlogs'),
    path('busquedaBlogs/', buscar_blogs, name='blogsAppBuscarBlogs'),
    path('eliminarBlog/<int:pk>/', eliminarBlog, name='blogsAppEliminarBlog'),
    path('editarBlog/<int:pk>/',editar_blog, name='blogsAppEditarBlog'),
    path('blog/<int:pk>/', detalle_blog, name='blogsAppDetalleBlog'),
    path('blogsExistentes/', listar_blogs, name='blogsAppListarLogs')
]
