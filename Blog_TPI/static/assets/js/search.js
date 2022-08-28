const secciones = [
    {nombre:'Inicio',dir:'http://localhost:8000/'},
    {nombre:'Publicaciones',dir:'http://localhost:8000/Noticias/listar/'},
    {nombre:'Eventos',dir:'http://localhost:8000/Enventos/principal/'},
    {nombre:'Galeria',dir:'http://localhost:8000/Galeria/principal/'},
    {nombre:'Preguntas frecuentes',dir:'http://localhost:8000/Fechas_Importantes/principal/'},
    {nombre:'Acerca de nosotros',dir:'http://localhost:8000/Acerca_Nosotros/principal/'},
    {nombre:'Contacto',dir:'http://localhost:8000/Contacto/principal/'},
    {nombre:'Login',dir:'http://localhost:8000/login/'},
    {nombre:'Registro',dir:'http://localhost:8000/Usuario/registro/'},
]

const formulario = document.querySelector('#formulario');
const boton = document.querySelector('#boton');
const resultado = document.querySelector('#resultados');

const filtrar = ()=>{
    //console.log(formulario.value);
    resultado.innerHTML='';

    const texto = formulario.value.toLowerCase();

    for(let seccion of secciones){
        let nombre = seccion.nombre.toLowerCase();
        if(nombre.indexOf(texto) !== -1){
            resultado.innerHTML += `
                <a href="${seccion.dir}"><li>${seccion.nombre}</li></a>
            `
        }
    }
    if(resultado.innerHTML === ''){
        resultado.innerHTML +=` 
                <li>Sección no encontrada</li>
        `
    }
}

boton.addEventListener('click',filtrar);
addEventListener('keydown',filtrar);