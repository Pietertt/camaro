<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Statistieken</h3>
        <GChart
            type="PieChart"
            :data="chartData"
            :options="chartOptions"
            />
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'
    import { GChart } from "vue-google-charts";

    @Component({
        components: {
            GChart
        }
    })

    export default class ActivitiesComponent extends Vue {
        
         private chartData = [['Task', 'Hours per Dy']];

        private chartOptions = {
            title: 'Activiteiten die deze maand plaats hebben gevonden',
            hAxis: {title: 'Dag',  titleTextStyle: {color: '#333'}},
            vAxis: {minValue: 0}
        };

        mounted(): void {
            this.validate();
        }

        validate(): void {
          
            axios.get('http://imac-van-pieter.local:5000/activities/percentage').then(response => {
                this.chartData.push(['Valid', response.data[0]]);
                this.chartData.push(['Invalid', response.data[1]]);
            });
        }
    }
    
</script>
       