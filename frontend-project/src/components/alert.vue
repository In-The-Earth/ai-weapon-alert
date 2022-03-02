<template>
<nav class="navbar navbar-light bg-warning">
  <a class="navbar-brand" href="#">Weapon Alert</a>
</nav>
<div class= "container">
            <h2 align = "center"> Alert </h2>
            
</div>
<div class= "container my-5">
  <div class="row">
    <div class="col-md-7">
      <img src="https://cdn.pixabay.com/photo/2014/08/22/21/45/child-424772_960_720.jpg" class="img-thumbnail" alt="" />
    </div>
    <div class="col-md-5">
      <h3 class="front-weight-light">Cam : ... </h3>
      <h3 class="mt-4">
      Detect : ...
      </h3>
      <h3 class="mt-4">
      Location : ...
      </h3>
      <h3 class="mt-4">
      Date : ...
      </h3>
      <h3 class="mt-4">
      Time : ...
      </h3>
    </div> <div class="text-center">
    <router-link to ="page2"><button type="button" class="btn btn-dark mt-3">OK</button></router-link>
  </div> </div>
</div>
<div class="text-center">
  <h4>stream Camera</h4>
  <img src="http://127.0.0.1:5000/video_feed/0" class="rounded" alt="">
</div>
</template>

<script>

</script>