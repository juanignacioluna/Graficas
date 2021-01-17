<template>
  <div class="nueva">


    <Navbar />


    <div class="row contenidoPrincipalNueva">
      <div class="sm-0 md-2 col"></div>
      <div class="sm-12 md-8 col">


        <h1 class="titulo">Nueva gráfica</h1>

        <div class="form-group">
          <select v-model="tipo" id="tipoSelect" @change="onChangeSelect($event)" class="input-block inputNueva">
            <option value="Barra">Barra</option>
            <option value="Torta">Torta</option>
          </select>
        </div>

        <div id="ajustes">

          <div v-for="ajuste in ajustes" :key="ajuste.id">

              <div class="form-group">
                <input @change="onChangeInput($event)" class="input-block inputNueva" :type="ajuste.tipo" :placeholder="ajuste.nombre">
              </div>

          </div>
          
        </div>

        <div class="barras"></div>

        <div class="porciones"></div>

        <button v-on:click="crear" class="btn-block btn-success">CREAR</button>




      </div>
      <div class="sm-0 md-2 col"></div>
    </div>




  </div>
</template>

<style>


  .inputNueva{

    background: white;

  }

  .contenidoPrincipalNueva{

    position: relative;

  }

  .titulo{
    color: black;
    text-shadow: -1px 0 white, 0 2px white, 1px 0 white, 0 -1px white;
  }


  @media only screen and (max-width: 990px) {

      .contenidoPrincipalNueva{

        margin-top: -35px;

      }

  }


</style>

<script>

import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Nueva',

  data(){

    return{

      tipo: "Barra",

      ajustes: [

            {id: 1, nombre: "Titulo", tipo: "text"},
            {id: 2, nombre: "Cantidad de barras", tipo: "number"},

      ],

    }
  },

  components: {
    Navbar,
  },

  mounted: function () {

  },

  methods: {

    crear(){

            let tipo = this.tipo;

            let titulo = document.getElementById("ajustes").firstChild.childNodes[0].firstChild.value;

            let cantidad = document.getElementById("ajustes").childNodes[1].childNodes[0].firstChild.value;

            let datos = [];


            let contenido;


            if(tipo=="Barra"){

              contenido = document.getElementsByClassName("barras")[0]

            }

            if(tipo=="Torta"){

              contenido = document.getElementsByClassName("porciones")[0]

            }


            for (let i = 0; i < contenido.childNodes.length; i++){

                  datos[i] = contenido.childNodes[i].value

            }



            fetch('https://graficas-back.herokuapp.com/polls/crear/',{
              method: 'POST',
              headers: new Headers({}),
              body: JSON.stringify({tipo: tipo, titulo: titulo, cantidad: cantidad, datos: datos}),
            })
            .then(response => response.text())
            .then((data) => {

              console.log(data)

              this.$router.push({ path: `/grafica/${data}` })

            })

    },

    onChangeInput(event){


      if(event.target.placeholder=="Cantidad de porciones"){


        document.getElementsByClassName("porciones")[0].innerHTML = "";

        for (let i = 0; i < event.target.value; i++){


            let nombre = document.createElement("input");    

            nombre.className = "input-block inputNueva"

            nombre.type = "text"

            nombre.style.display = "inline-block";

            nombre.placeholder = "Nombre de porcion " + (i+1)                     

            document.getElementsByClassName("porciones")[0].appendChild(nombre); 


            let numero = document.createElement("input");    

            numero.className = "input-block inputNueva"

            numero.type = "number"

            numero.style.display = "inline-block";

            numero.placeholder = "Nro de porcion " + (i+1)                     

            document.getElementsByClassName("porciones")[0].appendChild(numero); 

        }




      }


      if(event.target.placeholder=="Cantidad de barras"){


        document.getElementsByClassName("barras")[0].innerHTML = "";

        for (let i = 0; i < event.target.value; i++){


            let nombre = document.createElement("input");    

            nombre.className = "input-block inputNueva"

            nombre.type = "text"

            nombre.style.display = "inline-block";

            nombre.placeholder = "Nombre de barra " + (i+1)                     

            document.getElementsByClassName("barras")[0].appendChild(nombre); 


            let numero = document.createElement("input");    

            numero.className = "input-block inputNueva"

            numero.type = "number"

            numero.style.display = "inline-block";

            numero.placeholder = "Numero de barra " + (i+1)                     

            document.getElementsByClassName("barras")[0].appendChild(numero); 

        }




      }


    },

    onChangeSelect(event){
      document.getElementsByClassName("barras")[0].innerHTML = "";
      document.getElementsByClassName("porciones")[0].innerHTML = "";

      switch (event.target.value) {
        case 'Barra':
          this.ajustes = [];
          this.ajustes= [
            {id: 1, nombre: "Titulo", tipo: "text"},
            {id: 2, nombre: "Cantidad de barras", tipo: "number"},];
          break;
        case 'Torta':
          this.ajustes = [];
          this.ajustes= [
            {id: 1, nombre: "Titulo", tipo: "text"},
            {id: 2, nombre: "Cantidad de porciones", tipo: "number"},];
          break;
      }

      $("input").val('');

    },

  },
}
</script>
