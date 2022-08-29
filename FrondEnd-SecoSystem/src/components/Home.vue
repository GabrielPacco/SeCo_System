<template>
  <v-app>
    <v-main class="light-blue darken-4">
    <v-content>

      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">

            <v-card class="elevation-12" fab color="#ccffff" outline height="520">
              <v-window v-model="step" >
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-16">
                        <h1
                          class="text-center display-5 teal--blue text--blue" 
                        >Iniciar Sesion en Seco System</h1>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="#0000ff" outlined>
                            <v-icon>fab fa-facebook-f</v-icon>
                          </v-btn>

                          <v-btn class="mx-2" fab color="#ff0000" outlined>
                            <v-icon>fab fa-google-plus-g</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="#3399ff" outlined>
                            <v-icon>fab fa-linkedin-in</v-icon>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                      
                          label="Correo"
                          prepend-icon="email"
                          required
                          />
                          <v-text-field

                            id="password"
                            label="Contraseña"
                            prepend-icon="lock"
                            type="password"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn
                          color="blue darken-4"
                          v-bind="attrs"
                          v-on="on"
                          dark
                          rounded
                          link @click="$router.push({ path: '/admin' })"
                        >
                          INGRESAR
                        </v-btn>
                      </div>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-sheet color="blue darken-4" height="520" outlined>
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola Amigo!</h1>
                        <h5
                          class="text-center"
                        >Bienvenido a la semana de la computación, ingresa tus datos para resgistrarte</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded color="white" @click="step++">CREAR CUENTA</v-btn>
                      </div>
                    </v-sheet>
                    </v-col>

                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="blue darken-4">
                      <v-sheet color="blue darken-4" height="520" outlined>
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola! de nuevo</h1>
                        <h5
                          class="text-center"
                        >Para ingresa al apartado principal, ingresar tus datos</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded  color="white" @click="step--">INGRESAR</v-btn>
                      </div>
                      </v-sheet>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-8">
                        <h1 class="text-center display-2 teal--blue text--accent-3">Crear Cuenta</h1>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="#0000ff" outlined>
                            <v-icon>fab fa-facebook-f</v-icon>
                          </v-btn>

                          <v-btn class="mx-2" fab color="#ff0000" outlined>
                            <v-icon>fab fa-google-plus-g</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="#3399ff" outlined>
                            <v-icon>fab fa-linkedin-in</v-icon>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                          v-model='newTask.nombre'
                          :rules="nameRules"
                          label="Participante"
                          prepend-icon="person"
                          required
                          />
                          <v-text-field
                            v-model='newTask.email'
                            :rules="nameRules"
                            label="Correo"
                            prepend-icon="email"
                            type="text"
                            color="#ff0000"
                          />
                          <v-text-field
                            v-model='newTask.contrasenia'
                            :rules="nameRules"
                            id="password"
                            label="Contraseña"
                            prepend-icon="lock"
                            type="password"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-0">
                        <v-btn
                          color="blue darken-4"
                          v-bind="attrs"
                          v-on="on"
                          dark
                          rounded
                          link @click="addTask"
                        >
                          CREAR CUENTA
                        </v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-main>
  </v-app>
</template>

<script>
  import axios from 'axios'
  
  export default{    
      data(){ 
          return {
              step: 1,
              tasks: [],
              newTask: {},
              postURL: 'https://backendsecosystem.herokuapp.com',
              config_request: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*'
              }       
          }
      },
      props: {
      source: String
      },
      methods:{
          addTask(){ 
              axios.post(this.postURL + '/usuario/add_usuario', this.newTask, this.config_request)
                  .then(res => {                                         
                      this.tasks.push(res.data);
                      console.log(res.data)        ;
                  })
                  .catch((error) => {
                      console.log(error)
                  });
  
              this.newTask = {};
          },
  
          deleteTask(task){                      
              axios.post(this.postURL + '/usuario/delete_usuario', {ID_Concurso: task.id_conc}, this.config_request)
                  .then(() => {                      
                      this.tasks.splice(this.tasks.indexOf(task), 1);                    
                  })
                  .catch((error) => {
                      console.log(error)
                  });  
          },
          reset(){                      
              this.newTask = {};
          }
      },
  
      created(){ 
          axios.post(this.postURL + '/usuario/get_usuarios')
              .then(res => { this.tasks = res.data; })
              .catch((error) => { console.log(error) })
      }
  
  }
  
  </script>