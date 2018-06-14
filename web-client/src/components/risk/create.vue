
<template>
 <v-container fluid grid-list-md>
    <v-layout>
        <v-flex xs12>
            <v-card>
            <v-toolbar color="blue-grey lighten-3" flat dark>
                 <v-btn icon @click="$router.go(-1)">
                    <v-icon color="white">arrow_back</v-icon>
                  </v-btn>
                <v-toolbar-title color="white">Create model</v-toolbar-title>
                  <v-spacer></v-spacer>
             <v-btn flat icon dark  @click="addProperty()">
              <v-icon>add</v-icon>
            </v-btn>
          
            </v-toolbar>
          <v-card-text>
            <v-form v-model="valid" ref="form" lazy-validation>                
              <v-text-field label="Name" v-model="risk.name" :rules="nameRules" required></v-text-field>
                          
                        <v-list two-line subheader>
                        <v-list-tile avatar v-for="prop in risk.properties" :key="prop.name">
                            <v-list-tile-content>
                            <v-list-tile-title>{{ prop.caption }} - {{prop.name}}</v-list-tile-title>
                            <v-list-tile-sub-title>{{ prop.property_type.name }}</v-list-tile-sub-title>
                            </v-list-tile-content>
                            <v-list-tile-action>
                            <v-btn icon ripple  @click="editProperty(prop)">
                                <v-icon color="primary lighten-1">edit</v-icon>
                            </v-btn>
                     
                            </v-list-tile-action>
                             <v-list-tile-action>
                       
                            <v-btn icon ripple  @click.native.stop="dialog = true">
                                <v-icon color="red lighten-1">close</v-icon>
                            </v-btn>
                            </v-list-tile-action>
                        </v-list-tile>
                        </v-list>
            </v-form>
          </v-card-text>
                  <v-divider class="mt-5"></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary">Save</v-btn>
                    <v-btn flat>Cancel</v-btn>
                </v-card-actions>
               
            </v-card>
        </v-flex>

       
    
  </v-layout>
                <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
      >
        <v-card tile>
          <v-toolbar card dark color="primary">
            <v-btn icon dark @click.native="dialog = false">
              <v-icon>close</v-icon>
            </v-btn>
            <v-toolbar-title>Add Property</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn dark flat  @click="saveProperty()">Save</v-btn>
            </v-toolbar-items>

          </v-toolbar>
          <v-card-text>
         <v-container grid-list-md>
            <v-layout wrap>
                <v-flex xs12 sm6>
                <v-text-field v-model="property.name" label="Name*"></v-text-field>
              </v-flex>
                <v-flex xs12 sm6>
                <v-text-field v-model="property.caption"  label="Caption*"></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-select
                  :items="property_types"
                   item-text="name"
                  label="Type"
                  v-model="property.property_type"
                  required
                ></v-select>
              </v-flex>
               
              <v-flex xs12>
                <v-checkbox  v-model="property.display" label="Display"></v-checkbox>
              </v-flex>
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        
          </v-card-text>

          <div style="flex: 1 1 auto;"></div>
        </v-card>
      </v-dialog>  
 </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "RiskCreate",
  props: {
    msg: String
  },
  data: () => ({
    dialog: false,
    valid: true,
    property_types: [],
    property: {},
    risk: {
      name: "",
      properties: []
    },
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ]
  }),
  created: function() {
    this.loadPropertyTypes();
  },
  methods: {
    loadPropertyTypes() {
      axios
        .get("http://127.0.0.1:5000/propertytypes")
        .then(response => {
          this.property_types = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addProperty() {
      this.property = {};
      this.dialog = true;
    },
    editProperty(item) {
      this.property = item;
      this.dialog = true;
    },
    saveProperty() {
      this.risk.properties.push(this.property);
      this.dialog = false;
    }
  }
};
</script>