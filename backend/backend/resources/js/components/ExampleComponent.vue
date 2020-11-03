<template>

    
    <div class="uk-section uk-section-muted">
        <div class="uk-container">

            <h3>Welkom, Pieter Boersma</h3>

            <div class="uk-grid-match" uk-grid>

                <div class="uk-width-1-4">
                    <div class="uk-card uk-card-default">
                        <div class="uk-card-body">
                        <h3 class="uk-card-title">Menu</h3>
                            <ul class="uk-list">
                                <li>Startpagina</li>
                                <li>Profiel</li>
                                <li>Activiteiten</li>
                                <li>Uitloggen</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="uk-width-1-2">
                    <div class="uk-card uk-card-default uk-card-body">
                        <h3 class="uk-card-title">Deze maand</h3>
                        <line-chart :chart-data="totalData"></line-chart>
                    </div>
                </div>

                <div class="uk-width-1-4">
                    <div class="uk-card uk-card-default">
                        <div class="uk-card-body">
                            <h3 class="uk-card-title">Overzicht</h3>
                            
                        </div>
                    </div>
                </div>

                <div class="uk-width-1-2">
                     <div class="uk-card uk-card-default uk-card-body">
                     <h3 class="uk-card-title">Statistieken</h3>
                        <ul uk-tab>
                            <li class="uk-active"><a href="#">Validiteit</a></li>
                            <li><a href="#">Per maand</a></li>
                        </ul>

                        <pie-chart :chart-data="activityData"></pie-chart>
                    </div>
                </div>

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
                                    <tr v-for="d in recentData" :key="d.timestamp">
                                        <td>{{ d[0] }}</td>
                                        <td>{{ d[1] }}</td>
                                        <td>{{ d[2] }}</td>
                                    </tr>
                                </tbody>
                            </table>
                            <a class="uk-button uk-button-default" href="#">Alle activiteiten</a>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>





</template>

<script lang="ts">

    import LineChart from './LineChart.vue'
    import PieChart from './PieChart.vue'
    import BarChart from './BarChart.vue'

    export default {
        components: {
            LineChart,
            PieChart,
            BarChart
        },
    
        data () {
            return {
                totalData: null,
                activityData: null,
                monthlyData: null,
                recentData: null,
                totalValid: null,
                totalInvalid: null

            }
        },
   
        async mounted () {

            axios.get('http://imac-van-pieter.local:5000/activities/monthly').then(response => {
                    this.totalData = {
                        labels: response.data.map(x => x[1]),
                        datasets: [{
                            label: 'Activiteiten',
                            borderColor: '#cc65fe',
                            pointBackgroundColor: 'white',
                            borderWidth: 2,
                            pointBorderColor: '#cc65fe',
                            backgroundColor: 'transparent',
                            data: response.data.map(x => x[0])
                        }]
                    }
            });

            axios.get('http://imac-van-pieter.local:5000/activities/recent').then(response => {
                this.recentData = response.data;
            });

            axios.get('http://imac-van-pieter.local:5000/activities/valid/all').then(response => {
                this.totalValid = response.data;
            });

            axios.get('http://imac-van-pieter.local:5000/activities/invalid/all').then(response => {
                this.totalInvalid = response.data;

                this.activityData = {
                    labels: ["Aantal valide meldingen", "Aantal invalide meldingen"],
                    datasets: [{
                        data: [this.totalValid, this.totalInvalid],
                        backgroundColor: ['#ff6384', '#36a2eb']

                    }]
                }
            });
        },
    
        methods: {
            fillData () {
                this.activityData = {
                    labels: ["Aantal valide meldingen", "Aantal invalide meldingen"],
                    datasets: [{
                        data: [40, 60],
                        backgroundColor: ['#ff6384', '#36a2eb']

                    }]
                }
            }
        }
    }
    
</script>