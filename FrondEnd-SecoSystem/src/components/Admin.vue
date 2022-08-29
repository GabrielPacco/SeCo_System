<template>
    <v-app>
      <v-main class="light-blue darken-4">
      <v-container fill-height>
    
            <v-row
              justify="center"
              no-gutters
            >
              <v-dialog
                 max-width="700px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="white"
                    v-bind="attrs"
                    v-on="on"
                  >
                    AGREGAR UNA ACTIVIDAD
                  </v-btn>
    
                </template>
                <v-card>
                  <br>
                  <v-card-title>
                    <span class="text-h5 mx-auto">AGREGAR UNA ACTIVIDAD</span>
                  </v-card-title>
                  <v-card-text class="text-h6 text-center">
    
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Nombre'
                      :rules="nameRules"
                      label="Nombre"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Descripcion'
                      :rules="nameRules"
                      label="Descripcion"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Fecha'
                      :rules="nameRules"
                      label="Fecha"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.HoraIn'
                      :rules="nameRules"
                      label="Hora de inicio"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.HoraFin'
                      :rules="nameRules"
                      label="Hora de finalizacion"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Estado'
                      :rules="nameRules"
                      label="Estado"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Enlace'
                      :rules="nameRules"
                      label="Enlace a la reunion"
                      required
                    ></v-text-field>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="success"
                      class="mr-4"
                      @click="addTask"
                    >
                      AGREGAR
                    </v-btn>
                  </v-card-actions>
                  <br>
                </v-card>
              </v-dialog>
              &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj;
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/concurso' })"
              >
                Concurso
              </v-btn>
              &zwnj; &zwnj;
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/edicion' })"
              >
                Edicion
              </v-btn>
              &zwnj; &zwnj;
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/panel' })"
              >
                Panel
              </v-btn>
              &zwnj; &zwnj;
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/ponencia' })"
              >
                Ponencia
              </v-btn>
            </v-row>
    
          <v-layout row wrap align>
              <v-card
              height="650" text-h4 class="mx-auto my-2 text-center" width="1600" outlined elevation="20">
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-center">
                        Id
                      </th>
                      <th class="text-center">
                        Nombre
                      </th>
                      <th class="text-center">
                        Descripcion
                      </th>
                      <th class="text-center">
                        Fecha
                      </th>
                      <th class="text-center">
                        Hora de inicio
                      </th>
                      <th class="text-center">
                        Hora de finalización
                      </th>
                      <th class="text-center">
                        Estado
                      </th>
                      <th class="text-center">
                        Enlace a la reunión
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="task in tasks" :key="task"
                    >
                        <td>{{ task.id_act }} </td>
                        <td>{{ task.nombre }} </td>
                        <td>{{ task.descripcion }} </td>
                        <td>{{ task.fecha }} </td>
                        <td>{{ task.hora_inicio }} </td>
                        <td>{{ task.hora_fin }} </td>
                        <td>{{ task.estado }} </td>
                        <td>{{ task.enlace_reu }} </td>
                        <td><v-btn
                            small
                            color="error"
                            dark
                            class="grey  mx-2"
                            v-on:click='deleteTask(task)'
                            @click="messages--"
                          >
                            <v-icon dark>
                              mdi-delete
                            </v-icon>
                          </v-btn>
    
                          </td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
              </v-card>
            </v-layout>
      </v-container>
      </v-main>
    </v-app>
    </template>
    
    <script>
    import axios from 'axios'
    
    export default{    
        data(){ 
            return { 
                tasks: [],
                newTask: {},
                newTask2: {},
                postURL: 'https://backendsecosystem.herokuapp.com',
                config_request: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }       
            }
        },
        methods:{
            addTask(){ 
                axios.post(this.postURL + '/actividad/add_actividad', this.newTask2, this.config_request)
                    .then(res => {                                         
                        this.tasks.push(res.data);
                        console.log(res.data)        ;
                    })
                    .catch((error) => {
                        console.log(error)
                    });
    
                this.newTask2 = {};
            },

            deleteTask(task){                      
                axios.post(this.postURL + '/actividad/delete_actividad', {CUI: task.ID_Actividad}, this.config_request)
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
            axios.post(this.postURL + '/actividad/get_actividades')
                .then(res => { this.tasks = res.data; })
                .catch((error) => { console.log(error) })
        },
    
    }
    </script>
    