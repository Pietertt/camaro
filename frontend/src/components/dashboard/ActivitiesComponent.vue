<template>
    <div class="uk-card uk-card-primary">
        <div class="uk-card-body">
            <h3 class="uk-card-title">Activiteiten</h3>
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
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'
    
    @Component
    export default class ActivitiesComponent extends Vue {
        
        private chartData = [];

        mounted(): void {
            setTimeout(this.validate, 2000)
        }

        validate(): void {
          
            axios.get('http://imac-van-pieter.local:5000/activities/recent').then(response => {
                this.chartData = response.data;

            }).catch(error => {
                console.log(error);
            });
        }
    }
    
</script>