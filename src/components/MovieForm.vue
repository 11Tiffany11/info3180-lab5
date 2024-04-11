<template>
  
  <div>
    <h1>Movie Form</h1>

    <form @submit.prevent="saveMovie" enctype="multipart/form-data" method = "post" id ="movieForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title:</label>
        <input type="text" v-model="movie.title" name="title" class="form-control" required/>
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description:</label>
        <input type="textarea" v-model="movie.description" name="description" class="form-control" required/>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Upload Poster:</label>
        <input type="file" name="poster" class="form-control" required/>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

onMounted(() => {
  getCsrfToken();
});

let csrf_token = ref("");

  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      })
}

const movie = {
  title: '',
  description: '',
  poster: ''
};

function saveMovie () {

  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
}
  })
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    alert('Movie has been saved successfully!');
    console.log(data);

    movieForm.reset();

    movie.title = '';
    movie.description = '';
    movie.poster = '';
  })
  .catch(function (error) {
    console.log( error);
  });
};
</script>

<style>
/* Add your component-specific styles here */
</style>
