<template>
  <div>
    <h1> View Movies </h1>
    <div class="movie-items">
    <ul>
      <li  class= "movies-flex" v-for="movie in movies" :key="movie.id">
        <img class="movies-img" :src="'/api/v1/posters/' + movie.poster" alt="Poster of movie displayed" />
        <div class ="movies-info">
          <h4>{{ movie.title }}</h4>
          <p>{{ movie.description }}</p>
        </div>
      </li>
    </ul>
   </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

onMounted(() => {
  fetchMovies();
});


function fetchMovies() {


  fetch("/api/v1/movies", {
    method: 'GET'
  })

  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    movies.value = data.movies;
    console.log(data);
  })

  .catch(function (error) {
    console.log( error);
  });
};
</script>

<style>
.movie-items{
  align-content: center;
  width: auto;
}
.movies-flex {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  border: solid 1px black;
  border-radius: 4px;
  width: 25%;
}

.movie-info {
  flex: 1;
}

.movie-img {
  width: 150px; 
  height: auto;
  margin-right: 20px;
}

p{
  font-size: 10px;
}

h4{
  font-size: 12px;
}


</style>
