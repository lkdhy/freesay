<script setup lang="ts">
const particlesLoaded = async container => {
  console.log("Particles container loaded", container)
}
</script>
<template>
  <div class="Particles">
<!--    <vue-particles id="tsparticles" @particles-loaded="particlesLoaded" url="http://foo.bar/particles.json" />-->

    <vue-particles id="tsparticles"
        @particles-loaded="particlesLoaded"
        :options="{
                    background: {
                        color: {
                            value: '#0d47a1'
                        }
                    },
                    fpsLimit: 120,
                    interactivity: {
                        events: {
                            onClick: {
                                enable: true, // disabled by default
                                mode: 'push' // adds particles on click
                            },
                            onHover: {
                                enable: true, // disabled by default
                                mode: 'repulse' // repulse the particles on mouse hover
                            },
                        },
                        modes: {
                            bubble: {
                                distance: 400,
                                duration: 2,
                                opacity: 0.8,
                                size: 40
                            },
                            push: {
                                quantity: 4 // number of particles to add on click
                            },
                            repulse: {
                                distance: 200, // distance of the paricles from
                                duration: 0.4
                            }
                        }
                    },
                    particles: {
                        color: {
                            value: '#ffffff'
                        },
                        links: {
                            color: '#ffffff',
                            distance: 150,
                            enable: true,
                            opacity: 0.5,
                            width: 1
                        },
                        move: {
                            direction: 'none',
                            enable: true,
                            outModes: 'bounce',
                            random: false,
                            speed: 6,
                            straight: false
                        },
                        number: {
                            density: {
                                enable: true,
                            },
                            value: 80
                        },
                        opacity: {
                            value: 0.9
                        },
                        shape: {
                            type: 'circle'
                        },
                        size: {
                            value: { min: 1, max: 5 }
                        }
                    },
                    detectRetina: true
                }"
    />
  </div>
</template>

<style>
.Particles {
  position: absolute;
  z-index: -200;
}

</style>