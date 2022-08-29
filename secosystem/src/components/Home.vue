<template>
  <v-app id="inspire">
    <v-content>

      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12" fab color="#ccffff" outline>
              <v-window v-model="step" >
                <v-window-item :value="1">
                  <v-row>
                    
                    <v-col cols="12" md="8">
                      <!--<img src="src/assets/logo.png" height="50px" width="550px"/> -->
                      <v-card-text class="mt-12">
                        
                        <h1
                          class="text-center display-5 teal--blue text--blue" 
                        >Iniciar sesión en SeCo_System</h1>
                        
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="#0000ff " outlined>
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
                        <v-btn rounded color="blue darken-4" dark>INGRESAR</v-btn>
                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="blue darken-4">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola Amigo!</h1>
                        <h5
                          class="text-center"
                        >Bienvenido a la semana de la computación, ingresa tus datos para resgistrarte</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded color="light-green accent-3" dark @click="step++">CREAR CUENTA</v-btn>
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
                        <v-btn rounded  color="light-green accent-3" dark @click="step--">INGRESAR</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
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
                        <v-btn rounded color="blue darken-4" dark>CREAR CUENTA</v-btn>
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