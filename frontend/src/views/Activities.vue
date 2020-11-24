<template>
    <div class="uk-section uk-section-muted">
        <div class="uk-container">

            <h3>Welkom, Pieter Boersma</h3>

            <div class="uk-grid-match" uk-grid>

                <div class="uk-width-1-4">
                    <menu-component></menu-component>
                </div>

                <div class="uk-width-3-4">
                    <div class="uk-card uk-card-primary">
                        <div class="uk-card-body">
                            <h3 class="uk-card-title">Statistieken</h3>
                            <table class="uk-table uk-table-hover uk-table-divider uk-table-large">
                                <thead>
                                    <tr>
                                        <th>Nummer</th>
                                        <th>Datum</th>
                                        <th>Validiteit</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="d in recentData" :key="d.timestamp" v-on:click="navigate(d[0])">
                                        <td>{{ d[0] }}</td>
                                        <td>{{ d[1] }}</td>
                                        <td>{{ d[2] }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';
    
    import MenuComponent from '@/components/dashboard/MenuComponent.vue';
    import ActionsComponent from '@/components/dashboard/ActionsComponent.vue';
    import MonthlyComponent from '@/components/dashboard/MonthlyComponent.vue';
    import ActivitiesComponent from '@/components/dashboard/ActivitiesComponent.vue';
    import StatisticsComponent from '@/components/dashboard/StatisticsComponent.vue';

    @Component({
        components: {
            MenuComponent
        }
    })
    export default class Activities extends Vue {

        private recentData = [];

        mounted(): void {
            this.loadActivities();
        }

        private navigate(id: number){
            this.$router.push("/activity/" + id);
        }
        
        loadActivities(): void {
            axios.get('http://imac-van-pieter.local:5000/activities/all').then(response => {
                this.recentData = response.data;
            });
        }
    }
    
</script>