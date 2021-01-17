<template>
  <div class="home">


    <Navbar />



    <div class="row contenidoPrincipal">
      <div class="sm-0 lg-2 col"></div>
      <div class="sm-12 lg-8 col">


      <wired-card elevation="5" fill="#383838">

        <div class="bienvenida">

          <h1>Bienvenido al creador de graficas hechas a mano!</h1>

          <h4>Esta app te va a ayudar a crear tus propias graficas, con un
          diseño divertido. Ademas van a quedar guardadas en una base de datos,
          y puedes eliminarlas si quieres.</h4>

        </div>

      </wired-card>

      <router-link to="/verGraficas">
        <button class="btn-large btn-success">VER GRÁFICAS</button>
      </router-link>
      
      <router-link to="/nueva">
        <button class="btn-large btn-secondary">CREAR NUEVA GRÁFICA</button>
      </router-link>

      </div>
      <div class="sm-0 lg-2 col"></div>
    </div>


  </div>
</template>

<style>

  .bienvenida{
    color: #f2f2f2;
  }

  .contenidoPrincipal{

    margin-top: 60px;

  }

  button{
    position: relative;
    margin-right: 10px;
    margin-top: 20px;
  }

  @media only screen and (max-width: 768px) {

    .bienvenida *{
      font-size: 1.5em
    }

    .home button{
      font-size: 1.5em
    }

  }

  @media only screen and (max-width: 711px) {

    .contenidoPrincipal{

      margin-top: 30px;

    }

  }

  @media only screen and (max-width: 622px) {

    .contenidoPrincipal{

      margin-top: 25px;

    }

    .bienvenida *{
      font-size: 1.4em
    }

    .home button{
      font-size: 1.2em
    }

  }


  @media only screen and (max-width: 535px) {

    .bienvenida *{
      font-size: 1.3em
    }

    .home button{
      font-size: 1.0em
    }

  }


  @media only screen and (max-width: 465px) {

    .home button{
      font-size: 0.9em
    }

  }

</style>

<script>

import * as wired from "wired-elements";
import chartXkcd from 'chart.xkcd';
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Home',

  components: {
    Navbar,
  },

  mounted: function () {

  },

  data(){

    return{

    }
  },
}
</script>
