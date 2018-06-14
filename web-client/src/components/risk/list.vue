<template>
 <v-container fluid grid-list-md>
            <v-layout row wrap >
               <v-flex md3 xs12>
               <v-card hover color="grey lighten-2" :to="{name: 'risk-create', params: { id: 0 }}">
                   <v-card-media contain :src="require('@/assets/create-model.png')" height="275px">
 </v-card-media>
                  
                </v-card>
              </v-flex>
              <v-flex md3 xs12 v-for="risk in risks" :key="risk.id">
               <v-card>
                 <v-card-media contain :src="require('@/assets/model.png')" height="150px">
 </v-card-media>
                     <v-card-title primary-title>
                      <div>
                        <h3 class="headline" v-text="risk.name"></h3>
                      </div>
                    </v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn icon>
                      <v-icon>mode_edit</v-icon>
                    </v-btn>
                    <v-btn icon>
                      <v-icon>delete</v-icon>
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
            </v-layout>
 </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: "RiskList",
  props: {
    msg: String
  },
  data: () => ({
    risks: []
  }),
  created: function() {
    this.loadRisks();
  },
  methods: {
    loadRisks() {
      axios.get("http://127.0.0.1:5000/risks")
        .then(response => {
          this.risks = response.data;         
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>