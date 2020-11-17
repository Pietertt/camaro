<template>
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
                    <tr v-for="d in recentData" :key="d.timestamp">
                        <td>{{ d[0] }}</td>
                        <td>{{ d[1] }}</td>
                        <td>{{ d[2] }}</td>
                    </tr>
                </tbody>
            </table>
            <router-link class="uk-button uk-button-default" to="/dashboard/activiteiten">Alle activiteiten</router-link>
        </div>
    </div>
</template>

<script lang="ts">

    import axios from 'axios';

    export default {
        data () {
            return {
                recentData: [],
            }
        },  

        async mounted () {
            setTimeout(() =>
                axios.get('http://imac-van-pieter.local:5000/activities/recent').then(response => {
                    this.recentData = response.data;
                }), 2000); 
        }
    }
</script>