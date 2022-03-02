<template>
  <nav class="navbar navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Weapon Alert</a>
  </nav>

  
  <div id="app">
    <div class="container">
      <h1 align="center">CCTV</h1>
      <div>
  <DigitalClock/>
  </div>
      <hr />
      <div class="row">
        <div class="col-md-6" v-for="(item, index) in products" :key="index">
          <div class="card text-white bg-dark mb-3 h-100" style="max-width: 80rem;">
            <img :src="item.image" class="card-img-top" />
            <div class="card text-white bg-dark mb-3 body">
              <h4 class="card-title">{{ item.name }}</h4>
              <h5 class="card-title">{{ item.info }}</h5>
            </div>
            <div class="card-footer">
            
                <button
                  type="button"
                  class="btn btn-danger form-control"
                  v-if="item.display"
                  v-on:click="handlealert(item)"
                >
                  <h2>Alert</h2>
                </button>
              
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { io } from "socket.io-client";
import Swal from "sweetalert2"
// import { ref } from 'vue';
// import Popup from '../components/Popup';
import DigitalClock from '../components/DigitalClock.vue';
import axios from 'axios'

export default {
  
  name: "page2",
  components: {
    DigitalClock
  },
  data() {
    return {
      products: [
        // {
        //   name: "Cam 1",
        //   info: "Floor 1, Zone C, Front restaurant, cashier",
        //   image: "http://127.0.0.1:5000/video_feed/0",
        //   active: false,
        //   display: false,
        // },
        // {
        //   name: "Cam 2",
        //   info: "Floor 2, Zone C, Front restaurant, cashier",
        //   image: "http://127.0.0.1:5000/video_feed/1",
        //   active: false,
        //   display: false,
        // },
      ],
    };
  },
  
  mounted() {
    // fetch('http://192.168.1.5:8000/getdb')
    //   .then(res => res.json())
    //   .then(data => this.products = data)
    //   .catch(err => console.log(err.message))
    axios
      .get('http://127.0.0.1:8000/getdb')
      .then(response => (this.products = response.data,
      console.log(this.products)))
    
    const url = "http://127.0.0.1:8000/";
    let socket = io(url);
    socket.on("my event", (data) => {
      console.log(data);
      this.products[data.idcam - 1].display = true;
      this.products[data.idcam - 1].data = data
    });
  
  },
  methods:{
    handlealert: function(item){
        Swal.fire({
            width: 900,
            Height: 1000,
            title: "Weapon alert "+item.name,
            html:
          '<img src="http://127.0.0.1:5000/video_feed/0" height="300" width="400">' +"    "+
          '<img src= '+'"'+item.data.url+ '"'+' height="300" width="400">' + '<h1 class="front-weight-light"></h1>'+
          "Detect : "+item.data.detect+'<br>'+
          "Location : "+item.data.location+'<br>'+
          "Date : "+item.data.date+'<br>'+
          "Time : "+item.data.time+'<br>'
          ,
            
  
            imageAlt: 'Custom image',
        })
        this.products[item.data.idcam - 1].display = false;
    }
  },
};

</script>
