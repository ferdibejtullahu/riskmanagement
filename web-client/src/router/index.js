import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from "@/components/HelloWorld.vue";
import RiskCreate from "@/components/risk/create.vue";
import RiskList from "@/components/risk/list.vue";
import PropertyCreate from "@/components/property/create.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'hello-world',
      component: HelloWorld
    },
    {
      path: '/riskmodels',
      name: 'risk-list',
      component: RiskList
    },
    {
      path: '/riskmodels/:id',
      name: 'risk-create',
      component: RiskCreate
    },
    {
      path: '/riskmodels/:id/property/:id',
      name: 'property-create',
      component: PropertyCreate
    }
  ]
})