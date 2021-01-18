<template>
    <div class="uk-card uk-card-primary">
        <div class="uk-card-body">
            <h3 class="uk-card-title">Activiteiten</h3>
            
                    <template v-if="chartData.length > 0">
                        <table class="uk-table uk-table-hover uk-table-divider uk-table-large">
                            <thead>
                                <tr>
                                    <th>Nummer</th>
                                    <th>Datum</th>
                                    <th>Validiteit</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="d in chartData" :key="d.timestamp">
                                    <td>{{ d[0] }}</td>
                                    <td>{{ d[1] }}</td>
                                    <td>{{ d[2] }}</td>
                                </tr>
                            </tbody>
                        </table>
                        <router-link class="uk-button uk-button-default" to="/activities">Alle activiteiten</router-link>
                    </template>
                    <template v-if="chartData.length == 0">
                        <div class="uk-placeholder uk-text-center">Geen activiteiten opgeslagen</div>
                    </template>
         
            
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'
    import { User } from '../../models/User';
    import LoginService from '../../services/LoginService';
    
    @Component
    export default class ActivitiesComponent extends Vue {
        
        private chartData = [];
        private user: User;

        mounted(): void {
            setTimeout(this.validate, 250)
        }

        validate(): void {
            this.user = LoginService.getUserData();
            axios.get('http://imac-van-pieter.local:5000/activities/recent?userid=' + this.user.id).then(response => {
                this.chartData = response.data;

            }).catch(error => {
                console.log(error);
            });
        }
    }
    
</script>