<template>
<v-container fluid grid-list-md>
    <v-layout>
        <v-flex md12>
            <v-card>
                <v-toolbar color="blue-grey lighten-3" flat dark>
                    <v-btn icon @click="$router.go(-1)">
                    <v-icon color="white">arrow_back</v-icon>
                    </v-btn>
                    <v-toolbar-title color="white">Add property</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                    <v-form v-model="valid" ref="form" lazy-validation>                
                    <v-text-field label="Name" v-model="property.name" :rules="nameRules" required></v-text-field>                      
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
 </v-container>
</template>

<script>
export default {
  name: "PropertyCreate",
  props: {
    msg: String
  },
  data: () => ({
    property: { name: "" }
  })
};
</script>