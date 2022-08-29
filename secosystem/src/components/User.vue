<template>
    <v-app>
      <v-main class="light-blue darken-4">
        <v-row>
          <v-col
          cols="12"
          sm="4"
          >
            <v-card
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
            
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52317869177_947acfe4de_c.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52317869177_947acfe4de_c.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[0].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[0].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[0].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52320142909_9f4cb9a6fa_z.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52320142909_9f4cb9a6fa_z.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[1].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[1].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[1].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52320159650_48eaf1641d_c.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52320159650_48eaf1641d_c.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[2].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[2].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[2].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52319093509_e49455a1c5_c.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52319093509_e49455a1c5_c.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[3].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[3].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[3].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52319093554_b57eb9c125_c.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52319093554_b57eb9c125_c.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[4].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[4].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[4].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52318670561_ab0744784d_b.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52318670561_ab0744784d_b.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[5].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[5].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[5].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52317869302_e8d492c2c8_z.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52317869302_e8d492c2c8_z.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[6].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[6].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[6].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"

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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52318980188_053d054773_m.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52318980188_053d054773_m.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[7].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[7].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[7].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
            align="center" 
              elevation="24"
              width="550"
              class="mx-auto"
            >
              <v-system-bar lights-out></v-system-bar>
              <v-img
                lazy-src="https://live.staticflickr.com/65535/52318980208_87d313587c_c.jpg"
                max-height="400"
                max-width="450"
                src="https://live.staticflickr.com/65535/52318980208_87d313587c_c.jpg"
                ></v-img>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title><p> {{tasks[8].nombre}} </p></v-list-item-title>
                    <v-list-item-subtitle>{{tasks[8].descripcion}} </v-list-item-subtitle>
                    <p class="text-caption"> {{tasks[8].fecha}}  </p>
                    <v-card-title class="mx-5">
                      <v-btn
                      link @click="setmeet"
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
        }
      },
      methods:{
        setmeet(){
          window.location.href = "https://meet.google.com/ydt-sxvb-uwg";
        }
      },
      created(){ 
          axios.post(this.postURL + '/actividad/get_actividades')
              .then(res => { this.tasks = res.data; })
              .catch((error) => { console.log(error) })
      },
    }
  </script>