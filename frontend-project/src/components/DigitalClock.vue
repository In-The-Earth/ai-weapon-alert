<template>
<div class="container">
  
  <div class="clock-border">
    <div class="clock-inner" :class="color">
      <div class="hour">{{hours}}</div>
      <div class="dots">:</div>
      <div class="min">{{minutes}}</div>
      <div class="dots">:</div>
      <div class="secs">{{seconds}}</div>
      <div class="mode"></div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'DigitalClock',
  props: {
    color: {
      type: String,
      default: 'red'
    }
  },
  data () {
    return {
      hours: 0,
      minutes: 0,
      seconds: 0
    }
  },
  methods: {
    setTime () {
      setInterval(() => {
        const date = new Date()
        this.hours = date.getHours()
        this.minutes = this.checkSingleDigit(date.getMinutes())
        this.seconds = this.checkSingleDigit(date.getSeconds())
      }, 1000)
    },
    checkSingleDigit (digit) {
      return ('0' + digit).slice(-2)
    }
  },
  mounted () {
    this.setTime()
  }
}
</script>

<style>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    flex-direction: column;
  }
  .hour, .min, .secs {
    font-size: 3em;
  }
  strong {
    color: blue;
  }
  p {
    font-family: 'Lucida Sans', sans-serif;
    font-size: 20px;
  }
  
  .clock-inner {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 300px;
    height: 60px;
    background: black;
    border-radius: 20px;
    color: red;
  }
  .dots {
    font-size: 50px;
  }
  .red {
    color: red;
  }
  .yellow {
    color: yellow;
  }
  .green {
    color: green;
  }
</style>