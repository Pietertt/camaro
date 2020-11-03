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
                            <h5 class="uk-heading-line uk-text-center"><span>Acties</span></h5>
                            <button class="uk-button uk-button-danger uk-width-1-1 uk-margin-small-bottom" @click=deleteActivities><span v-if="!deleteActivitiyLoading">Activiteiten</span><span v-if="deleteActivitiyLoading"><div uk-spinner></div></span></button>
                            <button class="uk-button uk-button-danger uk-width-1-1 uk-margin-small-bottom" @click=deleteSensorData><span v-if="!deleteSensorLoading">Sensordata</span><span v-if="deleteSensorLoading"><div uk-spinner></div></span></button>
                             
                             
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
                deleteSensorLoading: false,
                deleteActivitiyLoading: false
            }
        },
   
        async mounted () {

            try {
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
            } catch(error){

            }

            // try {
            //     axios.get('http://imac-van-pieter.local:5000/activities/recent').then(response => {
            //         this.recentData = response.data;
            //     });
            // } catch(error){

            // }

            // try {
            //     axios.get('http://imac-van-pieter.local:5000/activities/valid/all').then(response => {
            //         this.totalValid = response.data;
            //     });
            // } catch(error){
                
            // }

            // try {
            //     axios.get('http://imac-van-pieter.local:5000/activities/invalid/all').then(response => {
            //         this.totalInvalid = response.data;

            //         this.activityData = {
            //             labels: ["Aantal valide meldingen", "Aantal invalide meldingen"],
            //             datasets: [{
            //                 data: [this.totalValid, this.totalInvalid],
            //                 backgroundColor: ['#ff6384', '#36a2eb']

            //             }]
            //         }
            //     });
            // } catch(error){

            // }
        },
    
        methods: {
            
            deleteActivities(){
                this.deleteActivitiyLoading = true;
                axios.get('http://imac-van-pieter.local:5000/activities/delete/all').then(response => {
                    if(response.data == 200){
                        this.deleteActivitiyLoading = false;
                    }
                });
            },

            deleteSensorData(){
                this.deleteSensorLoading = true;
                axios.get('http://imac-van-pieter.local:5000/sensor/delete/all').then(response => {
                    if(response.data == 200){
                        this.deleteSensorLoading = false;
                    }
                });
            }
        }
    }
    
</script>