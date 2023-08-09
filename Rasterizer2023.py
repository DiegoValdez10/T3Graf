from gl import Renderer
import shaders

# El tamaño del FrameBuffer
width = 1250
height = 960

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# Función para renderizar y guardar la imagen
def render_and_save(filename):
    # Se renderiza la escena
    rend.glRender()
    # Se crea el FrameBuffer con la escena renderizada
    rend.glFinish(filename)

 #Medium shot
#rend.glLookAt(camPos=(0, 0, 1),
#              eyePos=(0, 0, 0))
#rend.glLoadModel(filename="model.obj",
#                 textureName="textures/model.bmp",
#                 translate=(width / 2, height / 4, 0),
#                 scale=(50, 50, 50),
#                 rotate=(0, 180, 0))
#render_and_save("medium_shot.bmp")

# Low angle
#rend.glLookAt(camPos=(0, 1, 3),
#             eyePos=(0, -2, -3))
#rend.glLoadModel(filename="model.obj",
#                 textureName="textures/model.bmp",
#                 translate=(width / 2, height / 4, 0),
#                 scale=(50, 50, 50),
#                 rotate=(0, 180, 0))
#render_and_save("low_angle.bmp")

#High angle
#rend.glLookAt(camPos=(0, 15, 1),
#              eyePos=(0, 0, 0))
#rend.glLoadModel(filename="model.obj",
#                 textureName="textures/model.bmp",
#                 translate=(width / 2, height / 4, 0),
#                scale=(50, 50, 50),
#                 rotate=(0, 180, 0))
#render_and_save("high_angle.bmp")

 #Dutch angle
rend.glLookAt(camPos=(1, 1, 1),
              eyePos=(0, 0, 0))
rend.glLoadModel(filename="model.obj",
                 textureName="textures/model.bmp",
                 translate=(width / 2, height / 2, 0),
                 scale=(50, 50, 50),
                 rotate=(-30, 180, 10))  # Applying a Dutch angle rotation
render_and_save("dutch_angle.bmp")
