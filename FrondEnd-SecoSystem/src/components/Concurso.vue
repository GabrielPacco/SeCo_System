<template>
    <v-app>
      <v-main class="light-blue darken-4">
      <v-container fill-height>
        <v-row
              align ="center"
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
                    Agregar Concursos
                  </v-btn>
                  &zwnj; &zwnj;
                </template>
                <v-card>
                  <br>
                  <v-card-title>
                    <span class="text-h5 mx-auto">CONCURSOS</span>
                  </v-card-title>
                  <v-card-text class="text-h6 text-center">

                    <v-text-field
                      class="mx-10"
                      v-model='newTask.participante'
                      :rules="nameRules"
                      label="Participante"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask.base'
                      :rules="nameRules"
                      label="Base"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask.premio'
                      :rules="nameRules"
                      label="Premio"
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
                link @click="$router.push({ path: '/admin' })"
              >
                Volver a actividades
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
                        ID
                      </th>
                      <th class="text-center">
                        Participante
                      </th>
                      <th class="text-center">
                        Base
                      </th>
                      <th class="text-center">
                        Premio
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="task in tasks" :key="task"
                    >
                        <td>{{ task.id_conc }} </td>
                        <td>{{ task.participante }} </td>
                        <td>{{ task.base }} </td>
                        <td>{{ task.premio }} </td>
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
                postURL: 'https://backendsecosystem.herokuapp.com',
                config_request: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }       
            }
        },
        methods:{
            addTask(){ 
                axios.post(this.postURL + '/concurso/add_concurso', this.newTask, this.config_request)
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
                axios.post(this.postURL + '/concurso/delete_concurso', {ID_Concurso: task.id_conc}, this.config_request)
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
            axios.post(this.postURL + '/concurso/get_concursos')
                .then(res => { this.tasks = res.data; })
                .catch((error) => { console.log(error) })
        }
    
    }
    </script>