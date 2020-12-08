<template>
    <div class="uk-section uk-section-muted">
        <div class="uk-container">

            <h3>Welkom, {{username}}</h3>

            <div class="uk-grid-match" uk-grid>

                <div class="uk-width-1-2">
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
                                    <!-- <tr v-for="d in recentData" :key="d.timestamp" v-on:click="navigate(d[0])"> -->
                                    <tr v-for="d in recentData" :key="d.timestamp" v-on:click="setId(d[0]); setFootage(d[1])">
                                        <td>{{ d[0] }}</td>
                                        <td>{{ d[1] }}</td>
                                        <td>{{ d[2] }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <div class="uk-width-1-2">
                    <div class="uk-card uk-card-secondary">
                        <div class="uk-card-body">
                            <a v-on:click="navigate"><img v-bind:src=imagePath></a>
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
    import LoginService from '../services/LoginService';

    @Component({
        components: {
            MenuComponent
        }
    })
    export default class Activities extends Vue {
        private username: string = LoginService.getUserData().username;
        private recentData = [];
        private image = String(this.recentData[1]);
        private imagePath = '/images/' + String(this.image) + '.jpg';
        private route = "";
        private loaded = false;

        mounted(): void {
            this.loadActivities();
        }

        private setId(id: number){
            this.route = "/activity/" + String(id);
        }

        private navigate(){
            this.$router.push(this.route);
        }
        
        private setFootage(datum: string){
            this.image = String(datum);
            this.imagePath = '/images/' + String(datum) + '.jpg';
            // alert(this.path);
        }


        loadActivities(): void {
            axios.get('http://imac-van-pieter.local:5000/activities/all').then(response => {
                this.recentData = response.data;
                this.image = String()
            });
        }
    }
    
</script>