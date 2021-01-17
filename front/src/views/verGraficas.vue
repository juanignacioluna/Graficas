<template>
  <div class="verGraficas">


	<Navbar />


    <div class="row contenidoPrincipalGraficas">
      <div class="sm-0 lg-2 col"></div>
      <div class="sm-12 lg-8 col">


		<h1 class="titulo">Gráficas</h1>

		<router-link to="/nueva">
			<button class="btn-block btn-secondary">Agregar nueva gráfica</button>
		</router-link>


		<div class="row">
	        <div class="col-6 md-4 lg-3 col" v-for="grafica in graficas" :key="grafica.id">

	    		<router-link :to="{ name: 'Grafica', params: { id: grafica.id }}">
					<div class="card" style="background: white;">

					  <img :src="getImgUrl(grafica.tipo)">

					  <div class="card-body">
					    <p class="card-title">{{grafica.titulo}}</p>
					  </div>
					</div>
				</router-link>

	        </div>
        </div>

      	
      </div>
      <div class="sm-0 lg-2 col"></div>
    </div>


  </div>
</template>

<style>

	.contenidoPrincipalGraficas{

		position: relative;

	}

	.titulo{
		color: black;
		text-shadow: -1px 0 white, 0 2px white, 1px 0 white, 0 -1px white;
	}


	@media only screen and (max-width: 1200px) {

	    .contenidoPrincipalGraficas{

	      margin-top: -30px;

	    }

	}


</style>

<script>

import Navbar from '@/components/Navbar.vue'

export default {
  name: 'VerGraficas',
  data(){

    return{

    	graficas: [],

    }
  },
  components: {
  	Navbar,
  },
  mounted: function () {


		fetch('https://graficas-back.herokuapp.com/polls/verGraficas/',{
			method: 'GET',
			headers: new Headers({}),
		})
		.then(response => response.json())
		.then((data) => {


			let graficas = [];


			for (var i = 0; i < data['Graficas'].length; i++) {


				let jsonGrafica = {};


				jsonGrafica.tipo = data['Graficas'][i]['fields']['tipo'];

				jsonGrafica.titulo = data['Graficas'][i]['fields']['titulo'];

				jsonGrafica.id = data['Graficas'][i]['pk'];


				graficas.push(jsonGrafica);


			}

			this.graficas = graficas;




		})






  },
   methods: {


			getImgUrl(grafica) {

			    var images = require.context('../assets/', false, /\.png$/);

			    return images('./' + grafica + ".png");

			},



		}
	}

</script>
