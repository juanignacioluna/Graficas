<template>
  <div class="grafica">


    <Navbar />


    <div class="row contenidoPrincipalGrafica">
      <div class="sm-0 md-2 col"></div>
      <div class="sm-12 md-8 col">


        <h1 class="titulo">Gráfica</h1>

        <button v-on:click="eliminar" class="btn-block btn-danger">Eliminar</button>

        <br>

        <div class="chartContenedor">

          <svg class="line-chart"></svg>

        </div>




      </div>
      <div class="sm-0 md-2 col"></div>
    </div>




  </div>
</template>

<style>

  .contenidoPrincipalGrafica{

    position: relative;

  }

  .titulo{
    color: black;
    text-shadow: -1px 0 white, 0 2px white, 1px 0 white, 0 -1px white;
  }

  svg{
    position: relative;
  }

  .chartContenedor{
    max-width: 98%;
    max-height:700px;
  }



  @media only screen and (max-width: 991px) {

    .contenidoPrincipalGrafica{

      margin-top: -35px;

    }

  }


</style>

<script>

import Navbar from '@/components/Navbar.vue'
import chartXkcd from 'chart.xkcd';

export default {
  name: 'Grafica',

  data(){

    return{

      id: 404,

      titulo: "",

      tipo: "",

      cantidad: 404,

      datos: null

    }
  },

  components: {
    Navbar,
  },

  mounted: function () {


    this.id = this.$route.params.id;




    fetch('https://graficas-back.herokuapp.com/polls/getGrafica/',{
    method: 'POST',
    headers: new Headers({}),
    body: JSON.stringify({id: this.id}),
    })
    .then(response => response.json())
    .then((data) => {

      this.tipo = data['Grafica'][0]['fields']['tipo']

      this.titulo = data['Grafica'][0]['fields']['titulo']

      this.cantidad = data['Grafica'][0]['fields']['cantidad']

      this.datos = data['Grafica'][0]['fields']


      let nombres = []

      let numeros = []


      for (let i = 0; i < this.cantidad; i++) {

        switch ((i+1)) {
          case 1:
            nombres[i] = this.datos['nombre1'];
            numeros[i] = this.datos['numero1'];
            break;
          case 2:
            nombres[i] = this.datos['nombre2'];
            numeros[i] = this.datos['numero2'];
            break; 
          case 3: 
            nombres[i] = this.datos['nombre3'];
            numeros[i] = this.datos['numero3'];
            break; 
          case 4:
            nombres[i] = this.datos['nombre4'];
            numeros[i] = this.datos['numero4'];
            break;
          case 5:
            nombres[i] = this.datos['nombre5'];
            numeros[i] = this.datos['numero5'];
            break;
          case 6:
            nombres[i] = this.datos['nombre6'];
            numeros[i] = this.datos['numero6'];
            break;
          case 7:
            nombres[i] = this.datos['nombre7'];
            numeros[i] = this.datos['numero7'];
            break; 
          case 8: 
            nombres[i] = this.datos['nombre8'];
            numeros[i] = this.datos['numero8'];
            break; 
          case 9:
            nombres[i] = this.datos['nombre9'];
            numeros[i] = this.datos['numero9'];
            break;
          case 10:
            nombres[i] = this.datos['nombre10'];
            numeros[i] = this.datos['numero10'];
            break;

        }

      }


      if(this.tipo=="Barra"){

          const svg = document.querySelector('.line-chart')

          const myChart = new chartXkcd.Bar(svg, {
            title: this.titulo,
            data: {
              labels: nombres,
              datasets: [{
                data: numeros,
              }],
            },
          });

      }

      if(this.tipo=="Torta"){

          const svg = document.querySelector('.line-chart')

          const myChart = new chartXkcd.Pie(svg, {
            title: this.titulo, 
            data: {
              labels: nombres,
              datasets: [{
                data: numeros,
              }],
            },
            options: { 
              innerRadius: 0.5,
              legendPosition: chartXkcd.config.positionType.upRight,
            },
          });
        
      }

    })


  },

methods: {


  eliminar(){

      fetch('https://graficas-back.herokuapp.com/polls/eliminar/',{
        method: 'POST',
        headers: new Headers({}),
        body: JSON.stringify({id: this.id}),
      })
      .then(response => response.text())
      .then((data) => {

        console.log(data)

        this.$router.push({ path: `/verGraficas` })

      })



  }


},

}


</script>
