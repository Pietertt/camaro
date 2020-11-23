<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Deze maand</h3>
          <!-- <GChart
            type="AreaChart"
            :data="chartData"
            :options="chartOptions"
            /> -->
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios';

    export default class MonthlyComponent extends Vue {

        private chartData = [
            ['Jaar', 'Activiteiten']
        ]

                //  ['Year', 'Sales'],
                // ['2013',  1000],
                // ['2014',  1170],
                // ['2015',  660],
                // ['2016',  1030]

    private chartOptions = {
        title: 'Activiteiten die deze maand plaats hebben gevonden',
        hAxis: {title: 'Dag',  titleTextStyle: {color: '#333'}},
        vAxis: {minValue: 0}
    };

        mounted(): void {
            this.validate();
        }

        validate(): void {
          
            axios.get('http://imac-van-pieter.local:5000/activities/monthly').then(response => {
                const data = response.data
                for(let i = 0; i < data.length; i++){
                    this.chartData.push([data[i][1], data[i][0]]);
                }

            }).catch(error => {
                console.log(error);
            });
        }
    }
    
</script>