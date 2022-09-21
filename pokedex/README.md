# Pokemon Project

Este proyecto fue realizado como una prueba técnica. El objetivo de este fue realizar un "Pokedex Web". Este hará una petición a una API para extraer la información de los pokemones. Posteriormente los mostrará en pantalla, primordialmente deberá mostrar la imagen y el nombre del pokemon, durante 30 segundos y posteriormente cambiará a otro pokemón. También deberá tener un botón con el cual se pueda realizar la acción de cambiar pokemón.

Se pidió desarollarlo con javascript y utilizar cualquier librería, así como las apis necesarias, también se pidió una interfáz amigable, con una preferencia en bootstrap.

Por lo anterior el proyecto fue realizado con webpack y bootstrap.

## Instalation

Primero se tendrá que clonar el repositorio. Se puede hacer desde el siguiente link:

```
git clone https://github.com/JosephColinP/Projects.git
```


Una vez clonado existen dos carpetas, al momento de escribir esto, la carpeta del proyecto solicitado es "pokedex" por lo que entraremos a esta. 

```
cd Projects/pokedex/
```

*Nota: La otra carpeta se llama home-bees, esta puede ser eliminada ya que solo era un proyecto de práctica con solo css.*


Posteriormente se tiene que configurar el proyecto. Primero se tienen que instalar todos los paquetes de node:

```
npm i
```


Luego se tendrá que construir el proyecto.

```
npm run build
```


Por último se tendrá que arrancar el servidor.

```
npm run start
```


## Consideraciones


### env var

Normalmente las variables de entorno no se tienen que mostrar. Decidí omitirlo en el archivo .gitignore ya que por esta ocaciones es una API pública, así que no importa si se muestra o no.


### updates

Puede que al momento de ver este proyecto muchos paquetes estén desactualizados o el mismo node. Entonces se recomienda actualizar todo para una correcta ejecución.


