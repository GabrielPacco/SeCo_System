<template>
    <v-app>
      <v-main class="light-blue darken-4">
      <v-container fill-height>
    
            <v-row
              align="center"
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
                      v-model='newTask2.Marca'
                      :rules="nameRules"
                      label="Marca"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Nombre'
                      :rules="nameRules"
                      label="Nombre"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Precio'
                      :rules="nameRules"
                      label="Precio"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Stock'
                      :rules="nameRules"
                      label="Stock"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Descripcion'
                      :rules="nameRules"
                      label="Descripcion"
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
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/specs' })"
              >
                Concurso
              </v-btn>
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/specs' })"
              >
                Edicion
              </v-btn>

              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/specs' })"
              >
                Panel
              </v-btn>
              
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/specs' })"
              >
                Ponencia
              </v-btn>
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/specs' })"
              >
                Protocolar
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
                        ID_Cocina
                      </th>
                      <th class="text-center">
                        ID_Categoria
                      </th>
                      <th class="text-center">
                        Marca
                      </th>
                      <th class="text-center">
                        Nombre
                      </th>
                      <th class="text-center">
                        Precio
                      </th>
                      <th class="text-center">
                        Stock
                      </th>
                      <th class="text-center">
                        Descripcion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="task in tasks" :key="task"
                    >
                        <td>{{ task.ID_Cocina }} </td>
                        <td>{{ task.ID_Categoria }} </td>
                        <td>{{ task.Marca }} </td>
                        <td>{{ task.Nombre }} </td>
                        <td>{{ task.Precio }} </td>
                        <td>{{ task.Stock }} </td>
                        <td>{{ task.Descripcion }} </td>
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
                postURL: 'http://127.0.0.1:5000',
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
            axios.post(this.postURL + '/actividad/get_actividads')
                .then(res => { this.tasks = res.data; })
                .catch((error) => { console.log(error) })
        },
    
    }
    </script>
    