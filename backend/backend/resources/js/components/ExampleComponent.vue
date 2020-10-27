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
                                        <th>Datum</th>
                                        <th>Validiteit</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="d in recentData" :key="d.timestamp">
                                        <td>{{ d.timestamp }}</td>
                                        <td v-if="d.valid">Valide</td><td v-else="d.valid">Invalide</td>
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

<script>
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

            }
        },
   
        mounted () {
            this.fillData()
        },
    
        methods: {
            fillData () {
                this.totalData = {
                    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                    datasets: [{
                        label: 'Activiteiten',
                        borderColor: '#cc65fe',
                        pointBackgroundColor: 'white',
                        borderWidth: 2,
                        pointBorderColor: '#cc65fe',
                        backgroundColor: 'transparent',
                        data: [2, 3, 6, 2, 6, 3, 4, 9, 3, 2, 5, 1, 7, 4, 12, 23, 27, 12, 23, 10, 12, 9, 10, 12, 13, 20, 24, 28, 20, 15, 23]
                    }]
                },

                this.activityData = {
                    labels: ["Aantal valide meldingen", "Aantal invalide meldingen"],
                    datasets: [{
                        data: [40, 60],
                        backgroundColor: ['#ff6384', '#36a2eb']

                    }]
                },

                this.recentData = [
                    {
                        timestamp: 202010271154,
                        valid: true
                    },
                    {
                        timestamp: 202010271343,
                        valid: true
                    },
                    {
                        timestamp: 202010271412,
                        valid: false
                    },
                    {
                        timestamp: 202010271534,
                        valid: false
                    },
                    {
                        timestamp: 202010271719,
                        valid: false
                    }
                ]
            }
        }
    }
    
</script>