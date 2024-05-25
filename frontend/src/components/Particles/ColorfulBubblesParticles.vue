<script setup lang="ts">
const particlesLoaded = async container => {
  console.log("Particles container loaded", container)
}
const options = {
  fpsLimit: 50,
  background: {
    // color: rgb(12, 12, 29)
    color: "#0c0c1d"
  },
  fullScreen: {
    enable: true,
    zIndex: -1
  },
  particles: {
    color: {
      value: ["#FF8F84", "#FFAA86", "#B192FF", "#F9F871", "#67BAA7"]
    },
    move: {
      attract: {
        enable: false,
        rotate: {
          x: 800, y: 800
        }
      },
      direction: "none",
      enable: true,
      outModes: {
        default: "destroy"
      },
      random: true,
      speed: 2,
      straight: false
    },
    number: {
      density: {
        enable: false,
        area: 800,
      },
      value: 20
    },
    opacity: {
      value: 1
    },
    shape: {
      type: "circle"
    },
    size: {
      value: { min: 5, max: 35 },
      animation: {
        startValue: "min",
        enable: true,
        speed: 2,
        destroy: "max",
        sync: true
      }
    }
  },
  detectRetina: true,
  emitters: {
    direction: "none",
    rate: {
      quantity: 3,
      delay: 0.3
    },
    size: {
      width: 0, height: 0
    },
    position: {
      x: 50, y: 50
    }
  }
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

<style scoped>
.Particles {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>