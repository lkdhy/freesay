<script setup lang="ts">
const particlesLoaded = async container => {
  console.log("Particles container loaded", container)
}
const options = {
  background: {
    color: "#000", // this sets a background color for the canvas
  },
  particles: {
    number: {
      value: 300,
      density: {
        enable: true,
        value_area: 800,
      },
    },
    color: {
      value: "#fff",
    },
    shape: {
      type: "circle",
      stroke: {
        width: 0,
        color: "#000000",
      },
      polygon: {
        nb_sides: 5,
      },
    },
    opacity: {
      value: 1,
      random: false,
      anim: {
        enable: false,
        speed: 1,
        opacity_min: 0.1,
        sync: false,
      },
    },
    size: {
      value: 3,
      random: true,
      anim: {
        enable: false,
      },
    },
    line_linked: {
      enable: false,
    },
    move: {
      enable: true,
      speed: 2,
      direction: "bottom",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: {
        enable: false,
        rotateX: 600,
        rotateY: 1200,
      },
    },
  },
  retina_detect: true,
}

</script>

<template>
  <div class="Particles">
    <vue-particles
        id="tsparticles"
        :options="options"
        @particles-loaded="particlesLoaded"
    >
    </vue-particles>
  </div>
</template>

<style>
.Particles {
  position: absolute;
  z-index: -200;
}
</style>