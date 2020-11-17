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
                                    <tr v-for="d in recentData" :key="d.timestamp">
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

    import axios from 'axios';
    
    export default {
        data () {
            return {
                recentData: [],
            }
        },  

        async mounted () {
                axios.get('http://imac-van-pieter.local:5000/activities/all').then(response => {
                    this.recentData = response.data;
                });
        }
    }
</script>