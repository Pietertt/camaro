<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Statistieken</h3>
        <line
            :data="[86,114,106,106,107,111,133,221,783,2478]"
            :labels="[1500,1600,1700,1750,1800,1850,1900,1950,1999,2050]"
            :color="'#39f'"
            :title="'Activiteiten'"
        ></line>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'

    import Line from '../charts/Line.vue'

    @Component({
        components: {
            Line
        }
    })

    export default class StatisticsComponent extends Vue {
        
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
       