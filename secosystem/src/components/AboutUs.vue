<template>
  <v-app id="inspire">
    <v-main class="light-blue darken-4">
      <v-container pa-16 me-n4>
        <v-row>
          <v-col sm="8">
            <v-sheet min-height="800" rounded="lg" elevation="20">
              <p class="text-h2 text--primary text-center">
                <br>SeCo System
              </p>

              <v-sheet class="d-block text-center mx-auto mb-9 pa-12 text-h5" width="700"><br>
                Somos un grupo de estudiante de la Universidad Nacional de San Agustín de Arequipa que busca ayudar en
                gaaaaaaaaaaaaaaaaaaaaaaa
              </v-sheet>

            </v-sheet>
          </v-col>
          <v-col>
            <v-sheet rounded="lg" width="400" height="50" elevation="20">
              <div>
                <p class="text-h5 text--primary text-center pa-2">
                  Integrantes
                </p>
              </div>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Diego Aquino
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGDiego"> Instagram</v-list-item-title>
                </v-btn>

                <v-btn>
                  <v-list-item-icon>
                    <v-icon>mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBDiego">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>

            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Gabriel Pacco
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGGabriel"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBGabriel">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Erick Perez
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGErick"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBErick">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">LLicawom
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGLlica"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBLlica">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Ronald
              Gutierrez
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGRonald"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBRonald">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Uberto Garcia
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGUberto"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBUberto">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Fabrizio
              Mattos
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGFabrizio"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBFabrizio">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    selectedItem: 0,
    items: [
      { text: 'Diego Aquino', instagram: "https://www.instagram.com/diego_aquino_7w7/", facebook: 'https://www.facebook.com/Diego.AquinoQ/' },
      { text: 'Gabriel Pacco', instagram: 'https://www.instagram.com/gabriel_pacco_/', facebook: 'https://www.facebook.com/gabriel.pacco.3' },
      { text: 'Kerito Won', instagram: 'https://www.instagram.com/kerito_17/', facebook: 'https://www.facebook.com/profile.php?id=100004004602419' },
      {
        text: 'Fabrizio Mattos', instagram: 'https://www.instagram.com/fabrizio_mattos/', facebook: 'https://www.facebook.com/fabrizio.mattoscahui/'
      }
    ],
    social: [
      ['Instagram', 'mdi-instagram'],
      ['Facebook', 'mdi-facebook'],
    ],
  }),
  methods: {

    setIGDiego() {
      window.location.href = "https://www.instagram.com/diego_aquino_7w7/";
    },
    setIGGabriel() {
      window.location.href = "https://www.instagram.com/gabriel_pacco_/";
    },
    setIGErick() {
      window.location.href = "https://www.instagram.com/kerito_17/";
    },
    setIGLlica() {
      window.location.href = "https://www.instagram.com/diego_aquino_7w7/";
    },
    setIGRonald() {
      window.location.href = "https://www.instagram.com/gabriel_pacco_/";
    },
    setIGUberto() {
      window.location.href = "https://www.instagram.com/kerito_17/";
    },
    setIGFabrizio() {
      window.location.href = "https://www.instagram.com/fabrizio_mattos/";
    },

    ///////////////////

    setFBDiego() {
      window.location.href = "https://www.facebook.com/Diego.AquinoQ/";
    },
    setFBGabriel() {
      window.location.href = "https://www.facebook.com/gabriel.pacco.3";
    },
    setFBErick() {
      window.location.href = "https://www.facebook.com/profile.php?id=100004004602419";
    },
    setFBLlica() {
      window.location.href = "https://www.facebook.com/profile.php?id=100009062691118";
    },
    setFBRonald() {
      window.location.href = "https://www.facebook.com/ronaldjoaquin.gutierrezpastor.3";
    },
    setFBUberto() {
      window.location.href = "https://www.facebook.com/profile.php?id=100004004602419";
    },
    setFBFabrizio() {
      window.location.href = "https://www.facebook.com/fabrizio.mattoscahui/";
    },


  }
};

</script>

