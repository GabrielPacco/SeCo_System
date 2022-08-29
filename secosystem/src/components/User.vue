<template>
    <v-app>
      <v-main class="light-blue darken-4">
        <v-row>
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[0].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[0].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[0].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[0].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[1].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[1].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[1].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[1].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
  
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[2].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[2].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[2].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[2].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
  

        <v-row>
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[3].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[3].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[3].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[3].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[4].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[4].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[4].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[4].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
  
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[5].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[5].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[5].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[0].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
  
  
  
        <v-row>
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[6].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[6].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[6].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[6].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[7].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[7].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[7].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[7].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
  
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-carousel
                :continuous="false"
                hide-delimiter-background
                delimiter-icon="mdi-minus"
                height="280"
              >
                <v-carousel-item
                  v-for="(itemk1, i) in itemsk1"
                  :key="i"
                  :src="itemk1.src"
                >
                </v-carousel-item>
              </v-carousel>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[8].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[8].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[8].fecha}}  </p>
                    <v-card-title class="mx-15">
                      <v-btn
                      link @click="$router.push({ path: '/compra' })"
                      >
                        Enlace: {{tasks[8].enlace_reu}}
                      </v-btn>
                    </v-card-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
  
      </v-main>
    </v-app>
  </template>
  
  
  <script>
  import axios from 'axios'
    export default {
      data () {
        return {
          tasks: [],
          postURL: 'https://backendsecosystem.herokuapp.com',
          config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
  
          itemsk1: [
            {
              src: 'https://live.staticflickr.com/65535/51770516557_0f59d72d1f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772223475_412395280d_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770516607_0dafc42b0a_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771983314_54945cd8dd_c.jpg',
            },
          ],
  
          itemsk2: [
            {
              src: 'https://live.staticflickr.com/65535/51772230045_dc6d54583f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771343931_707e14c3c4_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772229985_a84bbc7f57_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770523387_10cc32b996_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771343841_0cf8826360_c.jpg',
            },
          ],
  
          itemsk3: [
            {
              src: 'https://live.staticflickr.com/65535/51771592858_8e4c252219_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771352516_7bfbbe6e85_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772229985_a84bbc7f57_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770523387_10cc32b996_c.jpg',
            },
          ],
  
          itemsk4: [
            {
              src: 'https://live.staticflickr.com/65535/51772244650_100c08b5d5_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771598708_68d31aa413_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772003739_7a1b98ff73_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772003714_f20ff02832_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772244515_fa4125437c_c.jpg',
            },
          ],
  
          itemsk5: [
            {
              src: 'https://live.staticflickr.com/65535/51771364091_007a55afec_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772249965_f693b610a5_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771364156_def5cb4b3b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771364166_35937b2706_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771364206_af1c96364b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770542957_ed83cfe135_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771604373_4a1ef3bc64_c.jpg',
            },
          ],
  
          itemsk6: [
            {
              src: 'https://live.staticflickr.com/65535/51772252960_c3f9962283_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770545672_be4f94e504_c.jpg',
            },
          ],
  
          itemsk7: [
            {
              src: 'https://live.staticflickr.com/65535/51770553947_7fff7f784b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771615293_67b4283713_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771375276_4dbbba2f3b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771615248_cf5ebd96a8_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771615233_034d53748f_c.jpg',
            },
          ],
          itemsk8: [
            {
              src: 'https://live.staticflickr.com/65535/51771618633_463598b183_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770557032_3be26f1be6_c.jpg',
            },
          ],
          itemsk9: [
            {
              src: 'https://live.staticflickr.com/65535/51771624198_2c018ca3e6_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772029369_7e5deb43eb_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771624168_398a2a795a_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771383741_d6ac184d3f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771383736_913f71c00b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772269530_6c28f3c341_c.jpg',
            },
          ],
  
          itemsk10: [
            {
              src: 'https://live.staticflickr.com/65535/51772032684_6e433a4f4f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772273090_0eaff92bd9_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772273060_ed9c2f8d1b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772272980_5a0fd089c6_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771387031_5f93dae40f_c.jpg',
            },
          ],
  
          itemsk11: [
            {
              src: 'https://live.staticflickr.com/65535/51772036504_55354f8143_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770569612_0bcd0e1d23_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770569252_6d1943b3d7_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772276780_1742556000_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770569532_3e307b3133_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771631153_f96015f2e2_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772036369_fff4284409_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772036314_a58e247170_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772036289_00d51348ce_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770569337_e133a9d4d1_c.jpg',
            },
          ],
  
          itemsk12: [
            {
              src: 'https://live.staticflickr.com/65535/51772039674_9cba18c2c6_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771634738_d73bc39534_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770572927_e944a58c18_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771634563_1cdf70075f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772280130_084a99e79e_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770572837_85e7705cb0_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772039564_fc0aebab6c_c.jpg',
            },
          ],
  
          itemsk13: [
            {
              src: 'https://live.staticflickr.com/65535/51771397261_de659c8310_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770576337_e5cb7f830c_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772042894_9a2f49d79f_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771397216_5916c1aa3b_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770576207_f9861c25dc_c.jpg',
            },
          ],
  
          itemsk14: [
            {
              src: 'https://live.staticflickr.com/65535/51772288285_617693fc31_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772047979_84659a4dac_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771642788_5e02942bf3_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772288225_a920d22cb0_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51770580987_624bf88b89_c.jpg',
            },
          ],
  
          itemsk15: [
            {
              src: 'https://live.staticflickr.com/65535/51771647013_332f1e1350_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51772052419_d4bdfc6e76_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771646993_5f5602d392_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771646993_5f5602d392_c.jpg',
            },
            {
              src: 'https://live.staticflickr.com/65535/51771646938_517f3c077e_c.jpg',
            },
          ],
        }
      },
      methods:{
  
      },
      created(){ 
          axios.post(this.postURL + '/actividad/get_actividades')
              .then(res => { this.tasks = res.data; })
              .catch((error) => { console.log(error) })
      },
    }
  </script>