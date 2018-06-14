<template>
 <v-app id="app">
    <v-navigation-drawer
      fixed
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      v-model="drawer">
      <v-list dense>
        <template v-for="item in items">
          <v-list-group
            v-if="item.children"
            v-model="item.model"
            :key="item.text"
            :prepend-icon="item.model ? item.icon : item['icon-alt']"
            append-icon="">
            <v-list-tile slot="activator">
                <v-list-tile-title>
                  {{ item.text }}
                </v-list-tile-title>
            </v-list-tile>         
            <v-list-tile
              v-for="(child, i) in item.children"
              :key="i"  @click="onMenuItemClick">             
                <v-list-tile-title>
                  {{ child.text }}
                </v-list-tile-title>
                 <v-list-tile-action v-if="child.icon">
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-tile-action>
            </v-list-tile>
             </v-list-group>
    
          <v-list-tile v-else :to="item.route" :key="item.text">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
              <v-list-tile-title>
                {{ item.text }}
              </v-list-tile-title>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="blue darken-3"
      dark
      app
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      fixed>
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">Risk Management</span>
      </v-toolbar-title>
    </v-toolbar>
    <v-content>
    
          <router-view></router-view>
           
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "app",
  data: () => ({
    drawer: null,
    items: [
      { icon: "build", text: "Risk model", route: "/riskmodels" },
      {
        icon: "keyboard_arrow_up",
        "icon-alt": "keyboard_arrow_down",
        model: true,
        text: "Risks",
        children: [{ text: "Risk one" }, { text: "Risk Two" }]
      }
    ]
  }),
  methods: {
    onMenuItemClick() {
      console.log("clicked");
    }
  }
};
</script>

<style>

</style>
