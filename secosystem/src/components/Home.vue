<template>
  <v-app>
    <v-main class="light-blue darken-4">
    <v-content>

      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">

            <v-card class="elevation-12" fab color="#ccffff" outline height="430">
              <v-window v-model="step" >
                <v-window-item :value="1">
                  <v-row>
                    
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1
                          class="text-center display-5 teal--blue text--blue" 
                        >Iniciar sesión en SeCo_System</h1>
                        
                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                            label="Correo"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="#ff0000"
                          />

                          <v-text-field
                            id="password"
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="#ff0000"
                          />
                        </v-form>
                        <h3 class="text-center mt-4">¿Ovidaste tu contraseña?</h3>
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
                    <v-col cols="12" md="4" class="blue darken-4" height="40">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola Amigo!</h1>
                        <h5
                          class="text-center"
                        >Bienvenido a la semana de la computación, ingresa tus datos para resgistrarte</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded color="white" @click="step++">CREAR CUENTA</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="blue darken-4">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola! de nuevo</h1>
                        <h5
                          class="text-center"
                        >Para ingresa al apartado principal, ingresar tus datos</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded  color="white" @click="step--">INGRESAR</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 teal--blue text--accent-3">Crear Cuenta</h1>

                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                            label="Nombre"
                            name="Name"
                            prepend-icon="person"
                            type="text"
                            color="#ff0000"
                          />
                          <v-text-field
                            label="Correo"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="#ff0000"
                          />

                          <v-text-field
                            id="password"
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="#ff0000"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn
                          color="blue darken-4"
                          v-bind="attrs"
                          v-on="on"
                          dark
                          rounded
                          link @click="$router.push({ path: '/admin' })"
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
export default {
  data: () => ({
    step: 1
  }),
  props: {
    source: String
  }
};
</script>