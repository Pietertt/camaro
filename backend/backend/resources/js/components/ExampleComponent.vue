<template>

    
    <div class="uk-section uk-section-muted">
        <div class="uk-container">

            <h3>Section</h3>

            <div uk-grid>

                <div class="uk-width-1-4">
                    <div class="uk-card uk-card-primary">
                        <div class="uk-card-body">
                            <h3 class="uk-card-title">Welkom, Pieter Boersma</h3>
                            <ul class="uk-list">
                                <li><a class="uk-link-muted" href="#">Profiel</a></li>
                                <li><a class="uk-link-muted" href="#">Activiteiten</a></li>
                                <li><a class="uk-link-muted" href="#">Uitloggen</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="uk-width-1-2">
                    <div class="uk-card uk-card-default uk-card-body">
                        <line-chart :chart-data="datacollection"></line-chart>
                    </div>
                </div>

                <div class="uk-width-1-4">
                        <div class="uk-card uk-card-primary uk-card-body">Item</div>
                </div>

            </div>

        </div>
    </div>





</template>

<script>
    import LineChart from './LineChart.vue'

    export default {
        components: {
            LineChart
        },
    
        data () {
            return {
                datacollection: null
            }
        },
   
        mounted () {
            this.fillData()
        },
    
        methods: {
            fillData () {
                this.datacollection = {
                    labels: [Math.floor(Math.random() * (50 - 5 + 1)) + 5, Math.floor(Math.random() * (50 - 5 + 1)) + 5],
                    datasets: [{
                        label: 'Activiteiten',
                        backgroundColor: '#f87979',
                        data: [Math.floor(Math.random() * (50 - 5 + 1)) + 5, Math.floor(Math.random() * (50 - 5 + 1)) + 5]
                    }]
                }
            }
        }
    }
    
</script>