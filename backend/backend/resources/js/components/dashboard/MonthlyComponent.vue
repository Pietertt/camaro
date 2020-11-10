<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Deze maand</h3>
        <line-component :chart-data="totalData"></line-component>
    </div>
</template>

<script lang="ts">

    import LineComponent from './../charts/LineComponent.vue'
    import axios from 'axios';

    export default {
        data () {
            return {
                totalData: null,
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
        }
    }
    
</script>