<template>

  <div id="navbar">


    <nav class="border fixed split-nav">
      <div class="nav-brand">
      	<router-link to="/">
        	<h3><a>Graficas a mano</a></h3>
        </router-link>
      </div>
      <div class="collapsible">
        <input id="collapsible1" type="checkbox" name="collapsible1">
        <button>
        <label for="collapsible1">
            <div class="bar1"></div>
            <div class="bar2"></div>
            <div class="bar3"></div>
          </label>
        </button>
        <div class="collapsible-body">
          <ul class="inline">
          	<router-link to="/verGraficas">
            	<li><a>Ver gráficas</a></li>
            </router-link>
          	<router-link to="/nueva">
            	<li><a>Crear nueva gráfica</a></li>
            </router-link>
          </ul>
        </div>
      </div>
    </nav>

    
  </div>

</template>

<script>
  
export default {
  name: 'Navbar',
	data(){
    return{

    }
	},
	mounted: function () {

	},
	methods: {

	},


}
</script>


<style scoped>


</style>
